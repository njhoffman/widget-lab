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
import re
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

HIGHLIGHT = {'deep-time': ('T011', 'main.panel.center.aw-deep-art', 'Interval artwork · verified'),
             'mythology': ('T040', '#awMythArtworkStage', 'Figure artwork · verified')}


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
        # Let Chrome flush its profile and stop renderer children before the
        # temporary-directory context attempts cleanup.
        try:
            self.ws.settimeout(5)
            self.call('Browser.close')
        except Exception:
            # Chrome may close the debugging connection before acknowledging.
            pass
        finally:
            self.ws.close()
        try:
            self.process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=5)


def task_lists(widget, release_version):
    catalog = json.loads((ROOT / 'atlas/data/project_catalog_v1.21.json').read_text())
    related = {x['id'] for key in ('goals', 'issues', 'suggestions') for x in catalog[key]
               if x['widget'] == widget or x['widget'] == 'Shared UI'}
    related.update(('WL-001', 'WL-003', 'WL-004', 'WL-005', 'WL-006', 'WL-010', 'WL-024'))
    if widget == 'Deep Time Atlas':
        related.update(('WL-011', 'WL-012', 'WL-013', 'WL-015'))
    if widget == 'Mythology Atlas':
        related.update(('WL-016', 'WL-017', 'WL-018'))
    if widget == 'Brain Atlas':
        related.update(('WL-019', 'WL-020', 'WL-021'))
    changelog = (ROOT / 'CHANGELOG.md').read_text()
    release = changelog.split(f'## [{release_version}]', 1)[-1].split('\n## [', 1)[0]
    recent_ids = set(re.findall(r'\b(?:WL-?|T|I|S)\d{3}\b', release))
    done, earlier, pending = [], [], []
    for match in TASK.finditer((ROOT / 'TODO.md').read_text()):
        if match[2] in related:
            item = {'id': match[2], 'title': match[3], 'priority': match[4], 'status': match[6]}
            if match[1] == 'x':
                (done if match[2] in recent_ids else earlier).append(item)
            else:
                pending.append(item)
    pending.sort(key=lambda t: ({'p1': 0, 'p2': 1, 'p3': 2}[t['priority']],
                                {'needs-verification': 0, 'triage': 1, 'approved': 2,
                                 'in-progress': 3, 'blocked': 4, 'proposed': 5}[t['status']], t['id']))
    shown, hidden = pending[:4], pending[4:]
    return done, len(earlier), shown, {'total': len(hidden),
                                       'needs_verification': sum(t['status'] == 'needs-verification' for t in hidden)}


def render_report(title, actual, goals, done, earlier_count, pending, hidden, metadata):
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
    earlier = f'<p>{earlier_count} completed in earlier updates</p>' if earlier_count else ''
    remainder = f'<p>… + {hidden["total"]} others; {hidden["needs_verification"]} need verification.</p>' if hidden['total'] else ''
    return f'''<!doctype html><html><meta charset="utf-8"><title>{escape(title)} comparison</title>
<style>*{{box-sizing:border-box}}body{{margin:0;padding:24px;background:#07121d;color:#e6f3ff;font:16px system-ui}}h1{{margin:0 0 8px}}h2{{font-size:23px}}h3{{font-size:16px;color:#55e8e7}}.meta{{color:#a9c5d7;margin-bottom:20px;line-height:1.7}}main{{display:grid;grid-template-columns:820px 820px 480px;gap:20px}}section{{background:#0d1d2c;border:1px solid #225571;border-radius:12px;padding:14px;overflow:hidden}}section img{{display:block;max-width:100%}}ul{{padding-left:20px}}li{{margin-bottom:12px;font-size:14px;line-height:1.4}}.done{{color:#6df5be}}.recent{{color:#07121d;background:#6df5be;padding:4px 8px;border-radius:8px}}.pending{{color:#ffdb86}}section p{{color:#d2e1ec;font-size:13px}}footer{{margin-top:18px;color:#b9cbd6;max-width:2100px}}code{{font-size:13px}}</style>
<h1>{escape(title)} · actual versus goal · repository {escape(metadata['repository_version'])}</h1>
<div class="meta">Captured {escape(metadata['captured_at'])} · {escape(metadata['browser'])} · 1440 × 1000 actual viewport<br>
Widget {escape(metadata['widget_version'])} · State: {escape(metadata['selection'])}<br><code>Source SHA-256 {metadata['source_sha256']}</code></div>
<main><section><h2>Actual · fresh browser capture</h2><img src="{metadata.get('annotated_actual', actual.name)}"><p>{escape(metadata.get('annotation_note', 'No app region changed in this update.'))} Clean capture is kept separately.</p></section>
<section><h2>Goal reference</h2>{''.join(pictures)}</section>
<section><h2 class="recent">Completed this update · {len(done)}</h2><ul>{items(done) if done else '<li>No tasks completed in this release.</li>'}</ul>{earlier}<h2 class="pending">Top priority pending · {len(pending)}</h2><ul>{items(pending)}</ul>{remainder}</section></main>
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
                capture_checks = {}
                browser.navigate(source, 1440, 1000)
                if slug == 'deep-time':
                    browser.evaluate("drill('triassic'); true")
                    selection = 'Triassic interval'
                elif slug == 'brain':
                    browser.evaluate("(()=>{const n=[...document.querySelectorAll('svg circle, svg [role=button]')].find(n=>n.textContent.includes('Orbitofrontal'));if(!n)throw Error('OFC marker missing');n.dispatchEvent(new MouseEvent('click',{bubbles:true}));return true})()")
                    browser.evaluate("(()=>{const b=document.getElementById('depthButton');if(b.getAttribute('aria-pressed')!=='true')b.click();return true})()")
                    strength = browser.evaluate("document.getElementById('awDepthStrength').selectedOptions[0].textContent")
                    selection = f'Orbitofrontal cortex, lateral schematic; estimated depth on ({strength.lower()})'
                    if component['release_version'] == '1.22.0':
                        browser.call('Emulation.setEmulatedMedia', {'features': [{'name': 'prefers-reduced-motion', 'value': 'reduce'}]})
                        reduced = browser.evaluate("getComputedStyle(document.querySelector('#tree .region.sel')).transitionDuration==='0s'")
                        browser.call('Emulation.setEmulatedMedia', {'features': []})
                        if not reduced:
                            raise RuntimeError('Brain controls ignore reduced-motion preference')
                        capture_checks['reduced_motion_control_transition'] = 'pass'
                elif slug == 'mythology':
                    browser.evaluate("selectFigure('zeus'); true")
                    browser.evaluate("(()=>{if(!document.getElementById('profileHead').innerText.includes('Zeus'))throw Error('Zeus selection failed');return true})()")
                    artwork_view = browser.evaluate("!document.getElementById('awMythArtworkStage').hidden")
                    selection = 'Greek Zeus, artwork view' if artwork_view else 'Greek Zeus, family tree view'
                else:
                    selection = 'Initial default view in clean browser profile'
                browser.evaluate('new Promise(resolve => setTimeout(resolve, 600))')
                actual = output / f'{slug}-actual.png'
                browser.call('Emulation.setDeviceMetricsOverride', {'width': 1440, 'height': 1000, 'deviceScaleFactor': 2, 'mobile': False})
                browser.screenshot(actual)
                goals = [{'path': ROOT / 'atlas/images' / name, 'crop': crop,
                          'approval': 'approved visual direction' if name.startswith('goal_') else 'proposed concept, not approved'}
                         for name, crop in references]
                done, earlier_count, pending, hidden = task_lists(title, version)
                annotation_note = 'No app layout changed this update.'
                annotated = actual
                highlight = None
                if slug in HIGHLIGHT and any(t['id'] == HIGHLIGHT[slug][0] for t in done):
                    task_id, selector, label = HIGHLIGHT[slug]
                    rect = browser.evaluate(f'''(()=>{{const n=document.querySelector({json.dumps(selector)});if(!n)throw Error('Missing highlight target');const r=n.getBoundingClientRect();return {{x:r.x,y:r.y,w:r.width,h:r.height}}}})()''')
                    browser.evaluate(f'''(()=>{{const r={json.dumps(rect)},d=document.createElement('div');d.id='wl-highlight';d.style='position:fixed;inset:0;z-index:2147483647;pointer-events:none';d.innerHTML=`<svg width="100%" height="100%"><rect x="${{r.x+2}}" y="${{r.y+2}}" width="${{r.w-4}}" height="${{r.h-4}}" rx="10" fill="none" stroke="#ffc247" stroke-width="5"/><rect x="${{r.x+8}}" y="${{r.y+8}}" width="290" height="38" rx="8" fill="#ffc247"/><text x="${{r.x+18}}" y="${{r.y+34}}" font-family="sans-serif" font-size="20" font-weight="bold" fill="#101820">{task_id} · verified area</text></svg>`;document.body.append(d);return true}})()''')
                    annotated = output / f'{slug}-actual-annotated.png'
                    browser.screenshot(annotated)
                    browser.evaluate("document.getElementById('wl-highlight').remove();true")
                    highlight = {'task_id': task_id, 'selector': selector, 'bounds_css_px': rect,
                                 'label': label, 'file': annotated.name, 'sha256': digest(annotated)}
                    annotation_note = f'{task_id} marks the {label.lower()}; this release verified offline coverage without changing the app.'
                metadata = {'widget': slug, 'widget_version': component['release_version'], 'repository_version': version,
                            'captured_at': datetime.now(timezone.utc).isoformat(), 'browser': browser.version,
                            'source': component['authoritative_source'], 'source_sha256': digest(source),
                            'actual_sha256': digest(actual), 'annotated_actual_sha256': digest(annotated),
                            'annotation_note': annotation_note, 'highlight': highlight,
                            'viewport': [1440, 1000], 'device_scale_factor': 2, 'selection': selection,
                            'goals': [{'path': str(g['path'].relative_to(ROOT)), 'sha256': digest(g['path']), 'crop': g['crop'], 'approval': g['approval']} for g in goals],
                            'complete_this_release': done, 'completed_earlier_count': earlier_count,
                            'pending_top_priority': pending, 'pending_summary': hidden,
                            'capture_checks': capture_checks,
                            'runtime_exceptions': [e['params']['exceptionDetails'] for e in browser.events if e.get('method') == 'Runtime.exceptionThrown'],
                            'review_scope': 'Fresh browser rendering and selected state only; full functional/scientific review pending.'}
                page = output / f'{slug}-comparison.html'
                page.write_text(render_report(title, actual, goals, done, earlier_count, pending, hidden, metadata))
                browser.navigate(page, 2240, 1100)
                height = browser.evaluate('Math.ceil(document.documentElement.scrollHeight)')
                browser.call('Emulation.setDeviceMetricsOverride', {'width': 2240, 'height': height, 'deviceScaleFactor': 2, 'mobile': False})
                browser.evaluate('new Promise(resolve => setTimeout(resolve, 300))')
                comparison = output / f'{slug}-comparison.png'
                browser.screenshot(comparison)
                metadata['comparison_sha256'] = digest(comparison)
                (output / f'{slug}-evidence.json').write_text(json.dumps(metadata, indent=2) + '\n')
                records.append(slug)
                print(f'Captured {slug}: {len(done)} recent, {len(pending)} shown, {hidden["total"]} summarized', flush=True)
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
