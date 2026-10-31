# Shared Taxa — Tree of Life Explorer source export

- **Source widget:** Tree of Life Explorer v1.7, dated 2026-10-15
- **Previous widget version:** v1.6
- **Purpose:** Extract all in-page reusable taxonomy, lineage history, species/organism examples, geologic chronology, diversity, population, and references for later comparison with the Deep Time Atlas.
- **Status:** Unreconciled; existing standalone widget untouched except for its version label and changelog.

## Dataset inventory

- 238 taxonomic nodes including one hidden `Life` root (237 indexed entries)
- 95 representative-organism entries (23 original, 62 extended, 10 v4 entries)
- 47 taxa with worldwide subdivision count references
- 12 population metadata entries; 11 not explicitly marked unknown
- 4 geological eons within a nested interval hierarchy
- 11 rank explanation guides
- 24 source links (footer and population links; may include same URL more than once)
- 11 organism examples with original Wikimedia Commons fallback filenames; others use runtime Wikipedia image APIs

See `SCHEMA.md` for fields, `AMBIGUITIES.md` for merge hazards, and `validation_report.json` for integrity checks. Do not assume source counts are complete or links are verified.

## Next steps for Shared Taxa chat

1. Import this ZIP and the equivalent Deep Time Atlas export.
2. Build a stable-ID crosswalk retaining each source's original `id` and source file/version.
3. Match records by accepted taxonomic identity, not simple string equality.
4. Resolve diverging ages and classifications with citations; preserve uncertainty and alternatives.
5. Publish new canonical dataset files and independent Shared Taxa version; rebuild widgets only after verification.
