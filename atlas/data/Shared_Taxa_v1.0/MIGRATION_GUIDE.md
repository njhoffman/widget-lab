# Compatibility and widget migration guide

## Version matrix

| Consumer | Compatible source input | Shared Taxa target | Status |
|---|---|---|---|
| Tree of Life Explorer v1.7 | embedded Tree JSON/JS | Shared Taxa schema 1.0 | Data crosswalk available; widget not migrated |
| Deep Time Atlas v1.6 | embedded Deep Time JS | Shared Taxa schema 1.0 | Data crosswalk available; widget not migrated |
| Future Atlas / quiz widgets | schema 1.0 JSON | Shared Taxa v1.0 | Integration contract ready |

## Safe migration sequence

1. Keep original widget source and embedded scientific records intact.
2. Include Shared Taxa JSON as a separate versioned dataset and load `manifest.json`.
3. Lookup original widget IDs in `ID_MAPPING.json`, keyed by both `source_export` and `source_id`.
4. For Tree widgets, use `parent_id` for the exported educational tree, but provide a classification selector for alternate rank conventions and disputed relationships.
5. For Deep Time, use geologic interval IDs and `geologic_taxon_links.json`; **never** use age-filter matches as a validated scientific relationship.
6. Preserve old page and card display text until UI audits confirm consistency.
7. Present source age interpretations and disagreements instead of selecting undocumented dates.
8. Use local verified images only with credit and illustration warnings; check live image URLs and licensing separately.
9. Run regression testing (same navigation, same lineage cards, same counts, source images), then switch source in a separate widget release.
10. Roll back by restoring original widget build; never let a dataset revision silently change a widget version.

## API contract

Each JSON file has `schema_version: "1.0"` and a top-level array of named records. Canonical taxon IDs have `stx:taxon:` namespace. `ID_MAPPING.json` supports taxon and geologic interval lookup. Optional attributes may remain `null`. Consumers must not assume all taxa have parent IDs, calibrated first-appearance dates, exact global abundance estimates, static public image URLs or taxon-specific bibliography.

## Change management

A new minor release should carry the prior ID mapping forward and be fully additive where practical. Breaking schema/reparenting changes need an explicit major version and migration checklist. Retain immutable prior archives for rollback.
