# Atlas Widgets Master Dashboard v1.20 — QA

## Verified in Chromium (inline HTML)
- Dashboard renders without page errors, and release traceability view displays two planned releases.
- Subject A001 cannot be approved from its existing draft preview.
- Imported JSON claiming `art: deep:earth` approved is downgraded to review.
- Imported JSON claiming `subject: A002` approved does not approve the draft.
- Demoting a subject to draft clears the approval flag.
- Valid goal decisions import alongside the quarantined artwork decisions.
- Creating an issue from suggestion S014 yields a linked issue referencing S014.
- Launcher v1.13 initially shows six preflight entries without errors.
- Importing a test HTML with `assets/deep_time/hero/jurassic.webp` displays `Assets missing` and warns on attempted open.
- JavaScript syntax passes Node.js `--check` for dashboard and launcher scripts.

## Not yet tested / deferred
- Real Windows folder synchronization and browser storage persistence, particularly on `file://`.
- Full bundled asset transfer into imported launcher records (not implemented).
- Production release promotion for the five draft calibration subjects (not implemented).
- Cross-widget exploratory regression; seven base scientific/atlas HTML files are carried over byte-for-byte except Launcher.
