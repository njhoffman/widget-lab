# Codex handoff — 2026-10-30

Atlas migration setup is complete for the available source package. The goal-image visual direction is documented; a redesigned widget release has not been implemented.

## Baseline and authority

Base commit: `f9f88dc` (`initial commit`); work remains uncommitted. User authorized inspection of incoming artifacts and curation of relevant project extracts after initial repository restrictions blocked access. Raw chats and account exports remain private.

Imported master dashboard v1.21 and seven widgets unchanged: Brain 1.21, Deep Time 1.18, Tree of Life 1.14, Mythology 1.13, Muscles 1.8, Emergence 1.10, Launcher 1.14. Actual titles/catalog agree, and six scientific widgets match v1.20 source checksums. The manifest now records source identities and verification scope. Quiz versions remain null/unverified.

## Changed files and audit trail

- `atlas/`: delivered HTML, project catalogs, tools, artwork, goal references, and historical release/QA documents, preserving relative layout. Distribution ZIPs excluded.
- `shared/taxa/`: restored manifest-matching README and two source archive ZIPs from the complete Atlas copy; all other imported dataset records preserved. Scaffold README retained in `docs/migration/`.
- `project_manifest.json`, root README, `atlas/specs/*.md` revision 1, component READMEs/changelogs, curated Atlas/Shared Taxa context, migration decision, and tooling/test instructions.
- `tools/verify_migration.py`, `tools/verify_atlas.py`, `tests/test_verify_migration.py`, and current reports in `docs/migration/`.
- `docs/migration/atlas_import_inventory.json`: 1,321 imported file records with source/destination, size, SHA-256. Original bootstrap CSV remains intact. No raw transcript was copied.

## Validation

Run from repository root:

```sh
python3 tools/verify_migration.py --output docs/migration/verification_report.json
python3 tools/verify_atlas.py > docs/migration/atlas_verification_report.json
python3 -m unittest discover -s tests -v
```

Current results: Shared Taxa 90/90 size/checksum matches; 15 JSON/schema checks pass including manifest. All 1,321 imported file records match; 543 artwork records match their hero/reference hashes and required thumbnails exist. JavaScript syntax passes for 39 inline scripts across 14 current widget/tool/dashboard pages. Two audit regression tests pass. Static src/href checks found no missing literal file targets in current dashboard/index/widget pages; dynamically constructed download actions are outside that check.

## Known limitations and next work

No interactive browser testing was performed. Folder picker, IndexedDB, offline launcher import/export, accessibility, and viewport regressions remain open. Historical package QA reports are preserved, not represented as fresh results. Artwork and scientific accuracy remain unreviewed; Brain is schematic/estimated-depth, not a registered 3D model. Dataset's 57 documented ambiguities remain.

Read `atlas/specs/visual-direction.md` for the approved direction from both goal pictures. Next visual work should first capture current Deep Time, Brain, and Mythology selections and browser regressions, then improve layout/artwork without dropping functionality. Historical suggestions and the proposed sequence remain unapproved implementation details.

The original Atlas dataset copy is retained alongside canonical Shared Taxa for compatibility. Distribution ZIPs remain in `incoming/`; dashboard package-download actions are unavailable. Import checks intentionally freeze original source/artifact bytes; future implementation should preserve originals and introduce reviewed new sources/releases rather than silently refreshing baseline checksums.

Launch with `python3 -m http.server 8765 --bind 127.0.0.1 --directory atlas` and open `http://localhost:8765/`. Stable origins preserve browser storage; no prior browser progress was imported. No commit, push, deployment, release, or cloud synchronization was performed.
