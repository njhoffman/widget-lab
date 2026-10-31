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
