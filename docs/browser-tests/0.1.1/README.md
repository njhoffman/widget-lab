# Atlas browser regression baseline — 0.1.1

Status: PASS — 45/45 scenario checks. Browser: Chrome/155.0.8059.84. Captured: 2026-10-31T03:27:12.646933+00:00. Full [JSON report](report.json) includes source hashes, per-assertion results, and task coverage.

| Widget | Width (px) | Passed | Selected-state screenshot |
|---|---|---|---|
| deep-time | 390 | 5/5 | [deep-time-390-selected.png](deep-time-390-selected.png) |
| deep-time | 768 | 5/5 | [deep-time-768-selected.png](deep-time-768-selected.png) |
| deep-time | 1440 | 5/5 | [deep-time-1440-selected.png](deep-time-1440-selected.png) |
| brain | 390 | 5/5 | [brain-390-selected.png](brain-390-selected.png) |
| brain | 768 | 5/5 | [brain-768-selected.png](brain-768-selected.png) |
| brain | 1440 | 5/5 | [brain-1440-selected.png](brain-1440-selected.png) |
| mythology | 390 | 5/5 | [mythology-390-selected.png](mythology-390-selected.png) |
| mythology | 768 | 5/5 | [mythology-768-selected.png](mythology-768-selected.png) |
| mythology | 1440 | 5/5 | [mythology-1440-selected.png](mythology-1440-selected.png) |

Each row covers initial layout, keyboard version-history open/dismiss/focus, widget navigation/filter/panel behavior, selected layout, and runtime errors. Deep Time clicks all five topic tabs, compares distinct substantive content, navigates adjacent Jurassic/Triassic intervals, verifies selected title/artwork/breadcrumb changes, and opens/closes a representative-life taxon profile. Brain exercises selected regions, all projection controls, schematic depth, keyboard time filtering, and reset. Mythology exercises figure search/selection, tradition switching, empty results, and reset.

Sources match the preserved imported widget hashes. Linux Chrome only: no Windows, launcher persistence, IndexedDB, folder-picker, screen-reader, full contrast/accessibility audit, or scientific fact-checking. A passing original taxon-profile UI does not prove canonical Shared Taxa migration; T021 stays open.

Rerun from the repository root: `python3 tools/test_atlas_browser.py`. Reports must have the complete unique matrix and current source hashes to pass `tools/check_project.py`.
