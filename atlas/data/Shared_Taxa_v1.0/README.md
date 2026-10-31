# Shared Taxa v1.0

**Release date:** 2026-10-15  
**Schema:** 1.0  
**Validation:** PASS_WITH_DOCUMENTED_SCIENTIFIC_WARNINGS

## Reconciliation overview

- Tree of Life Explorer v1.7 supplied **238** unique source nodes (237 indexed descendants plus hidden root).
- Deep Time Atlas v1.6 supplied **200** source taxon profiles; **70** mapped to an existing Tree concept and **130** retained as additional concepts.
- **368** canonical concepts in this release, including educational nodes and unplaced historical groups; not an estimate of worldwide extant taxa.
- **495** source representative examples (95 Tree, 400 Deep). These examples are not an exhaustive species census.
- **173** canonical geologic intervals; preserve 9 inter-source boundary disagreements.
- **580** curated Deep Time interval–taxon associations separate from **8916** UI age-filter display matches.
- **129** media references: 23 bundled images decoded and hash-verified locally; external images were not URL-tested.

## Files

The root contains `taxonomy.json`, `taxon_details.json`, `taxon_history.json`, `diversity.json`, `organisms.json`, `geologic_time.json`, `rank_guides.json`, `sources.json`, `images_manifest.json`, `geologic_taxon_links.json`, `additional_science.json`, `manifest.json`, `ID_MAPPING.json`, `VALIDATION_REPORT.json`, and `RECONCILIATION_REPORT.json`.

Machine-readable JSON Schema 2020-12 files live in `schemas/`. `source_exports/` and `source_archives/` preserve both original datasets and images losslessly.

## Rules for consumers

1. Join on canonical IDs from `ID_MAPPING.json`, **not** original widget IDs or names.
2. Accept `parent_id:null` for Deep Time concepts without scientifically grounded parent mapping; do not infer edges from literal cladogram text.
3. Read `classification_assertions[]` to distinguish ranking conventions.
4. Read source values under `source_age_assertions[]`; canonical crown/stem/earliest fossil ages remain **null** without specific evidence.
5. Do not use `ui_inferred_age_filter_matches` as observations or curated fossil-range evidence.
6. Population, taxonomic subdivisions and indexed record counts are separate kinds of quantities; unknown remains null.
7. Per-taxon citations remain sparse. Source URL presence is not independent verification.
8. Deep Time artworks are illustrative AI-generated images, and Tree images are runtime references with unverified licenses.
9. Do not remove embedded data from either original widget until separately tested migrations are complete.

## Release rollback and stability

v1.0 is fully self-contained. Keep this ZIP immutable and retain `ID_MAPPING.json`. Use stable IDs forever; future minor versions add records, while a breaking schema or ID migration needs a major version bump with a documented crosswalk.
