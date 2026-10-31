import importlib.util
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('check_project', Path(__file__).resolve().parents[1] / 'tools/check_project.py')
project = importlib.util.module_from_spec(spec)
spec.loader.exec_module(project)


class ProjectWorkflowTests(unittest.TestCase):
    def test_browser_report_cannot_claim_success_with_missing_coverage_or_stale_sources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            components = []
            sources = {}
            for slug in ('deep-time', 'brain', 'mythology'):
                path = root / f'{slug}.html'
                path.write_text('original source')
                components.append({'slug': slug, 'authoritative_source': path.name})
                sources[slug] = {'path': path.name, 'sha256': project.digest_file(path)}
            cases = [{'widget': slug, 'width': width, 'name': name, 'status': 'pass'}
                     for slug in sources for width in (390, 768, 1440)
                     for name in ('layout-initial', 'keyboard-history', 'navigation-filters-panels', 'layout-selected', 'runtime-errors')]
            report = {'status': 'pass', 'sources': sources, 'results': cases}
            self.assertEqual(project.validate_browser_report(root, report, components), [])
            report['results'] = [r for r in cases if r['width'] != 390]
            self.assertTrue(any('matrix' in e for e in project.validate_browser_report(root, report, components)))
            report['results'] = cases
            (root / 'brain.html').write_text('changed source')
            self.assertTrue(any('stale' in e for e in project.validate_browser_report(root, report, components)))
            cases[0]['status'] = 'fail'
            self.assertTrue(any('failures' in e for e in project.validate_browser_report(root, report, components)))

    def test_semver_rejects_legacy_and_invalid_prerelease_versions(self):
        for version in ('1.21', 'v0.1.0', '01.2.3', '1.2.3-01', '1.2.3-a..b'):
            with self.subTest(version=version):
                self.assertFalse(project.is_semver(version))
        for version in ('0.1.0', '1.2.3-rc.1', '1.2.3+build.01'):
            with self.subTest(version=version):
                self.assertTrue(project.is_semver(version))

    def test_metadata_drift_missing_tasks_and_false_completion_are_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'VERSION').write_text('0.1.0\n')
            (root / 'project_manifest.json').write_text(json.dumps({'repository': {'release_version': '0.1.1'}}))
            (root / 'CHANGELOG.md').write_text('## [Unreleased]\n## [0.1.0] - 2026-10-30\n')
            (root / 'TODO.md').write_text('- [x] **WL-001 — Not yet done.** (p1) [test] [approved]\n')
            path = root / 'atlas/data/project_catalog_v1.21.json'
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({'goals': [{'id': 'T001'}], 'issues': [], 'suggestions': []}))
            errors = project.validate(root)
            self.assertTrue(any('Manifest' in e for e in errors))
            self.assertTrue(any('T001' in e for e in errors))
            self.assertTrue(any('checkbox' in e for e in errors))

    def test_current_repository_metadata_and_backlog_agree(self):
        self.assertEqual(project.validate(project.ROOT), [])

    def test_changed_actual_screenshot_invalidates_visual_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'VERSION').write_text('0.1.0\n')
            source = root / 'widget.html'
            source.write_text('original')
            actual = root / 'brain-actual.png'
            actual.write_bytes(b'changed screenshot')
            (root / 'brain-comparison.png').write_bytes(b'comparison')
            evidence = {'widget_version': '1.21', 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                        'actual_sha256': hashlib.sha256(b'original screenshot').hexdigest(),
                        'comparison_sha256': hashlib.sha256(b'comparison').hexdigest(), 'goals': []}
            (root / 'brain-evidence.json').write_text(json.dumps(evidence))
            (root / 'project_manifest.json').write_text(json.dumps({
                'repository': {'release_version': '0.1.0'}, 'atlas': [{
                    'slug': 'brain', 'release_version': '1.21', 'authoritative_source': 'widget.html',
                    'visual_evidence': 'brain-evidence.json'}]}))
            (root / 'CHANGELOG.md').write_text('## [Unreleased]\n## [0.1.0] - 2026-10-30\n')
            (root / 'TODO.md').write_text('')
            path = root / 'atlas/data/project_catalog_v1.21.json'
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps({'goals': [], 'issues': [], 'suggestions': []}))
            self.assertEqual(project.validate(root), ['brain: missing or changed actual.png'])
