# Scientific reconciliation and unresolved ambiguities

**Matched taxon source profiles:** 70 (matching by exact scientific names plus two explicit domain and two curated synonym resolutions).

**Additional Deep Time concepts:** 130; no unsupported cladogram parent edges invented.

**Rank disagreements:** 1. **Approximate source age differences:** 22. **Chronological boundary differences:** 9. **Source ambiguity notes:** 25.

## Identity policy

Shared names do not always imply an identical taxonomic rank, circumscription or classification. The Bacteria and Archaea domain concepts are matched to the Tree of Life domain records rather than similarly named kingdom records. Kingdom records remain available as distinct *classification concepts* to avoid self-parenting cycles. Cyanobacteria ↔ Cyanobacteriota and Angiosperms ↔ Angiospermae are explicit curated aliases, not fuzzy substring matches.

## Sample lineage age disagreements (Ma)

- `stx:taxon:tree-bacillota-93ef9452d9`: Tree origin 1800; Deep first-range boundary 1500. Not equivalent evidence types.
- `stx:taxon:tree-methanobacteria-cc958a1f2d`: Tree origin 1700; Deep first-range boundary 3000. Not equivalent evidence types.
- `stx:taxon:tree-tracheophyta-edbb3057cf`: Tree origin 440; Deep first-range boundary 425. Not equivalent evidence types.
- `stx:taxon:tree-pinaceae-367119cea8`: Tree origin 140; Deep first-range boundary 150. Not equivalent evidence types.
- `stx:taxon:tree-ciliophora-6a3102b4e7`: Tree origin 850; Deep first-range boundary 750. Not equivalent evidence types.
- `stx:taxon:tree-placozoa-5467ccd011`: Tree origin 550; Deep first-range boundary 540. Not equivalent evidence types.
- `stx:taxon:tree-anthozoa-6aac4e96ad`: Tree origin 530; Deep first-range boundary 540. Not equivalent evidence types.
- `stx:taxon:tree-octopoda-66344b31f7`: Tree origin 160; Deep first-range boundary 155. Not equivalent evidence types.

## Sample geologic boundary differences (Ma)

- Hadean: deep_time_atlas_v1.6 4567–4031; tree_of_life_explorer_v1.7 4600–4031
- Paleozoic: deep_time_atlas_v1.6 538.8–251.902; tree_of_life_explorer_v1.7 538.8–251.9
- Permian: deep_time_atlas_v1.6 298.9–251.902; tree_of_life_explorer_v1.7 298.9–251.9
- Mesozoic: deep_time_atlas_v1.6 251.902–66; tree_of_life_explorer_v1.7 251.9–66
- Triassic: deep_time_atlas_v1.6 251.902–201.4; tree_of_life_explorer_v1.7 251.9–201.4
- Paleogene: deep_time_atlas_v1.6 66–23.04; tree_of_life_explorer_v1.7 66–23.03
- Oligocene: deep_time_atlas_v1.6 33.9–23.04; tree_of_life_explorer_v1.7 33.9–23.03
- Neogene: deep_time_atlas_v1.6 23.04–2.58; tree_of_life_explorer_v1.7 23.03–2.58

## Outstanding issues

- Deep Time cladogram strings are not an edge-resolved taxonomy; unmatched groups remain unplaced rather than forcing a Tree parent.
- Tree of Life historic kingdom headings include non-monophyletic groupings; retain alternative classifications and provenance.
- First occurrence, lineage origin, crown group and stem divergence are not interchangeable. Canonical calibrated dates remain null.
- Counts from disparate catalogs, categories and geographic scopes cannot be added as if they were one census.
- Deep Time geologic association links are curated source associations, not independently reviewed fossil finds; 8,916 UI-derived matches are strictly separate.
- Source reference URLs do not substantiate every entry; URL verification and scientific fact-checking remain outstanding.
- Deep Time embedded images are illustrative AI paleoart; Tree Wikipedia and Commons links remain unchecked.

All recorded differences and source metadata are in `RECONCILIATION_REPORT.json`. Original files are available verbatim in `source_exports/`.
