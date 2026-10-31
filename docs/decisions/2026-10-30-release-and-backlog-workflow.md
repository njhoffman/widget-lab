# Repository releases, living backlog, and Atlas visual evidence

**Status:** APPROVED by explicit user requests on 2026-10-30.  
**Affected specs:** Atlas component specs and visual direction revision 2; `AGENTS.md`.

## Context

The user requested SemVer/GitHub tags, a root changelog, a categorized prioritized TODO similar to `~/.config/claude`, task updates alongside specs/features, task capture for issues/suggestions, and routine commit/push after update batches. They also required actual-versus-goal images with completed/pending items after each Atlas update, opened automatically in feh.

## Decision

Start repository VERSION at 0.1.0 with annotated `vX.Y.Z` tags. Mirror the version in the manifest; use a root Keep a Changelog structure and one version bump per finished batch. Routine validated batch commits/tags/pushes are authorized. This supersedes the scaffold's blanket stop before commit/push for this workflow. Deployment, publishing GitHub Releases, destructive actions, force-pushes, and tag rewrites remain separately controlled.

Use TODO.md as the live register, with Claude-style p1/p2/p3 priorities, category labels, stable IDs, approval/status, acceptance criteria, and evidence. Preserve all 137 historical goal/issue/suggestion IDs. Historical implemented/done items become verification tasks; task registration does not approve an old proposal. Immutable catalogs and the browser dashboard remain provenance/tools, not a second authoritative live backlog.

Capture actual applications in a real browser, render reports beside original goal references with completed/pending task sidebars, retain hashes/viewport/selection/timestamps/browser metadata, and open the final PNGs in feh. Use the two approved goal images for the primary three widgets. Other existing concept targets are explicitly proposed. Save versioned evidence; do not paint or synthesize actual screenshots. Compare current sources/goals against saved hashes during project checks.

## Alternatives and consequences

Renumbering imported components would rewrite history; repository SemVer is separate. Reusing imported screenshots would misrepresent freshness; fresh browser captures are required. A generated live TODO would overwrite decisions; agents maintain the file and a coverage check detects lost historical IDs. External GitHub Issues synchronization is not configured or required by these requests.

Initial captures exercise selected Triassic/OFC/Zeus states and render the other four defaults in a clean profile. This is not full interaction, accessibility, or scientific QA. Browser/feh execution may require tool sandbox permission even though the recurring workflow is already user-authorized.
