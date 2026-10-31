#!/usr/bin/env python3
"""Read-only import audit. Never rebuild data or infer release authority."""
import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIVATE = {'.local', 'incoming', '.git'}


def safe_file(root, relative):
    path = Path(relative)
    if path.is_absolute() or '..' in path.parts or PRIVATE.intersection(path.parts):
        raise ValueError(f'Forbidden inventory path: {relative}')
    target = root / path
    # Do not follow symlinks into private or external locations.
    if any(p.is_symlink() for p in [target, *target.parents]):
        raise ValueError(f'Symlink inventory path: {relative}')
    return target


def audit(root):
    registry = json.loads((root / 'project_manifest.json').read_text())
    dataset = root / 'shared/taxa'
    manifest = json.loads((dataset / 'manifest.json').read_text())
    findings = []
    matched = 0
    for entry in manifest['files']:
        relative = entry['path']
        try:
            path = safe_file(dataset, relative)
        except ValueError as error:
            findings.append({'path': relative, 'status': 'unsafe', 'detail': str(error)})
            continue
        if not path.is_file():
            findings.append({'path': relative, 'status': 'missing'})
            continue
        content = path.read_bytes()
        if len(content) != entry['size_bytes'] or hashlib.sha256(content).hexdigest() != entry['sha256']:
            findings.append({'path': relative, 'status': 'checksum_mismatch'})
        else:
            matched += 1

    schemas = {'status': 'not_run', 'reason': 'Install jsonschema to check imported schemas.'}
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        pass
    else:
        errors = []
        checked = 0
        for entry in [*manifest['files'], {'path': 'manifest.json'}]:
            name = entry['path']
            if '/' in name or not name.endswith('.json'):
                continue
            data_path = safe_file(dataset, name)
            schema_path = safe_file(dataset, f'schemas/{name}.schema.json')
            if not data_path.is_file() or not schema_path.is_file():
                errors.append({'path': name, 'detail': 'Data or schema missing'})
                continue
            try:
                schema = json.loads(schema_path.read_text())
                # Audits must stay offline; imported schemas currently use no refs.
                if '"$ref"' in json.dumps(schema):
                    raise ValueError('References require an explicitly reviewed offline resolver')
                Draft202012Validator.check_schema(schema)
                validator = Draft202012Validator(schema)
                for error in validator.iter_errors(json.loads(data_path.read_text())):
                    errors.append({'path': name, 'location': list(error.absolute_path), 'detail': error.message})
                checked += 1
            except (ValueError, TypeError) as error:
                errors.append({'path': name, 'detail': str(error)})
        schemas = {'status': 'pass' if checked and not errors else 'fail', 'files_checked': checked, 'errors': errors}

    components = []
    source_errors = []
    for family in ('atlas', 'quiz'):
        for component in registry[family]:
            folder = safe_file(root, f'{family}/widgets/{component["slug"]}/src')
            html = sorted(str(p.relative_to(root)) for p in folder.glob('*.html') if not p.is_symlink())
            if component.get('authoritative_source'):
                source = safe_file(root, component['authoritative_source'])
                if source.is_file():
                    html.append(str(source.relative_to(root)))
                    if component.get('sha256') and hashlib.sha256(source.read_bytes()).hexdigest() != component['sha256']:
                        source_errors.append({'path': str(source.relative_to(root)), 'status': 'checksum_mismatch'})
                else:
                    source_errors.append({'path': component['authoritative_source'], 'status': 'missing'})
            elif component['verified']:
                source_errors.append({'component': component['slug'], 'status': 'verified_without_source'})
            components.append({'family': family, 'slug': component['slug'], 'html_sources': html,
                               'release_version': component['release_version'], 'verified': component['verified']})
    complete = not findings and not source_errors and schemas['status'] == 'pass'
    return {
        'status': 'pass' if complete else 'incomplete',
        'scope': 'Imported file integrity and JSON schemas only; no scientific or widget release certification.',
        'shared_taxa': {'claimed_version': manifest['dataset_version'],
                        'files_listed': len(manifest['files']), 'files_matching': matched,
                        'findings': findings, 'schemas': schemas},
        'components': components,
        'component_source_findings': source_errors,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Save JSON report relative to repository root')
    args = parser.parse_args()
    report = audit(ROOT)
    rendered = json.dumps(report, indent=2) + '\n'
    if args.output:
        safe_file(ROOT, args.output).write_text(rendered)
    else:
        print(rendered, end='')
    return 0 if report['status'] == 'pass' else 1


if __name__ == '__main__':
    raise SystemExit(main())
