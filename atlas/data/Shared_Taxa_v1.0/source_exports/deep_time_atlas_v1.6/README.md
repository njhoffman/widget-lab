# Shared Taxa — Deep Time Atlas source export

**Source widget:** Deep Time Atlas **v1.6**, updated 2026-10-15.  
**Embedded data snapshot:** v1.5, copied unchanged into v1.6.  
**Migration:** None. The HTML widget still runs entirely on its existing built-in data.

## Contents

- `metadata.json` — origin, version, counts, source checksum and extraction policy.
- `data/geologic_intervals.json` — **172** original geologic nodes with original IDs, ranges in Ma, direct parent and children, event lists, taxa IDs, environment text, plus computed geologic subdivision counts.
- `data/taxa.json` — **200** original profiles, original IDs, rank/kind, etymology, pronunciation, description, traits, raw cladogram strings and lines, life-age metadata when present, and **400** original example records/status labels.
- `data/geologic_taxon_links.json` — **580** directly stored interval/taxon links, separately from **8916** reproducible display-rule matches. Includes original add-on association tables.
- `data/taxon_source_layers.json` — unmodified profile arrays from historical expansions (v3 and v4).
- `data/geologic_details.json` — supplementary epoch notes, detailed highlight overrides, environmental insight texts, and original age/stage arrays.
- `data/paleogeography.json` — **7** original illustrative SVG continent-shape presets and their age selector rules.
- `data/source_logic.json` — raw JS snippets for environmental inheritance, atmospheric generalizations, illustrative paleomap selection, popularity sorting, and interval filtering.
- `data/images_manifest.json` — original image keys, hashes, MIME types, example image references, and relative paths; actual embedded art in `images/` (**23** files).
- `data/source_references.json` — the ICS global chart link and original generated-art description, with limitations noted.
- `data/widget_display_metadata.json` — rank labels and historical changelog information.
- `SCHEMA.json` — JSON Schema draft 2020-12 definitions and file-to-schema mapping.
- `AMBIGUITIES.json` — all known extraction ambiguities, scientific limitations and deferred reconciliation choices.
- `validation.json` — referential-integrity and source-record validation results.

## Preservation rules

1. Every original `id` remains the same. Do not silently remap overlapping terms from another atlas when merging.
2. The **geologic timeline** has explicit graph links (`parent`, `children`). The **taxon cladograms** are preserved verbatim, but the source did not supply machine-readable parent taxon IDs. `asserted_parent_taxon_id` stays null rather than inventing edges.
3. Original evolutionary date fields (`first`, `last`, in Ma) are left unchanged and recorded under `lineage_age`; these are approximate UI spans, not verified origination dates.
4. Original fossil/living status labels belong to **examples**. Parent-taxon extinction state is not reliably encoded by them, so its normalized field is null.
5. The original source has **no organism population-estimate figures or taxonomic subdivision counts**; these remain `null`. By contrast, geologic subdivision counts are accurately derived as the number of child interval IDs.
6. The source has **one global geologic time reference** (International Commission on Stratigraphy 2026/06). It lacks source citations for individual biological records. Nothing was invented.
7. Image keys are preserved, and the byte-for-byte decoded embedded image files are packaged. Some cards have emoji rather than image data.
8. Explicit links and computed UI links are **not interchangeable**. Maintain the separation during merging.

## Suggested reconciliation process

Import both widgets' exports independently. Deduplicate or synonym-match by curated taxonomic identity rather than display name alone, preserve source IDs as aliases, review topology and geologic correlations, then publish a normalized Shared Taxa dataset. Only then migrate either HTML widget to use it. The current files are preservation-first, not an authoritative taxonomy.
