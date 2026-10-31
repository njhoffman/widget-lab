# Codex handoff — regression verification 0.1.1

Date: 2026-10-30 (America/Chicago). Base: `abfa853` / annotated tag `v0.1.0`. This batch closes a few high-priority tasks that require no new design or scientific decisions. Repository version advances to 0.1.1 for test/verification improvements; component versions and source bytes are unchanged. Previous handoff is preserved in `2026-10-30-release-0.1.0.md`.

## Completed tasks

- WL-005: real-browser interaction/layout baseline for Deep Time, Brain, and Mythology at 390/768/1440px.
- T018: neighboring Jurassic/Triassic controls update selected title, artwork, and breadcrumb at each width.
- T022: all five Deep Time tabs activate and show distinct substantive content from the unchanged source dataset. Independent scientific review remains open in I007.
- WL-010: repeatable real-input test driver plus guards against missing matrix cells, failed cases, and outdated source hashes.

T021 remains open. Its representative-life UI/profile interaction passes, but opening an original embedded profile does not establish canonical Shared Taxa identity or provenance. No original application bug was confirmed: early Enter/slider failures were driver mistakes corrected before recording the final matrix. Temporary failed-driver runs remain outside Git in /tmp; only final evidence is committed.

## Changes

Added `tools/test_atlas_browser.py`; updated project consistency guard and its tests. VERSION/manifest/changelog/TODO now record the batch. Primary component/shared visual specs are revision 3; component changelogs/readmes, context, workflow, and check documentation are synchronized. Browser evidence is in `docs/browser-tests/0.1.1/`; new primary-widget actual-versus-goal images and viewer outcome are in `docs/visual-reviews/0.1.1/`.

## Validation

45/45 real Chrome/Linux scenario checks pass: initial/selected horizontal overflow and title/version bounds, Enter history opening, Escape dismissal and returned focus, visible Tab focus, widget navigation/filter/detail controls, and runtime errors across the full nine-row widget/viewport matrix. Nine selected-state screenshots are retained. Depth control, projection changes, keyboard time filtering/reset, myth tradition switching/search/no-results/reset, distinct Deep Time tabs, neighboring artwork/breadcrumb changes, and taxon-profile open/close were exercised.

Seven unit tests pass, including rejection of incomplete, failed, or stale browser reports. Shared Taxa 90/90 hashes and 15 schemas pass; Atlas 1,321 imported file records and 543 artwork records still match. All 39 inline scripts compile. Project metadata/evidence and staged whitespace checks pass. No scientific, ID, stored-state, or source-version changes were made.

Fresh comparison images for Deep Time, Brain, and Mythology show completed/pending items and are opened automatically in feh; `viewer.json` records whether launch succeeded. Release finalization commits, annotated-tags, atomically pushes, and verifies remote refs; the final user response reports the actual outcome.

## Remaining limits and next priority

Linux Chrome coverage only. Windows folder-picker/sync, IndexedDB/persistence, offline import/export, screen readers/full contrast/accessibility, scientific validation, canonical taxon migration, and bespoke/registered artwork remain open. Shared history tests cover only these three widgets; T005's wider family acceptance is not closed. WL-009 remains an ongoing maintenance task.

Next: begin WL-006 in small visual batches toward the two approved goal images, using the new browser matrix and fresh comparison/feh workflow. Preserve original sources; introduce separately reviewed source versions if modifying implementation. Do not claim anatomical 3D accuracy for schematic Brain projections.
