# Widget Lab — Codex / contributor instructions

## Authoritative inputs
- Read project_manifest.json first. Any `release_version: null` is **unverified**, not v1.0.
- Read the relevant atlas/specs/ or quiz/specs/ document and docs/context/ before implementing.
- Use docs/decisions/ to understand why earlier choices were made.
- Treat approved requirements as binding; clearly distinguish drafts, proposals, and implemented releases.
- Preserve existing standalone HTML files until tests verify an alternative implementation.
- Shared Taxa is authoritative only when the actual dataset/manifest is verified, not merely because a filename exists.

## Safety and history
- Do not replace latest scientific functionality with an older UI branch.
- Preserve stable taxon and question identifiers and existing stored progress formats.
- Do not silently drop historical changelog entries or change release versions.
- Do not import, read, or commit .local/, incoming/, full ChatGPT exports, secrets, or personal data.
- Do not implement ideas from archived conversation transcripts until curated and marked APPROVED in the specification.

## Change workflow
1. Check git status and read relevant specs, manifest, and tests.
2. Implement **approved** requirements only; clarify ambiguities rather than guessing.
3. Run tests/checks and report limitations.
4. Update TODO.md, the root and affected component changelogs, manifest (when verified), and docs/handoffs/latest.md.
5. Record a brief audit trail: changed files, spec revision, test results, known issues.
6. Finish each agreed batch by running checks, reviewing the staged diff, bumping the repository version once, committing, creating an annotated SemVer tag, and pushing the commit and tag to origin atomically. The user explicitly authorized this recurring workflow on 2026-10-30. Do not force-push, overwrite tags, delete source artifacts, deploy, or publish GitHub Releases without separate authorization.

## Versioning and release batches
- Use root VERSION as the repository's SemVer source of truth, mirrored in project_manifest.json under repository.release_version. Start at 0.1.0. Use annotated GitHub tags vX.Y.Z.
- Bump once per finished batch: patch for fixes/docs/small changes, minor for new features, major for breaking changes (before 1.0, breaking changes bump minor). Preserve original imported component versions and history; a repository bump does not renumber them.
- Maintain root CHANGELOG.md with an Unreleased section and dated release sections under Added / Changed / Fixed / Removed as applicable. Move the batch's entries into its version section when releasing. Never fabricate releases for earlier unversioned history.
- Read docs/development-workflow.md before closing a batch. Report the version, commit, tag, checks, push outcome, and material limitations. If push fails, retain the local commit/tag and report the blocker; never mark the batch pushed without evidence.

## Living task list
- TODO.md is the live repository backlog. Read it at the start of work and update it in the same batch as every spec change, feature, discovered issue, suggestion, test finding, or completion.
- Use stable IDs, checkboxes, (p1) high / (p2) normal / (p3) low priorities, and [bug], [feature], [refactor], [docs], [test], [chore], or [perf] categories. Include status/approval, source/spec links, actionable scope, and acceptance criteria.
- Capture discovered issues as tasks and suggestions as proposed tasks immediately. A task's existence or historical completion claim is not implementation approval. Triage duplicates, cross-link them, and retain their IDs.
- Mark done only after the acceptance checks pass and evidence is linked. Historical implemented/done records require verification tasks. Do not reset or regenerate the live TODO from imported catalogs.
- Keep spec revisions, linked task acceptance criteria, changelog, and handoff synchronized. Run tools/check_project.py to catch missing historical IDs and release metadata drift.

## Atlas visual evidence
- Every batch updating Atlas widgets must produce fresh actual-versus-goal comparison PNGs for each affected widget, with completed and pending items listed in a side column. Also capture a baseline during initial workflow setup.
- Use tools/capture_atlas_comparisons.py with the current VERSION. Preserve original widget bytes: capture the actual application in a browser, never synthesize or repaint actual screenshots. Record source SHA-256, goal SHA-256, viewport, selection, browser version, task IDs, and capture date in the companion evidence JSON.
- Match the relevant section of goal_1.png and goal_2.png for Deep Time, Brain, and Mythology. Other components use existing concept references explicitly labeled proposed until approved. Never invent a target or label an old actual screenshot as fresh evidence.
- Completion/pending labels must come from TODO.md and evidence, not from an AI picture or an imported claim. Clearly distinguish render-only checks from interactive/scientific review.
- Open produced comparison PNGs automatically with feh at the end of Atlas batches, as explicitly requested by the user. Use --no-open only for automated/headless verification; disclose if the desktop viewer cannot launch.
