# Mythology — Atlas specification

**Status:** APPROVED migration safeguards and shared visual direction; detailed new features remain proposed.  
**Spec revision:** 4  
**Current release:** 1.14.0 (standalone visual update)  
**Preserved imported baseline:** 1.13  
**Last reviewed:** 2026-10-30

## Purpose and existing implementation

The current implementation is `atlas/widgets/Mythology_Atlas_v1.14.0.html`, derived from the preserved 1.13 import plus the presentation adapter in `atlas/widgets/mythology/src/`. Original data/control source and historical entries remain intact. Only the document title and added presentation blocks differ; verified existing featured-image bytes are embedded for offline rendering.

## Approved requirements

- Preserve the imported implementation and scientific content while establishing repository management.
- Follow [shared visual direction](visual-direction.md) revision 5, derived from the user's selected goal pictures.
- Preserve identifiers, stored-state formats, and historical changelogs. Do not bump release versions during migration setup.

## Scientific / pedagogical integrity

Preserve tradition-specific figure IDs, filters, figure relationships, genealogy, and story associations. Keep modern/generated imagery distinct from historical artwork and source evidence.

## UI and behavior

The existing source is the behavior baseline. Goal-image direction is approved; screenshot counts and versions are illustrative. No new runtime interface or scientific data changes were implemented during repository setup.

## Acceptance tests

- Imported source hash and title/catalog version agree with `project_manifest.json`.
- JavaScript syntax and imported artifact/artwork integrity checks pass.
- Before replacing the original: test navigation, filters, selection, panel content, keyboard/mobile layouts, and applicable persistence/import/export behavior in a browser.
- Produce fresh actual-versus-goal PNGs with completed/pending side lists for every update; preserve screenshot/hash evidence and automatically open the results in feh. See shared visual specification revision 5 and `docs/development-workflow.md`.

## Proposed or unresolved changes (NOT APPROVED)

Historical dashboard issues/suggestions and old chat proposals are retained as evidence only. New subject-specific features and art promotion need reviewed requirements. See the shared spec for the proposed visual work sequence and current artwork/anatomical limits.

## Decision history

See [curated Atlas context](../../docs/context/atlas_master.md) and [migration decision](../../docs/decisions/2026-10-30-atlas-migration-baseline.md).

## Verified regression baseline — repository 0.1.1

Approved QA scope from WL-005 and the user's request to begin low-feedback high-priority tasks. The [browser report](../../docs/browser-tests/0.1.1/README.md) records all 45 checks passing across Deep Time, Brain, and Mythology at 390/768/1440px in Chrome on Linux. Inputs use browser mouse/key events; no original widget bytes or scientific records changed.

Coverage includes initial/selected horizontal layout and title/version bounds, Enter-opened history, Escape dismissal and returned focus, visible Tab focus, widget-specific navigation/filter/detail controls, and runtime errors. Deep Time additionally checks distinct five-tab content, neighboring title/artwork/breadcrumb updates, and representative-life profile opening/closing. Brain checks projections, selected details, schematic depth, keyboard time-range input and reset. Mythology checks figure selection, tradition switching, empty-result state and reset.

Before source changes, rerun `python3 tools/test_atlas_browser.py` and retain the source-hashed report and selected screenshots. `tools/check_project.py` rejects missing matrix cells, failures, and stale source evidence. This is not Windows/IndexedDB/folder-picker, full accessibility, scientific, or exhaustive interaction certification. T021 remains open for canonical taxon identity/provenance despite passing its UI interaction check.

## Approved visual batch — repository 0.3.0 / Mythology 1.14.0

Scope follows WL-006 and the user's instruction to continue with next tasks. Build on the existing artwork/genealogy modes: default to artwork, expose clear Artwork / Family tree controls, move existing search into a compact header, refine selected-figure stage/profile readability, and preserve all original filters, name controls, relationships and tree tools.

Reuse verified local artwork only. The existing featured Greek Zeus concept may be used for the large stage with its AI/interpretive-art disclosure; all other figures retain their current local illustrations and review limitations. No new art, text claims, historical provenance, licensed gallery, or family edges are introduced. Related-figure thumbnails must use the active tradition's asset key, with modern interpretation clearly separated from historical artwork. This does not close the broader historical-artwork gallery requirement.

Keep the complete 1.13 standalone import unchanged. Add a separate 1.14.0 build containing all original data/control source, with only document title and added presentation blocks differing; the verified featured-image bytes are embedded by the builder. New history entry precedes all retained original entries. Update the current launch page from the manifest.

Acceptance: preserve source bytes/IDs and offline standalone behavior; complete browser matrix plus artwork/tree switching with retained selected ID, source-backed feature disclosure, all five tradition keys, related thumbnails matching the selected tradition, independent figure/profile updates, and reduced motion. Review actual screenshots at 390/768/1440px, generate the real-versus-goal comparison with task sidebar, and open feh. Bespoke portraits, historical gallery attribution/licenses, and remaining WL-006 work stay pending.

Figure changes reset the profile pane to its heading; artwork mode hides tree-only legends. This corrects display context while leaving original relationship handlers intact. Existing group/story/symbol filtering, complementary Greek/Roman names, five-tradition result thumbnails, and parent/child navigation are covered by the browser suite. Exact asset-key tests verify current-tradition thumbnails. No historical-artwork carousel or new cultural approval is claimed.
