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
4. Update component changelog, manifest (when verified), and docs/handoffs/latest.md.
5. Record a brief audit trail: changed files, spec revision, test results, known issues.
6. Do not commit, push, publish a release, or delete sources unless explicitly instructed.
