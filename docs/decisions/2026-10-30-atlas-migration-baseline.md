# Atlas migration baseline and visual references

**Date:** 2026-10-30  
**Status:** Accepted for repository setup and visual direction, based on the user's migration request and follow-up authorization.  
**Affected specs:** `atlas/specs/*.md` revision 1.

## Context

The bootstrap imported Shared Taxa but left all component versions null. Atlas files had been copied into `incoming/atlas/` as an entire distribution, which does not match the bootstrap's component inbox routing. Import collisions retained the scaffold Shared Taxa README, and the initial import omitted two source ZIPs. Older project chat titles are not proof of current release versions.

## Decision

Preserve the delivered Atlas relative layout under `atlas/`, including original HTML, assets, project catalog, tools, goal pictures, and historical documents. Use actual HTML titles, the v1.21 catalog, SHA-256 inventory, and prior v1.20 checksums to establish source identities. All six scientific widgets match prior package checksums; Launcher v1.14 is corroborated by its HTML, catalog, and v1.21 release notes.

Restore Shared Taxa from the complete package after validating all 90 manifest entries. Preserve the displaced scaffold README in `docs/migration/`. The canonical dataset is `shared/taxa/`; the delivered Atlas copy remains for compatibility. No scientific records, identifiers, progress formats, or release versions are changed.

Retain both user-selected goal images as approved visual direction. Their sample data and renderings are not scientific specifications. Existing asset review statuses and uncertainty disclosures remain binding. Curated project context replaces dependence on raw conversations; historical proposals remain unapproved unless independently accepted.

## Alternatives

Reorganizing every widget into component `src/` folders would require modifying relative paths or maintaining generated copies. Rebuilding from older chat snippets would risk losing later functionality. Importing the nested full distribution ZIP would duplicate the source package and complicate release identity.

## Consequences

The original flat widget paths are authoritative for this migration. Component subdirectories retain docs, specs, and changelogs. There is temporary duplication of Shared Taxa to preserve the delivered dashboard; a future packaging change can remove that duplication after link and runtime verification. Large distribution ZIPs remain private imports, so historical package-download actions are unavailable. No deployment, cloud synchronization, commit, or push is part of this work.

Integrity and syntax pass independently of scientific accuracy, artwork approval, and interactive browser QA. Those limits are recorded in the reports and handoff.
