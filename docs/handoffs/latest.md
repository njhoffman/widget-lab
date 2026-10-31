# Codex handoff — offline artwork verification 0.4.2

Date: 2026-10-31 (America/Chicago). Base: `6bd0e9f` / tag `v0.4.1`. Repository patch release 0.4.2 completes high-priority verification tasks without changing widget HTML, data, stored-state formats or component versions.

## Delivered

Closed T011 (172/172 indexed Deep Time intervals resolve direct artwork), T040 (363/363 tradition-specific Mythology figure illustrations available offline), T078 (canonical Shared Taxa unchanged), and WL-023 (repeatable exhaustive offline artwork QA). T012 remains open: parity with adjacent files and isolated standalone decoding does not prove a separately runnable bundle edition and its offline navigation. Broader WL-006 remains in progress.

`tools/test_atlas_artwork.py` copies current HTML into an otherwise empty temporary folder, uses a clean Chrome profile with networking disabled and HTTP(S) blocked, matches runtime indexed IDs uniquely against asset manifests, compares embedded hero/thumbnail bytes with adjacent files, and decodes every image with nonzero dimensions. All 535 IDs and 1,070 images pass. Mythology's separate featured Zeus adapter remains covered by the existing build/browser suite; this exhaustive mapping audit covers the original figure library. No artwork is promoted or newly approved.

`just artwork-test` repeats the audit. Evidence defaults to `docs/artwork-tests/<VERSION>/` and refuses overwrites; use `--output /tmp/...` for exploration. `repository.artwork_regression_report` registers the current report. The project guard rejects incomplete or failed evidence, missing decode rows, and stale source/manifest/adjacent-asset hashes. Unit regressions cover corrupted embedded thumbnails, duplicate manifest IDs, missing decodes/IDs and stale sources.

## Audit trail and verification

Deep Time/Mythology specs advance from revision 4 to 5 to document verification acceptance and limits; component changelogs, context, root CHANGELOG, VERSION, manifest, TODO and developer documentation are synchronized. New files include the audit driver, two unit tests and source-hashed evidence/readme under `docs/artwork-tests/0.4.2/`. Prior handoff is preserved as `2026-10-30-release-0.4.1.md`.

Fresh canonical integrity evidence: 90/90 files and 15/15 schemas pass in `docs/artwork-tests/0.4.2/data-integrity.json`. Full Atlas/import/JavaScript audit and all 16 unit tests pass via `just check`. No widget, asset or canonical dataset source bytes changed. The complete three-widget browser matrix and selected-state screenshots are retained under `docs/browser-tests/0.4.2/`; all 45 scenarios and 341 assertions pass.

Fresh Deep Time and Mythology actual-versus-goal PNGs were captured, inspected, and automatically opened with feh under `docs/visual-reviews/0.4.2/`. They reflect T011/T040 completion; viewer.json records successful launch. Both original goal images and previous evidence remain unchanged. Current per-widget evidence pointers identify the new captures; Brain source/comparison remain unchanged.

## Remaining limits and next tasks

Image decoding and matching bytes do not certify scientific reconstruction, cultural accuracy, rights or final artwork approval. Existing procedural/symbolic and AI-concept disclosures remain. Windows, folder-picker/IndexedDB persistence, screen readers/contrast, all-region anatomy and registered 3D remain separate work. T012's bundle edition and T021's canonical taxon provenance remain open. Safe next work includes scoped header/overlay/history verification against existing acceptance criteria; proposed new artwork/features require approval before implementation.

Finish by committing, annotated-tagging v0.4.2, atomically pushing and verifying remote objects. The final response reports actual publication outcome.
