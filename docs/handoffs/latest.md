# Codex handoff — repository release 0.1.0

Date: 2026-10-30 (America/Chicago). Previous migration detail is preserved in [migration handoff](2026-10-30-atlas-migration.md). Repository source is identified by annotated tag `v0.1.0` after batch finalization; initial scaffold commit was `f9f88dc`.

## Current batch

Imported Atlas baseline and verified Shared Taxa are preserved unchanged. Added root VERSION/CHANGELOG/TODO, permanent task/spec synchronization instructions, SemVer batch commit/tag/push workflow, and fresh Atlas comparisons with automatic feh preview. This implements explicit user requests; routine batch publishing is now authorized. Deployment, source deletion, force-push, tag rewrites, and publishing GitHub Releases remain outside that authorization.

Root repository version is 0.1.0. Legacy widget/data versions remain unchanged. Root changelog preserves earlier unversioned scaffold history without inventing historical repository releases.

TODO.md holds all 84 historical goals, 28 issues, 25 suggestions, and nine WL tasks. Imported implemented/done claims remain unchecked verification tasks. New findings/suggestions must be recorded and triaged, not silently implemented. WL-005 (interaction regressions) precedes the approved WL-006 layout refinement. Quiz remains unverified.

## Files and specifications

- VERSION, CHANGELOG.md, TODO.md, requirements-dev.txt, AGENTS.md, README.md, and project_manifest.json.
- `docs/development-workflow.md` and approved release/backlog decision.
- Atlas component specs and shared visual direction revision 2; READMEs/component changelogs/context updated.
- `tools/check_project.py`, `tests/test_project_workflow.py`, `tools/capture_atlas_comparisons.py`, and tooling/test documentation.
- Fresh evidence under `docs/visual-reviews/0.1.0/`: seven actual screenshots, seven actual-versus-goal PNGs, HTML reports, companion JSON, index, and viewer result. Original source hashes are unchanged.

## Validation and visual evidence

Shared Taxa: 90/90 listed files match size/SHA-256; 15 JSON schemas pass. Atlas: 1,321 import records and 543 artwork records verified; 39 inline scripts across 14 current HTML pages compile. Six unit tests pass, covering import safety/corruption, SemVer, release drift, missing tasks, false completion, and changed screenshot detection. Project checks also verify current source/goal/actual/comparison hashes and reject recorded runtime exceptions. Staged whitespace checks are part of finalization.

Real Chrome 155 browser captures rendered all seven components with zero captured runtime exceptions. Deep Time was selected to Triassic, Brain to orbitofrontal cortex, Mythology to Greek Zeus; other four used their clean initial state. Both approved goal images are cropped through HTML/CSS for the primary three. Other concept references are clearly labeled proposed. Completed/pending sidebar items are snapshots from TODO.md; full acceptance text remains in TODO and catalogs.

The generator launched feh successfully with all seven comparison PNGs (see `viewer.json`). Fresh browser rendering and targeted selection are smoke checks, not full keyboard/mobile, folder-import, IndexedDB, offline, or scientific testing. External HTTP(S) was blocked to keep screenshots local/deterministic. Scientific uncertainties and artwork/anatomical limitations remain as previously documented.

## Batch finalization and next work

Current authorized batch is committed, annotated-tagged, and pushed only after checks/staged review pass; the final user response reports the actual commit/tag/push outcome. Fetch before pushing, push branch and tag atomically, and verify remote objects. Never imply success after a rejected push.

At future batch start, read AGENTS, manifest, TODO, and affected specs/context. Update tasks/specs/changelog with changes, bump repository VERSION once, capture fresh images for affected Atlas widgets, open them in feh, validate/review, commit/tag/push, and report results. Capture new bugs and proposed improvements as tasks. Do not regenerate the live TODO from historical catalogs.

Next implementation priority: WL-005 browser interaction/viewport coverage, then small WL-006 visual batches toward both goal images. Preserve original widget sources and history. Full custom artwork and registered 3D Brain geometry remain outside the initial layout scope. See the workflow and TODO for other open science, storage, packaging, and Quiz tasks.
