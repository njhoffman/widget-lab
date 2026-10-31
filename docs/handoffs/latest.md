# Codex handoff — Brain visual batch 0.4.0

Date: 2026-10-30 (America/Chicago). Base: `2cf49b9` / tag `v0.3.0`. Repository advances to 0.4.0 for Brain Atlas 1.22.0; original 1.21 remains unchanged. Current Deep Time/Mythology source files are unchanged.

## Delivered

Native projection/estimated-depth controls and strength selection now sit in a compact responsive header. Selected-region context is larger; orientation reference and depth context are moved off the interactive drawing. Desktop details scroll locally, while mobile/tablet details remain in document flow. The hierarchy retains usable widths and selected controls at each target viewport.

The SVG geometry, transforms, original region/circuit records, scientific/clinical text, original handlers and depth mathematics are unchanged. This remains authored schematic anatomy, with explicit estimated/not-volumetric labels. No new image assets, registered model, calibrated geometry, anatomical claims or progress migration. Depth strength is disabled while depth is off; startup remains unselected/depth-off.

## Tasks and specifications

Closed WL-019 (Brain visual layout), WL-020 (native projection/depth verification), WL-021 (mobile hierarchy grid), T025/T026/T029, and I003 through its accepted explicit-labeling alternative. I003's live title now states that labeling resolution; it does not imply a registered model. T027/T032/T033/T037/T039 remain open for wider assets, selected-inset overlays and anatomical/all-region alignment review. The broader WL-006 task remains in progress beyond these three first visual batches.

Brain spec is revision 4; shared visual direction is revision 6. Version/changelog/manifest/TODO, component docs, context, current launch page and build/check instructions are synchronized. Editable adapter is under `atlas/widgets/brain/src/`; builder is `tools/build_brain.py`. Prior standalone/history entries are retained. Previous handoff is archived as `2026-10-30-release-0.3.0.md`.

## Verification

45/45 Chrome/Linux scenarios and 341 recorded assertions pass across Deep Time/Brain/Mythology at 390/768/1440px; detailed source hashes and assertions are in `docs/browser-tests/0.4.0/`. Brain checks add header containment/compactness, keyboard OFC selection, retained hierarchy/identity across all projections, marker bounds, three distinct orientation references, per-projection depth on/off, Low/Medium/High opacity/radius differences, crisp selected marker, restored cues, explicit labels, time preset/reset counts, actual panel/control widths and native hierarchy click.

14 unit tests pass, including complete Brain import byte preservation after removing only added presentation blocks and reversing the title. Original Shared Taxa/artwork/import files remain unchanged: 90 dataset entries/15 schemas, 543 artwork records and 1,321 import records pass. Active title/version and current links are checked; 62 inline scripts across 18 HTML pages compile. Actual/goal/comparison source hashes are checked by the project guard.

A draft regression caught schematic text moving outside the drawing; a visible note remains beside the map. Screenshot review exposed an implicit-column mobile collapse despite no document overflow; matching responsive selector specificity fixed it and new width/click assertions prevent regression. Intermediate diagnostics stayed outside committed evidence.

Fresh Brain comparison under `docs/visual-reviews/0.4.0/` uses OFC/lateral schematic with estimated depth on at native Medium, matching the goal's mode. Older comparisons used depth-off and are retained. Capture JSON records that configuration and a passing reduced-motion control-transition check; default product startup is unchanged. Automatic feh opening is recorded in viewer.json.

Finalization commits, annotated-tags, atomically pushes and verifies remote objects; the final response states the actual commit/tag/push outcome.

## Remaining limits and next work

Orientation references update by projection but do not highlight a registered selected structure. Representative native bounds/selection checks are not all-region anatomical validation, medical imaging, clinical advice, or independent scientific review. Windows/storage/folder-picker, full screen-reader/contrast/touch accessibility and registered 3D remain separate tasks. No scientific dates/relationships or source records changed.

The first Deep Time, Mythology and Brain layout batches are complete. Continue with concrete remaining QA/compatibility tasks or a separately scoped visual/artwork batch; preserve originals and avoid claiming full goal-image fidelity or new validated anatomy. Follow TODO/specs and the comparison/feh/release workflow.
