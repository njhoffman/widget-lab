import base64
import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_mythology', ROOT / 'tools/build_mythology.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class MythologyBuildTests(unittest.TestCase):
    def test_original_records_and_controls_are_preserved_byte_for_byte(self):
        result = builder.build()
        stripped, styles = re.subn(r'<style id="wl-myth-layout">.*?</style>', '', result, count=1, flags=re.S)
        stripped, scripts = re.subn(r'<script id="wl-myth-layout-script">.*?</script>', '', stripped, count=1, flags=re.S)
        self.assertEqual((styles, scripts), (1, 1))
        self.assertEqual(stripped.replace(builder.TITLE_AFTER, builder.TITLE_BEFORE, 1).encode(), builder.BASE.read_bytes())
        self.assertEqual(builder.OUTPUT.read_bytes(), result.encode(), 'Standalone Mythology output is stale')

    def test_offline_featured_zeus_is_the_verified_existing_artwork(self):
        assets = builder.featured_assets()
        self.assertEqual(set(assets), {'greek:zeus'})
        original = (ROOT / 'atlas/assets/mythology/hero/greek/zeus.webp').read_bytes()
        self.assertEqual(base64.b64decode(assets['greek:zeus']['src'].split(',', 1)[1]), original)
        self.assertIn(assets['greek:zeus']['src'], builder.OUTPUT.read_text())
