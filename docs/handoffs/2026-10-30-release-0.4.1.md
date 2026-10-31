# Codex handoff — justfile tooling batch 0.4.1

Date: 2026-10-30 (America/Chicago). Base: `3872a1a` / tag `v0.4.0`. Repository patch release 0.4.1 adds development commands; component versions, specs and widget sources remain unchanged.

## Delivered and audit trail

Closed user-requested WL-022: root `justfile` lists commands by default and wraps dependency installation, all four current builders, integrity audits, unit tests, project consistency checks, Atlas-only localhost serving, browser regression and comparison capture. Python is overridable; positional arguments forward browser options and the server port. Comparison capture retains automatic feh opening and versioned evidence behavior.

Changed files: `justfile`, README, tools README, development workflow, TODO, VERSION, root CHANGELOG, repository manifest release version and this handoff. Prior Brain handoff is preserved as `docs/handoffs/2026-10-30-release-0.4.0.md`. Workflow decision remains approved; no component specification revision is needed for tooling wrappers.

## Verification

`just --list`, formatter check, serve dry run, browser/capture help forwarding, `just build`, and `just check` pass. The combined check runs migration/data/schema checks, Atlas integrity/inline JavaScript checks, all 14 unit tests and release/task/registered-evidence checks. Rebuilding produces byte-identical widget files and current launch page. No Python dependencies were reinstalled.

Existing complete 0.4.0 browser matrix and earlier per-widget goal comparisons remain registered and hash-valid. No widgets or goals changed, so no new browser matrix/comparison images were generated or opened for this tooling-only release. Browser/desktop recipes require Chrome/Chromium and feh; audits also require Node.js, and Python requirements are in requirements-dev.txt. Commands were validated on just 1.59.0.

## Remaining work and publishing

Continue the live TODO and prior Brain handoff for visual, scientific, accessibility and compatibility limits. `just check` checks existing evidence; run `just browser-test` and `just compare --widgets ...` separately when changing widgets after selecting the new batch VERSION. A narrow exploratory browser run does not satisfy the full matrix gate.

Finish by committing, annotated-tagging v0.4.1, atomically pushing and verifying remote branch/tag objects. Actual publication outcome is reported in the final response.
