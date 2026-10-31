# Atlas browser regression — 0.2.0

PASS: 45/45 scenario checks, 169 recorded assertions. Browser: Chrome/155.0.8059.84. Captured: 2026-10-31T03:44:23.000845+00:00. See the [JSON report](report.json) for current source hashes and per-assertion results.

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

Deep Time 1.19.0 passes the previous control/navigation/history/focus/overflow matrix plus header containment and desktop compactness, source-backed preview ages, actual preview navigation/current state, reduced-motion emulation, and Holocene 0.0117 Ma precision. The three selected-state screenshots per widget now start at the top of the page for readable cross-viewport comparisons.

Brain/Mythology retain their previous source hashes and pass the same matrix. This is Chrome/Linux coverage: Windows, storage/folder-picker, screen readers/full accessibility, scientific review, and canonical provenance remain separate work. The Chrome shutdown/profile-cleanup race was corrected and the final matrix process exits successfully.
