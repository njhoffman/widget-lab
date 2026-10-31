# Atlas interaction regression — 0.4.2

Chrome/Linux, 2026-10-31: **45/45 scenarios pass, 341 assertions**. See [report.json](report.json) for browser, capture time, source hashes and per-assertion outcomes. The complete three-widget × three-width × five-scenario matrix covers Deep Time 1.19.0, Brain 1.22.0 and Mythology 1.14.0 at 390/768/1440px. Nine selected-state screenshots are retained alongside this file.

Sources are unchanged from 0.4.0. Real mouse/key input verifies initial/selected layouts, keyboard history dismissal/focus, navigation/filter/panel behavior and runtime exceptions, including the existing widget-specific presentation assertions. Registered source hashes and complete unique coverage are enforced by `just check`.

Run `just browser-test` after choosing a new batch VERSION. Image coverage/byte parity is separately verified in [offline artwork evidence](../../artwork-tests/0.4.2/README.md). Windows, IndexedDB/folder-picker/storage, screen readers/contrast and scientific/cultural approval remain outside this matrix.
