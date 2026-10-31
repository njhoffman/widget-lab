# Codex handoff — Deep Time visual batch 0.2.0

Date: 2026-10-30 (America/Chicago). Base commit: `e4344b8` / tag `v0.1.1`. Repository advances to 0.2.0 for the first visible layout feature batch. Deep Time advances to the new standalone version 1.19.0; historical 1.18 remains unchanged and is not retroactively renumbered.

## Delivered

- Deep Time header now contains the original topic navigation and search alongside title, actual data chips and version, with responsive wrapping.
- Selected interval scene and panel composition refined; existing nearby previews enlarged with source age labels, current state and native navigation. Recent Holocene 0.0117 Ma precision is preserved.
- Existing science cards, filters, timelines, taxon profiles, IDs, source payloads and artwork limitations retained.
- New `atlas/current.html` links all seven registered active sources; imported dashboards/catalogs remain historical. Start at `http://localhost:8765/current.html` when serving atlas/.
- Original Deep Time HTML stays intact. New standalone is built deterministically from that import plus editable presentation CSS/JS in `atlas/widgets/deep-time/src/`.

## Tasks and specs

Closed WL-011 (Deep Time layout batch), WL-012 (current-build launch page), WL-013 (recent-age preview precision), WL-015 (graceful browser shutdown), T016 (topic/search header), and T017 (thumbnail/age/current state). Broader WL-006 remains in progress; Brain/Mythology layout and bespoke artwork are future batches. Added WL-014 as a proposed improvement for overly tall comparison sheets; it is not implemented.

Deep Time and shared visual specs are revision 4. Component changelog adds 1.19.0 ahead of retained history. Root changelog/version/manifest/TODO/context and build/check instructions are synchronized.

## Verification

All 45 Chrome/Linux browser scenario checks pass at 390/768/1440px for Deep Time, Brain and Mythology. The Deep Time scenario now also tests compact header containment/height, manifest-backed ages, clickable preview selection/current state, reduced-motion preferences, and Holocene precision. Source hashes are in `docs/browser-tests/0.2.0/report.json`; selected-state screenshots and summary are adjacent.

All 11 unit tests pass, including original-source byte preservation after removing only added presentation blocks/reversing the title, deterministic generated output, all current launcher source links, shutdown behavior, stale/incomplete reports, release/task metadata and import safety. The new source title/version and original imported versions are both checked; 47 inline scripts across 16 HTML pages compile. Original Shared Taxa 90-file/15-schema, 543 artwork-record, and 1,321 imported-file checks pass unchanged.

During screenshot review, an inherited `grid-template-columns:none!important` rule caused excess desktop header height; fixed with explicit scoped grid placement and a height assertion. Initial three-decimal preview formatting could round recent boundaries; fixed before release and covered by Holocene assertion. Chrome profile cleanup once raced renderer writes after forced termination; switched to graceful Browser.close with bounded fallbacks. Final browser run exits cleanly; no cleanup errors are suppressed. Intermediate diagnostic runs stayed outside committed evidence.

Fresh Deep Time actual-versus-goal PNG, HTML, actual screenshot, hashes and task statuses are in `docs/visual-reviews/0.2.0/`. Automatic feh opening is recorded in viewer.json. Original comparison evidence for previous versions is retained. Release finalization commits, annotated-tags and atomically pushes the batch; final user response reports actual remote outcome.

## Boundaries and next work

No new artwork, scientific claims, paleomaps, taxonomy, date values or progress/storage migration. Triassic art remains procedural; goal-like cinematic artwork still needs individual creation/review. T021 canonical taxon provenance remains open. Browser coverage is Linux Chrome, not Windows storage, folder-picker, exhaustive accessibility, screen-reader or scientific validation.

Next: continue WL-006 with a similarly scoped Brain or Mythology visual batch against both goal references. Preserve originals, add an explicit standalone version, rerun the browser matrix and source-preservation checks, produce comparisons and open feh, then release the validated batch.
