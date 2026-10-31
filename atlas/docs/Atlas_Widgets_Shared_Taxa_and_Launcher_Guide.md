# Atlas Widgets — Shared Taxa & Widget Launcher Guide

**Guide updated:** October 16, 2026  
**Dataset referenced:** Shared Taxa **v1.0** (released October 15, 2026; schema **1.0**)  
**Launcher implementation inspected:** Widget Launcher **v1.7** from `atlas_v1.7.zip`  
**Dataset release archive:** `Shared_Taxa_v1.0_2026-10-15.zip`  
**Scope:** Installing, verifying, using, and maintaining the scientific dataset alongside the standalone Atlas widgets.

> **Important version distinction:** This document does **not** create a new Shared Taxa release or change any widget version. It describes the inspected v1.0 dataset and v1.7 launcher. The project has discussed newer launcher builds, but those were not available for code inspection here; their behavior may differ.

## 1. What Shared Taxa is

**Shared Taxa** is a **versioned scientific data release**, not a launchable atlas and not a shared live database server. It consolidates records from:

- **Tree of Life Explorer v1.7** — taxonomy, lineage information, representative organisms, classifications, diversity and population estimates.
- **Deep Time Atlas v1.6** — geological intervals, taxon profiles, interval associations, paleoenvironmental context, and illustrative images.

Shared Taxa supplies stable canonical IDs and shared definitions so multiple atlases can refer to the same concepts. **Each atlas still owns its interface, navigation, embedded/offline data snapshot, and independent widget version number.**

```text
                       Shared Taxa v1.0
                      Canonical JSON + IDs
                               |
                  +------------+------------+
                  |                         |
           Tree of Life Atlas         Deep Time Atlas
           own HTML / UI              own HTML / UI
           embedded snapshot          embedded snapshot
                  |                         |
                  +------------+------------+
                               |
                        Widget Launcher
           imports/verifies dataset; syncs/opens HTML
           shows declared dependency compatibility
```

**The launcher importing a dataset is different from a widget consuming it.** The launcher can store and describe Shared Taxa, but it does **not** inject the JSON into an existing HTML widget or silently update that widget's embedded scientific data.

## 2. Confirmed Shared Taxa v1.0 inventory

| Metric | Result | Interpretation |
|---|---:|---|
| Canonical taxon concepts | **368** | Dataset concepts, not all described species worldwide |
| Original Tree of Life taxon records | 238 | Includes hidden `Life` root |
| Original Deep Time taxon profiles | 200 | 70 matched; 130 additional canonical concepts |
| Cross-source profiles reconciled | 70 | Original assertions retained |
| Representative organism entries | 495 | 95 Tree + 400 Deep; examples rather than worldwide species list |
| Canonical geologic intervals | 173 | Sources contribute 44 Tree + 172 Deep interval records |
| Curated interval–taxon associations | 580 | Source-curated, not independently verified fossil observations |
| UI-derived age-filter matches | 8,916 | **Not** scientific observations; keep distinct from curated associations |
| Population-estimate records | 12 | One expressly unknown; scopes/units vary |
| Taxa with subdivision references | 47 | 104 subdivision estimate values |
| Image reference records | 129 | 23 bundled assets hash-checked locally; 0 external links checked |
| Scientific ambiguity items | 57 | Retained in reconciliation reports |
| Release file count | 91 | `manifest.json` + 90 inventoried files |
| Structural validation | 32 checks passed | Release status includes scientific warnings |

**Exact release status:** `published_with_documented_scientific_ambiguities`  
**Exact validation status:** `PASS_WITH_DOCUMENTED_SCIENTIFIC_WARNINGS`

Passing schema and relationship checks is **not** independent verification of scientific claims, source URLs, image licenses, or fossil identifications.

## 3. File layout and responsibilities

After extracting the release ZIP, you should have a folder named `Shared_Taxa_v1.0` containing:

| File / directory | Purpose |
|---|---|
| `manifest.json` | Version, schema, release status, counts, sources, compatibility, file names, SHA-256 hashes and sizes |
| `taxonomy.json` | Canonical taxon concepts, ranks, parent relationships, alternative classifications |
| `taxon_details.json` | Descriptions, pronunciation, etymology, characteristics, original source text |
| `taxon_history.json` | Source-specific lineage and temporal assertions; uncertain crown/stem dates remain distinct or null |
| `diversity.json` | Species richness, populations, subdivisions, units, uncertainty and provenance |
| `organisms.json` | Organism examples linked to canonical taxa |
| `geologic_time.json` | Geologic interval IDs, ordering, boundaries and source assertions |
| `geologic_taxon_links.json` | Curated links **separate from** inferred UI age-filter matches |
| `rank_guides.json` | Rank education and monophyly guidance |
| `sources.json` | Source references and attribution information |
| `images_manifest.json` | Image references, local assets, verification/licensing status |
| `additional_science.json` | Additional source scientific content |
| `ID_MAPPING.json` | Full source-ID → canonical-ID crosswalk for taxa and intervals |
| `RECONCILIATION_REPORT.json` / `RECONCILIATION.md` | Matched, conflicting and unresolved source assertions |
| `VALIDATION_REPORT.json` | Structural tests, statistics, scientific warnings |
| `schemas/` | JSON Schema 2020-12 definitions |
| `source_exports/` and `source_archives/` | Verbatim inputs for audits, recovery and reprocessing |
| `README.md`, `MIGRATION_GUIDE.md`, `CHANGELOG.md`, `CHANGELOG.html` | Documentation, migration rules, and release history |

**Do not edit the source archives or change values inside the published v1.0 release.** Treat each released ZIP as immutable.

## 4. Recommended Windows folder arrangement

Keep an extracted **working dataset** available for the launcher, while separately preserving the immutable ZIP under your version-controlled project:

```text
C:\Projects\Atlas-Widgets\
|-- launcher\
|   `-- widget_launcher_v1.7.html
|-- widgets\
|   |-- Deep_Time_Atlas_v1.7.html
|   |-- tree_of_life_explorer_v1.8.html
|   `-- [other current atlas HTML files]
|-- shared-taxa\
|   `-- Shared_Taxa_v1.0\
|       |-- manifest.json
|       |-- taxonomy.json
|       |-- ID_MAPPING.json
|       |-- schemas\
|       |-- source_exports\
|       `-- [remaining release files]
|-- releases\
|   `-- Shared_Taxa_v1.0_2026-10-15.zip
`-- docs\
    `-- Atlas_Widgets_Shared_Taxa_and_Launcher_Guide.md
```

The launcher can **scan nested folders** for widget HTML and dataset `manifest.json` files. You can therefore choose `C:\Projects\Atlas-Widgets` as the source folder, or choose `shared-taxa\Shared_Taxa_v1.0` directly with **Import dataset folder**. Avoid leaving several *different* widget builds with confusingly similar names in the active scan tree; store old versions in a separate archive outside it or carefully check which HTML build was chosen.

### Extracting the dataset

1. Download `Shared_Taxa_v1.0_2026-10-15.zip`.
2. In Windows File Explorer, right-click it and select **Extract All**.
3. Keep the resulting `Shared_Taxa_v1.0` directory **intact**, including nested `schemas`, `source_exports`, and `source_archives` folders.
4. Move the extracted directory under `C:\Projects\Atlas-Widgets\shared-taxa\`.
5. Keep the original ZIP under `releases\` as a rollback and provenance copy.

**A ZIP alone cannot be imported by the inspected launcher.** It expects an **extracted folder** with `manifest.json` and every file named in the manifest. Also, the inspected `atlas_v1.7.zip` launcher bundle does **not** contain the full `Shared_Taxa_v1.0` directory; extract the dataset release ZIP separately.

## 5. Import Shared Taxa into the Widget Launcher

The procedure below is confirmed from the **v1.7 launcher implementation**, which works best in current Chromium-based browsers such as **Edge** or **Chrome**.

### Method A — Import the dataset directly

1. Open `widget_launcher_v1.7.html` in Edge or Chrome.
2. Locate the **Shared Data** section.
3. Click **Import dataset folder**.
4. Select the **extracted `Shared_Taxa_v1.0` folder**, not the ZIP.
5. Allow the browser to read the selected folder.
6. The launcher checks the manifest, validates listed files, and imports the canonical data if the inventory matches.
7. Click the **Shared Taxa** item in Shared Data to inspect version, dataset statistics, checksum inventory, linked widgets, source provenance and outstanding ambiguities.

### Method B — Sync widgets and dataset together

1. Click **Source folder** and choose `C:\Projects\Atlas-Widgets` (or a suitable parent containing the current widget HTML files and extracted dataset).
2. Click **Sync latest widgets**.
3. The launcher scans for recognized atlas HTML files and nested dataset manifests.
4. Check the **Shared Data** card for **Shared Taxa v1.0**, **368 indexed taxa**, and the **57 scientific ambiguities** warning.
5. Check individual widget cards for their sync status and any **declared** Shared Taxa dependency.

**Difference:** **Import HTML files** accepts widget `.html` files; **Import dataset folder** checks a scientific dataset folder. They are separate operations. **Sync latest widgets** searches the chosen local source folder for both.

### What the launcher validates on import

- A published/canonical manifest; unreconciled or draft source exports are rejected.
- Dataset and schema versions, release date, required source and compatibility metadata, and record counts.
- Paths, **SHA-256 checksums**, and byte sizes for all **90 manifest-inventoried files** (including binary images and source ZIPs).
- Valid UTF-8 and valid JSON for JSON entries.
- The published scientific-warning status against `VALIDATION_REPORT.json`.
- Supported import limits in v1.7: at most **200 inventory entries** and **70 MiB** of total referenced files.

**Limits:** The launcher does not independently review taxonomy or geology, test external image URLs, or verify licenses. It does not alter the scientific source HTML files.

## 6. What the launcher stores — and does not store

| Launcher behavior | What it means |
|---|---|
| Reads and validates extracted release files | Detects missing or altered files at import time |
| Stores dataset metadata and verified **top-level JSON text** in browser IndexedDB (`AtlasWidgetLauncher`, v2) | Shows releases and dependency comparisons without rereading the folder every time |
| Keeps imported widget HTML in browser storage | Launches HTML snapshots even without an active folder connection |
| Does **not** store full source archives or image directories as browser dataset files | Keep the extracted folder and original release ZIP backed up on disk |
| Does **not** patch existing HTML with new Shared Taxa JSON | A data update requires a separately built/tested widget release |
| Does **not** automatically check the internet for new releases | **Sync latest widgets** scans your selected **local** folder |
| **Output folder** copies synced HTML and a launcher-generated inventory manifest | This is **not** a complete exported Shared Taxa release or a full scientific backup |

If browser site data/IndexedDB is cleared or unavailable, you may have to import again. Keep authoritative files on disk and in Git or another backup location instead of relying on the browser cache.

## 7. How atlas widgets should consume Shared Taxa

### Canonical-ID lookup

1. Identify the source widget record, such as a Tree of Life `taxon_id` or a Deep Time taxon profile ID.
2. Find the matching `source_export` **and** `source_id` in `ID_MAPPING.json`.
3. Use `canonical_id` (`stx:taxon:...`) to join `taxonomy.json`, `taxon_details.json`, `taxon_history.json`, and related files.
4. Use canonical interval IDs (`stx:geo:...`) for `geologic_time.json` and `geologic_taxon_links.json`.
5. Preserve the source identifiers and provenance for debugging and rollback.

**Do not** join only by display name, guess a parent for an unmatched taxon, or replace canonical IDs because a name or classification changed.

### Scientific rules for consumers

- Treat `classification_assertions`, `alternative_classifications`, and historical kingdom categories as **source assertions**, not universally agreed modern taxonomy.
- Distinguish approximate **lineage origin**, **earliest fossil evidence**, **crown-group origin**, **stem divergence**, and **extinction**. Missing calibrated values remain `null` rather than invented estimates.
- Never treat a count of named clades **indexed in the atlas** as the world's total number of clades.
- Keep extant species estimates, extinct species estimates, population individuals, populations of **mature animals**, **colonies**, and subdivision counts in separate quantities, with scope and date.
- Keep 580 source-curated interval links distinct from 8,916 mechanically inferred display matches; neither group is independently verified fossil evidence.
- Respect image `verification_status` and license/credit uncertainties. Local integrity checking is not copyright clearance.

### Standalone HTML distribution

For offline-capable atlases, the migration guide recommends **embedding the approved canonical Shared Taxa snapshot in a newly generated widget** rather than assuming the launcher will serve the scientific JSON at runtime. Preserve the old embedded data as rollback until the new widget is regression-tested.

If a future widget instead loads separate JSON at runtime, host it from an appropriate local HTTP server or website and explicitly manage fetch paths, CORS, caching and offline fallbacks. A standalone `file://` page cannot reliably fetch arbitrary local JSON files in every browser. **The current launcher is not a JSON web server.**

## 8. Dependency metadata in widget HTML

The inspected v1.7 launcher recognizes a JSON `<script>` tag with ID `atlas-widget-metadata` and the **camelCase** `dependencies` array. Once a widget **really embeds** a particular dataset release, a future audited build can expose metadata like this:

```html
<script type="application/json" id="atlas-widget-metadata">
{
  "widgetId": "tree",
  "widgetVersion": "1.8",
  "dependencies": [{
    "datasetId": "shared-taxa",
    "embeddedVersion": "1.0",
    "embeddedSchemaVersion": "1.0",
    "schemaRange": "1.x",
    "integration": "embedded",
    "updateMethod": "rebuild"
  }]
}
</script>
```

For Deep Time use `widgetId: "time"` and its actual independently released widget version. **This is a format example, not an instruction to falsely label an unmigrated widget.** Declare only the data genuinely embedded in the HTML, and revalidate the widget when changing the metadata.

### Important compatibility caveat in the inspected files

- The bundled **Tree of Life Explorer v1.8** HTML in `atlas_v1.7.zip` contains `atlas-widget-metadata` with **snake_case** fields `dataset_dependencies` and `dataset_id`. The inspected **launcher v1.7** reader looks for camelCase `dependencies` and `datasetId`, so it can treat the declared script as **“No dependency”** even when the Tree widget actually embeds Shared Taxa.
- The bundled **Deep Time Atlas v1.7** HTML presents a Shared Taxa v1.0 offline badge and a canonical snapshot but **does not expose a launcher-recognized `atlas-widget-metadata` script**. The launcher can therefore report its dependency as **“Unknown.”**

**Action for the next audited widget/launcher builds:** standardize the metadata contract (or teach the launcher to read both formats), verify the embedded dataset against the release ZIP, and check that the dependency status is accurate. Do not conclude from a `No dependency` or `Unknown` badge alone that the embedded scientific data is absent. Newer launcher versions may already have corrected this; verify their implementation separately.

### Typical dependency status labels (launcher v1.7)

| Status | Interpretation |
|---|---|
| **Up to date** | Declared embedded version matches newest imported schema-compatible release |
| **Needs rebuild** | A newer compatible dataset is imported, but standalone HTML still embeds an older snapshot |
| **Update available** | A runtime/replacement update was declared; the replacement widget still needs importing |
| **Incompatible** | No imported dataset satisfies the declared schema range, or declared schema is inconsistent |
| **Dataset missing** | No matching canonical dataset imported |
| **Unknown / No dependency** | Metadata is absent, incomplete, or not recognized; **not proof** about actual embedded content |

## 9. Updating Shared Taxa without breaking widgets

Suppose the next additive scientific release is **Shared Taxa v1.1**.

1. Start from the validated **v1.0 ZIP**, its `ID_MAPPING.json`, and preserved source exports.
2. Reconcile new data with existing canonical concepts. Keep existing IDs stable; track changed classifications, values, dates, and citations.
3. Update every affected canonical file, JSON schema (if necessary), source inventory, reconciliation report and release documentation.
4. Increment the dataset **minor** version for additive scientific expansion; reserve a **major** bump for breaking schema/compatibility changes.
5. Update release date, changelog/history and `manifest.json` file checksums; run the complete validation suite.
6. Publish an **immutable full release ZIP**, e.g. `Shared_Taxa_v1.1_YYYY-MM-DD.zip`. Keep v1.0 for rollback.
7. Extract the new ZIP beside the old release, rather than overwriting the old directory.
8. Click **Import dataset folder** or **Sync latest widgets** in the launcher. Verify the new version and scientific warnings.
9. **Separately rebuild and regression-test** Tree of Life, Deep Time, or other dependent widgets to embed v1.1, each with its **own independent widget version**.
10. Import the new widget HTML into the launcher; check dependency metadata and navigation; tag/commit the release in Git.

The launcher rejects **different bytes using the same dataset ID + version** rather than silently replacing an earlier imported canonical release. Never edit an already published version in place. Publishing v1.1 does **not** automatically change Tree of Life v1.8, Deep Time v1.7 or the launcher's own version.

## 10. Recommended Git/GitHub Desktop workflow

Commit and tag dataset releases **separately** from widget releases:

```text
shared-taxa-v1.0           -> immutable scientific dataset
shared-taxa-v1.1           -> next validated scientific release
widget-launcher-v1.7       -> launcher code release
tree-of-life-v1.8          -> Tree of Life widget release
deep-time-v1.7             -> Deep Time widget release
```

The Git tag describes the state of the **whole repository at the tagged commit**, so use distinct commit messages and tags for each release. Also save the final ZIP outside browser storage. Never rely exclusively on IndexedDB or a ChatGPT conversation as your backup.

## 11. Troubleshooting

| Symptom | Check / fix |
|---|---|
| Dataset still says **Not imported** | Ensure you selected the **extracted** release folder containing `manifest.json`, not a ZIP or a source-only unreconciled export |
| **Missing file** | Extract the **entire** v1.0 ZIP without omitting nested archives, images or documentation |
| **SHA-256 mismatch** | Restore the untouched published ZIP; do not manually change JSON without a new version/release |
| **Release is not published/canonical** | You selected an original Tree/Deep source export or a staging package instead of the authoritative reconciled release |
| JSON parse / byte-size error | Restore the original files, preserve their paths and UTF-8 encoding |
| Widget still shows old scientific information | Launcher import does not replace embedded data; import a **newly rebuilt** widget HTML |
| Dependency says **Unknown** or **No dependency** | Check whether HTML includes **launcher-recognized** metadata; see the known v1.7 format mismatch above |
| External images don't load | Source image URLs have **not** been network-verified; also check connectivity, URL availability, licensing and local fallback assets |
| Previously imported dataset disappears | Browser IndexedDB/site data may have been cleared; re-import the extracted folder; restore from the release ZIP |
| Output folder lacks Shared Taxa JSON | Expected in v1.7: launcher output exports synced HTML plus an inventory manifest, **not** a complete dataset archive |

## 12. Release acceptance checklist

- [ ] The full, unmodified Shared Taxa ZIP is preserved and backed up.
- [ ] All canonical file inventories and source-record counts reconcile.
- [ ] `ID_MAPPING.json` retains previously published IDs.
- [ ] All JSON schemas and cross-file references validate.
- [ ] Conflicting ranks, lineage ages, interval boundaries and quantities remain source-attributed.
- [ ] Source-curated and UI-inferred interval links stay separate.
- [ ] Population estimates retain units, geographic scope, dates and uncertainty.
- [ ] Image links are marked **checked** only if actually tested; local file integrity is not mistaken for a license check.
- [ ] Launcher imported the correct published dataset and verified all manifest files.
- [ ] Dependent widget HTML was explicitly rebuilt and tested before declaring it current.
- [ ] Dataset and widget version histories were updated **independently**.
- [ ] Git commits/tags and archival ZIPs exist for rollback.

---

## Primary documentation inside the release

For authoritative details, consult `Shared_Taxa_v1.0/README.md`, `MIGRATION_GUIDE.md`, `RECONCILIATION.md`, `RECONCILIATION_REPORT.json`, `VALIDATION_REPORT.json`, `ID_MAPPING.json`, and `manifest.json`. For the inspected launcher, consult `WIDGET_LAUNCHER_v1.7_README.md` and `widget_launcher_v1.7.html` in `atlas_v1.7.zip`.

**Bottom line:** Shared Taxa is the **versioned source of truth**; the Widget Launcher is the **local import, verification and launch dashboard**; independently released widget HTML files are the **actual scientific-data consumers**. Keeping those three responsibilities distinct makes updates auditable and recoverable.
