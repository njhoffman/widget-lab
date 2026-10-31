# Widget Launcher v1.14 — offline artwork bundles

## Folder import
1. Extract the illustrated asset ZIP (do not import the ZIP directly).
2. Open the launcher in Chrome or Edge using a stable web origin, preferably `http://localhost:8765` after starting `py -m http.server 8765` in the package directory.
3. Choose **Import artwork folder**. Select a directory containing one or more recognized atlas HTML files and an `assets/` folder; assets can also be inside a subdirectory if unambiguous.
4. Check the widget card for **Bundle ready**. If it displays **Assets missing**, inspect the count and import the complete folder. Standalone HTML files do not need a separate artwork directory.
5. Click the card to open an offline page; the launcher reads image blobs from IndexedDB and constructs a temporary self-contained HTML document.
6. Optionally choose an **Output folder** to export the HTML and referenced image folders with `manifest.json` to `launcher_widgets/`.

## Storage and limitations
- Browser IndexedDB stores artwork; records are bound to the exact HTML checksum, not merely its filename. If HTML changes, re-import the corresponding assets.
- Images are verified against manifest SHA-256 values when corresponding checksums exist and Web Crypto is available. Assets without a matching manifest are stored but not called verified.
- Safe relative paths only; images cannot exceed 12 MiB individually or 90 MiB total; no more than 1,600 image references per widget. Browser quota may impose stricter limits.
- Import original trusted widget HTML only. The launcher executes imported code in a new tab. It is not an untrusted HTML sandbox.
- Automated ZIP unpacking, additional non-image external scripts/fonts, and end-to-end Windows persistence remain outside this version's tested scope.

## Validation on Windows
1. Import bundle, observe image count and status.
2. Launch atlas, change intervals/figures/views, verify loaded images.
3. Close/reopen launcher tab and ensure bundle remains ready.
4. Import a deliberately incomplete test folder and verify it stays in warning status.
5. Set output folder; inspect exported `launcher_widgets/assets/` and verify re-open works.
6. Reimport a revised HTML edition and confirm the old bundle is not incorrectly marked ready.
