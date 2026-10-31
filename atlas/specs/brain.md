# Brain — Atlas specification

**Status:** APPROVED migration safeguards and shared visual direction; detailed new features remain proposed.  
**Spec revision:** 3  
**Imported source release:** 1.21 (source identity verified; defined browser matrix passed; wider QA remains open)  
**Last reviewed:** 2026-10-30

## Purpose and existing implementation

The authoritative imported implementation is `atlas/widgets/Brain_Atlas_v1.21.html`. Its actual HTML title and delivered v1.21 catalog establish the version. Original functionality and embedded release history are preserved byte-for-byte. Component `src/` placeholders are not the current source location; the delivered relative package layout was retained deliberately.

## Approved requirements

- Preserve the imported implementation and scientific content while establishing repository management.
- Follow [shared visual direction](visual-direction.md) revision 3, derived from the user's selected goal pictures.
- Preserve identifiers, stored-state formats, and historical changelogs. Do not bump release versions during migration setup.

## Scientific / pedagogical integrity

Preserve hierarchy selection, anatomical highlighting, view controls, evolutionary/time information, and the existing estimated-depth disclosure. True registered 3D anatomy is unresolved and is not authorized by mockup imagery alone.

## UI and behavior

The existing source is the behavior baseline. Goal-image direction is approved; screenshot counts and versions are illustrative. No new runtime interface or scientific data changes were implemented during repository setup.

## Acceptance tests

- Imported source hash and title/catalog version agree with `project_manifest.json`.
- JavaScript syntax and imported artifact/artwork integrity checks pass.
- Before replacing the original: test navigation, filters, selection, panel content, keyboard/mobile layouts, and applicable persistence/import/export behavior in a browser.
- Produce fresh actual-versus-goal PNGs with completed/pending side lists for every update; preserve screenshot/hash evidence and automatically open the results in feh. See shared visual specification revision 2 and `docs/development-workflow.md`.

## Proposed or unresolved changes (NOT APPROVED)

Historical dashboard issues/suggestions and old chat proposals are retained as evidence only. New subject-specific features and art promotion need reviewed requirements. See the shared spec for the proposed visual work sequence and current artwork/anatomical limits.

## Decision history

See [curated Atlas context](../../docs/context/atlas_master.md) and [migration decision](../../docs/decisions/2026-10-30-atlas-migration-baseline.md).

## Verified regression baseline — repository 0.1.1

Approved QA scope from WL-005 and the user's request to begin low-feedback high-priority tasks. The [browser report](../../docs/browser-tests/0.1.1/README.md) records all 45 checks passing across Deep Time, Brain, and Mythology at 390/768/1440px in Chrome on Linux. Inputs use browser mouse/key events; no original widget bytes or scientific records changed.

Coverage includes initial/selected horizontal layout and title/version bounds, Enter-opened history, Escape dismissal and returned focus, visible Tab focus, widget-specific navigation/filter/detail controls, and runtime errors. Deep Time additionally checks distinct five-tab content, neighboring title/artwork/breadcrumb updates, and representative-life profile opening/closing. Brain checks projections, selected details, schematic depth, keyboard time-range input and reset. Mythology checks figure selection, tradition switching, empty-result state and reset.

Before source changes, rerun `python3 tools/test_atlas_browser.py` and retain the source-hashed report and selected screenshots. `tools/check_project.py` rejects missing matrix cells, failures, and stale source evidence. This is not Windows/IndexedDB/folder-picker, full accessibility, scientific, or exhaustive interaction certification. T021 remains open for canonical taxon identity/provenance despite passing its UI interaction check.
