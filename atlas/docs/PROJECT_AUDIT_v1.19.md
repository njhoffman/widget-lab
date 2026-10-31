# Atlas Widgets — Project Audit v1.19

**Scanned:** October 17, 2026  
**Baseline:** Master Dashboard v1.18, all seven packaged HTML widget builds, artwork manifests, and Shared Taxa v1.0.  
**Scope:** static integrity, browser smoke rendering, data-review and release-workflow checks; not a claim of full functional testing.

## Verified baseline

- 7 widget HTML + dashboard script syntax passed
- 538/538 artwork checksums match
- 90/90 Shared Taxa package files match checksums
- 0 broken static dashboard hyperlinks
- 7/7 widget smoke-rendered without page errors

Shared Taxa published v1.0 remains unchanged; 57 documented ambiguities require separate scientific review. A passing checksum is not a correctness verdict. The historical 173 canonical intervals and Deep Time's 172 UI indices represent different scopes.

## Newly recorded issues

### I013 · Artwork approval can bypass on-screen safeguards via imported JSON (P0, Confirmed)

- **Component:** Master Dashboard / Data integrity
- **Finding:** The review checkbox rejects a draft, but importState() copies approved:true into state.subject without checking phase, image quality or provenance. A prepared JSON can therefore mark an unreviewed collage crop approved.
- **Evidence:** `MASTER_DASHBOARD_v1.18.html :: importState() versus change handler approval check`
- **Acceptance:** Use a single guarded approveSubject() pathway for form changes, imports and saved-HTML restoration; reject approval unless full-resolution asset, rights, and human review are recorded.

### I014 · Previously approved artwork can be moved back to draft without clearing approval (P0, Confirmed)

- **Component:** Master Dashboard / Data integrity
- **Finding:** The phase select is editable independently, and the draft guard runs only when the approved checkbox is changed to true. Switching an approved review to draft can leave a contradictory approved:true state.
- **Evidence:** `MASTER_DASHBOARD_v1.18.html :: setField(), change handler subject phase`
- **Acceptance:** Validate both phase and approved together on every mutation; migrate contradictory saved states and show an audit warning.

### I015 · Launcher HTML import does not transport external artwork directories (P1, Confirmed)

- **Component:** Widget Launcher / Compatibility
- **Finding:** The direct HTML picker accepts HTML and importFiles classifies selected filenames; external artwork assets are not included with a single imported HTML document. Standalone and bundle editions require different handling.
- **Evidence:** `widgets/Widget_Launcher_v1.12.html :: file-input accept=.html, importFiles(); README launcher-ready guidance`
- **Acceptance:** Provide import-mode detection and a readiness warning; recommend standalone HTML for launcher imports or implement a verified asset-bundle copying flow.

### I016 · Nested full-content ZIP duplicates a large fraction of the distribution (P1, Confirmed)

- **Component:** Master Dashboard / Packaging
- **Finding:** The dashboard folder includes downloads/Atlas_Widgets_Full_Content_v1.18.zip (~31.9 MB), which is itself stored inside the ~63.7 MB top-level package. This increases download/archive size and complicates identifying the canonical package.
- **Evidence:** `downloads/Atlas_Widgets_Full_Content_v1.18.zip and parent release ZIP`
- **Acceptance:** Choose a single canonical full release artifact; for the in-dashboard download, generate a nonrecursive export or document the nested bundle purpose and verify both.

### I017 · Reduced-motion support is inconsistent with the rest of the atlas family (P2, Confirmed)

- **Component:** Tree of Life Atlas / Accessibility
- **Finding:** Tree of Life includes CSS transitions but no prefers-reduced-motion override, unlike the other six current HTML files. Animation impact is likely modest, but shared accessibility behavior is inconsistent.
- **Evidence:** `widgets/Tree_of_Life_Atlas_v1.14.html :: two transition rules, zero prefers-reduced-motion clauses`
- **Acceptance:** Add a shared prefers-reduced-motion media rule and keyboard/focus regression checks while retaining intended static transitions.

### I018 · Suggestion-to-issue action copies text but does not create a linked backlog item (P1, Confirmed)

- **Component:** Master Dashboard / Workflow
- **Finding:** The “Copy proposal as backlog note” control invokes clipboard copy only. Suggestions and issues have no persistent cross-reference or automatic status linkage.
- **Evidence:** `MASTER_DASHBOARD_v1.18.html :: suggestionNote() and suggestionToIssue`
- **Acceptance:** Add Convert to issue and Related goal / issue IDs, with duplicate detection and traceable acceptance criteria.

### I019 · Review decisions are not integrated with release manifests and binaries (P1, Confirmed)

- **Component:** Artwork Studio / Workflow
- **Finding:** The dashboard updates its internal art-review status but does not change asset manifest SHA-256, provenance, local image files or standalone HTML artwork. The existing release pipeline remains manual.
- **Evidence:** `MASTER_DASHBOARD_v1.18.html :: setField() and exports; README artwork workflow`
- **Acceptance:** Build a guarded staging queue with source/license check, checksum generation, manifest diff and standalone/bundle parity tests before promotion.

### I020 · Automated release behavior checks do not yet cover full Windows file sync and storage (P1, Needs testing)

- **Component:** Master Dashboard / QA coverage
- **Finding:** Script and inline browser smoke checks exist, but folder permissions, persisted IndexedDB data, cross-version restart behavior and local file integration have not been verified on Windows.
- **Evidence:** `README.md :: Review limitations; Widget Launcher v1.12 source`
- **Acceptance:** Execute a repeatable Windows Edge/Chrome QA matrix and attach a dated pass/fail log for launcher import, offline reopen, and dataset/art persistence.

### I021 · Goal comparisons cover only three of six atlas widgets (P1, Confirmed)

- **Component:** Master Dashboard / Evidence
- **Finding:** The current dashboard includes generated-versus-actual comparisons for Deep Time, Brain, and Mythology. Tree of Life, Muscle, Emergence and launcher have no equivalent approved visual target and before/current side-by-side record.
- **Evidence:** `data/project_catalog_v1.18.json :: comparisonEmbeds keys deep/brain/myth; qa screenshots`
- **Acceptance:** Capture comparable actual screenshots for every widget, document subject-specific design criteria and add a mockup approval workflow for the remaining four.

### I022 · Canonical interval and Deep Time interval totals are not explicitly distinguished in dashboard metrics (P2, Confirmed)

- **Component:** Shared Taxa / Terminology
- **Finding:** Shared Taxa identifies 173 canonical intervals while Deep Time currently indexes 172 HTML intervals. Both counts are valid for different scopes, but the interface can appear contradictory.
- **Evidence:** `data/Shared_Taxa_v1.0/manifest.json; assets/deep_time/manifest.json`
- **Acceptance:** Label counts as 173 canonical Shared Taxa intervals versus 172 Deep Time indexed intervals and link to the mapping/coverage explanation.

### I023 · Checksums validate assets but do not validate scientific or cultural interpretation (P1, Needs testing)

- **Component:** Master Dashboard / QA coverage
- **Finding:** All 538 artwork and 90 Shared Taxa file hashes match package manifests. Hash correctness only proves bytes match; visual accuracy and 57 source ambiguities remain separate review tasks.
- **Evidence:** `assets/*/manifest.json review_status; data/Shared_Taxa_v1.0/VALIDATION_REPORT.json`
- **Acceptance:** Add evidence-grade review fields and subject expert sign-off distinct from checksum validation; do not use a verified hash as an accuracy badge.

### I024 · Artwork source rights and final approval can be represented only as free-form state (P1, Confirmed)

- **Component:** Artwork Studio / Review safety
- **Finding:** Production artwork manifests have disclosure/review fields, but the integrated dashboard can mark assessment “approved” without a structured source URL, license, or scientist/cultural reviewer; release gating is not enforced.
- **Evidence:** `MASTER_DASHBOARD_v1.18.html :: renderArtEditor()/setField(); assets manifests`
- **Acceptance:** Require provenance, license/permission, subject-review identity and timestamp before allowing approved-for-release status.

### I025 · Goal, issue and improvement status updates can drift independently (P2, Confirmed)

- **Component:** Master Dashboard / Workflow
- **Finding:** 84 goals, 12 baseline issues and 11 suggestions are distinct mutable registers with no stable dependency links or automatic acceptance-test closure when related work completes.
- **Evidence:** `MASTER_DASHBOARD_v1.18.html :: separate CATALOG.goals/issues/suggestions and record()`
- **Acceptance:** Attach structured related IDs and per-release change evidence; offer a linked issue → proposal → goal detail and closure checklist.

### I026 · Keyboard, contrast and responsive coverage is not maintained as a uniform regression matrix (P2, Needs testing)

- **Component:** Shared UI / Regression QA
- **Finding:** All seven pages rendered in a Chromium smoke check; this does not prove keyboard-only navigation, dialogs/focus traps, screen readers or all viewport breakpoints across all flows.
- **Evidence:** `QA source checks; widget HTML aria-label and motion styles`
- **Acceptance:** Run axe/keyboard/contrast and 320/390/768/1440 responsive checks per release, recording exceptions by widget.

### I027 · Full decisions import accepts arbitrary review states without schema validation (P1, Confirmed)

- **Component:** Master Dashboard / Data integrity
- **Finding:** The imported master JSON is merged into mutable review/goal/issue state and custom arrays without a schema check for permitted status values, approved flags, reference IDs or contradiction.
- **Evidence:** `MASTER_DASHBOARD_v1.18.html :: importState()`
- **Acceptance:** Validate import against a versioned JSON schema; preserve unknown fields in quarantine and preview a diff before applying changes.

### I028 · Path verification cannot establish local file existence automatically under file:// (P2, Confirmed)

- **Component:** Master Dashboard / Usability
- **Finding:** The UI uses HTTP HEAD when served and a folder picker when local, so links remain Not verified in file:// until a manual directory scan. This is expected browser behavior but can be mistaken for missing assets.
- **Evidence:** `MASTER_DASHBOARD_v1.18.html :: checkPaths()/applyScan()`
- **Acceptance:** Make offline mode explicit and add a one-click guided directory-check wizard with separate states for blocked/unverified/missing.

## Suggested improvements

- **S012 · Master Dashboard [P0] One unified audit-to-release triage panel** — Turn scan findings into linked issue, acceptance check, proposed improvement and test evidence, not disconnected status cards.
- **S013 · Widget Launcher [P0] Preflight bundled-artwork compatibility before syncing** — Detect whether imported HTML contains local asset references and confirm a self-contained build or all adjacent files exist before marking ready.
- **S014 · Tree of Life Atlas [P1] Add an evidence-backed selected-clade focus panel** — Retain the existing hierarchy, but show curated organism visual, dated lineage summary and source link next to the active selection.
- **S015 · Muscle Atlas [P1] Clear selected muscle anatomy and exercise context** — Keep muscle labels/navigation but provide a consistent selected-muscle highlight and a compact exercise-role card, with actual exercise data only.
- **S016 · Emergence Atlas [P1] Add evidence-and-scale comparison for the active emergence level** — Use the existing level model to link its components, interactions, scale ranges and uncertainties in a compact network-evidence view.
- **S017 · Shared Taxa [P1] Explain 172 vs 173 interval scope through a mapping view** — Show canonical Shared Taxa interval coverage beside Deep Time UI interval IDs and explain intentionally nonmatching scope.
- **S018 · Artwork Studio [P0] Use a gated artwork promotion and manifest-diff wizard** — After human approval, show license provenance, checksum, affected thumbnails and exact standalone/bundle rebuild list before promotion.
- **S019 · Master Dashboard [P1] Portable project-state snapshots with previewable diff** — Offer versioned import validation, review-only changes, audit logs and merge choices before replacing existing approval/checklist states.
- **S020 · Brain Atlas [P1] Add a coordinate-provenance route for future true depth** — Keep existing estimated-depth mode, but prepare a separate registered model path for anatomical 3D coordinates and view-specific overlays.
- **S021 · Mythology Atlas [P1] Separate generated narrative portraits from documented historical artwork** — Add figure-level Source artwork tab with credit, object date, museum/license and external records rather than implying modern art is ancient.
- **S022 · Shared UI [P1] Standard keyboard, reduced-motion and visual-contrast test plan** — Apply the same focus, motion and popup keyboard handling to all six atlases and launcher; save a per-version acceptance log.
- **S023 · Master Dashboard [P0] One-click release verification report** — Generate a read-only local audit of linked files, asset hashes, application syntax, version buttons, comparison coverage and data dependencies.
- **S024 · Deep Time Atlas [P1] Link interval artwork to traceable paleomaps and representative life** — Add verified interval-specific continents/paleomap assets and dated taxon references with citations and exclusions where evidence is weak.
- **S025 · Widget Launcher [P1] Show authoritative package and asset health per widget** — On each launcher card, display actual linked HTML version, dataset dependency, image bundle type, last validation and sync errors.

## Limits / deferred validation

- Direct file:// Chromium navigation blocked in audit environment
- Actual Windows folder sync and persistence not tested
- Artwork checksum validation is not scientific/cultural accuracy review
- Concept proposals are not implemented code


## Release impact

Dashboard v1.19 adds issue/suggestion metadata, audited state and visual proposal examples. **No source widget files, Shared Taxa records or original artwork binaries were changed.** Baseline checklist statuses remain 27 implemented, 30 partial and 27 planned across 84 goals. This audit adds separate issue backlog and suggestion records, not fictitious accepted or closed goals.
