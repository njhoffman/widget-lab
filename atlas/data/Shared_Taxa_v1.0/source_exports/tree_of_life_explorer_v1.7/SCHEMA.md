# Shared Taxa source export — schema v1.0.0

## General model
Each data JSON file is an object containing `_metadata` with origin and version details, plus one or more collections. This is a **widget-specific source export**, not the future shared canonical schema. Numeric ages are millions of years before present (`Ma`); zero means present.

- **`taxonomy.json` → `records[]`**: `id` (exact source key, string), `parent_id` (nullable exact source key), `rank` (verbatim string), `common_name` (string), `extinct` (derived boolean), `icon` (emoji); `raw_source_fields` includes every unmodified *effective* runtime field from the original `a(...)` taxon object: `id,parent,rank,common,age,end,count,pron,ety,traits,note,emoji`. One `source_initialization_override` preserves two Animalia pre-mutation literal values.
- **`taxon_details.json` → `records[]`**: `taxon_id`; pronunciation, etymology, diagnostic traits, evolutionary history, and unparsed original diversity/count text. Join via `taxonomy.records[].id`.
- **`taxon_history.json` → `records[]`**: `taxon_id`, `estimated_lineage_origin_ma` (number), `lineage_end_ma` (nullable number), `extinct` boolean, and explicit interpretation of estimated age and last-known occurrence. These values duplicate the raw fields but make chronology interoperable.
- **`diversity.json` → `worldwide_subdivision_count_references[]`**: `taxon_id` and `estimates_by_rank` object with source-native number/string values; `population_estimates[]`: named species/organism key and verbatim `estimate`, `scope`, `note`, `source`, `href`. These are different types of statistics; don't combine them.
- **`geologic_time.json` → `source_hierarchy`**: root geologic interval and nested `children[]` with `name`, `rank`, `old`, `young` in Ma; terminal children may omit `children`.
- **`organisms.json` → `representatives[]`**: `key` (unique example ID), `linked_taxon_id`, `name`, `status`, originating constant (`E`, `EXTRA_EXAMPLES`, `V4_EXAMPLES`), Wikipedia article title/URL, optional Commons fallback filename/URL, verification status, plus entire `source_record` verbatim. `popularity_order` preserves the source's explicit ranking preference.
- **`rank_guides.json` → `guides`**: rank-to-educational-reference records with five named fields derived from the source's complete `RANK_GUIDES` array.
- **`sources.json` → `references[]`**: original footer source label and URL, plus population-specific references; `original_footer_cautions` and `source_count_notes` give associated caveats. These are source-attributed links, not validated per-taxon citations.
- **`validation_report.json`**: source counts, integrity checks, and extraction provenance.
- **`AMBIGUITIES.md`**: unresolved classification, identification, chronology, media, and statistic uncertainties.

## Referential integrity
`taxonomy.parent_id → taxonomy.id` except root `Life`; `taxon_details.taxon_id`, `taxon_history.taxon_id`, and `organisms.linked_taxon_id` each refer to `taxonomy.id`. `diversity.worldwide_subdivision_count_references.taxon_id` refers to `taxonomy.id`; `diversity.population_estimates[].taxon_or_organism_name` can refer to a taxon **or an organism's name** and therefore must not be treated as a strict foreign key.

## Preservation / import guidance
All records are copied without changing the widget's taxonomy or age assumptions. Keep original keys as `source_id`, then assign new stable canonical IDs in Shared Taxa with a crosswalk (`source_widget`, `source_id`, `canonical_id`). Do not collapse ambiguous synonyms or identical names across namespaces until verified. Use source-specific version (`1.7`) and export SHA-256 for deduplication. The existing standalone widget remains self-contained and continues to embed its original scientific data.
