# Codex handoff — Mythology visual batch 0.3.0

Date: 2026-10-30 (America/Chicago). Base: `0a1f2e6` / tag `v0.2.0`. Repository advances to 0.3.0 for Mythology Atlas 1.14.0; the original 1.13 standalone remains unchanged. Deep Time/Brain current sources are unchanged.

## Delivered

Artwork-first Mythology view using the existing native artwork mode, clear Artwork / Family tree controls, compact search header, selected-figure composition, and readable profile styling. The existing verified Greek Zeus concept image is embedded offline; its modern/AI and pending cultural-review disclosure remains visible. Other figures retain original local illustrations; no new artwork or cultural/historical claims.

Related thumbnails now use exact active-tradition keys instead of Greek-first lookup. Profile panes reset to the figure heading after identity changes, tree-only legends stay out of artwork mode, and screenshot resets use instant scrolling to avoid partially captured headers. Original filters, IDs, records, complementary names, genealogy/relationship handlers and historical entries are retained.

Current launch page routes to 1.14.0. Editable CSS/JS is under `atlas/widgets/mythology/src/`; `tools/build_mythology.py` verifies the import and featured image hashes, then adds presentation blocks and a new title to a separate standalone file. Preservation tests remove only those allowed changes and compare every remaining original byte.

## Tasks and specs

Closed WL-016, WL-017, WL-018, T043, T044, T045 and T048 with browser/source evidence. Broader WL-006 remains in progress for Brain/general layout and art work. T041/T042/T047, I005's full licensed historical-artwork workflow, and T049's gallery provenance categories remain open; current disclosures/related-figure labels are recorded as partial progress.

Mythology spec is revision 4 and shared visual direction is revision 5. Version/changelog/manifest/TODO, component docs, context, current launch page, build/test instructions and handoff are synchronized. Prior handoff is archived as `2026-10-30-release-0.2.0.md`.

## Verification

45/45 Chrome/Linux scenarios and 259 recorded assertions pass across three widgets and 390/768/1440px; the JSON report records per-assertion details and current source hashes under `docs/browser-tests/0.3.0/`. Added Mythology checks cover initial artwork mode/disclosure, header search, mode switching with retained selected ID, keyboard view activation, parent/child links, profile scroll reset, native group/story/symbol filters, complementary names without identity changes, all five traditions' exact related/result thumbnail keys, selected state, tree legend visibility and reduced motion.

13 unit tests pass, including original Mythology byte preservation and verified offline Zeus asset identity. Existing import/Shared Taxa/artwork checks pass unchanged; active-source title/version and current launch links are checked, and standalone scripts compile. New source/actual/goal/comparison hashes are validated by the project guard. 54 inline scripts across 17 HTML pages compile; 90 Shared Taxa manifest entries/15 schemas, 543 artwork records, and 1,321 imported file records pass unchanged.

Fresh Mythology actual-versus-goal PNG/HTML/actual image/JSON under `docs/visual-reviews/0.3.0/` records the artwork view and completed/pending task snapshot. Automatic feh launch is recorded in viewer.json. Finalization commits, annotated-tags, atomically pushes, and verifies remote objects; the final response states the actual outcome.

## Limits and next work

This reuses a concept derivative; it is not new bespoke portrait coverage or an approved historical-artwork library. No original genealogy, cultural records, identifiers, progress format, dataset, or scientific values changed. Linux Chrome coverage does not include Windows storage, full accessibility/screen-reader/contrast, or cultural/scientific review. Existing external artwork previews are optional and HTTP(S) was blocked during deterministic capture.

Next scoped WL-006 candidate: Brain layout, with truthful schematic/estimated-depth labels and preserved hierarchy, regions/circuits, time filters and explanatory panels. Continue source-preserving standalone builds, browser checks, actual-versus-goal evidence/feh, and routine validated releases.
