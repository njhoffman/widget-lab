#!/usr/bin/env python3
"""Build a separate Brain visual release from the immutable scientific import."""
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'atlas/widgets/Brain_Atlas_v1.21.html'
OUTPUT = ROOT / 'atlas/widgets/Brain_Atlas_v1.22.0.html'
BASE_SHA256 = 'e0d06998612440905f37ea2ab7ac686035132177b0f6bf4d8ac8c6acb71966dd'
TITLE_BEFORE = '<title>Brain Atlas — v1.21</title>'
TITLE_AFTER = '<title>Brain Atlas — v1.22.0</title>'


def build():
    content = BASE.read_bytes()
    if hashlib.sha256(content).hexdigest() != BASE_SHA256:
        raise ValueError('Imported Brain baseline changed; refusing to rebuild')
    text = content.decode()
    css = (ROOT / 'atlas/widgets/brain/src/layout.css').read_text()
    js = (ROOT / 'atlas/widgets/brain/src/layout.js').read_text()
    text = text.replace(TITLE_BEFORE, TITLE_AFTER, 1)
    text = text.replace('</head>', '<style id="wl-brain-layout">\n' + css + '</style></head>', 1)
    before, after = text.rsplit('</body>', 1)
    return before + '<script id="wl-brain-layout-script">\n' + js + '</script></body>' + after


if __name__ == '__main__':
    OUTPUT.write_text(build())
    print(OUTPUT.relative_to(ROOT))
