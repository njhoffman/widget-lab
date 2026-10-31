import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_brain', ROOT / 'tools/build_brain.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class BrainBuildTests(unittest.TestCase):
    def test_all_original_geometry_records_and_handlers_are_preserved(self):
        result = builder.build()
        stripped, styles = re.subn(r'<style id="wl-brain-layout">.*?</style>', '', result, count=1, flags=re.S)
        stripped, scripts = re.subn(r'<script id="wl-brain-layout-script">.*?</script>', '', stripped, count=1, flags=re.S)
        self.assertEqual((styles, scripts), (1, 1))
        self.assertEqual(stripped.replace(builder.TITLE_AFTER, builder.TITLE_BEFORE, 1).encode(), builder.BASE.read_bytes())
        self.assertEqual(builder.OUTPUT.read_bytes(), result.encode(), 'Standalone Brain output is stale')
