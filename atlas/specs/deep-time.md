# Deep Time — Atlas specification

**Status:** APPROVED migration safeguards and shared visual direction; detailed new features remain proposed.  
**Spec revision:** 4  
**Current release:** 1.19.0 (standalone visual update)  
**Preserved imported baseline:** 1.18  
**Last reviewed:** 2026-10-30

## Purpose and existing implementation

The current implementation is `atlas/widgets/Deep_Time_Atlas_v1.19.0.html`, built from the preserved imported `Deep_Time_Atlas_v1.18.html` plus the presentation adapter in `atlas/widgets/deep-time/src/`. Original scripts/data are retained; the document title and added presentation blocks identify the visual release. Original version 1.18 remains available unchanged with its historical release notes.

## Approved requirements

- Preserve the imported implementation and scientific content while establishing repository management.
- Follow [shared visual direction](visual-direction.md) revision 3, derived from the user's selected goal pictures.
- Preserve identifiers, stored-state formats, and historical changelogs. Do not bump release versions during migration setup.

## Scientific / pedagogical integrity

Preserve interval identifiers, navigation, existing topic panels, and representative-life information. Keep 172 UI intervals distinct from Shared Taxa’s 173 canonical intervals, and curated links distinct from inferred age matches.

## UI and behavior

The existing source is the behavior baseline. Goal-image direction is approved; screenshot counts and versions are illustrative. No new runtime interface or scientific data changes were implemented during repository setup.

## Acceptance tests

- Imported source hash and title/catalog version agree with `project_manifest.json`.
- JavaScript syntax and imported artifact/artwork integrity checks pass.
- Before replacing the original: test navigation, filters, selection, panel content, keyboard/mobile layouts, and applicable persistence/import/export behavior in a browser.
- Produce fresh actual-versus-goal PNGs with completed/pending side lists for every update; preserve screenshot/hash evidence and automatically open the results in feh. See shared visual specification revision 4 and `docs/development-workflow.md`.

## Proposed or unresolved changes (NOT APPROVED)

Historical dashboard issues/suggestions and old chat proposals are retained as evidence only. New subject-specific features and art promotion need reviewed requirements. See the shared spec for the proposed visual work sequence and current artwork/anatomical limits.

## Decision history

See [curated Atlas context](../../docs/context/atlas_master.md) and [migration decision](../../docs/decisions/2026-10-30-atlas-migration-baseline.md).

## Verified regression baseline — repository 0.1.1

Approved QA scope from WL-005 and the user's request to begin low-feedback high-priority tasks. The [browser report](../../docs/browser-tests/0.1.1/README.md) records all 45 checks passing across Deep Time, Brain, and Mythology at 390/768/1440px in Chrome on Linux. Inputs use browser mouse/key events; no original widget bytes or scientific records changed.

Coverage includes initial/selected horizontal layout and title/version bounds, Enter-opened history, Escape dismissal and returned focus, visible Tab focus, widget-specific navigation/filter/detail controls, and runtime errors. Deep Time additionally checks distinct five-tab content, neighboring title/artwork/breadcrumb updates, and representative-life profile opening/closing. Brain checks projections, selected details, schematic depth, keyboard time-range input and reset. Mythology checks figure selection, tradition switching, empty-result state and reset.

Before source changes, rerun `python3 tools/test_atlas_browser.py` and retain the source-hashed report and selected screenshots. `tools/check_project.py` rejects missing matrix cells, failures, and stale source evidence. This is not Windows/IndexedDB/folder-picker, full accessibility, scientific, or exhaustive interaction certification. T021 remains open for canonical taxon identity/provenance despite passing its UI interaction check.

## Approved visual batch — repository 0.2.0 / Deep Time 1.19.0

Scope derives from WL-006 and the user's instruction to continue with the next tasks. Move the existing topic navigation and search into a compact responsive header; keep search results anchored to the input, filters and random/reset controls usable, and the header free from overlap. Improve the selected-interval scene composition and enlarge the existing nearby-interval previews. Add actual manifest age ranges and a clear selected state to previews, retaining their current interval-navigation behavior.

Use the existing art without changing its scientific/review status; no new artwork, maps, counts, dates, or taxon relationships are introduced. All original scripts, data payloads, IDs and scientific panels must remain byte-identical within the derived standalone build. Only the document title and appended presentation CSS/JS may differ. The imported `Deep_Time_Atlas_v1.18.html` remains intact. The new independently versioned file is `Deep_Time_Atlas_v1.19.0.html`; this adopts three-part SemVer without renumbering the historical 1.18 entry.

Editable presentation sources live in `atlas/widgets/deep-time/src/layout.css` and `layout.js`; build with `python3 tools/build_deep_time.py`. `atlas/current.html` links registered current builds; the original dashboard remains historical. Add the new changelog entry ahead of all existing entries, and reflect the true active version in the title/header/history dialog.

Acceptance: full browser matrix passes, plus current tabs/search are inside the header, real age labels and active states appear on previews, preview clicks update the selected interval, reduced-motion settings suppress adapter transitions, original science/control bytes match the preserved baseline, and new screenshots are reviewed at 390/768/1440px. Produce the actual-versus-goal image and open it in feh. WL-006 remains open for the other widgets and remaining visual/artwork gaps.
