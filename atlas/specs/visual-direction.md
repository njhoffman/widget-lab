# Atlas visual direction

**Status:** APPROVED direction and migration safeguards; implementation backlog is proposed.  
**Spec revision:** 6  
**Last reviewed:** 2026-10-30  
**Authority:** User's request to prioritize Atlas and `goal_1.png` / `goal_2.png`, followed by authorization to curate and finish repository setup.

## Approved direction

Use [goal_1.png](../images/goal_1.png) and [goal_2.png](../images/goal_2.png) as visual references. Both are retained unchanged. The second image illustrates a compact, integrated layout; preserve verified scientific functionality throughout visual changes.

- Dark navy backgrounds, thin cyan borders, rounded panels, cyan/mint selected states, and readable light text.
- Consistent compact headers with topic identity, contextual controls, actual data counts, and the real component version.
- A hierarchy or figure browser beside an illustrated focal region and relevant detail panels, as viewport space allows.
- Deep Time: illustrated selected interval, adjacent intervals, topic tabs, and separate environmental/life/context information.
- Brain: selected region alongside hierarchy, view controls, explanatory information, and clearly described depth behavior.
- Mythology: figure artwork, searchable/filterable figure list, tradition-aware metadata, and related figures or stories.
- Preserve stable identifiers, existing scientific content, embedded release histories, and browser-state formats throughout visual changes.
- Derive counts and version labels from actual verified artifacts. Mockup numbers, including image/link totals and geological labels, are illustrative.

## Baseline and limits

The source baseline is the delivered master v1.21 package. See `project_manifest.json` and `docs/migration/atlas_verification_report.json` for actual widget versions and checks.

The source asset library has 172 Deep Time entries, 363 Mythology entries, 3 Brain schematic views, and 5 featured concepts. Hero/thumbnail files make the physical file count larger. Procedural illustrations and collage crops are not a complete set of bespoke paintings. Source artwork review flags remain intact.

The Brain source uses authored schematic projections and estimated depth. The reference's volumetric-looking brain is an aspiration requiring registered geometry, provenance, and anatomical review before it can be represented as accurate anatomy. Keep current depth limitations visible in any redesign.

## Required evidence for every Atlas update

Approved on 2026-10-30: every widget update must end with fresh real-versus-goal comparison PNGs, completed/pending items listed alongside, and automatic opening in `feh`. Run `tools/capture_atlas_comparisons.py` for affected widgets with the new repository VERSION. Retain the actual browser screenshot, comparison HTML/PNG, and companion JSON containing source/goal hashes, viewport, selection, browser version, capture date, and task IDs under `docs/visual-reviews/<VERSION>/`.

Both approved goal images apply to Deep Time, Brain, and Mythology. Other components' existing concept images are explicitly proposed until individually approved. Use the actual app rendering, never generated or repainted UI. Report screenshot smoke checks separately from interaction/science review. See [workflow](../../docs/development-workflow.md), TODO tasks WL-004/T084, and the initial [visual review](../../docs/visual-reviews/0.1.0/index.html).

## Acceptance criteria for subsequent visual implementation

- Compare the same selections before and after at desktop and narrow mobile widths; preserve working hierarchy navigation, filters, tabs, selected-state highlighting, and existing scientific panels.
- Record screenshots against both goal references and distinguish implemented details from aspirational artwork.
- Exercise keyboard focus, selected-state contrast, reduced-motion behavior, and panel stacking without clipping important controls.
- Preserve existing localStorage / IndexedDB keys and stored-state shapes; test import/export and launcher artwork handling before any storage migration.
- Retain original sources until functional regression tests pass. New widget releases require an explicit source/version/changelog review.
- Treat artwork review and scientific claims separately from checksum validation. Never promote old chat proposals or dashboard suggestions into approved features automatically.

## Proposed sequence — not a completed release

1. Establish interactive browser screenshots and regression coverage for the imported Deep Time, Brain, and Mythology builds.
2. Refine the compact shared header/panel layout against the references while preserving existing controls.
3. Develop selected-subject artwork individually, retaining provenance and review status. Start with existing calibration subjects rather than replacing the entire dataset.
4. Evaluate true registered Brain geometry separately from layout work.

Tree of Life, Muscles, Emergence, and Launcher inherit the shared visual language. Their subject-specific layouts require their own approved targets; the two images do not define those details.

## Decision history

See [migration decision](../../docs/decisions/2026-10-30-atlas-migration-baseline.md) and [curated Atlas context](../../docs/context/atlas_master.md).

## Verified starting point — repository 0.1.1

WL-005 is complete for the defined Chrome/Linux matrix: [45 checks](../../docs/browser-tests/0.1.1/README.md) across three widgets and three viewport widths. Repeat the suite before/after a visual-source change. The complete matrix and source hashes are enforced by the project consistency check. Fresh [goal comparisons](../../docs/visual-reviews/0.1.1/index.html) retain exact imported source hashes.

WL-006 layout refinements may now begin in small batches; full accessibility, scientific review, canonical taxon provenance, Windows storage and launcher persistence remain separately tracked. No visual redesign or new scientific claim is part of this verification release.

## First visual implementation — repository 0.2.0

Deep Time 1.19.0 implements the first scoped WL-006 batch: compact topic/search header, clearer interval stage, larger nearby previews with actual ages/current state, and responsive panel styling. Its original 1.18 science/control source is retained verbatim, except for the standalone document title; added CSS/JS changes presentation and release metadata only. The current-build launch page routes to registered source versions without rewriting imported dashboards.

Age labels retain recent four-decimal boundaries, including Holocene 0.0117 Ma. Added browser checks enforce header compactness, manifest-backed preview ages, preview navigation/current state, and reduced motion. The original art and anatomical/scientific disclosures remain unchanged. Further bespoke artwork and the other widgets' layout refinements remain pending under WL-006 and their linked tasks.

## Mythology visual implementation — repository 0.3.0

Mythology 1.14.0 continues WL-006 with an artwork-first stage, clear Artwork / Family tree controls, compact search header, readable profile, and tradition-correct related thumbnails. It reuses the verified existing Greek Zeus concept with explicit modern/AI interpretation and review caveats; other figures retain their current local illustrations. Original 1.13 data/control source and historical entries are preserved in the new standalone build.

Mode changes retain selected figure identity; original filters, name controls and genealogy tools remain functional. Related thumbnails use the current tradition rather than searching Greek first. Newly selected profiles begin at their heading, and tree-only labels are hidden in artwork mode. Cross-viewport browser checks and byte-preservation tests are required. Bespoke portraits, historical gallery licensing/provenance, and remaining Brain/general layout work remain pending.

## Brain visual implementation — repository 0.4.0

Brain 1.22.0 continues WL-006 with native projection/estimated-depth controls in the compact header, a larger live selected-region summary, clear scientific details, and orientation/depth context moved off the interactive map. Authored SVG paths, region/circuit records, transforms, clinical/evolutionary text and native depth mathematics are preserved unchanged. The original 1.21 file remains intact.

Depth strength is inactive while depth is off; original Low/Medium/High choices and cue behavior remain. Authored schematic/not-volumetric labels stay visible beside the drawing. References remain orientation-only; registered 3D, new calibrated assets and selected-structure inset overlays remain pending. Mobile hierarchy controls must retain usable widths, and source-preserving builds plus native browser checks cover projections, depth, time filters, keyboard/hierarchy selection and reduced motion.

Fresh Brain comparisons select OFC, lateral schematic, estimated depth on at Medium to match the goal reference's mode; startup defaults are unchanged. This configuration is recorded in evidence and differs from older depth-off comparison snapshots. The broad WL-006 visual/artwork work remains in progress beyond these first three primary-widget batches.
