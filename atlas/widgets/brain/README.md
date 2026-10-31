# Brain (Atlas)

Current standalone: [Brain_Atlas_v1.22.0.html](../Brain_Atlas_v1.22.0.html). Preserved import: [Brain_Atlas_v1.21.html](../Brain_Atlas_v1.21.html).

The new presentation moves native view/depth controls into a compact header, enlarges selected-region context, and moves orientation references off the map. Original geometry, records, time filters, region/circuit handlers and depth calculations are retained. The map is authored schematic anatomy with estimated depth, not registered 3D or medical imaging.

Edit `src/layout.css` and `src/layout.js`, then run `python3 tools/build_brain.py`. Preservation tests compare every original byte after removing the added presentation blocks and reversing the title change. Retain prior artifacts/history when creating later releases. Refresh current links with `python3 tools/build_atlas_index.py` after manifest changes.

See [specification revision 4](../../specs/brain.md), [visual direction](../../specs/visual-direction.md), and root manifest. Serve `atlas/` and open `/current.html`. Product startup remains unselected/depth-off; the goal comparison explicitly demonstrates OFC with Medium estimated depth enabled.
