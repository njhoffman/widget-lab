#!/usr/bin/env python3
"""Exhaustively verify indexed artwork bytes and decoding in isolated offline widgets."""
import argparse
import base64
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile

from capture_atlas_comparisons import Browser, digest
from verify_migration import ROOT, safe_file


CONFIG = {
    'deep-time': ('deep_time', 'id', 'thumb', 'ARTWORK_MAP', 'thumbnailData', 172),
    'mythology': ('mythology', 'key', 'thumbnail', 'ART', 'THUMB', 363),
}


def embedded_map(source, name):
    match = re.search(r'\bconst\s+' + re.escape(name) + r'\s*=\s*', source)
    if not match:
        raise ValueError(f'Missing embedded mapping: {name}')
    value, _ = json.JSONDecoder().raw_decode(source[match.end():])
    if not isinstance(value, dict):
        raise ValueError(f'Invalid embedded mapping: {name}')
    return value


def compare_bytes(entries, key_field, thumb_field, hero, thumb, asset_root):
    """Compare every embedded byte with its adjacent edition, including thumbnails."""
    keys = [entry[key_field] for entry in entries]
    errors = []
    if len(keys) != len(set(keys)):
        errors.append('Duplicate manifest IDs')
    for kind, mapping in [('hero', hero), (thumb_field, thumb)]:
        if set(mapping) != set(keys):
            errors.append(f'{kind} mapping IDs differ from manifest')
    rows = []
    for entry in entries:
        row = {'id': entry[key_field], 'assets': {}, 'status': 'pass'}
        for kind, mapping in [('hero', hero), (thumb_field, thumb)]:
            try:
                uri = mapping[entry[key_field]]
                header, payload = uri.split(',', 1)
                if not header.startswith('data:image/') or not header.endswith(';base64'):
                    raise ValueError('Expected an embedded base64 image')
                data = base64.b64decode(payload, validate=True)
                path = safe_file(asset_root, entry[kind])
                checksum = hashlib.sha256(data).hexdigest()
                if data != path.read_bytes():
                    raise ValueError('Embedded and adjacent image bytes differ')
                if kind == 'hero' and checksum != entry['sha256']:
                    raise ValueError('Hero checksum differs from manifest')
                row['assets'][kind] = {'path': str(path.relative_to(ROOT)), 'sha256': checksum}
            except (KeyError, ValueError, OSError) as error:
                row['status'] = 'fail'
                row['assets'][kind] = {'error': str(error)}
        rows.append(row)
    return rows, errors


def check_widget(browser, component, isolated):
    slug = component['slug']
    folder, key_field, thumb_field, hero_name, thumb_name, expected = CONFIG[slug]
    source = safe_file(ROOT, component['authoritative_source'])
    text = source.read_text()
    manifest_path = ROOT / 'atlas/assets' / folder / 'manifest.json'
    manifest = json.loads(manifest_path.read_text())
    entries = manifest['entries']
    rows, errors = compare_bytes(entries, key_field, thumb_field,
                                embedded_map(text, hero_name), embedded_map(text, thumb_name), manifest_path.parent)
    # Copy just the HTML: no adjacent assets, original path or cached profile can help it.
    standalone = isolated / source.name
    standalone.write_bytes(source.read_bytes())
    browser.events.clear()
    browser.navigate(standalone, 1440, 1000)
    if slug == 'deep-time':
        runtime = browser.evaluate('AtlasDeepTimeArtwork.coverage()')
        runtime_keys = [row['id'] for row in runtime]
        if any(not row['direct'] or row['scene'] != row['id'] for row in runtime):
            errors.append('An indexed interval inherits artwork instead of resolving directly')
        # Private embedded maps are read from the loaded script, without altering app behavior.
        browser.evaluate('''window.__artworkAuditMap = name => {
          const text=[...document.scripts].map(s=>s.textContent).find(t=>t.includes('const '+name+'='));
          const start=text.indexOf('const '+name+'=')+('const '+name+'=').length;
          return JSON.parse(text.slice(start,text.indexOf('};',start)+1));
        }; window.__artworkAuditHero=__artworkAuditMap('ARTWORK_MAP');
        window.__artworkAuditThumb=__artworkAuditMap('thumbnailData'); true''')
        resolver = '(kind === "hero" ? __artworkAuditHero[key] : __artworkAuditThumb[key])'
    else:
        runtime_keys = browser.evaluate('Object.entries(TRADITIONS).flatMap(([tradition,t])=>t.data.map(n=>tradition+":"+n.id))')
        resolver = '(kind === "hero" ? AtlasMythologyArtwork.sceneFor(key) : AtlasMythologyArtwork.thumbFor(key))'
    keys = [entry[key_field] for entry in entries]
    if len(runtime_keys) != expected or len(set(runtime_keys)) != expected or set(runtime_keys) != set(keys):
        errors.append(f'Expected {expected} unique application IDs matching the artwork manifest')
    decoded = []
    # Bounded batches keep memory and CDP response times predictable for all 1,070 images.
    for offset in range(0, len(keys), 24):
        decoded.extend(browser.evaluate('''(async () => {
          const rows=[];
          for(const key of KEYS) for(const kind of ['hero','thumbnail']) {
            const src=RESOLVER;
            try {
              if(!src || !src.startsWith('data:image/')) throw Error('Not an embedded image');
              const image=new Image(); image.src=src;
              await Promise.race([image.decode(),new Promise((_,reject)=>setTimeout(()=>reject(Error('Decode timed out')),5000))]);
              if(!image.naturalWidth || !image.naturalHeight) throw Error('Empty image');
              rows.push({id:key,kind,status:'pass',width:image.naturalWidth,height:image.naturalHeight});
            } catch(error) {rows.push({id:key,kind,status:'fail',error:String(error)});}
          }
          return rows;
        })()'''.replace('KEYS', json.dumps(keys[offset:offset + 24])).replace('RESOLVER', resolver)))
    for row in rows:
        row['decode'] = [result for result in decoded if result['id'] == row['id']]
        if len(row['decode']) != 2 or any(result['status'] != 'pass' for result in row['decode']):
            row['status'] = 'fail'
    exceptions = [e['params']['exceptionDetails'] for e in browser.events if e.get('method') == 'Runtime.exceptionThrown']
    if exceptions:
        errors.append('Runtime exceptions during isolated offline loading')
    return {'widget': slug, 'source': component['authoritative_source'], 'source_sha256': digest(source),
            'manifest': str(manifest_path.relative_to(ROOT)), 'manifest_sha256': digest(manifest_path),
            'expected': expected, 'indexed': len(runtime_keys), 'images_decoded': len(decoded),
            'status': 'fail' if errors or any(row['status'] != 'pass' for row in rows) else 'pass',
            'errors': errors, 'runtime_exceptions': exceptions, 'entries': rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'docs/artwork-tests' / (ROOT / 'VERSION').read_text().strip())
    args = parser.parse_args()
    executable = shutil.which('google-chrome') or shutil.which('chromium')
    if not executable:
        parser.error('Chrome/Chromium is required')
    if (args.output / 'report.json').exists():
        parser.error('Refusing to overwrite existing artwork evidence; use a new output directory')
    registry = json.loads((ROOT / 'project_manifest.json').read_text())
    with tempfile.TemporaryDirectory(prefix='widget-lab-artwork-') as temporary:
        root = Path(temporary)
        standalone = root / 'standalone'
        standalone.mkdir()
        browser = Browser(executable, root / 'profile')
        try:
            browser.call('Network.emulateNetworkConditions', {'offline': True, 'latency': 0, 'downloadThroughput': 0, 'uploadThroughput': 0})
            results = []
            for slug in CONFIG:
                component = next(c for c in registry['atlas'] if c['slug'] == slug)
                result = check_widget(browser, component, standalone)
                results.append(result)
                print(f'{slug}: {result["status"]}, {result["indexed"]} IDs, {result["images_decoded"]} images', flush=True)
            report = {'repository_version': (ROOT / 'VERSION').read_text().strip(),
                      'captured_at': datetime.now(timezone.utc).isoformat(), 'browser': browser.version,
                      'mode': 'file:// isolated HTML copies; clean temporary profile; network offline and HTTP(S) blocked',
                      'status': 'pass' if all(r['status'] == 'pass' for r in results) else 'fail', 'results': results,
                      'limits': ['Image coverage, byte parity and browser decoding only; no scientific/cultural approval.',
                                 'Adjacent bundle paths are checked as files; this does not test a separate bundle edition or Windows.',
                                 'Existing interaction and visual regression reports remain separate.']}
        finally:
            browser.close()
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'report.json').write_text(json.dumps(report, indent=2) + '\n')
    return report['status'] != 'pass'


if __name__ == '__main__':
    sys.exit(main())
