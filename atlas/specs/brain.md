# Brain — Atlas specification

**Status:** APPROVED migration safeguards and shared visual direction; detailed new features remain proposed.  
**Spec revision:** 4  
**Current release:** 1.22.0 (standalone visual update)  
**Preserved imported baseline:** 1.21  
**Last reviewed:** 2026-10-30

## Purpose and existing implementation

The current implementation is `atlas/widgets/Brain_Atlas_v1.22.0.html`, derived from the preserved 1.21 import and presentation in `atlas/widgets/brain/src/`. All original geometry, scientific records and control source remain intact apart from the document title and appended CSS/JS. The original standalone and historical entries remain available unchanged.

## Approved requirements

- Preserve the imported implementation and scientific content while establishing repository management.
- Follow [shared visual direction](visual-direction.md) revision 6, derived from the user's selected goal pictures.
- Preserve identifiers, stored-state formats, and historical changelogs. Do not bump release versions during migration setup.

## Scientific / pedagogical integrity

Preserve hierarchy selection, anatomical highlighting, view controls, evolutionary/time information, and the existing estimated-depth disclosure. True registered 3D anatomy is unresolved and is not authorized by mockup imagery alone.

## UI and behavior

The existing source is the behavior baseline. Goal-image direction is approved; screenshot counts and versions are illustrative. No new runtime interface or scientific data changes were implemented during repository setup.

## Acceptance tests

- Imported source hash and title/catalog version agree with `project_manifest.json`.
- JavaScript syntax and imported artifact/artwork integrity checks pass.
- Before replacing the original: test navigation, filters, selection, panel content, keyboard/mobile layouts, and applicable persistence/import/export behavior in a browser.
- Produce fresh actual-versus-goal PNGs with completed/pending side lists for every update; preserve screenshot/hash evidence and automatically open the results in feh. See shared visual specification revision 6 and `docs/development-workflow.md`.

## Proposed or unresolved changes (NOT APPROVED)

Historical dashboard issues/suggestions and old chat proposals are retained as evidence only. New subject-specific features and art promotion need reviewed requirements. See the shared spec for the proposed visual work sequence and current artwork/anatomical limits.

## Decision history

See [curated Atlas context](../../docs/context/atlas_master.md) and [migration decision](../../docs/decisions/2026-10-30-atlas-migration-baseline.md).

## Verified regression baseline — repository 0.1.1

Approved QA scope from WL-005 and the user's request to begin low-feedback high-priority tasks. The [browser report](../../docs/browser-tests/0.1.1/README.md) records all 45 checks passing across Deep Time, Brain, and Mythology at 390/768/1440px in Chrome on Linux. Inputs use browser mouse/key events; no original widget bytes or scientific records changed.

Coverage includes initial/selected horizontal layout and title/version bounds, Enter-opened history, Escape dismissal and returned focus, visible Tab focus, widget-specific navigation/filter/detail controls, and runtime errors. Deep Time additionally checks distinct five-tab content, neighboring title/artwork/breadcrumb updates, and representative-life profile opening/closing. Brain checks projections, selected details, schematic depth, keyboard time-range input and reset. Mythology checks figure selection, tradition switching, empty-result state and reset.

Before source changes, rerun `python3 tools/test_atlas_browser.py` and retain the source-hashed report and selected screenshots. `tools/check_project.py` rejects missing matrix cells, failures, and stale source evidence. This is not Windows/IndexedDB/folder-picker, full accessibility, scientific, or exhaustive interaction certification. T021 remains open for canonical taxon identity/provenance despite passing its UI interaction check.

## Approved visual batch — repository 0.4.0 / Brain 1.22.0

Continue WL-006 using the existing authored schematic and data. Move native projection/depth controls and depth-strength selector into a compact responsive header; enlarge the selected-region summary and improve map/detail hierarchy. Move the existing reference outline and callout out of the interactive map into context areas so they do not cover markers. Keep the timeline, divisions/regions/circuits, scientific sections, statistics and history controls available.

Do not change paths, transforms, region/circuit records, dates, selection handlers, or depth calculations. Keep estimated/schematic/not-volumetric labels visible; the reference inset is orientation-only and does not become a registered selected-structure overlay. The depth-strength selector may be disabled while estimated depth is off. A selected region/detail context should begin at its heading after selection changes without disrupting detail shortcuts.

Preserve the complete imported 1.21 source. New standalone 1.22.0 differs only in document title and appended presentation CSS/JS, with a new history entry ahead of retained entries. No new anatomical image, true 3D model, clinical advice or scientific claim is part of this batch.

Acceptance: source-preservation build test; full browser matrix; all three projections retain selected identity, visible marker bounds and orientation reference; depth on/off and low/medium/high visibly affect native cue attributes while selected marker stays crisp; keyboard region selection, native time filtering/reset, header containment and reduced-motion checks; real goal comparison opened in feh. T027/T032/T033/T037/T039 retain their wider data/registered-overlay/scientific review scope.

Mobile layout must keep the actual hierarchy panel and selected control wide enough to use, rather than merely passing a no-overflow test. Regression assertions require at least 180px hierarchy width and 150px selected-control width at the target viewports, plus a native hierarchy click. Desktop detail panels scroll locally; tablet/mobile details remain in normal document flow.

The goal comparison uses the orbitofrontal cortex in lateral schematic view with estimated depth on at the native Medium setting, matching the goal's depth-mode presentation. Product startup remains depth-off with no region selected. Evidence records that state explicitly; earlier comparison captures used depth-off. Browser regressions independently exercise both states and all three projections. Orientation references are not selected-structure overlays or true registered anatomy.
