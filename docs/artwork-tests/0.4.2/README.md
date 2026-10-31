# Offline artwork verification — 0.4.2

Chrome/Linux verification on 2026-10-31. [Full report](report.json) records source and manifest SHA-256, every indexed ID, each adjacent hero/thumbnail hash, image dimensions, decode result, timestamp and browser version. [Shared Taxa integrity report](data-integrity.json) verifies all 90 canonical manifest files and 15 JSON schemas.

| Widget | Runtime IDs | Decoded hero/thumbnail images | Embedded/adjacent byte parity |
| --- | ---: | ---: | --- |
| Deep Time 1.19.0 | 172/172 | 344/344 | Pass |
| Mythology 1.14.0 | 363/363 | 726/726 | Pass |

Each current HTML is copied into an otherwise empty temporary directory. Chrome uses a clean temporary profile, file:// loading, disabled networking and blocked HTTP(S). Every runtime ID must uniquely match the external artwork manifest; Deep Time must resolve directly rather than inherit an ancestor image. Both embedded mappings must cover exactly that manifest. All decoded images require nonzero dimensions, and each embedded image must match the corresponding adjacent asset bytes. Hero hashes also match the asset manifest. No application data or source bytes change.

Repeat with `just artwork-test` after choosing a new batch VERSION, or use `just artwork-test --output /tmp/atlas-artwork-check`. Existing reports cannot be overwritten. `just check` validates registered coverage and source/manifest/adjacent-image freshness, with regressions for missing decodes, missing IDs, stale sources, corrupted embedded thumbnails and duplicate manifest IDs.

Closes T011 (172 indexed interval images), T040 (363 indexed local figure illustrations), T078 (unchanged canonical dataset) and WL-023 (repeatable exhaustive coverage). Does not close T012: isolated standalone image loading and adjacent byte parity do not verify a separately runnable bundle edition or all offline navigation. Mythology's featured Zeus adapter is checked separately by the existing build/browser suite; the exhaustive mapping audit covers the original library. Generated/symbolic images remain generated/symbolic, with existing review disclosures; scientific/cultural accuracy, licensing, curated-taxonomy relationships and final artwork approval are not certified. Windows, storage and wider accessibility remain open.
