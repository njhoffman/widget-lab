#!/usr/bin/env python3
"""Build a separate standalone visual release from the immutable Deep Time import."""
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'atlas/widgets/Deep_Time_Atlas_v1.18.html'
OUTPUT = ROOT / 'atlas/widgets/Deep_Time_Atlas_v1.19.0.html'
BASE_SHA256 = '778624d6ae08e6c461ab5e7e7c55700e4867c589fe2145b01eb5e57393ed9cea'
TITLE_BEFORE = '<title>Deep Time Atlas — v1.18</title>'
TITLE_AFTER = '<title>Deep Time Atlas — v1.19.0</title>'


def build():
    content = BASE.read_bytes()
    if hashlib.sha256(content).hexdigest() != BASE_SHA256:
        raise ValueError('Imported Deep Time baseline changed; refusing to rebuild')
    text = content.decode()
    css = (ROOT / 'atlas/widgets/deep-time/src/layout.css').read_text()
    js = (ROOT / 'atlas/widgets/deep-time/src/layout.js').read_text()
    text = text.replace(TITLE_BEFORE, TITLE_AFTER, 1)
    text = text.replace('</head>', '<style id="wl-deep-layout">\n' + css + '</style></head>', 1)
    before, after = text.rsplit('</body>', 1)
    return before + '<script id="wl-deep-layout-script">\n' + js + '</script></body>' + after


if __name__ == '__main__':
    OUTPUT.write_text(build())
    print(OUTPUT.relative_to(ROOT))
