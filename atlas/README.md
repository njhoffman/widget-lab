# Atlas Widgets Master Dashboard v1.21

Start with `MASTER_DASHBOARD_v1.21.html` or `index.html` after extracting the archive. Use Chrome/Edge. For reliable assets and links, run a local server in this directory with `py -m http.server 8765` and visit `http://localhost:8765/`.

## Included
- Six atlas widgets unchanged from v1.19, including their scientific content and history.
- Widget Launcher v1.14 with complete offline folder artwork import and persistent asset storage.
- Shared Taxa v1.0 preserved intact, its ZIP and extracted dataset.
- The Goal Tracker, Artwork Studio, Artwork Calibration tools and 538 artwork assets.
- Dashboard views for project overview, 84 goals, 538 artwork records, five calibration subjects, 28 issues, 25 suggestions, audits, dependencies, usage and **Release traceability**.
- Main landing page's `Full package download` link resolves to `downloads/Atlas_Widgets_Full_Content_v1.21.zip` (included).

## Safe workflow
1. Import prior dashboard decisions JSON if needed; previous v1.18/v1.19 browser state is also read when accessible.
2. Artwork approvals from imported decisions are moved to review; explicitly re-evaluate them with original image, reviewer, source/rights, review notes and source checksum.
3. The current five calibration previews are drafts and cannot be approved just by toggling a checkbox.
4. Use Suggestions → Create linked backlog issue to connect proposals to problems.
5. Use Release traceability to organize issues, suggestions, goals and QA status. A `QA` plan is not a published release.
6. For art-rich widgets imported into the Launcher, choose **Import artwork folder** and select the extracted package root with HTML and its assets folder. The Launcher caches both locally for offline launch; standalone HTML is still supported.
7. Export decisions JSON before changing browsers, directories or release versions. Do not rely solely on localStorage.

## Unchanged science and open items
Shared Taxa v1.0: 368 canonical taxa, 173 canonical geologic intervals, 580 curated associations, 57 documented ambiguities. Full automated external artwork importing, Windows folder/IndexedDB regression testing and final scientific/cultural review remain future work.

## Artwork bundle import (Launcher v1.14)
1. Extract an illustrated atlas bundle. Open Launcher in a stable Chrome/Edge origin (prefer localhost).
2. Click **Import artwork folder**, select the directory containing the atlas HTML file and its `assets/` tree. On browsers without native folder picker, choose the same extracted directory via the fallback folder-upload control.
3. Check the relevant launcher card for `Bundle ready` and the stored image count. Incomplete bundles remain clearly marked.
4. Click that card to open a temporary self-contained HTML window; the launcher reads cached image blobs and substitutes their image URLs.
5. Choose an **Output folder** to export both original HTML and the required image directories into `launcher_widgets/`.
6. Browser artwork caching requires working IndexedDB and enough quota; missing images or quota failure do not count as a successful bundle. Check your browser storage settings and re-import if necessary.

**Security:** Import trusted widget HTML only: these files execute local JavaScript. The importer rejects unsafe image paths, ambiguous references, and oversized images. Image hashes are computed when Web Crypto is available, but uploaded artwork is not automatically scientifically approved.
