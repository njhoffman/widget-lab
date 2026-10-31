#!/usr/bin/env python3
"""Generate the current-build launcher without rewriting imported dashboards."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build():
    registry = json.loads((ROOT / 'project_manifest.json').read_text())
    names = {'brain': 'Brain Atlas', 'deep-time': 'Deep Time Atlas', 'tree-of-life': 'Tree of Life Atlas',
             'mythology': 'Mythology Atlas', 'muscles': 'Muscle Atlas', 'emergence': 'Emergence Atlas', 'launcher': 'Widget Launcher'}
    cards = []
    for component in registry['atlas']:
        source = Path(component['authoritative_source']).relative_to('atlas').as_posix()
        title = html.escape(names[component['slug']])
        version = html.escape(component['release_version'])
        cards.append(f'<a class="card" data-widget="{component["slug"]}" href="{html.escape(source, quote=True)}"><h2>{title}</h2><span>Open atlas</span><strong>v{version}</strong></a>')
    return '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Atlas Widgets — current builds</title><style>*{box-sizing:border-box}body{margin:0;background:#06121d;color:#e8f4ff;font:16px/1.6 system-ui}main{max-width:1100px;margin:0 auto;padding:40px 22px}h1{font-size:34px;margin:0}h1 span,a{color:#62e7eb}p{color:#abc5d7}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin:28px 0}.card{display:block;text-decoration:none;border:1px solid #205268;border-radius:12px;background:linear-gradient(140deg,#102b3d,#091a28);padding:22px}.card:hover{border-color:#76f3ed}.card:focus-visible{outline:3px solid #9ff;outline-offset:4px}.card h2{font-size:21px;margin:0 0 20px;color:#f1f9ff}.card span{font-size:13px}.card strong{float:right;color:#75efc7;font-size:13px}footer{border-top:1px solid #204356;padding-top:20px;font-size:14px}</style>
<main><h1>Atlas <span>Widgets</span></h1><p>Explore the current atlas builds.</p><div class="grid">''' + ''.join(cards) + '''</div><footer><a href="index.html">Original project dashboard and artwork tools</a><p>Existing illustrations retain their scientific and cultural review limitations.</p></footer></main></html>\n'''


if __name__ == '__main__':
    (ROOT / 'atlas/current.html').write_text(build())
    print('atlas/current.html')
