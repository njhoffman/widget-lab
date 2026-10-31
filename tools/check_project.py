#!/usr/bin/env python3
"""Check release metadata and living backlog coverage without changing files."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TASK = re.compile(r'^- \[([ x])\] \*\*([A-Z]+-?\d+) — (.+?)\*\* \((p[123])\) \[(bug|feature|refactor|docs|test|chore|perf)\] \[(approved|triage|proposed|needs-verification|in-progress|blocked|done)\]$', re.M)


def is_semver(version):
    match = re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-([0-9A-Za-z.-]+))?(?:\+([0-9A-Za-z.-]+))?', version)
    if not match:
        return False
    for identifiers in (match[4], match[5]):
        if identifiers is not None and any(not part for part in identifiers.split('.')):
            return False
    return not match[4] or all(not part.isdigit() or len(part) == 1 or not part.startswith('0') for part in match[4].split('.'))


def validate_browser_report(root, report, components):
    errors = []
    if report.get('status') != 'pass' or any(r.get('status') != 'pass' for r in report.get('results', [])):
        errors.append('Browser regression report contains failures')
    names = {'layout-initial', 'keyboard-history', 'navigation-filters-panels', 'layout-selected', 'runtime-errors'}
    required = {(slug, width, name) for slug in ('deep-time', 'brain', 'mythology') for width in (390, 768, 1440) for name in names}
    observed = [(r.get('widget'), r.get('width'), r.get('name')) for r in report.get('results', [])]
    if not required.issubset(set(observed)) or len(observed) != len(set(observed)):
        errors.append('Browser regression report lacks the full unique 3-widget/3-width matrix')
    for slug in ('deep-time', 'brain', 'mythology'):
        component = next((c for c in components if c['slug'] == slug), None)
        source = report.get('sources', {}).get(slug, {})
        if not component or source.get('path') != component['authoritative_source']:
            errors.append(f'{slug}: browser report source differs from manifest')
        elif not (root / source['path']).is_file() or digest_file(root / source['path']) != source.get('sha256'):
            errors.append(f'{slug}: browser regression report is stale for current source')
    return errors


def digest_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_artwork_report(root, report, components):
    errors = []
    results = report.get('results', [])
    if report.get('status') != 'pass' or sorted(r.get('widget', '') for r in results) != ['deep-time', 'mythology']:
        return ['Artwork report must pass and cover Deep Time and Mythology exactly once']
    for result in results:
        slug = result['widget']
        component = next(c for c in components if c['slug'] == slug)
        expected = 172 if slug == 'deep-time' else 363
        if result.get('source') != component['authoritative_source'] or digest_file(root / component['authoritative_source']) != result.get('source_sha256'):
            errors.append(f'{slug}: offline artwork report is stale for current source')
        folder = 'deep_time' if slug == 'deep-time' else 'mythology'
        manifest_path = root / 'atlas/assets' / folder / 'manifest.json'
        if result.get('manifest') != str(manifest_path.relative_to(root)) or digest_file(manifest_path) != result.get('manifest_sha256'):
            errors.append(f'{slug}: offline artwork manifest changed')
        manifest = json.loads(manifest_path.read_text())
        indexed = {e['id' if slug == 'deep-time' else 'key']: e for e in manifest['entries']}
        keys = set(indexed)
        rows = result.get('entries', [])
        if (result.get('status') != 'pass' or result.get('errors') or result.get('runtime_exceptions')
                or result.get('expected') != expected or result.get('indexed') != expected
                or result.get('images_decoded') != expected * 2 or len(rows) != expected
                or {r.get('id') for r in rows} != keys):
            errors.append(f'{slug}: offline artwork coverage incomplete or failed')
        for row in rows:
            decodes = row.get('decode', [])
            assets = row.get('assets', {})
            if (row.get('status') != 'pass' or len(decodes) != 2
                    or {d.get('kind') for d in decodes} != {'hero', 'thumbnail'}
                    or any(d.get('status') != 'pass' or d.get('id') != row.get('id')
                           or d.get('width', 0) <= 0 or d.get('height', 0) <= 0 for d in decodes)
                    or set(assets) != {'hero', 'thumb' if slug == 'deep-time' else 'thumbnail'}):
                errors.append(f'{slug}/{row.get("id")}: incomplete or failed artwork evidence')
            for kind, asset in assets.items():
                entry = indexed.get(row.get('id'), {})
                if kind not in entry:
                    errors.append(f'{slug}/{row.get("id")}: unexpected artwork kind')
                    continue
                path = manifest_path.parent / entry[kind]
                if asset.get('path') != str(path.relative_to(root)):
                    errors.append(f'{slug}/{row.get("id")}: artwork path differs from manifest')
                if not path.is_file() or digest_file(path) != asset.get('sha256'):
                    errors.append(f'{slug}/{row.get("id")}: changed adjacent artwork')
    return errors


def validate(root):
    errors = []
    version = (root / 'VERSION').read_text().strip()
    if not is_semver(version):
        errors.append('VERSION must be a valid SemVer version')
    registry = json.loads((root / 'project_manifest.json').read_text())
    if registry.get('repository', {}).get('release_version') != version:
        errors.append('Manifest repository.release_version differs from VERSION')
    changelog = (root / 'CHANGELOG.md').read_text()
    if not re.search(r'^## \[Unreleased\]$', changelog, re.M):
        errors.append('CHANGELOG lacks Unreleased section')
    if not re.search(r'^## \[' + re.escape(version) + r'\] - \d{4}-\d{2}-\d{2}$', changelog, re.M):
        errors.append('CHANGELOG lacks a dated section for VERSION')
    todo = (root / 'TODO.md').read_text()
    tasks = list(TASK.finditer(todo))
    ids = [m[2] for m in tasks]
    for ident in set(ids):
        if ids.count(ident) > 1:
            errors.append(f'Duplicate task ID: {ident}')
    for match in tasks:
        if (match[1] == 'x') != (match[6] == 'done'):
            errors.append(f'{match[2]}: checkbox and done status disagree')
    checkbox_lines = re.findall(r'^- \[[ x]\].*$', todo, re.M)
    if len(checkbox_lines) != len(tasks):
        errors.append('Some tasks lack required ID/priority/category/status formatting')
    catalog = json.loads((root / 'atlas/data/project_catalog_v1.21.json').read_text())
    expected = {x['id'] for key in ('goals', 'issues', 'suggestions') for x in catalog[key]}
    missing = expected - set(ids)
    if missing:
        errors.append('Missing historical tasks: ' + ', '.join(sorted(missing)))
    browser_report = registry.get('repository', {}).get('browser_regression_report')
    if browser_report:
        path = root / browser_report
        if not path.is_file():
            errors.append('Missing browser regression report')
        else:
            errors.extend(validate_browser_report(root, json.loads(path.read_text()), registry.get('atlas', [])))
    artwork_report = registry.get('repository', {}).get('artwork_regression_report')
    if artwork_report:
        path = root / artwork_report
        if not path.is_file():
            errors.append('Missing offline artwork regression report')
        else:
            errors.extend(validate_artwork_report(root, json.loads(path.read_text()), registry.get('atlas', [])))
    for component in registry.get('atlas', []):
        source = root / component['authoritative_source']
        if not source.is_file():
            errors.append(f'Missing registered source: {source.relative_to(root)}')
        evidence_name = component.get('visual_evidence')
        if evidence_name:
            evidence_path = root / evidence_name
            if not evidence_path.is_file():
                errors.append(f'Missing visual evidence: {evidence_name}')
                continue
            evidence = json.loads(evidence_path.read_text())
            if evidence.get('runtime_exceptions'):
                errors.append(f'{component["slug"]}: browser capture recorded runtime exceptions')
            if source.is_file() and hashlib.sha256(source.read_bytes()).hexdigest() != evidence['source_sha256']:
                errors.append(f'{component["slug"]}: visual evidence is stale for current source')
            if evidence['widget_version'] != component['release_version']:
                errors.append(f'{component["slug"]}: visual evidence version differs from manifest')
            for suffix, key in (('actual.png', 'actual_sha256'), ('comparison.png', 'comparison_sha256')):
                image = evidence_path.parent / f'{component["slug"]}-{suffix}'
                if not image.is_file() or hashlib.sha256(image.read_bytes()).hexdigest() != evidence[key]:
                    errors.append(f'{component["slug"]}: missing or changed {suffix}')
            for goal in evidence['goals']:
                image = root / goal['path']
                if not image.is_file() or hashlib.sha256(image.read_bytes()).hexdigest() != goal['sha256']:
                    errors.append(f'{component["slug"]}: goal reference changed since capture')
    return errors


if __name__ == '__main__':
    errors = validate(ROOT)
    print(json.dumps({'status': 'fail' if errors else 'pass', 'version': (ROOT / 'VERSION').read_text().strip(), 'errors': errors}, indent=2))
    sys.exit(bool(errors))
