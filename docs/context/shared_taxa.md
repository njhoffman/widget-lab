# Shared Taxa — curated dataset context

**Status:** Imported v1.0 byte integrity and JSON schemas verified on 2026-10-30; scientific interpretation remains subject to documented uncertainties.

The canonical package is `shared/taxa/manifest.json`, dataset/schema version 1.0. All 90 listed files now match their size and SHA-256. The initial bootstrap had retained a scaffold README and omitted two original source ZIPs; the complete Atlas dataset supplied matching replacements. The displaced README is preserved in `docs/migration/shared-taxa-scaffold-readme.md`. No taxonomic records or identifiers changed.

The package records 368 canonical taxa, 173 canonical intervals, 495 organism examples, 580 curated taxon/interval associations, and 57 unresolved scientific ambiguities. The 8,916 inferred age-filter matches must remain separate from curated associations. Deep Time's 172 indexed UI intervals use a different scope from the 173 canonical intervals.

Stable `stx:` IDs and `ID_MAPPING.json` crosswalks must be carried forward. Read `shared/taxa/MIGRATION_GUIDE.md` and `RECONCILIATION.md` before changing consumers. Source age assertions, alternate classifications, and provenance are retained; null calibrated dates are not missing values to invent.

The delivered duplicate at `atlas/data/Shared_Taxa_v1.0/` is preserved for dashboard link compatibility. Treat `shared/taxa/` as canonical for new integrations. Do not edit published release bytes in place. Future consolidation needs link/runtime testing and an explicit packaging decision.

Checksums establish matching bytes; schemas establish structural validity. Neither verifies fossil claims, anatomical interpretation, external artwork URLs, licenses, or the 57 ambiguities. Existing dataset validation reports are historical evidence; current import checks are in `docs/migration/verification_report.json`.
