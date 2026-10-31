# Deep Time — Atlas specification

**Status:** APPROVED migration safeguards and shared visual direction; detailed new features remain proposed.  
**Spec revision:** 2  
**Imported source release:** 1.18 (source identity verified; interactive/scientific QA remains open)  
**Last reviewed:** 2026-10-30

## Purpose and existing implementation

The authoritative imported implementation is `atlas/widgets/Deep_Time_Atlas_v1.18.html`. Its actual HTML title and delivered v1.21 catalog establish the version. Original functionality and embedded release history are preserved byte-for-byte. Component `src/` placeholders are not the current source location; the delivered relative package layout was retained deliberately.

## Approved requirements

- Preserve the imported implementation and scientific content while establishing repository management.
- Follow [shared visual direction](visual-direction.md) revision 2, derived from the user's selected goal pictures.
- Preserve identifiers, stored-state formats, and historical changelogs. Do not bump release versions during migration setup.

## Scientific / pedagogical integrity

Preserve interval identifiers, navigation, existing topic panels, and representative-life information. Keep 172 UI intervals distinct from Shared Taxa’s 173 canonical intervals, and curated links distinct from inferred age matches.

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
