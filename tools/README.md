# Developer tooling

Run from the repository root:

```sh
python3 tools/verify_migration.py
python3 tools/verify_atlas.py
```

Migration verification checks Shared Taxa's recorded sizes/checksums and JSON schemas, plus registered source hashes. It reports missing optional validation dependencies as incomplete and exits nonzero. It never rebuilds scientific data. Install Python `jsonschema` for schema checks.

Atlas verification checks imported artifacts against `docs/migration/atlas_import_inventory.json`, artwork manifests, delivered widget versions, the prior scientific-widget baseline, and inline JavaScript syntax via Node.js. It does not execute applications or certify scientific/artwork approval.

Both tools operate on imported repository artifacts. They reject private/traversal/symlink inventory paths and do not open incoming files or raw conversations. The existing inventory's source strings are provenance only; verification reads destination paths.

Original imported bytes are a frozen baseline. Preserve them when developing future versions; do not regenerate the inventory to conceal a changed original. Run `python3 -m unittest discover -s tests -v` for audit regression checks.

The imported `shared/taxa/tools/build_shared_taxa_v1.py` is historical release tooling. Do not run it against the canonical package as a setup step: it can rewrite published data and evidence.

`python3 tools/check_project.py` checks repository SemVer, manifest/changelog consistency, task formatting/statuses, complete coverage of the 137 imported task IDs, and current visual evidence hashes. It rejects stale source/goal/screenshot evidence and recorded browser exceptions.

`python3 tools/capture_atlas_comparisons.py --widgets deep-time brain mythology` captures actual applications in headless Chrome, renders comparison reports against original goal references using HTML/CSS, and automatically opens the PNGs in feh. It uses a temporary clean browser profile and local debugging endpoint, blocks external HTTP(S), and leaves original widget bytes unchanged. It refuses to overwrite an existing version/widget comparison. `--no-open` is for CI only. Outputs live under `docs/visual-reviews/<VERSION>/`.

Install Python dependencies from `requirements-dev.txt`; Chrome/Chromium and feh are system prerequisites. Follow `docs/development-workflow.md` for release/version/task maintenance.
