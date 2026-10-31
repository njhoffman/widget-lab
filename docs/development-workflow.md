# Development and release workflow

Approved on 2026-10-30. This repository follows the user's Claude setup conventions for VERSION, changelog, annotated tags, priorities, and categories. Existing imported components retain their historical version formats.

## Start a batch

Read `project_manifest.json`, `AGENTS.md`, `TODO.md`, the relevant specs/context, and git status. Select an approved coherent group of tasks. New findings become tasks immediately; new suggestions become proposed tasks. Add acceptance criteria and source/spec references. Proposals must be curated and approved before implementation.

TODO task format: checkbox, stable ID and title, `(p1)` / `(p2)` / `(p3)`, category, and status. Statuses are `approved`, `triage`, `proposed`, `needs-verification`, `in-progress`, `blocked`, or `done`. Use `WL-001` onward for new repository tasks; retain original T/I/S IDs for imported records. Record dependencies, duplicates, completion evidence, and spec revisions in task details.

Historical priorities P0 and P1 map to high (p1), P2 to normal (p2), P3 to low (p3); original priorities remain in the immutable catalog. Historical implemented/done items become unchecked verification tasks until their acceptance checks are independently demonstrated. The four issues marked done historically are not automatically reopened bugs. Triage I015 specifically against Launcher v1.14's newer artwork-folder implementation before changing it.

## During work

Update the live TODO and relevant spec revision in the same change. Capture bugs, test findings, and suggestions with concrete triggers and acceptance criteria. Link rather than duplicate overlapping tasks. Close only with evidence; preserve deferred work and historical IDs. Keep changelog Unreleased entries current. Do not regenerate TODO from the catalog: the imported catalog is provenance, not mutable task state.

## Atlas evidence

For every affected Atlas widget, capture a fresh real browser screenshot, compare with the relevant goal reference(s), and list completed/pending items alongside the pictures. Run:

```sh
python3 tools/capture_atlas_comparisons.py --widgets deep-time brain mythology
```

Omit `--widgets` to capture all seven components. The tool writes HTML, PNG, actual screenshot and JSON evidence under `docs/visual-reviews/<VERSION>/`, then opens comparison PNGs with `feh`. For CI only, use `--no-open`. No screenshot synthesizes actual UI. Evidence includes version/source/goal hashes, viewport, deterministic selection, browser version, timestamp, and task IDs. Goal reference versions and counts are illustrative; existing concept targets for the other four components remain proposed. The report labels those approvals explicitly.

Read and inspect the images; rendering alone does not validate interactions or scientific accuracy. Capture details/selection changes and additional viewport evidence when the task requires them. Keep existing baseline images; a later batch has a new repository version and evidence directory.

## Finish and publish a batch

1. Run meaningful checks, inspect results, and update task statuses with evidence. Include `python3 tools/verify_migration.py`, `python3 tools/verify_atlas.py`, `python3 tools/check_project.py`, and `python3 -m unittest discover -s tests -v` for this setup.
2. Bump root VERSION once for the batch, mirror `repository.release_version` in the project manifest, move Unreleased changelog entries into `## [X.Y.Z] - YYYY-MM-DD`, and refresh the handoff. Patch for fixes/docs/small changes; minor for new features; major for breaking changes, with minor used for breaking changes before 1.0.
3. Generate final Atlas comparison evidence using that version; automatically open it in feh. Review staged files for accidental private imports, unrelated changes, and unexpected source/hash changes. Never stage `.local/`, `incoming/`, full exports, secrets, or browser profiles.
4. Fetch origin and confirm the branch can fast-forward. Commit the complete reviewed batch and create an annotated `vX.Y.Z` tag on that commit. Push the branch and tag together with `git push --atomic origin HEAD:main refs/tags/vX.Y.Z` (use the actual branch if not main).
5. Verify remote branch/tag objects, report version, commit, tag and checks. Preserve local work and explain any rejected/failed push; do not force or overwrite a tag.

The user authorized routine commit/tag/push at batch completion, so another conversational confirmation is unnecessary. Tool sandbox approvals may still be required. This authorization does not include deployment, publishing GitHub Releases, force-pushing, deleting sources, or resolving an unexpected destructive conflict.

For primary Atlas work, run `python3 tools/test_atlas_browser.py` after selecting the batch VERSION and before closing WL-005-related regressions. Keep the complete 3-widget × 3-width report and selected-state screenshots. `repository.browser_regression_report` identifies the current registered report; project checks require its source hashes to match current implementations and all 45 scenario cells to pass. A narrower exploratory run does not satisfy that gate. Screenshots and interaction results do not close canonical provenance or scientific-review tasks.

Initial repository release is 0.1.0. Legacy imported versions such as Brain 1.21 are intentionally unchanged. A future independently released widget can adopt a full three-part version with explicit migration documentation rather than retroactively renumbering historical artifacts.
