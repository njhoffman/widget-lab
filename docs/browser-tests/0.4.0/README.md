# Atlas browser regression — 0.4.0

PASS: 45/45 scenarios, 341 recorded assertions. Browser: Chrome/155.0.8059.84. Captured: 2026-10-31T04:31:49.392875+00:00. [JSON report](report.json) records current hashes and per-assertion results.

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

Brain 1.22.0 additionally verifies native controls in the compact header, disabled strength while depth is off, keyboard OFC selection, identity/hierarchy retention across all projections, selected-marker bounds, three distinct orientation references, per-projection depth on/off cue changes, low/medium/high opacity/radius changes, crisp selected marker, cue restoration, visible schematic labels, time preset/reset counts, usable hierarchy/control widths and actual hierarchy click.

Product source geometry and data remain unchanged. These are native UI/attribute checks, not anatomical calibration or clinical/scientific validation. The orientation inset is not a selected-structure registered overlay. Browser coverage is Linux Chrome; storage/Windows/full accessibility remain separate. Brain comparison evidence separately checks reduced-motion suppression and captures OFC with Medium estimated depth enabled; these matrix screenshots end with depth off after verifying cue restoration.
