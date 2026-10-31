import importlib.util
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / f'tools/{name}.py')
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


class DeepTimeBuildTests(unittest.TestCase):
    def test_original_scientific_source_is_preserved_except_title_and_appended_presentation(self):
        builder = module('build_deep_time')
        derived = builder.build()
        stripped, style_count = re.subn(r'<style id="wl-deep-layout">.*?</style>', '', derived, count=1, flags=re.S)
        stripped, script_count = re.subn(r'<script id="wl-deep-layout-script">.*?</script>', '', stripped, count=1, flags=re.S)
        self.assertEqual((style_count, script_count), (1, 1))
        self.assertEqual(stripped.replace(builder.TITLE_AFTER, builder.TITLE_BEFORE, 1).encode(), builder.BASE.read_bytes())
        self.assertEqual(builder.OUTPUT.read_bytes(), derived.encode(), 'Standalone build is stale; rebuild the edited adapter')

    def test_current_launcher_matches_registered_sources(self):
        builder = module('build_atlas_index')
        self.assertEqual((ROOT / 'atlas/current.html').read_text(), builder.build())
        page = builder.build()
        links = re.findall(r'class="card"[^>]*href="([^"]+)"', page)
        self.assertEqual(len(links), 7)
        self.assertTrue(all((ROOT / 'atlas' / link).is_file() for link in links))
        self.assertIn('widgets/Deep_Time_Atlas_v1.19.0.html', links)
        self.assertIn('widgets/Mythology_Atlas_v1.14.0.html', links)
        self.assertIn('widgets/Brain_Atlas_v1.22.0.html', links)
