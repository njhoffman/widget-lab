"""Guard against false integrity passes and reading private inventory paths."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('verify_migration', Path(__file__).resolve().parents[1] / 'tools/verify_migration.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)


class MigrationAuditTests(unittest.TestCase):
    def test_private_and_escape_paths_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ('../secret', '/etc/passwd', 'incoming/a', '.local/a', '.git/config'):
                with self.subTest(name=name), self.assertRaises(ValueError):
                    verify.safe_file(root, name)
            (root / 'link').symlink_to('/tmp')
            with self.assertRaises(ValueError):
                verify.safe_file(root, 'link/file')

    def test_missing_and_corrupted_inventory_is_incomplete(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'project_manifest.json').write_text(json.dumps({'atlas': [], 'quiz': []}))
            data = root / 'shared/taxa'
            data.mkdir(parents=True)
            (data / 'changed.txt').write_text('changed')
            (data / 'manifest.json').write_text(json.dumps({
                'dataset_version': '1.0', 'files': [
                    {'path': name, 'size_bytes': 0, 'sha256': 'invalid'}
                    for name in ('missing.txt', 'changed.txt')]}))
            report = verify.audit(root)
            self.assertEqual(report['status'], 'incomplete')
            self.assertEqual([f['status'] for f in report['shared_taxa']['findings']],
                             ['missing', 'checksum_mismatch'])


if __name__ == '__main__':
    unittest.main()
