# Developer tooling

Run from the repository root:

```sh
python3 tools/verify_migration.py
python3 tools/verify_atlas.py
```

Migration verification checks Shared Taxa's recorded sizes/checksums and JSON schemas, plus registered source hashes. It reports missing optional validation dependencies as incomplete and exits nonzero. It never rebuilds scientific data. Install Python `jsonschema` for schema checks.

Atlas verification checks imported artifacts against `docs/migration/atlas_import_inventory.json`, artwork manifests, delivered widget versions, the prior scientific-widget baseline, and inline JavaScript syntax via Node.js. It does not execute applications or certify scientific/artwork approval.

Both tools operate on imported repository artifacts. They reject private/traversal/symlink inventory paths and do not open incoming files or raw conversations. The existing inventory's source strings are provenance only; verification reads destination paths.

Original imported bytes are a frozen baseline. Preserve them when developing future versions; do not regenerate the inventory to conceal a changed original. Run `python3 -m unittest discover -s tests -v` for audit regression checks.

The imported `shared/taxa/tools/build_shared_taxa_v1.py` is historical release tooling. Do not run it against the canonical package as a setup step: it can rewrite published data and evidence.

`python3 tools/check_project.py` checks repository SemVer, manifest/changelog consistency, task formatting/statuses, complete coverage of the 137 imported task IDs, and current visual evidence hashes. It rejects stale source/goal/screenshot evidence and recorded browser exceptions.

`python3 tools/capture_atlas_comparisons.py --widgets deep-time brain mythology` captures actual applications in headless Chrome, renders comparison reports against original goal references using HTML/CSS, and automatically opens the PNGs in feh. It uses a temporary clean browser profile and local debugging endpoint, blocks external HTTP(S), and leaves original widget bytes unchanged. It refuses to overwrite an existing version/widget comparison. `--no-open` is for CI only. Outputs live under `docs/visual-reviews/<VERSION>/`.

Install Python dependencies from `requirements-dev.txt`; Chrome/Chromium and feh are system prerequisites. Follow `docs/development-workflow.md` for release/version/task maintenance.

`python3 tools/test_atlas_browser.py` performs browser mouse/key input against the three primary Atlas widgets at 390/768/1440px. It tests history keyboard activation/dismissal/focus, search/filter/selection/panels, initial/selected overflow, and runtime errors. Deep Time additionally verifies neighboring title/artwork/breadcrumb changes, all five distinct tabs, and taxon-profile opening/closing. Results and selected screenshots go to `docs/browser-tests/<VERSION>/`; `--output /tmp/... --widths 1440` supports exploratory narrower runs. Only a complete passing matrix against current sources satisfies the registered browser-report check.

The driver sends the Enter character event needed for native button activation and focuses the actual range input before keyboard adjustment. It does not edit or inject application behavior. Sources, science, and original progress formats stay unchanged.

`python3 tools/build_deep_time.py` produces the separate `Deep_Time_Atlas_v1.19.0.html` standalone build from the immutable 1.18 import plus editable presentation CSS/JS in `atlas/widgets/deep-time/src/`. It verifies the original hash first. Preservation tests remove only the added presentation blocks and reverse the document title change, then compare the entire remaining file with the original.

`python3 tools/build_atlas_index.py` updates `atlas/current.html` from current manifest sources. Imported dashboards/catalogs remain historical and unchanged. The Atlas audit now reports both imported versions and active registered sources, and compiles new standalone scripts too.

`python3 tools/build_mythology.py` produces `Mythology_Atlas_v1.14.0.html` from the preserved 1.13 import and editable presentation in `atlas/widgets/mythology/src/`. It embeds the existing featured Greek Zeus image only after matching its manifest checksum. Preservation tests compare all original bytes apart from the document title and added presentation blocks; the offline asset test checks the embedded image against the original file. Later releases must keep prior standalone artifacts/history entries and update builder version/output explicitly.

The Mythology browser scenario also checks both view modes, retained identity, native filters, complementary names, parent/child navigation and profile scroll reset, all five tradition thumbnail keys, current result treatment, disclosures, and reduced motion. These checks do not certify cultural accuracy or a licensed historical-artwork collection.

`python3 tools/build_brain.py` produces `Brain_Atlas_v1.22.0.html` from the preserved 1.21 import and presentation under `atlas/widgets/brain/src/`. The preservation test retains every original geometry/data/control byte apart from the document title and added presentation blocks. No new anatomy assets or depth mathematics are introduced.

Brain browser checks exercise native projections, keyboard/hierarchy selection, usable panel/control widths, orientation-reference changes, per-view depth toggles, Low/Medium/High opacity/radius cues, crisp selected marker, and time presets/reset. The comparison demonstrates OFC with native Medium estimated depth enabled and separately verifies reduced-motion suppression. Startup remains unselected/depth-off; orientation references are not registered selected-structure overlays.
