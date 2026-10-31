# Mythology (Atlas)

Current standalone: [Mythology_Atlas_v1.14.0.html](../Mythology_Atlas_v1.14.0.html). Preserved import: [Mythology_Atlas_v1.13.html](../Mythology_Atlas_v1.13.html).

The new build defaults to the existing artwork view with explicit Artwork / Family tree controls and a compact search header. Genealogy, filters, IDs, source caveats and original handlers remain intact. Related thumbnails follow the active tradition. Featured Greek Zeus artwork reuses a verified existing concept image; it is modern interpretation pending cultural review, not historical artwork.

Edit `src/layout.css` and `src/layout.js`, then run `python3 tools/build_mythology.py`. It preserves the original import and embeds verified featured-image bytes for offline use. Run `python3 tools/build_atlas_index.py` after manifest source/version changes. Later releases must retain prior standalone files and release-history entries.

See [specification revision 4](../../specs/mythology.md), [visual direction](../../specs/visual-direction.md), and root `project_manifest.json`. Open `/current.html` when serving `atlas/`.
