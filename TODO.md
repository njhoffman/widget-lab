# Widget Lab task list

Reviewed: 2026-10-30 · Repository release: 0.2.0

Every task has a stable ID, priority `(p1)` high / `(p2)` normal / `(p3)` low,
a category `[bug]`, `[feature]`, `[refactor]`, `[docs]`, `[test]`, `[chore]`, or `[perf]`,
and a status. Checked items are complete with evidence. Unchecked imported
implemented/done records are verification tasks, not newly confirmed regressions.

Live backlog: update alongside specs, features, findings, suggestions, and batch releases.
`approved` authorizes the written scope; `triage`, `proposed`, and `needs-verification`
do not authorize speculative features. See [workflow](docs/development-workflow.md).
Historical IDs and acceptance criteria come from the [v1.21 catalog](atlas/data/project_catalog_v1.21.json).
Historical P0/P1 map to p1; P2 to p2. Within each section, work approved p1 items first.

## 1. Repository, workflow, and migration

- [x] **WL-001 — Import and verify the Atlas baseline.** (p1) [chore] [done]
  Preserve original HTML/science/history; restore the complete Shared Taxa package.
  Acceptance/evidence: [import report](docs/migration/atlas_verification_report.json) and [dataset report](docs/migration/verification_report.json) pass; source identities are in the manifest.
- [x] **WL-002 — Establish SemVer and batch publishing.** (p1) [chore] [done]
  Add VERSION, root changelog, annotated tag policy, and recurring commit/push authorization.
  Acceptance/evidence: [workflow](docs/development-workflow.md), [AGENTS.md](AGENTS.md), and project consistency checks; final push result is reported at batch completion.
- [x] **WL-003 — Maintain a categorized, prioritized live backlog.** (p1) [docs] [done]
  Preserve all 84 T, 28 I, and 25 S records; require task updates with specs/features/issues/suggestions.
  Acceptance/evidence: this file, approval/status conventions, and `tools/check_project.py` catalog coverage checks.
- [x] **WL-004 — Produce actual-versus-goal evidence and open it in feh.** (p1) [feature] [done]
  Capture all seven original components in a real browser, add goal crops and completed/pending side lists, retain hashes and selection evidence, and open the produced PNGs automatically.
  Acceptance/evidence: [visual review index](docs/visual-reviews/0.1.0/index.html), companion JSON, and `tools/capture_atlas_comparisons.py`; desktop viewer outcome is recorded in the handoff.
- [x] **WL-005 — Exercise Atlas browser interactions before visual refactoring.** (p1) [test] [done]
  Test hierarchy/filter/selection/topic panels, keyboard focus, and 390/768/1440px layouts for Deep Time, Brain, and Mythology.
  Acceptance/evidence: [45/45 real-browser checks](docs/browser-tests/0.1.1/README.md) and nine selected-state screenshots at 390/768/1440px; original source hashes preserved. Spec: [visual direction r3](atlas/specs/visual-direction.md). Chrome/Linux coverage; storage/Windows/scientific checks remain separate.
- [ ] **WL-006 — Refine the goal-image layout without scientific regressions.** (p1) [feature] [in-progress]
  Work in small reviewed widget batches toward the two goal references; preserve existing controls and informative panels.
  Acceptance: browser checks pass and new real-versus-goal images show completed/pending items with source/version metadata. Depends on WL-005; speculative science and new anatomical geometry remain outside this scope.
- [ ] **WL-007 — Import and verify Quiz sources.** (p2) [chore] [triage]
  Locate artifacts, verify actual versions/question IDs/storage formats, curate specs, and capture initial checks before enabling new features.
  Acceptance: manifest source evidence and approved Quiz specs; null versions remain unverified until then.
- [ ] **WL-008 — Reconcile distribution downloads and dataset duplication.** (p2) [refactor] [triage]
  Choose a nonrecursive distribution and canonical dataset routing while retaining originals. Related: I016.
  Acceptance: dashboard download actions and source links tested; no unexplained duplicated release archive or lost data.
- [ ] **WL-009 — Extend task coverage to new spec changes and findings.** (p2) [docs] [approved]
  During each future batch, add concrete tasks for newly found issues and proposed suggestions; update affected acceptance criteria and spec revisions.
  Acceptance: no new requirement or known issue left only in chat/handoff; checklist guard and review pass. This is an ongoing process, not automatically completed by the initial import.

- [x] **WL-010 — Guard browser evidence against incomplete coverage and stale sources.** (p1) [test] [done]
  Add a repeatable real-input regression runner and validate its full unique 3-widget/3-width matrix against current source hashes. Correct Enter character events and focus the overlapping range input for keyboard testing.
  Acceptance/evidence: [browser report](docs/browser-tests/0.1.1/report.json), `tools/test_atlas_browser.py`, and `test_browser_report_cannot_claim_success_with_missing_coverage_or_stale_sources` in the unit suite. No application bugs inferred from test-driver mistakes.

- [x] **WL-011 — Refine Deep Time header, interval scene, and preview strip.** (p1) [feature] [done]
  First WL-006 implementation batch: move existing topics/search into the header, enlarge interval previews with actual ages/selected state, and retain all scientific panels and original baseline bytes.
  Acceptance/evidence: Deep Time spec revision 4, [complete browser matrix](docs/browser-tests/0.2.0/README.md), preview/header/reduced-motion assertions, preserved-source build test, and fresh goal comparison opened in feh.
- [x] **WL-012 — Launch current builds without rewriting imported dashboards.** (p1) [feature] [done]
  Generate `atlas/current.html` from registered sources and direct users to current versions while retaining original dashboard/source artifacts.
  Acceptance/evidence: [current launch page](atlas/current.html), all seven source links exist and match the manifest (`test_current_launcher_matches_registered_sources`); Deep Time 1.19.0 passes browser checks.

- [x] **WL-013 — Preserve recent interval age precision in previews.** (p1) [bug] [done]
  The new preview formatter initially rounded four-decimal source boundaries. Preserve the manifest precision, including Holocene 0.0117 Ma, without changing the dataset.
  Acceptance/evidence: [browser report](docs/browser-tests/0.2.0/report.json) checks Holocene 0.0117 Ma at 390/768/1440px.
- [ ] **WL-014 — Make visual comparison sheets easier to scan.** (p2) [feature] [proposed]
  Current full backlog sidebars make comparison PNGs tall. Explore concise priority summaries while keeping complete task details/evidence available.
  Acceptance: approve the report layout, retain actual/goal provenance and completed/pending IDs, and compare readability at typical feh window sizes.
- [x] **WL-015 — Close Chrome gracefully before removing its test profile.** (p1) [bug] [done]
  A passing matrix exposed a renderer/profile cleanup race after forced browser termination. Request browser shutdown and wait, retaining bounded terminate/kill fallbacks.
  Acceptance/evidence: two shutdown unit tests and the final real browser matrix exit successfully without suppressing profile cleanup errors; fresh capture/viewer result is retained with this release.

## 2. Shared UI and accessibility

- [ ] **T001 — Verify existing: Retain compact one-line title/subtitle with responsive natural wrap.** (p1) [test] [needs-verification]
  Acceptance: No overlap at 320, 390, 768 and 1440px; badges flow after title
  Source: catalog `goals/T001`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T005 — Verify existing: Preserve historical changelog entries and click-to-expand version control.** (p1) [test] [needs-verification]
  Acceptance: All previous releases accessible; newest open
  Source: catalog `goals/T005`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T006 — Verify existing: Compact statistics typography and balanced rows.** (p1) [test] [needs-verification]
  Acceptance: Segoe UI/system stack, ~12px rows with compact padding
  Source: catalog `goals/T006`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T010 — Automate regression for header, popup, versions and mobile breakpoints.** (p1) [feature] [proposed]
  Acceptance: Recorded checks plus Windows folder-launch verification
  Source: catalog `goals/T010`; historical status `partial`, priority `P0`.

- [ ] **T002 — Apply consistent navy gradient with subtle colored subject identity.** (p1) [feature] [proposed]
  Acceptance: Same sizing and palette tokens across all seven components
  Source: catalog `goals/T002`; historical status `partial`, priority `P1`.

- [ ] **T003 — Match illustrated reference icon scale and clarity.** (p1) [feature] [proposed]
  Acceptance: Icon artwork matched in proportions without image/text distortion
  Source: catalog `goals/T003`; historical status `partial`, priority `P1`.

- [ ] **T004 — Verify existing: Align version and data chips, equal control heights.** (p1) [test] [needs-verification]
  Acceptance: Equal heights across desktop and narrow layouts
  Source: catalog `goals/T004`; historical status `implemented`, priority `P1`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T007 — Verify existing: Unify overlay spacing and one-row title/close control.** (p1) [test] [needs-verification]
  Acceptance: No separate header bar; accessible dismiss
  Source: catalog `goals/T007`; historical status `implemented`, priority `P1`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T008 — Consolidate hover/active/selected/focus styles and common green stat emphasis.** (p1) [feature] [proposed]
  Acceptance: No gold selected styles in shared controls; keyboard focus visible
  Source: catalog `goals/T008`; historical status `partial`, priority `P1`.

- [ ] **I001 — Close remaining header/hero visual gap.** (p1) [bug] [triage]
  Scope: Target-vs-current comparisons still show differences in compactness, panel composition, and controls.
  Acceptance: Before/after screenshots reviewed on 390px, 768px, and 1440px.
  Source: catalog `issues/I001`; historical status `open`, priority `P1`.

- [ ] **S022 — Standard keyboard, reduced-motion and visual-contrast test plan.** (p1) [feature] [proposed]
  Scope: Apply the same focus, motion and popup keyboard handling to all six atlases and launcher; save a per-version acceptance log.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S022`; historical status `proposed`, priority `P1`.

- [ ] **T009 — Match reference luminous panel edges and restrained atmospheric fills.** (p2) [feature] [proposed]
  Acceptance: Shared elevation/token system; accessible contrast
  Source: catalog `goals/T009`; historical status `partial`, priority `P2`.

- [ ] **I026 — Keyboard, contrast and responsive coverage is not maintained as a uniform regression matrix.** (p2) [bug] [triage]
  Scope: All seven pages rendered in a Chromium smoke check; this does not prove keyboard-only navigation, dialogs/focus traps, screen readers or all viewport breakpoints across all flows.
  Acceptance: Run axe/keyboard/contrast and 320/390/768/1440 responsive checks per release, recording exceptions by widget.
  Source: catalog `issues/I026`; historical status `open`, priority `P2`.

## 3. Deep Time Atlas

- [ ] **T011 — Verify existing: Resolve image for every indexed Deep Time interval.** (p1) [test] [needs-verification]
  Acceptance: 172/172 IDs resolve without missing images
  Source: catalog `goals/T011`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T012 — Verify existing: Maintain adjacent-folder bundle and single-file offline editions.** (p1) [test] [needs-verification]
  Acceptance: Both work without network; checksums match
  Source: catalog `goals/T012`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T013 — Verify existing: Large interval-specific illustrated hero with text-safe overlay.** (p1) [test] [needs-verification]
  Acceptance: Text remains legible over varied images
  Source: catalog `goals/T013`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T014 — Replace procedural palette/silhouette variations with bespoke period scenes.** (p1) [feature] [proposed]
  Acceptance: Major intervals have distinct compositions and curated captions
  Source: catalog `goals/T014`; historical status `partial`, priority `P0`.

- [ ] **T015 — Complete 13 flagship scene upgrades in Batch 1.** (p1) [feature] [proposed]
  Acceptance: 13/13 scientifically reviewed and approved
  Source: catalog `goals/T015`; historical status `planned`, priority `P0`.

- [ ] **T023 — Track geological data provenance and artwork uncertainty.** (p1) [feature] [proposed]
  Acceptance: Separate facts from illustration and date sources
  Source: catalog `goals/T023`; historical status `partial`, priority `P0`.

- [ ] **I002 — Replace procedural interval artwork with researched scenes.** (p1) [bug] [triage]
  Scope: 172 intervals have direct assignments but many are variations from shared themes.
  Acceptance: Flagship scenes separately commissioned/generated and reviewed for period plausibility.
  Source: catalog `issues/I002`; historical status `open`, priority `P0`.

- [ ] **S001 — Turn the interval hero into a cohesive editorial scene.** (p1) [feature] [proposed]
  Scope: Rebalance scene, title, tabs and supporting facts; keep period art and existing five-topic data.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S001`; historical status `proposed`, priority `P0`.

- [x] **T016 — Place compact view tabs and search alongside header like concept, without crowding.** (p1) [feature] [done]
  Acceptance: All controls available, no title overlap, responsive
  Source: catalog `goals/T016`; historical status `partial`, priority `P1`.
  Approved scope/evidence: Deep Time spec revision 4, [0.2.0 browser report](docs/browser-tests/0.2.0/README.md), and [fresh goal comparison](docs/visual-reviews/0.2.0/deep-time-comparison.png). Existing artwork/review limits remain.

- [x] **T017 — Show polished geology thumbnail previews with selected outline.** (p1) [feature] [done]
  Acceptance: Period thumb/age text and selected state clear
  Source: catalog `goals/T017`; historical status `partial`, priority `P1`.
  Approved scope/evidence: Deep Time spec revision 4, [0.2.0 browser report](docs/browser-tests/0.2.0/README.md), and [fresh goal comparison](docs/visual-reviews/0.2.0/deep-time-comparison.png). Existing artwork/review limits remain.

- [x] **T018 — Verify existing: Click neighboring intervals to navigate.** (p1) [test] [done]
  Acceptance: Selection updates text, artwork, breadcrumbs
  Source: catalog `goals/T018`; historical status `implemented`, priority `P1`.
  Evidence: [0.1.1 browser report](docs/browser-tests/0.1.1/report.json), Deep Time navigation-filters-panels at 390/768/1440px; source checksum unchanged. Scientific interpretation remains separately tracked in I007.

- [ ] **T019 — Replace generic sidebar with period-specific icon/fact rows and soft scene background.** (p1) [feature] [proposed]
  Acceptance: Rank, range, duration, previous/next, paleoenvironments and representative life
  Source: catalog `goals/T019`; historical status `partial`, priority `P1`.

- [ ] **T020 — Real paleomap/continental reconstruction by geologic interval.** (p1) [feature] [proposed]
  Acceptance: Licensed/source-attributed maps from suitable dated reconstructions
  Source: catalog `goals/T020`; historical status `planned`, priority `P1`.

- [ ] **T021 — Verify existing: Clickable representative organism art and taxon details.** (p1) [test] [needs-verification]
  Acceptance: Click representative life -> canonical taxon profile with evidence
  Source: catalog `goals/T021`; historical status `implemented`, priority `P1`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.
  Partial verification: current UI cards open substantive original taxon profiles at all three widths (0.1.1 report). Keep this task open until canonical Shared Taxa identity/provenance is independently checked; the original embedded dataset has not been migrated.

- [x] **T022 — Verify existing: Distinct Overview/Climate/Continents/Geology/Life content presentation.** (p1) [test] [done]
  Acceptance: All tabs interactive and scientifically grounded; no fake datasets
  Source: catalog `goals/T022`; historical status `implemented`, priority `P1`.
  Evidence: [0.1.1 browser report](docs/browser-tests/0.1.1/report.json), Deep Time navigation-filters-panels at 390/768/1440px; source checksum unchanged. Scientific interpretation remains separately tracked in I007.

- [ ] **S002 — Make representative-life cards into a richer specimen browser.** (p1) [feature] [proposed]
  Scope: Expand cards to real linked taxa and verified source previews, not mockup species or invented counts.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S002`; historical status `proposed`, priority `P1`.

- [ ] **S024 — Link interval artwork to traceable paleomaps and representative life.** (p1) [feature] [proposed]
  Scope: Add verified interval-specific continents/paleomap assets and dated taxon references with citations and exclusions where evidence is weak.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S024`; historical status `proposed`, priority `P1`.

- [ ] **T024 — In-atlas artwork gallery with alternative views for interval.** (p2) [feature] [proposed]
  Acceptance: Thumbnails can change hero within same interval
  Source: catalog `goals/T024`; historical status `planned`, priority `P2`.

## 4. Brain Atlas

- [ ] **T025 — Verify existing: Schematic per-angle depth visualization.** (p1) [test] [needs-verification]
  Acceptance: Toggle on/off adjusts dots and preserves region selection
  Source: catalog `goals/T025`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T027 — Upgrade from schematic to independently verified anatomical render assets.** (p1) [feature] [proposed]
  Acceptance: Licensed open 3D dataset with validated region overlays
  Source: catalog `goals/T027`; historical status `planned`, priority `P0`.

- [ ] **T028 — Create striking sculptural main brain centerpiece with dimensional shadows.** (p1) [feature] [proposed]
  Acceptance: More surface detail without implying voxel-accurate geometry
  Source: catalog `goals/T028`; historical status `partial`, priority `P0`.

- [ ] **T029 — Verify existing: Keep existing region dots with exact click targets and view transforms.** (p1) [test] [needs-verification]
  Acceptance: Region selection stable across views/depth
  Source: catalog `goals/T029`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T032 — Additional high-quality lateral/medial/dorsal/ventral view graphics.** (p1) [feature] [proposed]
  Acceptance: Distinct view images registered to projection markers
  Source: catalog `goals/T032`; historical status `partial`, priority `P0`.

- [ ] **T033 — Correct 3D coordinates/volumetric mesh for depth and structures.** (p1) [feature] [proposed]
  Acceptance: Cited anatomical source, verified geometry, no approximated depth claims
  Source: catalog `goals/T033`; historical status `planned`, priority `P0`.

- [ ] **T038 — Show evolutionary dates with scientific uncertainty.** (p1) [feature] [proposed]
  Acceptance: No fabricated age for unique brain region
  Source: catalog `goals/T038`; historical status `partial`, priority `P0`.

- [ ] **T039 — Verify marker alignment and selection at every angle.** (p1) [feature] [proposed]
  Acceptance: All angles and mobile layouts tested
  Source: catalog `goals/T039`; historical status `planned`, priority `P0`.

- [ ] **I003 — Schematic depth is not calibrated 3D.** (p1) [bug] [triage]
  Scope: Depth cue estimates are illustrative; no registered anatomical coordinate model.
  Acceptance: Retain schematic labeling or adopt verified registered model with provenance.
  Source: catalog `issues/I003`; historical status `open`, priority `P0`.

- [ ] **S003 — Improve brain centerpiece and selected-region emphasis.** (p1) [feature] [proposed]
  Scope: Keep schematic projection but refine shading, layering and selected-region focus.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S003`; historical status `proposed`, priority `P0`.

- [ ] **T026 — Verify existing: Low / medium / high depth strength.** (p1) [test] [needs-verification]
  Acceptance: Visible strength difference for same view
  Source: catalog `goals/T026`; historical status `implemented`, priority `P1`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T030 — Bright selected region outlines and location annotation.** (p1) [feature] [proposed]
  Acceptance: Selection spotlight accurate and unclipped
  Source: catalog `goals/T030`; historical status `partial`, priority `P1`.

- [ ] **T031 — Near-to-far opacity, size and subtle desaturation cues.** (p1) [feature] [proposed]
  Acceptance: Cues perceptible, accessible, selected item crisp
  Source: catalog `goals/T031`; historical status `partial`, priority `P1`.

- [ ] **T034 — Show large selected-region name with functional/evolution tags.** (p1) [feature] [proposed]
  Acceptance: Readable selected region summary tied to live region
  Source: catalog `goals/T034`; historical status `partial`, priority `P1`.

- [ ] **T035 — Tabs for evolutionary history / function & circuits / clinical relevance.** (p1) [feature] [proposed]
  Acceptance: Each tab displays sourced, relevant content
  Source: catalog `goals/T035`; historical status `partial`, priority `P1`.

- [ ] **T037 — Current view inset with selected structure accurately indicated.** (p1) [feature] [proposed]
  Acceptance: Inset updates with angle and selection
  Source: catalog `goals/T037`; historical status `partial`, priority `P1`.

- [ ] **S004 — Persistent selected-region facts panel.** (p1) [feature] [proposed]
  Scope: Show function, evolution, clinical implications and transmitters using existing detail records.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S004`; historical status `proposed`, priority `P1`.

- [ ] **S020 — Add a coordinate-provenance route for future true depth.** (p1) [feature] [proposed]
  Scope: Keep existing estimated-depth mode, but prepare a separate registered model path for anatomical 3D coordinates and view-specific overlays.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S020`; historical status `proposed`, priority `P1`.

- [ ] **T036 — Region-specific neurotransmitters and mechanisms.** (p2) [feature] [proposed]
  Acceptance: No generic transmitter lists presented as locality proof
  Source: catalog `goals/T036`; historical status `partial`, priority `P2`.

## 5. Mythology Atlas

- [ ] **T040 — Verify existing: Provide local illustration for all 363 indexed records.** (p1) [test] [needs-verification]
  Acceptance: 363/363 available offline
  Source: catalog `goals/T040`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T041 — Cinematic selected-figure hero art with readable left-aligned text.** (p1) [feature] [proposed]
  Acceptance: Image/text safe area consistent across traditions
  Source: catalog `goals/T041`; historical status `partial`, priority `P0`.

- [ ] **T042 — Commission/generate distinctive iconography for 33 flagship figures.** (p1) [feature] [proposed]
  Acceptance: 33/33 reviewed and approved by tradition
  Source: catalog `goals/T042`; historical status `planned`, priority `P0`.

- [ ] **T043 — Verify existing: Preserve switchable family tree and artwork views.** (p1) [test] [needs-verification]
  Acceptance: Selection persists across switches
  Source: catalog `goals/T043`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T044 — Verify existing: Keep tradition filters, search, genealogy, parent and child navigation.** (p1) [test] [needs-verification]
  Acceptance: No losses after art loading
  Source: catalog `goals/T044`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T048 — Verify existing: Greek/Roman name toggles with independent traditions.** (p1) [test] [needs-verification]
  Acceptance: No conflation of genealogy
  Source: catalog `goals/T048`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T049 — Artwork type and historical accuracy provenance visible.** (p1) [feature] [proposed]
  Acceptance: Labels AI illustrative vs public domain historical vs licensed
  Source: catalog `goals/T049`; historical status `partial`, priority `P0`.

- [ ] **T050 — Verify existing: Keep shared teal/green active states while letting paintings vary by tradition.** (p1) [test] [needs-verification]
  Acceptance: No gold on shared selected widgets
  Source: catalog `goals/T050`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **S005 — Cinematic profile and richer right-side relationships.** (p1) [feature] [proposed]
  Scope: Emphasize artwork with readable overlays; preserve original genealogy.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S005`; historical status `proposed`, priority `P0`.

- [ ] **T045 — Verify existing: Figure result thumbnails with selected treatment.** (p1) [test] [needs-verification]
  Acceptance: Works across all five traditions
  Source: catalog `goals/T045`; historical status `implemented`, priority `P1`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T046 — Rich illustrated right-side figure facts, attribution and relations.** (p1) [feature] [proposed]
  Acceptance: Truthful family edges, role, references, provenance
  Source: catalog `goals/T046`; historical status `partial`, priority `P1`.

- [ ] **T047 — Clickable related-artwork thumbnails/carousel.** (p1) [feature] [proposed]
  Acceptance: Navigate images, display license/source and attribution
  Source: catalog `goals/T047`; historical status `partial`, priority `P1`.

- [ ] **T051 — Matching pills for lineage, epics, symbols and role.** (p1) [feature] [proposed]
  Acceptance: Clicking chip filters/searches or opens related info
  Source: catalog `goals/T051`; historical status `partial`, priority `P1`.

- [ ] **I004 — More tradition-specific hero portraits.** (p1) [bug] [triage]
  Scope: 363 entries have art coverage, but most are symbolic.
  Acceptance: Featured hero/thumbnail set reviewed by subject and tradition.
  Source: catalog `issues/I004`; historical status `open`, priority `P1`.

- [ ] **I005 — Separate related figures from linked historical artwork.** (p1) [bug] [triage]
  Scope: Related-figure navigation exists; licensed artwork carousel is a separate unbuilt workflow.
  Acceptance: Display source, attribution, license and related art separately.
  Source: catalog `issues/I005`; historical status `open`, priority `P1`.

- [ ] **S006 — Licensed related-artwork gallery.** (p1) [feature] [proposed]
  Scope: Separate actual historical artwork with credits, external links and rights metadata from generated portraits.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S006`; historical status `proposed`, priority `P1`.

- [ ] **S021 — Separate generated narrative portraits from documented historical artwork.** (p1) [feature] [proposed]
  Scope: Add figure-level Source artwork tab with credit, object date, museum/license and external records rather than implying modern art is ancient.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S021`; historical status `proposed`, priority `P1`.

- [ ] **T052 — Improve person/entity equivalents, variant myths and sources.** (p2) [feature] [proposed]
  Acceptance: Reference-specific relationships; no invented parentage
  Source: catalog `goals/T052`; historical status `partial`, priority `P2`.

## 6. Tree of Life Atlas

- [ ] **T066 — Preserve existing dataset and interactions while upgrading visual shell.** (p1) [feature] [proposed]
  Acceptance: No regression in current controls
  Source: catalog `goals/T066`; historical status `planned`, priority `P0`.

- [ ] **S014 — Add an evidence-backed selected-clade focus panel.** (p1) [feature] [proposed]
  Scope: Retain the existing hierarchy, but show curated organism visual, dated lineage summary and source link next to the active selection.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S014`; historical status `proposed`, priority `P1`.

- [ ] **T065 — Translate common illustrated-header and story-card language to this widget.** (p2) [feature] [proposed]
  Acceptance: Keep widget-specific visualization and data
  Source: catalog `goals/T065`; historical status `planned`, priority `P2`.

- [ ] **T067 — Capture new goal reference and actual screenshot at same viewport.** (p2) [feature] [proposed]
  Acceptance: Source goal concept approved before release
  Source: catalog `goals/T067`; historical status `planned`, priority `P2`.

- [ ] **I009 — Extend illustrated atlas styling beyond first three.** (p2) [bug] [triage]
  Scope: Tree of Life has shared headers; main-stage visual richness remains behind the concept direction.
  Acceptance: Approved subject-appropriate reference composition and screenshot comparison.
  Source: catalog `issues/I009`; historical status `open`, priority `P2`.

- [ ] **I017 — Reduced-motion support is inconsistent with the rest of the atlas family.** (p2) [bug] [triage]
  Scope: Tree of Life includes CSS transitions but no prefers-reduced-motion override, unlike the other six current HTML files. Animation impact is likely modest, but shared accessibility behavior is inconsistent.
  Acceptance: Add a shared prefers-reduced-motion media rule and keyboard/focus regression checks while retaining intended static transitions.
  Source: catalog `issues/I017`; historical status `open`, priority `P2`.

- [ ] **S007 — Illustrated clade/organism focus stage.** (p2) [feature] [proposed]
  Scope: Preserve taxonomy hierarchy and show sourced organism imagery for selected taxa.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S007`; historical status `proposed`, priority `P2`.

## 7. Muscle Atlas

- [ ] **T069 — Preserve existing dataset and interactions while upgrading visual shell.** (p1) [feature] [proposed]
  Acceptance: No regression in current controls
  Source: catalog `goals/T069`; historical status `planned`, priority `P0`.

- [ ] **S015 — Clear selected muscle anatomy and exercise context.** (p1) [feature] [proposed]
  Scope: Keep muscle labels/navigation but provide a consistent selected-muscle highlight and a compact exercise-role card, with actual exercise data only.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S015`; historical status `proposed`, priority `P1`.

- [ ] **T068 — Translate common illustrated-header and story-card language to this widget.** (p2) [feature] [proposed]
  Acceptance: Keep widget-specific visualization and data
  Source: catalog `goals/T068`; historical status `planned`, priority `P2`.

- [ ] **T070 — Capture new goal reference and actual screenshot at same viewport.** (p2) [feature] [proposed]
  Acceptance: Source goal concept approved before release
  Source: catalog `goals/T070`; historical status `planned`, priority `P2`.

- [ ] **I010 — Improve anatomy-stage clarity and visual depth.** (p2) [bug] [triage]
  Scope: Keep muscle map and exercises functional while upgrading selected muscle focus.
  Acceptance: Enhanced visual with exercise mapping preserved.
  Source: catalog `issues/I010`; historical status `open`, priority `P2`.

- [ ] **S008 — Muscle region render and compact exercise panel.** (p2) [feature] [proposed]
  Scope: Enhance muscle illustration with primary/secondary exercise attribution.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S008`; historical status `proposed`, priority `P2`.

## 8. Emergence Atlas

- [ ] **T072 — Preserve existing dataset and interactions while upgrading visual shell.** (p1) [feature] [proposed]
  Acceptance: No regression in current controls
  Source: catalog `goals/T072`; historical status `planned`, priority `P0`.

- [ ] **S016 — Add evidence-and-scale comparison for the active emergence level.** (p1) [feature] [proposed]
  Scope: Use the existing level model to link its components, interactions, scale ranges and uncertainties in a compact network-evidence view.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S016`; historical status `proposed`, priority `P1`.

- [ ] **T071 — Translate common illustrated-header and story-card language to this widget.** (p2) [feature] [proposed]
  Acceptance: Keep widget-specific visualization and data
  Source: catalog `goals/T071`; historical status `planned`, priority `P2`.

- [ ] **T073 — Capture new goal reference and actual screenshot at same viewport.** (p2) [feature] [proposed]
  Acceptance: Source goal concept approved before release
  Source: catalog `goals/T073`; historical status `planned`, priority `P2`.

- [ ] **I011 — Improve interactive level diagrams and evidence panels.** (p2) [bug] [triage]
  Scope: Broaden visual clarity without implying unsupported quantitative certainty.
  Acceptance: Each active level shows a tested relation/evidence panel.
  Source: catalog `issues/I011`; historical status `open`, priority `P2`.

- [ ] **S009 — Interactive emergence-layer network comparison.** (p2) [feature] [proposed]
  Scope: Show comparative scales and explanatory caveats by selected level.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S009`; historical status `proposed`, priority `P2`.

## 9. Widget Launcher

- [ ] **T075 — Support optional external asset manifests and local artwork bundles.** (p1) [feature] [proposed]
  Acceptance: File selection includes dependent image directories or standalone mode
  Source: catalog `goals/T075`; historical status `planned`, priority `P0`.

- [ ] **T076 — Verify existing: Retain Shared Taxa as nonlaunchable versioned resource.** (p1) [test] [needs-verification]
  Acceptance: Import records hashes and current dependency compatibility
  Source: catalog `goals/T076`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T077 — Regression-test folder sync / imported artwork / IndexedDB in Windows.** (p1) [feature] [proposed]
  Acceptance: Successful refresh and persistence after restart
  Source: catalog `goals/T077`; historical status `planned`, priority `P0`.

- [ ] **I006 — Test folder sync and persistence on Windows.** (p1) [bug] [triage]
  Scope: File System Access, IndexedDB, and local persistent settings need actual Windows Edge/Chrome tests.
  Acceptance: Successful re-open with synced HTML, dataset, and local artwork.
  Source: catalog `issues/I006`; historical status `open`, priority `P0`.

- [ ] **S013 — Preflight bundled-artwork compatibility before syncing.** (p1) [feature] [proposed]
  Scope: Detect whether imported HTML contains local asset references and confirm a self-contained build or all adjacent files exist before marking ready.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S013`; historical status `proposed`, priority `P0`.

- [ ] **T074 — Extend illustrated card gradients and status panel polish.** (p1) [feature] [proposed]
  Acceptance: Same common design without hypothetical metrics
  Source: catalog `goals/T074`; historical status `partial`, priority `P1`.

- [ ] **I015 — Launcher HTML import does not transport external artwork directories.** (p1) [bug] [triage]
  Scope: The direct HTML picker accepts HTML and importFiles classifies selected filenames; external artwork assets are not included with a single imported HTML document. Standalone and bundle editions require different handling.
  Acceptance: Provide import-mode detection and a readiness warning; recommend standalone HTML for launcher imports or implement a verified asset-bundle copying flow.
  Source: catalog `issues/I015`; historical status `open`, priority `P1`.
  Triage note: v1.21 notes document a newer folder importer in Launcher v1.14; reproduce the remaining defect before editing.

- [ ] **S010 — Dependency and readiness visualization.** (p1) [feature] [proposed]
  Scope: Use real sync, linked files and dataset import status; never hard-code mockup 248MB counts.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S010`; historical status `proposed`, priority `P1`.

- [ ] **S025 — Show authoritative package and asset health per widget.** (p1) [feature] [proposed]
  Scope: On each launcher card, display actual linked HTML version, dataset dependency, image bundle type, last validation and sync errors.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S025`; historical status `proposed`, priority `P1`.

## 10. Shared Taxa and science

- [ ] **T078 — Verify existing: Preserve Shared Taxa v1.0 authoritative dataset unaffected by artwork.** (p1) [test] [needs-verification]
  Acceptance: No scientific data mutations for UI/art updates
  Source: catalog `goals/T078`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T079 — Link selected taxon from Deep Time representative life view.** (p1) [feature] [proposed]
  Acceptance: Use canonical concept IDs and traceable scientific source
  Source: catalog `goals/T079`; historical status `planned`, priority `P1`.

- [ ] **I007 — Review 57 documented scientific ambiguities.** (p1) [bug] [triage]
  Scope: Immutable v1.0 dataset published with scientific warnings; changes require a new dataset release.
  Acceptance: Ambiguities resolved or explicitly carried into next version with sources.
  Source: catalog `issues/I007`; historical status `open`, priority `P1`.

- [ ] **S017 — Explain 172 vs 173 interval scope through a mapping view.** (p1) [feature] [proposed]
  Scope: Show canonical Shared Taxa interval coverage beside Deep Time UI interval IDs and explain intentionally nonmatching scope.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S017`; historical status `proposed`, priority `P1`.

- [ ] **I022 — Canonical interval and Deep Time interval totals are not explicitly distinguished in dashboard metrics.** (p2) [bug] [triage]
  Scope: Shared Taxa identifies 173 canonical intervals while Deep Time currently indexes 172 HTML intervals. Both counts are valid for different scopes, but the interface can appear contradictory.
  Acceptance: Label counts as 173 canonical Shared Taxa intervals versus 172 Deep Time indexed intervals and link to the mapping/coverage explanation.
  Source: catalog `issues/I022`; historical status `open`, priority `P2`.

## 11. Artwork Studio and promotion

- [ ] **T053 — Verify existing: Search, inspect and filter all 538 image records.** (p1) [test] [needs-verification]
  Acceptance: 172 + 363 + 3 records
  Source: catalog `goals/T053`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T054 — Verify existing: Add review status/notes and export decisions JSON.** (p1) [test] [needs-verification]
  Acceptance: Export valid JSON; updates persist where supported
  Source: catalog `goals/T054`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T055 — View actual image beside matching goal crop.** (p1) [feature] [proposed]
  Acceptance: Reference/current/assets side-by-side
  Source: catalog `goals/T055`; historical status `planned`, priority `P0`.

- [ ] **T056 — Separate featured / standard / fallback / needs replacement.** (p1) [feature] [proposed]
  Acceptance: All records tagged and filtering consistent
  Source: catalog `goals/T056`; historical status `partial`, priority `P0`.

- [ ] **T057 — Generate prompt for selected asset from scientific notes.** (p1) [feature] [proposed]
  Acceptance: Prompt links to exact manifest ID
  Source: catalog `goals/T057`; historical status `planned`, priority `P0`.

- [ ] **T058 — Copy prompt or export multiple prompts in Markdown/JSON.** (p1) [feature] [proposed]
  Acceptance: Download ready; no API credentials required
  Source: catalog `goals/T058`; historical status `planned`, priority `P0`.

- [ ] **T059 — Import approved replacement images via user-selected file and validate dimensions.** (p1) [feature] [proposed]
  Acceptance: No silent overwrite; confirmed license and subject
  Source: catalog `goals/T059`; historical status `planned`, priority `P0`.

- [ ] **T060 — Record rights, attribution, source URLs, date and source quality.** (p1) [feature] [proposed]
  Acceptance: Clear license/reuse rights and citation fields
  Source: catalog `goals/T060`; historical status `planned`, priority `P0`.

- [ ] **T063 — Persist status changes and import/export decisions across sessions.** (p1) [feature] [proposed]
  Acceptance: Win/Edge test + export/import backup
  Source: catalog `goals/T063`; historical status `partial`, priority `P0`.

- [ ] **S011 — One-click art-promotion staging with provenance.** (p1) [feature] [proposed]
  Scope: Review → license check → manifest diff → build; artwork not promoted just from a status change.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S011`; historical status `proposed`, priority `P0`.

- [ ] **S018 — Use a gated artwork promotion and manifest-diff wizard.** (p1) [feature] [proposed]
  Scope: After human approval, show license provenance, checksum, affected thumbnails and exact standalone/bundle rebuild list before promotion.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S018`; historical status `proposed`, priority `P0`.

- [ ] **T061 — Show fallback/inherited-image chain.** (p1) [feature] [proposed]
  Acceptance: Direct vs inherited transparent
  Source: catalog `goals/T061`; historical status `planned`, priority `P1`.

- [ ] **T062 — Improve preview quality, card density, comparison composition.** (p1) [feature] [proposed]
  Acceptance: Readable cards desktop/mobile
  Source: catalog `goals/T062`; historical status `partial`, priority `P1`.

- [ ] **T064 — Batch status and next-up recommendations.** (p1) [feature] [proposed]
  Acceptance: Queue sortable by tier, source, priority and review status
  Source: catalog `goals/T064`; historical status `planned`, priority `P1`.

- [ ] **I008 — Connect artwork review approvals to release rebuilds.** (p1) [bug] [triage]
  Scope: Review records do not automatically update production manifests or HTML.
  Acceptance: Build manifest diff and checksum reconciliation before release.
  Source: catalog `issues/I008`; historical status `open`, priority `P1`.

- [ ] **I019 — Review decisions are not integrated with release manifests and binaries.** (p1) [bug] [triage]
  Scope: The dashboard updates its internal art-review status but does not change asset manifest SHA-256, provenance, local image files or standalone HTML artwork. The existing release pipeline remains manual.
  Acceptance: Build a guarded staging queue with source/license check, checksum generation, manifest diff and standalone/bundle parity tests before promotion.
  Source: catalog `issues/I019`; historical status `open`, priority `P1`.

- [ ] **I024 — Artwork source rights and final approval can be represented only as free-form state.** (p1) [bug] [triage]
  Scope: Production artwork manifests have disclosure/review fields, but the integrated dashboard can mark assessment “approved” without a structured source URL, license, or scientist/cultural reviewer; release gating is not enforced.
  Acceptance: Require provenance, license/permission, subject-review identity and timestamp before allowing approved-for-release status.
  Source: catalog `issues/I024`; historical status `open`, priority `P1`.

## 12. Master Dashboard

- [ ] **I013 — Verify existing: Artwork approval can bypass on-screen safeguards via imported JSON.** (p1) [test] [needs-verification]
  Scope: The review checkbox rejects a draft, but importState() copies approved:true into state.subject without checking phase, image quality or provenance. A prepared JSON can therefore mark an unreviewed collage crop approved.
  Acceptance: Use a single guarded approveSubject() pathway for form changes, imports and saved-HTML restoration; reject approval unless full-resolution asset, rights, and human review are recorded.
  Source: catalog `issues/I013`; historical status `done`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **I014 — Verify existing: Previously approved artwork can be moved back to draft without clearing approval.** (p1) [test] [needs-verification]
  Scope: The phase select is editable independently, and the draft guard runs only when the approved checkbox is changed to true. Switching an approved review to draft can leave a contradictory approved:true state.
  Acceptance: Validate both phase and approved together on every mutation; migrate contradictory saved states and show an audit warning.
  Source: catalog `issues/I014`; historical status `done`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **S012 — One unified audit-to-release triage panel.** (p1) [feature] [proposed]
  Scope: Turn scan findings into linked issue, acceptance check, proposed improvement and test evidence, not disconnected status cards.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S012`; historical status `proposed`, priority `P0`.

- [ ] **S023 — One-click release verification report.** (p1) [feature] [proposed]
  Scope: Generate a read-only local audit of linked files, asset hashes, application syntax, version buttons, comparison coverage and data dependencies.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S023`; historical status `proposed`, priority `P0`.

- [ ] **I016 — Nested full-content ZIP duplicates a large fraction of the distribution.** (p1) [bug] [triage]
  Scope: The dashboard folder includes downloads/Atlas_Widgets_Full_Content_v1.18.zip (~31.9 MB), which is itself stored inside the ~63.7 MB top-level package. This increases download/archive size and complicates identifying the canonical package.
  Acceptance: Choose a single canonical full release artifact; for the in-dashboard download, generate a nonrecursive export or document the nested bundle purpose and verify both.
  Source: catalog `issues/I016`; historical status `open`, priority `P1`.

- [ ] **I018 — Verify existing: Suggestion-to-issue action copies text but does not create a linked backlog item.** (p1) [test] [needs-verification]
  Scope: The “Copy proposal as backlog note” control invokes clipboard copy only. Suggestions and issues have no persistent cross-reference or automatic status linkage.
  Acceptance: Add Convert to issue and Related goal / issue IDs, with duplicate detection and traceable acceptance criteria.
  Source: catalog `issues/I018`; historical status `done`, priority `P1`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **I020 — Automated release behavior checks do not yet cover full Windows file sync and storage.** (p1) [bug] [triage]
  Scope: Script and inline browser smoke checks exist, but folder permissions, persisted IndexedDB data, cross-version restart behavior and local file integration have not been verified on Windows.
  Acceptance: Execute a repeatable Windows Edge/Chrome QA matrix and attach a dated pass/fail log for launcher import, offline reopen, and dataset/art persistence.
  Source: catalog `issues/I020`; historical status `open`, priority `P1`.

- [ ] **I021 — Goal comparisons cover only three of six atlas widgets.** (p1) [bug] [triage]
  Scope: The current dashboard includes generated-versus-actual comparisons for Deep Time, Brain, and Mythology. Tree of Life, Muscle, Emergence and launcher have no equivalent approved visual target and before/current side-by-side record.
  Acceptance: Capture comparable actual screenshots for every widget, document subject-specific design criteria and add a mockup approval workflow for the remaining four.
  Source: catalog `issues/I021`; historical status `open`, priority `P1`.

- [ ] **I023 — Checksums validate assets but do not validate scientific or cultural interpretation.** (p1) [bug] [triage]
  Scope: All 538 artwork and 90 Shared Taxa file hashes match package manifests. Hash correctness only proves bytes match; visual accuracy and 57 source ambiguities remain separate review tasks.
  Acceptance: Add evidence-grade review fields and subject expert sign-off distinct from checksum validation; do not use a verified hash as an accuracy badge.
  Source: catalog `issues/I023`; historical status `open`, priority `P1`.

- [ ] **I027 — Verify existing: Full decisions import accepts arbitrary review states without schema validation.** (p1) [test] [needs-verification]
  Scope: The imported master JSON is merged into mutable review/goal/issue state and custom arrays without a schema check for permitted status values, approved flags, reference IDs or contradiction.
  Acceptance: Validate import against a versioned JSON schema; preserve unknown fields in quarantine and preview a diff before applying changes.
  Source: catalog `issues/I027`; historical status `done`, priority `P1`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **S019 — Portable project-state snapshots with previewable diff.** (p1) [feature] [proposed]
  Scope: Offer versioned import validation, review-only changes, audit logs and merge choices before replacing existing approval/checklist states.
  Acceptance: triage this proposal, record the decision and concrete criteria in the relevant spec, then validate with regression checks and actual-versus-goal evidence before completion.
  Source: catalog `suggestions/S019`; historical status `proposed`, priority `P1`.

- [ ] **I025 — Goal, issue and improvement status updates can drift independently.** (p2) [bug] [triage]
  Scope: 84 goals, 12 baseline issues and 11 suggestions are distinct mutable registers with no stable dependency links or automatic acceptance-test closure when related work completes.
  Acceptance: Attach structured related IDs and per-release change evidence; offer a linked issue → proposal → goal detail and closure checklist.
  Source: catalog `issues/I025`; historical status `open`, priority `P2`.

- [ ] **I028 — Path verification cannot establish local file existence automatically under file://.** (p2) [bug] [triage]
  Scope: The UI uses HTTP HEAD when served and a folder picker when local, so links remain Not verified in file:// until a manual directory scan. This is expected browser behavior but can be mistaken for missing assets.
  Acceptance: Make offline mode explicit and add a one-click guided directory-check wizard with separate states for blocked/unverified/missing.
  Source: catalog `issues/I028`; historical status `open`, priority `P2`.

## 13. Goal tracking workspace

- [ ] **T080 — Verify existing: Goal image and actual browser screenshot shown side by side.** (p1) [test] [needs-verification]
  Acceptance: Three atlas comparisons in one offline HTML
  Source: catalog `goals/T080`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T081 — Verify existing: Searchable acceptance-based register with visual/functional axes.** (p1) [test] [needs-verification]
  Acceptance: Filter, edit statuses, export/import decisions
  Source: catalog `goals/T081`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T082 — Verify existing: Batch 1 prompts keyed to real artwork manifest records.** (p1) [test] [needs-verification]
  Acceptance: 13 intervals, 33 figures, 8 brain render requests
  Source: catalog `goals/T082`; historical status `implemented`, priority `P0`.
  Required evidence: rerun the stated acceptance checks; imported completion is not a fresh pass.

- [ ] **T083 — Browser-local changes with portable backup and restore.** (p1) [feature] [proposed]
  Acceptance: Export and import round-trip test in Windows Edge
  Source: catalog `goals/T083`; historical status `partial`, priority `P0`.

- [ ] **T084 — Automate fresh screenshot capture and comparison after each release.** (p1) [feature] [proposed]
  Acceptance: Matching viewport, same selected state, repeatable screenshots
  Source: catalog `goals/T084`; historical status `planned`, priority `P1`.

- [ ] **I012 — Resolve historical checklist summary mismatch.** (p1) [bug] [triage]
  Scope: Previous summary was 28/30/26; row-based count is 27/30/27.
  Acceptance: Counts generated directly from 84 item statuses with no manual override.
  Source: catalog `issues/I012`; historical status `open`, priority `P1`.

