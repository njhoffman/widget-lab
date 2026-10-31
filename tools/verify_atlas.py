#!/usr/bin/env python3
"""Verify the imported Atlas baseline without executing widget applications."""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import subprocess
import sys

from verify_migration import ROOT, safe_file


class Scripts(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.active = False
        self.current = []
        self.scripts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'script':
            self.active = not attrs.get('src') and attrs.get('type', '').lower() in ('', 'text/javascript', 'application/javascript')
            self.current = []

    def handle_data(self, data):
        if self.active:
            self.current.append(data)

    def handle_endtag(self, tag):
        if tag == 'script' and self.active:
            self.scripts.append(''.join(self.current))
            self.active = False


def audit():
    errors = []
    inventory = json.loads((ROOT / 'docs/migration/atlas_import_inventory.json').read_text())
    for entry in inventory['files']:
        path = safe_file(ROOT, entry['destination'])
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256']:
            errors.append({'path': entry['destination'], 'check': 'import_checksum'})

    artwork = 0
    for manifest in (ROOT / 'atlas/assets').glob('*/manifest.json'):
        data = json.loads(manifest.read_text())
        entries = data.get('entries', data.get('views', list(data.get('assets', {}).values())))
        for entry in entries:
            name = entry.get('hero', entry.get('illustration', entry.get('path')))
            path = safe_file(manifest.parent, name)
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != entry['sha256']:
                errors.append({'path': str(path.relative_to(ROOT)), 'check': 'artwork_checksum'})
            for field in ('thumb', 'thumbnail'):
                if entry.get(field) and not safe_file(manifest.parent, entry[field]).is_file():
                    errors.append({'path': entry[field], 'check': 'missing_thumbnail'})
            artwork += 1

    catalog = json.loads((ROOT / 'atlas/data/project_catalog_v1.21.json').read_text())
    versions = []
    baseline = json.loads((ROOT / 'atlas/docs/v1.20_source_checksums.json').read_text())
    for widget in catalog['widgets']:
        path = safe_file(ROOT / 'atlas', widget['file'])
        text = path.read_text()
        expected = widget['version']
        title = text.split('<title>', 1)[1].split('</title>', 1)[0]
        if expected not in title:
            errors.append({'path': widget['file'], 'check': 'title_version'})
        old_hash = baseline.get(widget['file'])
        if old_hash and hashlib.sha256(path.read_bytes()).hexdigest() != old_hash:
            errors.append({'path': widget['file'], 'check': 'prior_scientific_widget_checksum'})
        versions.append({'file': widget['file'], 'title': title, 'catalog_version': expected,
                         'matches_v1_20_checksum': bool(old_hash)})

    html_files = sorted((ROOT / 'atlas/widgets').glob('*.html'))
    html_files += sorted((ROOT / 'atlas/tools').glob('*.html'))
    html_files += [ROOT / 'atlas/MASTER_DASHBOARD_v1.21.html', ROOT / 'atlas/index.html']
    syntax = {'status': 'not_run', 'reason': 'Node.js unavailable'}
    if shutil.which('node'):
        count = 0
        for path in html_files:
            parser = Scripts()
            parser.feed(path.read_text())
            for script in parser.scripts:
                result = subprocess.run(['node', '-e', 'new Function(require("fs").readFileSync(0,"utf8"))'],
                                        input=script, text=True, capture_output=True)
                if result.returncode:
                    errors.append({'path': str(path.relative_to(ROOT)), 'check': 'javascript_syntax', 'detail': result.stderr[:1500]})
                count += 1
        syntax = {'status': 'pass' if not any(e['check'] == 'javascript_syntax' for e in errors) else 'fail',
                  'html_files': len(html_files), 'scripts': count}
    return {'status': 'pass' if not errors and syntax['status'] == 'pass' else 'incomplete',
            'imported_files_checked': len(inventory['files']), 'artwork_records_checked': artwork,
            'versions': versions, 'javascript_syntax': syntax, 'errors': errors,
            'limitations': ['No interactive browser, IndexedDB, folder-picker, or offline persistence testing.',
                            'Checksums and syntax do not certify scientific accuracy or artwork approval.',
                            'Distribution download ZIPs remain in incoming; original dashboard download links are unavailable.']}


if __name__ == '__main__':
    report = audit()
    print(json.dumps(report, indent=2))
    sys.exit(0 if report['status'] == 'pass' else 1)
