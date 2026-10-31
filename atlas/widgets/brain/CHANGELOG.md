# Brain — release history

## [1.22.0] - 2026-10-30

### Added

- Compact native projection/estimated-depth header and inactive strength control while depth is off.
- Larger selected-region summary, non-overlapping orientation reference, and readable responsive scientific details.
- Separate source-preserving build and expanded native projection/depth/hierarchy/time-filter checks.

### Fixed

- New mobile grid rules retain usable hierarchy/control widths instead of collapsing into an implicit column.

### Preserved

- Original 1.21 HTML and history, authored geometry/transforms, region/circuit IDs, source records, depth calculations and controls. All schematic/estimated limitations remain explicit; no registered anatomy is introduced.


<!-- Bring forward all VERIFIED historical releases from existing files; none are inferred yet. -->

## Unreleased — repository migration, 2026-10-30

- Registered the delivered source and documented verified version identity without changing the original HTML or scientific content.
- Added specification revision 1, shared goal-image direction, repeatable integrity/syntax checks, and a Codex handoff.
- Preserved historical release entries in the source HTML; no widget version bump. Interactive browser QA remains open.

- Workflow update: specification revision 2 requires fresh actual-versus-goal comparison images, completed/pending task lists, and automatic feh preview for every future widget update. The initial browser-rendered baseline is in `docs/visual-reviews/0.1.0/`; original source version remains unchanged.

## Unreleased — regression verification, repository 0.1.1

- Verified actual navigation/filter/panel and keyboard/history behavior at 390/768/1440px in Chrome/Linux; see `docs/browser-tests/0.1.1/`.
- Captured new goal comparisons and advanced component spec to revision 3. Widget HTML, science, stored-state formats, and component version remain unchanged.
