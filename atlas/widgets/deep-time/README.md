# Deep Time (Atlas)

Current standalone: [Deep_Time_Atlas_v1.19.0.html](../Deep_Time_Atlas_v1.19.0.html). Preserved import: [Deep_Time_Atlas_v1.18.html](../Deep_Time_Atlas_v1.18.html).

The new build adds a compact responsive header, interval-stage refinements, and source-age thumbnail previews. Original scientific/control scripts, payloads, IDs, panels, and historical source remain intact. Artwork retains its illustrative/procedural review limitations.

Edit `src/layout.css` and `src/layout.js`, then run `python3 tools/build_deep_time.py` from the repository root. Preservation tests ensure the imported source is retained apart from its document title and added presentation blocks. Do not edit the imported 1.18 file.

See [specification revision 4](../../specs/deep-time.md), [visual direction](../../specs/visual-direction.md), and root `project_manifest.json`. Start at `/current.html` when serving `atlas/`. Original component histories remain embedded; the new release entry precedes them without renumbering any prior entry.
