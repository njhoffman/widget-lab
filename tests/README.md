# Verification

```sh
python3 -m unittest discover -s tests -v
python3 tools/verify_migration.py
python3 tools/verify_atlas.py
python3 tools/check_project.py
```

The audit regression tests check rejected private/traversal/symlink paths and detection of missing/corrupted inventory files. Full repository audits check Shared Taxa bytes/schemas, source identities, imported Atlas bytes, artwork hashes, and inline JavaScript syntax.

Dependencies: Python 3.9+, `jsonschema`, and Node.js. Missing schema/syntax dependencies produce incomplete results, not a validation pass.

Interactive browser flows, responsive and keyboard behavior, accessibility, offline storage, stable ID/progress compatibility during future changes, and scientific correctness still need dedicated coverage. Existing historical QA reports must not be cited as fresh test results.

Project workflow tests also exercise SemVer edge cases, manifest drift, missing historical tasks, and false task completion. The consistency check validates saved visual evidence hashes against current source/goal images. `tools/capture_atlas_comparisons.py` supplies fresh browser render/selection evidence; it does not replace full interaction tests.

`python3 tools/test_atlas_browser.py` now supplies the defined Chrome/Linux interaction matrix: 45 scenario checks over three widgets at three widths. The prior baseline is in `docs/browser-tests/0.1.1/`. The unit suite additionally verifies that a nominally successful report cannot pass with missing widths, failed cases, or stale sources. Uncovered platforms/storage/full accessibility/scientific claims remain open.

The current 0.2.0 report in `docs/browser-tests/0.2.0/` adds Deep Time header/preview/reduced-motion/age-precision assertions. Unit coverage also checks exact preservation of the original source after removing the allowed presentation blocks and title update, deterministic standalone output, current launch links, and graceful browser shutdown with bounded fallbacks.

Current 0.3.0 evidence is in `docs/browser-tests/0.3.0/`. Mythology coverage adds mode/selection retention, native group/story/symbol filters, complementary Greek/Roman names, related/result thumbnails across all five traditions, parent/child navigation, profile context, art disclosure, and reduced motion. New unit tests preserve the entire 1.13 source and verify that the offline featured Zeus image is exactly the existing checked asset. Historical gallery rights and cultural review remain separate.

Current 0.4.0 evidence adds Brain projection/depth/header/hierarchy/time-filter checks; source-preservation coverage now includes the complete 1.21 Brain import and all authored geometry/transforms. Brain comparison JSON records a reduced-motion transition check and its explicit Medium estimated-depth capture configuration. Per-view cue/selection checks do not certify all-region anatomical registration or clinical accuracy.
