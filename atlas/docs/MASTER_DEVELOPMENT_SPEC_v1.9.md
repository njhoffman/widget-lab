# Atlas Widgets — Master Development v1.9

**Release date:** 2026-10-16. **Source:** Master Development v1.8.

## New versions
- Deep Time Atlas **v1.17**, Brain Atlas **v1.20**, Mythology Atlas **v1.12**
- Unchanged: Tree of Life v1.14, Muscle v1.8, Emergence v1.10, Widget Launcher v1.12, Shared Taxa v1.0.

## Implemented
1. Refined shared header styling: compact cyan/mint chips, stronger navy gradient and subtle lighting, natural wrap; all status counts remain live.
2. Deep Time now has a dedicated illustrated lead panel with separate scientific cards and clickable previews of nearby intervals. All 172 actual interval IDs remain in the image manifest.
3. Brain gets enhanced depth-state explanations, a selected-view callout, and stronger contrast; no true anatomical 3-D model is implied.
4. Mythology's illustrated figure stage and profile panels have stronger visual hierarchy; 363 tradition-specific illustrations, genealogy and filters remain.
5. Artwork Studio v1.9 adds text/family/quality/review filters, image preview, browser-local review decisions and JSON review export, with 538 indexed assets.
6. Two select Mesozoic illustrations (Mesozoic and Jurassic) and the Greek Zeus illustration have been updated with higher-detail visual concept crops from the approved image references. They are marked **featured AI illustration concepts requiring scientific/historical review**, not factual reconstructions. The other scene/portrait records remain procedural/symbolic.
7. Bundle and standalone HTML distributions retained; use the `launcher_ready` folder for the existing Widget Launcher v1.12.

## Art-fidelity limitation
No full set of individually directed cinematic paintings was generated in this release. 170 of the 172 existing Deep Time scenes still use procedural theme variations; 362 of the 363 Mythology illustrations remain symbolic rather than individually directed paintings. Two Mesozoic concept crops and one Zeus painting represent featured examples, not complete bespoke coverage. The asset library now explicitly records their quality and review status. Licensed, subject-specific sources and/or dedicated image-generation assets remain necessary for a genuine full cinematic-content replacement.

## Attribution and reliability
- `assets/featured/`: crops/derivatives from AI-generated project concept artwork; illustrative only, not geographically/medically/historically calibrated.
- `assets/deep_time` and `assets/mythology`: existing procedurally generated content with added review metadata.
- No canonical Shared Taxa source data was altered.

## Browser QA
See `qa/QA_REPORT_v1.9.json` for runtime checks.

**Suggested chat title:** Atlas Widgets — Master Development v1.9

## Validation detail
- Core scientific and genealogical application code retained byte-for-byte inside the updated release HTML.
- 538 artwork records checked against local files; 172 Deep Time, 363 Mythology, 3 schematic Brain.
- Tested standalone HTML via Chromium page-content loading. Local `file://` and hosted URL navigation were restricted in this environment; real file/directory access should be checked on Windows.
- 12 viewport checks (320/600/850/1350 range; recorded 360/600/850/1350) showed no header title/status collisions.
- Artwork Studio allows browser-memory review edits and export; local persistence depends on origin/storage permissions.
