#!/usr/bin/env python3
"""Capture real Atlas UI, render goal/checklist comparison PNGs, and open feh."""
import argparse
import base64
from datetime import datetime, timezone
import hashlib
import html
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
import urllib.request

from check_project import ROOT, TASK

CONFIG = {
    'deep-time': ('Deep Time Atlas', [('goal_1.png', [0, 0, 817, 505]), ('goal_2.png', [0, 0, 1536, 411])]),
    'brain': ('Brain Atlas', [('goal_1.png', [828, 0, 708, 505]), ('goal_2.png', [0, 414, 1536, 332])]),
    'mythology': ('Mythology Atlas', [('goal_1.png', [0, 538, 1536, 486]), ('goal_2.png', [0, 750, 1536, 274])]),
    'tree-of-life': ('Tree of Life Atlas', [('audit_tree_concept.png', None)]),
    'muscles': ('Muscle Atlas', [('audit_muscle_concept.png', None)]),
    'emergence': ('Emergence Atlas', [('audit_emergence_concept.png', None)]),
    'launcher': ('Widget Launcher', [('audit_launcher_concept.png', None)]),
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Browser:
    def __init__(self, executable, profile):
        import websocket
        self.process = subprocess.Popen([
            executable, '--headless', '--no-sandbox', '--disable-dev-shm-usage',
            '--disable-gpu', '--no-first-run', '--hide-scrollbars', '--allow-file-access-from-files',
            '--remote-debugging-port=0', f'--user-data-dir={profile}', 'about:blank'],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        try:
            active = Path(profile) / 'DevToolsActivePort'
            deadline = time.monotonic() + 20
            while not active.exists():
                if time.monotonic() > deadline or self.process.poll() is not None:
                    raise RuntimeError('Chrome did not start its local debugging endpoint')
                time.sleep(.1)
            port = active.read_text().splitlines()[0]
            # Use only the localhost endpoint; do not inherit HTTP proxy settings.
            opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
            with opener.open(f'http://127.0.0.1:{port}/json/list', timeout=10) as response:
                pages = json.load(response)
            page = next(p for p in pages if p['type'] == 'page')
            self.ws = websocket.create_connection(page['webSocketDebuggerUrl'], timeout=30, suppress_origin=True)
            self.sequence = 0
            self.events = []
            self.call('Page.enable')
            self.call('Runtime.enable')
            self.call('Network.enable')
            self.call('Network.setBlockedURLs', {'urls': ['http://*', 'https://*']})
            self.version = self.call('Browser.getVersion')['product']
        except BaseException:
            self.process.terminate()
            self.process.wait(timeout=10)
            raise

    def call(self, method, params=None):
        self.sequence += 1
        self.ws.send(json.dumps({'id': self.sequence, 'method': method, 'params': params or {}}))
        while True:
            message = json.loads(self.ws.recv())
            if message.get('id') != self.sequence:
                self.events.append(message)
                continue
            if 'error' in message:
                raise RuntimeError(f'{method}: {message["error"]}')
            return message.get('result', {})

    def evaluate(self, expression):
        result = self.call('Runtime.evaluate', {'expression': expression, 'awaitPromise': True, 'returnByValue': True})
        if result.get('exceptionDetails'):
            raise RuntimeError(str(result['exceptionDetails']))
        return result.get('result', {}).get('value')

    def navigate(self, path, width, height):
        self.call('Emulation.setDeviceMetricsOverride', {'width': width, 'height': height, 'deviceScaleFactor': 1, 'mobile': False})
        self.call('Page.navigate', {'url': path.resolve().as_uri()})
        self.evaluate('new Promise(resolve => setTimeout(resolve, 1200))')
        self.evaluate('document.fonts.ready.then(() => true)')

    def screenshot(self, path):
        data = self.call('Page.captureScreenshot', {'format': 'png', 'captureBeyondViewport': False})['data']
        path.write_bytes(base64.b64decode(data))

    def close(self):
        self.ws.close()
        self.process.terminate()
        try:
            self.process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait()


def task_lists(widget):
    catalog = json.loads((ROOT / 'atlas/data/project_catalog_v1.21.json').read_text())
    related = {x['id'] for key in ('goals', 'issues', 'suggestions') for x in catalog[key]
               if x['widget'] == widget or x['widget'] == 'Shared UI'}
    related.update(('WL-001', 'WL-003', 'WL-004', 'WL-005', 'WL-006', 'WL-010'))
    done, pending = [], []
    for match in TASK.finditer((ROOT / 'TODO.md').read_text()):
        if match[2] in related:
            item = {'id': match[2], 'title': match[3], 'priority': match[4], 'status': match[6]}
            (done if match[1] == 'x' else pending).append(item)
    return done, pending


def render_report(title, actual, goals, done, pending, metadata):
    escape = html.escape
    pictures = []
    for goal in goals:
        image = goal['path']
        image_url = html.escape(os.path.relpath(image, actual.parent), quote=True)
        crop = goal['crop']
        if crop:
            x, y, width, height = crop
            # CSS cropping preserves original pixels; the browser renders the report.
            scale = 790 / width
            visual = f'<div style="position:relative;overflow:hidden;height:{height*scale}px"><img src="{image_url}" style="position:absolute;width:{1536*scale}px;max-width:none;left:{-x*scale}px;top:{-y*scale}px"></div>'
        else:
            visual = f'<img style="width:100%" src="{image_url}">'
        pictures.append(f'<h3>{escape(image.name)} · {goal["approval"]}</h3>{visual}')
    def items(entries):
        return ''.join(f'<li><b>{escape(t["id"])} · {escape(t["priority"])} · {escape(t["status"])}</b><br>{escape(t["title"])}</li>' for t in entries)
    return f'''<!doctype html><html><meta charset="utf-8"><title>{escape(title)} comparison</title>
<style>*{{box-sizing:border-box}}body{{margin:0;padding:24px;background:#07121d;color:#e6f3ff;font:16px system-ui}}h1{{margin:0 0 8px}}h2{{font-size:23px}}h3{{font-size:16px;color:#55e8e7}}.meta{{color:#a9c5d7;margin-bottom:20px;line-height:1.7}}main{{display:grid;grid-template-columns:820px 820px 480px;gap:20px}}section{{background:#0d1d2c;border:1px solid #225571;border-radius:12px;padding:14px;overflow:hidden}}section img{{display:block;max-width:100%}}ul{{padding-left:20px}}li{{margin-bottom:12px;font-size:14px;line-height:1.4}}.done{{color:#6df5be}}.pending{{color:#ffdb86}}footer{{margin-top:18px;color:#b9cbd6;max-width:2100px}}code{{font-size:13px}}</style>
<h1>{escape(title)} · actual versus goal · repository {escape(metadata['repository_version'])}</h1>
<div class="meta">Captured {escape(metadata['captured_at'])} · {escape(metadata['browser'])} · 1440 × 1000 actual viewport<br>
Widget {escape(metadata['widget_version'])} · State: {escape(metadata['selection'])}<br><code>Source SHA-256 {metadata['source_sha256']}</code></div>
<main><section><h2>Actual · fresh browser capture</h2><img src="{actual.name}"><p>Original widget source unchanged. External HTTP(S) requests blocked for this offline capture.</p></section>
<section><h2>Goal reference</h2>{''.join(pictures)}</section>
<section><h2 class="done">Complete · {len(done)}</h2><ul>{items(done)}</ul><h2 class="pending">Pending / verify · {len(pending)}</h2><ul>{items(pending)}</ul></section></main>
<footer>Task status comes from TODO.md. Historical implementation claims remain pending verification. Rendering, source integrity, and goal similarity do not certify interactions, anatomical accuracy, cultural interpretation, artwork approval, or scientific claims. Goal counts/versions are illustrative. This report does not mark visual gaps complete.</footer></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--widgets', nargs='+', choices=CONFIG, default=list(CONFIG))
    parser.add_argument('--no-open', action='store_true', help='CI only: skip the explicitly requested desktop preview')
    args = parser.parse_args()
    executable = shutil.which('google-chrome') or shutil.which('chromium')
    if not executable:
        raise SystemExit('Chrome/Chromium is required for fresh actual screenshots')
    version = (ROOT / 'VERSION').read_text().strip()
    output = ROOT / 'docs/visual-reviews' / version
    if any((output / f'{slug}-comparison.png').exists() for slug in args.widgets):
        raise SystemExit('Evidence already exists for this version/widget. Preserve it; use a new batch version.')
    output.mkdir(parents=True, exist_ok=True)
    registry = json.loads((ROOT / 'project_manifest.json').read_text())
    records = []
    with tempfile.TemporaryDirectory(prefix='widget-lab-capture-') as profile:
        browser = Browser(executable, profile)
        try:
            for slug in args.widgets:
                title, references = CONFIG[slug]
                component = next(c for c in registry['atlas'] if c['slug'] == slug)
                source = ROOT / component['authoritative_source']
                browser.events.clear()
                browser.navigate(source, 1440, 1000)
                if slug == 'deep-time':
                    browser.evaluate("drill('triassic'); true")
                    selection = 'Triassic interval'
                elif slug == 'brain':
                    browser.evaluate("(()=>{const n=[...document.querySelectorAll('svg circle, svg [role=button]')].find(n=>n.textContent.includes('Orbitofrontal'));if(!n)throw Error('OFC marker missing');n.dispatchEvent(new MouseEvent('click',{bubbles:true}));return true})()")
                    selection = 'Orbitofrontal cortex, lateral schematic'
                elif slug == 'mythology':
                    browser.evaluate("selectFigure('zeus'); true")
                    browser.evaluate("(()=>{if(!document.getElementById('profileHead').innerText.includes('Zeus'))throw Error('Zeus selection failed');return true})()")
                    selection = 'Greek Zeus'
                else:
                    selection = 'Initial default view in clean browser profile'
                browser.evaluate('new Promise(resolve => setTimeout(resolve, 600))')
                actual = output / f'{slug}-actual.png'
                browser.screenshot(actual)
                goals = [{'path': ROOT / 'atlas/images' / name, 'crop': crop,
                          'approval': 'approved visual direction' if name.startswith('goal_') else 'proposed concept, not approved'}
                         for name, crop in references]
                done, pending = task_lists(title)
                metadata = {'widget': slug, 'widget_version': component['release_version'], 'repository_version': version,
                            'captured_at': datetime.now(timezone.utc).isoformat(), 'browser': browser.version,
                            'source': component['authoritative_source'], 'source_sha256': digest(source),
                            'actual_sha256': digest(actual), 'viewport': [1440, 1000], 'selection': selection,
                            'goals': [{'path': str(g['path'].relative_to(ROOT)), 'sha256': digest(g['path']), 'crop': g['crop'], 'approval': g['approval']} for g in goals],
                            'complete': done, 'pending': pending,
                            'runtime_exceptions': [e['params']['exceptionDetails'] for e in browser.events if e.get('method') == 'Runtime.exceptionThrown'],
                            'review_scope': 'Fresh browser rendering and selected state only; full functional/scientific review pending.'}
                page = output / f'{slug}-comparison.html'
                page.write_text(render_report(title, actual, goals, done, pending, metadata))
                browser.navigate(page, 2240, 1100)
                height = browser.evaluate('Math.ceil(document.documentElement.scrollHeight)')
                browser.call('Emulation.setDeviceMetricsOverride', {'width': 2240, 'height': height, 'deviceScaleFactor': 1, 'mobile': False})
                browser.evaluate('new Promise(resolve => setTimeout(resolve, 300))')
                comparison = output / f'{slug}-comparison.png'
                browser.screenshot(comparison)
                metadata['comparison_sha256'] = digest(comparison)
                (output / f'{slug}-evidence.json').write_text(json.dumps(metadata, indent=2) + '\n')
                records.append(slug)
                print(f'Captured {slug}: {len(done)} complete, {len(pending)} pending', flush=True)
        finally:
            browser.close()
    links = ''.join(f'<li><a href="{s}-comparison.png">{s} comparison PNG</a> · <a href="{s}-evidence.json">evidence</a></li>' for s in CONFIG if (output / f'{s}-comparison.png').exists())
    (output / 'index.html').write_text(f'<!doctype html><meta charset="utf-8"><title>Atlas visual review {html.escape(version)}</title><h1>Atlas visual review {html.escape(version)}</h1><ul>{links}</ul>')
    viewer = {'requested': not args.no_open, 'launched': False}
    if not args.no_open:
        if not shutil.which('feh'):
            viewer['reason'] = 'feh unavailable'
        elif not os.environ.get('DISPLAY'):
            viewer['reason'] = 'DISPLAY unavailable'
        else:
            log = output / 'feh.log'
            with log.open('w') as stream:
                process = subprocess.Popen(['feh', '--auto-zoom', '--scale-down', '--title', f'Atlas actual versus goal · {version}', *[str(output / f'{s}-comparison.png') for s in records]], stdout=stream, stderr=stream, start_new_session=True)
            time.sleep(.5)
            viewer.update(launched=process.poll() is None, pid=process.pid, exit_code=process.poll())
    (output / 'viewer.json').write_text(json.dumps(viewer, indent=2) + '\n')
    print(json.dumps({'output': str(output.relative_to(ROOT)), 'viewer': viewer}), flush=True)
    if not args.no_open and not viewer['launched']:
        raise SystemExit('Comparisons saved, but feh could not launch; see viewer.json')


if __name__ == '__main__':
    main()
