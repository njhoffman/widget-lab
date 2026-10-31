import base64
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import test_atlas_artwork as artwork
from check_project import validate_artwork_report


class ArtworkCoverageTests(unittest.TestCase):
    def test_changed_embedded_thumbnail_and_duplicate_ids_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'hero.svg').write_bytes(b'hero')
            (root / 'thumb.svg').write_bytes(b'thumb')
            entry = {'id': 'sample', 'hero': 'hero.svg', 'thumb': 'thumb.svg',
                     'sha256': hashlib.sha256(b'hero').hexdigest()}
            uri = lambda data: 'data:image/svg+xml;base64,' + base64.b64encode(data).decode()
            with patch.object(artwork, 'ROOT', root):
                rows, errors = artwork.compare_bytes([entry], 'id', 'thumb', {'sample': uri(b'hero')}, {'sample': uri(b'corrupt')}, root)
                self.assertFalse(errors)
                self.assertEqual(rows[0]['status'], 'fail')
                self.assertIn('bytes differ', rows[0]['assets']['thumb']['error'])
                _, errors = artwork.compare_bytes([entry, entry], 'id', 'thumb', {'sample': uri(b'hero')}, {'sample': uri(b'thumb')}, root)
                self.assertIn('Duplicate manifest IDs', errors)

    def test_report_cannot_hide_missing_decodes_or_stale_sources(self):
        registry = json.loads((ROOT / 'project_manifest.json').read_text())
        report = json.loads((ROOT / registry['repository']['artwork_regression_report']).read_text())
        self.assertEqual(validate_artwork_report(ROOT, report, registry['atlas']), [])
        incomplete = copy.deepcopy(report)
        incomplete['results'][0]['entries'][0]['decode'].pop()
        self.assertTrue(validate_artwork_report(ROOT, incomplete, registry['atlas']))
        missing = copy.deepcopy(report)
        missing['results'][1]['entries'].pop()
        self.assertTrue(validate_artwork_report(ROOT, missing, registry['atlas']))
        stale = copy.deepcopy(report)
        stale['results'][0]['source_sha256'] = '0' * 64
        self.assertTrue(any('stale' in e for e in validate_artwork_report(ROOT, stale, registry['atlas'])))


if __name__ == '__main__':
    unittest.main()
