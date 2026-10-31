# Atlas Widgets Master Dashboard — v1.20

Release date: 2026-10-17. Previous: v1.19.

## Changes
- Artwork-approval eligibility now enforced centrally during in-page changes, imports, and migration from old saved states.
- Imported approvals are quarantined pending explicit review. Downgrading a subject to draft or queued revokes approval.
- Approval requires a documented source/license, creator, reviewer, review note and a valid-format SHA-256; the dashboard **does not independently verify** image provenance or scientific accuracy.
- Existing calibration artwork remains a draft and cannot be promoted through this dashboard alone.
- Suggestions can create real linked issues; release traceability shows named issue/suggestion/goal IDs and editable plan stages.
- Launcher v1.13 adds asset readiness indicators and refuses to falsely open broken bundle-dependent HTML via blob URL. Standalone HTML imports are unchanged.
- Updated changelogs, dashboards, version and file catalog; retained every widget's previous history and the unmodified Shared Taxa v1.0 release.

## Limitations
- Launcher v1.13 does not copy or inline external artwork directories into imported HTML. Its preflight is deliberately conservative and flags recognized relative artwork references.
- Source attribution/rights entered by users is not automatically verified. Final user approval and release manifest rebuild must be documented separately.
- Direct file:// and local HTTP navigation were blocked by the test sandbox; tests used inline Chromium rendering. Windows IndexedDB/permissions are not verified.
