#!/usr/bin/env python3
"""Build Mythology's visual release from the preserved import and verified assets."""
import base64
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'atlas/widgets/Mythology_Atlas_v1.13.html'
OUTPUT = ROOT / 'atlas/widgets/Mythology_Atlas_v1.14.0.html'
BASE_SHA256 = 'c674057629c975b1f54e64be6f831660ce9ff19d563d78a2216dc2ec12dc0c19'
TITLE_BEFORE = '<title>Mythology Atlas — v1.13</title>'
TITLE_AFTER = '<title>Mythology Atlas — v1.14.0</title>'


def featured_assets():
    folder = ROOT / 'atlas/assets/mythology'
    manifest = json.loads((folder / 'manifest.json').read_text())
    assets = {}
    for entry in manifest['entries']:
        if entry.get('quality_tier') != 'featured':
            continue
        path = folder / entry['hero']
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != entry['sha256']:
            raise ValueError(f'Featured artwork checksum mismatch: {entry["key"]}')
        assets[entry['key']] = {'src': 'data:image/webp;base64,' + base64.b64encode(data).decode(), 'sha256': entry['sha256']}
    return assets


def build():
    content = BASE.read_bytes()
    if hashlib.sha256(content).hexdigest() != BASE_SHA256:
        raise ValueError('Imported Mythology baseline changed; refusing to rebuild')
    text = content.decode()
    css = (ROOT / 'atlas/widgets/mythology/src/layout.css').read_text()
    js = (ROOT / 'atlas/widgets/mythology/src/layout.js').read_text().replace('__WL_FEATURED_ASSETS__', json.dumps(featured_assets(), separators=(',', ':')))
    text = text.replace(TITLE_BEFORE, TITLE_AFTER, 1)
    text = text.replace('</head>', '<style id="wl-myth-layout">\n' + css + '</style></head>', 1)
    before, after = text.rsplit('</body>', 1)
    return before + '<script id="wl-myth-layout-script">\n' + js + '</script></body>' + after


if __name__ == '__main__':
    OUTPUT.write_text(build())
    print(OUTPUT.relative_to(ROOT))
