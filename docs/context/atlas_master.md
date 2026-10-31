# Atlas Widgets — curated master context

**Status:** Verified imported source baseline; visual direction approved on 2026-10-30. Future feature proposals remain unapproved.

## Authoritative component versions and files

The delivered Atlas master v1.21 catalog and actual HTML titles agree on these versions:

| Component | Imported version | Source |
|---|---|---|
| Brain | 1.21 | `atlas/widgets/Brain_Atlas_v1.21.html` |
| Deep Time | 1.18 | `atlas/widgets/Deep_Time_Atlas_v1.18.html` |
| Tree of Life | 1.14 | `atlas/widgets/Tree_of_Life_Atlas_v1.14.html` |
| Mythology | 1.13 | `atlas/widgets/Mythology_Atlas_v1.13.html` |
| Muscles | 1.8 | `atlas/widgets/Muscle_Atlas_v1.8.html` |
| Emergence | 1.10 | `atlas/widgets/Emergence_Atlas_v1.10.html` |
| Launcher | 1.14 | `atlas/widgets/Widget_Launcher_v1.14.html` |

All six scientific widgets match the delivered v1.20 source checksums. Launcher v1.14 is documented by the actual HTML, v1.21 catalog, and release notes. The SHA inventory records imported bytes. This verifies source identity, not scientific claims, publication history outside the package, or interactive browser behavior. No new release was created during that migration step.

## Approved UI, scientific, and data requirements

The user prioritized Atlas and selected `atlas/images/goal_1.png` and `goal_2.png` as direction. See `atlas/specs/visual-direction.md` revision 4 for the approved design language and regression constraints. Preserve scientific content, stable identifiers, historical changelogs, and browser progress formats. Repository setup and relevant context curation were explicitly authorized; raw account exports and transcripts stay private.

The images favor dark navy, cyan/mint accents, compact headers, illustrated selected-subject stages, and adjacent navigation/detail panels. Their versions and numerical badges are examples. The more compact second composition is useful for subsequent layout work without removing existing scientific panels.

## Design alternatives and existing limitations

Source manifests distinguish 172 Deep Time entries, 363 Mythology figures, 3 Brain schematic views, and 5 featured concepts. Most existing art is procedural, symbolic, or schematic. The imported development spec documents two featured Mesozoic scene crops and one Zeus concept; a complete bespoke art library has not been delivered.

Brain imagery uses authored projections and estimated depth, not registered volumetric anatomy. Keep this distinction visible. The source manifest says registered 3D geometry is unavailable.

Five artwork calibration subjects remain draft/review, with no final approval: Hadean Earth, Archean microbial coast, Jurassic river basin, Greek Zeus, and Greek Athena. Do not convert a preferred picture or successful checksum into scientific/artwork approval.

## Dependencies on Shared Taxa

Canonical Shared Taxa v1.0 is now complete at `shared/taxa/`; the delivered Atlas copy is preserved for its existing relative links. It has 368 canonical taxa, 173 canonical intervals, 580 curated associations, and 57 documented ambiguities. Deep Time indexes 172 UI intervals, a separate scope. Preserve the curated/inferred link distinction, source-specific ages, and crosswalks. Existing widget embedded datasets remain untouched; do not infer a completed runtime migration from a dependency label.

## Outstanding issues

Current checks cover imported bytes, source identity, JSON schemas, JavaScript syntax, and the defined Chrome/Linux browser matrix at 390/768/1440px. Wider interaction/accessibility coverage, Windows folder import, IndexedDB persistence, and offline launch/export still need testing. Historical audits and suggestions remain evidence/backlog, not blanket implementation authorization.

Distribution download ZIPs were intentionally not copied; the original dashboard still describes them. Maintain the source package until a deliberate packaging change reconciles its download actions. Dataset duplication is a compatibility measure for this initial migration.

## Provenance

Primary evidence: delivered `atlas/README.md`, `atlas/docs/CHANGELOG_Master_Dashboard_v1.21.md`, `atlas/docs/QA_v1.21.md`, `atlas/docs/MASTER_DEVELOPMENT_SPEC_v1.9.md`, catalogs, actual HTML, and asset manifests. Historical QA claims are attributed to those documents and were not treated as current test results.

A limited relevant Brain Atlas project extract (October 14–16, 2026) corroborates older hierarchy, timeline, and shared-header discussions; its older release claims do not supersede imported sources. No transcript text was imported. The remaining project extracts remain private and were not comprehensively curated in this pass.

## Live backlog and ongoing evidence

As of 2026-10-30, root TODO.md is the live task register, retaining all 84 historical goals, 28 issues, and 25 suggestions. The immutable catalog remains provenance. Imported implemented/done claims become verification tasks; new suggestions remain proposed. User authorizes routinely committing/tagging/pushing finished validated batches using repository SemVer, separate from original component version labels.

Every Atlas update must produce fresh actual-versus-goal PNGs with completed/pending sidebars and open them automatically in feh. Initial real-browser captures for all seven components are in `docs/visual-reviews/0.1.0/`; Triassic, OFC, and Zeus selections were exercised for the primary widgets. These are render/selection smoke checks, not comprehensive interaction or scientific QA. Other four concept targets remain explicitly proposed.

## Regression verification — repository 0.1.1

WL-005, T018, T022, and WL-010 are complete with [45 passing scenario checks](../browser-tests/0.1.1/README.md). The suite uses real mouse/key input, verifies selected title/artwork/breadcrumb changes and five distinct topic tabs, and guards against empty or stale source reports. Spec revisions for the primary three widgets and shared direction are now 3. Actual original widget/data bytes and versions remain unchanged.

T021 remains open: the UI card/profile interaction passes, but canonical Shared Taxa identity/provenance is not established by opening the original embedded taxon profile. No scientific correctness or data migration is inferred from UI tests. The larger WL-006 visual refinement can begin next against this baseline. Fresh primary-widget comparisons in `docs/visual-reviews/0.1.1/` reflect the updated completed/pending task list.

## Deep Time visual update — repository 0.2.0

Current Deep Time source is `atlas/widgets/Deep_Time_Atlas_v1.19.0.html`; imported 1.18 remains unchanged. The new standalone adds a compact topic/search header, interval scene refinement, larger preview cards with actual age labels and current state, and responsive/reduced-motion styling. Its original source is preserved verbatim except document title plus appended presentation CSS/JS. No scientific payloads, IDs, classifications, dates, or original event/control handlers changed.

Use `atlas/current.html` for current registered builds. Imported dashboards/catalogs remain historical. Editable Deep Time presentation is under `atlas/widgets/deep-time/src/`; deterministic builders and preservation tests guard the generated file. All prior release entries are retained, with 1.19.0 added ahead of them.

WL-006 remains in progress for later widget/layout/artwork work. Procedural Triassic imagery remains procedural; no cinematic reconstruction or canonical taxon migration is claimed. Browser tooling now requests graceful Chrome shutdown after a profile cleanup race found during QA; bounded termination fallbacks remain for stuck processes.
