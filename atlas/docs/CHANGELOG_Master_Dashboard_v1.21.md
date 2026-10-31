# Atlas Widgets Master Dashboard — v1.21

Date: 2026-10-17. Previous: v1.20.

## Added
- Widget Launcher v1.14 with import of extracted artwork folders including HTML and sibling images.
- IndexedDB v3 `widgetBundles` store keyed by widget ID and bound to the exact widget HTML content hash.
- Image completeness check and manifest SHA-256 comparison (when crypto supported and manifest hashes available).
- Offline launch construction of temporary self-contained HTML with source artwork, and output folder writing with sibling image directories.
- Card status: missing assets / verified bundle ready / standalone ready.
- Master Dashboard links, version metadata, usage guide, and I015 progress evidence updated.

## Preserved
- Six atlas HTML scientific application files byte-identical to v1.20.
- Shared Taxa v1.0 unchanged, independent of image import.
- The full historical launcher changelog, widget history, 84 goal records, 538 artwork records, and review safeguards.

## Not verified in this environment
- Actual Windows Edge/Chrome folder-picker permissions and long-term IndexedDB persistence.
- Browser launched-tab round trip and output-directory permissions (local navigation was blocked by runtime).
- Automatic import of raw ZIP archives (extract folders first); untrusted HTML must not be imported.
