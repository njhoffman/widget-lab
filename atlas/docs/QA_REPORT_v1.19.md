# Dashboard v1.19 — QA report

**Date:** 2026-10-17  
**Scope:** dashboard audit views and static package integrity; no atlas scientific content edited.

- 7 widget HTML plus dashboard JS passed `node --check`.
- 538/538 artwork SHA-256 hashes matched their manifests.
- 90/90 Shared Taxa published file checksums matched.
- 7/7 widget HTML smoke-rendered in Chromium via inline document loading, with no page errors.
- All 7 widget HTML paths exist and initial static dashboard anchor links resolved in the v1.18 source package.
- Audit dashboard rendered 16 new items; confidence filter returned 3 live-QA gaps.
- Backlog rendered 28 issues total and suggestions rendered 25 proposals total.
- Browser-rendered desktop 1440px and mobile 390px: no horizontal overflow, no page errors.
- Export decisions JSON v1.19 and Save updated HTML reopened in a fresh Chromium page without errors.
- All new suggestion before/after reference images exist; conceptual proposals are labeled not implemented.

**Limitations:** `file://` navigation is administrator-blocked in audit runtime. Browser screenshots were taken with inline content loading, not the full Windows folder/HTTP environment. Relative linked assets were verified as files but not all fetched through the browser. Windows launcher folder sync, IndexedDB persistence, final art-source permissions, scientific validity, keyboard accessibility, and full interaction regressions remain outstanding.

**Release safety:** Items I013/I014/I027 are confirmed audit findings and are **not fixed** by this metadata-only dashboard release.
