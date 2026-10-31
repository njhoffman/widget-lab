# Atlas Widgets — Master Goal Checklist v1.17

This is an interactive presentation update; no scientific/widget goal status has been changed from v1.16. The HTML dashboard is the editable copy.

# Atlas Widgets — Master Goal Checklist v1.10

**Baseline:** Master Development v1.9 (October 16, 2026). **Functional/style review:** Master Development v1.16, October 17, 2026. Original review states inherited unless updated below.

Status reflects v1.9 evidence; **implemented does not imply user approval**. Mockup concepts are not verified scientific data.

## New verified updates (v1.16)

- **T021:** planned → implemented. Indexed representative-life cards actually open the linked taxon profile for the selected interval.
- **T022:** partial → implemented. Five topic tabs are active and use the existing science data; the content remains contextual, not newly researched.
- **T035:** remains partial. Functional region-section shortcuts work, but the goal concept's comprehensive integrated profile still requires design improvements.
- **T047:** planned → partial. Related *figures* have a navigable portrait strip; a source-attributed historic *artwork* carousel is not yet implemented.
- **T008, T009:** remain partial because shared refinements need propagation across Tree of Life, Muscle, Emergence, and Launcher.

**Status totals after new evidence:** 28 implemented, 30 partial, 26 planned (84 goals). Implementation status is not user approval.

## Progress by widget

### Shared UI
10 items — 5 implemented, 5 partial, 0 planned.

| ID | Area | Visual / functional goal | Status | Priority | Acceptance test |
|---|---|---|---|---|---|
| T001 | Header | Retain compact one-line title/subtitle with responsive natural wrap | implemented | P0 | No overlap at 320, 390, 768 and 1440px; badges flow after title |
| T002 | Header | Apply consistent navy gradient with subtle colored subject identity | partial | P1 | Same sizing and palette tokens across all seven components |
| T003 | Header | Match illustrated reference icon scale and clarity | partial | P1 | Icon artwork matched in proportions without image/text distortion |
| T004 | Header | Align version and data chips, equal control heights | implemented | P1 | Equal heights across desktop and narrow layouts |
| T005 | Release history | Preserve historical changelog entries and click-to-expand version control | implemented | P0 | All previous releases accessible; newest open |
| T006 | Dialog | Compact statistics typography and balanced rows | implemented | P0 | Segoe UI/system stack, ~12px rows with compact padding |
| T007 | Dialog | Unify overlay spacing and one-row title/close control | implemented | P1 | No separate header bar; accessible dismiss |
| T008 | Controls | Consolidate hover/active/selected/focus styles and common green stat emphasis | partial | P1 | No gold selected styles in shared controls; keyboard focus visible |
| T009 | Panels | Match reference luminous panel edges and restrained atmospheric fills | partial | P2 | Shared elevation/token system; accessible contrast |
| T010 | QA | Automate regression for header, popup, versions and mobile breakpoints | partial | P0 | Recorded checks plus Windows folder-launch verification |

Evidence reference: Master spec v1.9 + responsive QA.

### Deep Time Atlas
14 items — 6 implemented, 5 partial, 3 planned.

| ID | Area | Visual / functional goal | Status | Priority | Acceptance test |
|---|---|---|---|---|---|
| T011 | Artwork | Resolve image for every indexed Deep Time interval | implemented | P0 | 172/172 IDs resolve without missing images |
| T012 | Assets | Maintain adjacent-folder bundle and single-file offline editions | implemented | P0 | Both work without network; checksums match |
| T013 | Hero | Large interval-specific illustrated hero with text-safe overlay | implemented | P0 | Text remains legible over varied images |
| T014 | Artwork | Replace procedural palette/silhouette variations with bespoke period scenes | partial | P0 | Major intervals have distinct compositions and curated captions |
| T015 | Artwork | Complete 13 flagship scene upgrades in Batch 1 | planned | P0 | 13/13 scientifically reviewed and approved |
| T016 | Header | Place compact view tabs and search alongside header like concept, without crowding | partial | P1 | All controls available, no title overlap, responsive |
| T017 | Hierarchy | Show polished geology thumbnail previews with selected outline | partial | P1 | Period thumb/age text and selected state clear |
| T018 | Hierarchy | Click neighboring intervals to navigate | implemented | P1 | Selection updates text, artwork, breadcrumbs |
| T019 | Info panel | Replace generic sidebar with period-specific icon/fact rows and soft scene background | partial | P1 | Rank, range, duration, previous/next, paleoenvironments and representative life |
| T020 | Paleomaps | Real paleomap/continental reconstruction by geologic interval | planned | P1 | Licensed/source-attributed maps from suitable dated reconstructions |
| T021 | Representative life | Clickable representative organism art and taxon details | implemented | P1 | Click representative life -> canonical taxon profile with evidence |
| T022 | Tabs | Distinct Overview/Climate/Continents/Geology/Life content presentation | implemented | P1 | All tabs interactive and scientifically grounded; no fake datasets |
| T023 | Sources | Track geological data provenance and artwork uncertainty | partial | P0 | Separate facts from illustration and date sources |
| T024 | Gallery | In-atlas artwork gallery with alternative views for interval | planned | P2 | Thumbnails can change hero within same interval |

Evidence reference: 172 entries in asset manifest.

### Brain Atlas
15 items — 3 implemented, 9 partial, 3 planned.

| ID | Area | Visual / functional goal | Status | Priority | Acceptance test |
|---|---|---|---|---|---|
| T025 | Depth | Schematic per-angle depth visualization | implemented | P0 | Toggle on/off adjusts dots and preserves region selection |
| T026 | Depth | Low / medium / high depth strength | implemented | P1 | Visible strength difference for same view |
| T027 | Brain render | Upgrade from schematic to independently verified anatomical render assets | planned | P0 | Licensed open 3D dataset with validated region overlays |
| T028 | Brain render | Create striking sculptural main brain centerpiece with dimensional shadows | partial | P0 | More surface detail without implying voxel-accurate geometry |
| T029 | Regions | Keep existing region dots with exact click targets and view transforms | implemented | P0 | Region selection stable across views/depth |
| T030 | Regions | Bright selected region outlines and location annotation | partial | P1 | Selection spotlight accurate and unclipped |
| T031 | Depth | Near-to-far opacity, size and subtle desaturation cues | partial | P1 | Cues perceptible, accessible, selected item crisp |
| T032 | Views | Additional high-quality lateral/medial/dorsal/ventral view graphics | partial | P0 | Distinct view images registered to projection markers |
| T033 | Anatomy | Correct 3D coordinates/volumetric mesh for depth and structures | planned | P0 | Cited anatomical source, verified geometry, no approximated depth claims |
| T034 | Detail panel | Show large selected-region name with functional/evolution tags | partial | P1 | Readable selected region summary tied to live region |
| T035 | Profiles | Tabs for evolutionary history / function & circuits / clinical relevance | partial | P1 | Each tab displays sourced, relevant content |
| T036 | Neurochemistry | Region-specific neurotransmitters and mechanisms | partial | P2 | No generic transmitter lists presented as locality proof |
| T037 | Sidebar | Current view inset with selected structure accurately indicated | partial | P1 | Inset updates with angle and selection |
| T038 | Terminology | Show evolutionary dates with scientific uncertainty | partial | P0 | No fabricated age for unique brain region |
| T039 | QA | Verify marker alignment and selection at every angle | planned | P0 | All angles and mobile layouts tested |

Evidence reference: Brain v1.20.

### Mythology Atlas
13 items — 6 implemented, 6 partial, 1 planned.

| ID | Area | Visual / functional goal | Status | Priority | Acceptance test |
|---|---|---|---|---|---|
| T040 | Coverage | Provide local illustration for all 363 indexed records | implemented | P0 | 363/363 available offline |
| T041 | Hero | Cinematic selected-figure hero art with readable left-aligned text | partial | P0 | Image/text safe area consistent across traditions |
| T042 | Artwork | Commission/generate distinctive iconography for 33 flagship figures | planned | P0 | 33/33 reviewed and approved by tradition |
| T043 | Views | Preserve switchable family tree and artwork views | implemented | P0 | Selection persists across switches |
| T044 | Navigation | Keep tradition filters, search, genealogy, parent and child navigation | implemented | P0 | No losses after art loading |
| T045 | Results | Figure result thumbnails with selected treatment | implemented | P1 | Works across all five traditions |
| T046 | Info panel | Rich illustrated right-side figure facts, attribution and relations | partial | P1 | Truthful family edges, role, references, provenance |
| T047 | Related artwork | Clickable related-artwork thumbnails/carousel | partial | P1 | Navigate images, display license/source and attribution |
| T048 | Identity | Greek/Roman name toggles with independent traditions | implemented | P0 | No conflation of genealogy |
| T049 | Artwork | Artwork type and historical accuracy provenance visible | partial | P0 | Labels AI illustrative vs public domain historical vs licensed |
| T050 | Palette | Keep shared teal/green active states while letting paintings vary by tradition | implemented | P0 | No gold on shared selected widgets |
| T051 | Overview | Matching pills for lineage, epics, symbols and role | partial | P1 | Clicking chip filters/searches or opens related info |
| T052 | Cross-links | Improve person/entity equivalents, variant myths and sources | partial | P2 | Reference-specific relationships; no invented parentage |

Evidence reference: Mythology manifest v1.9.

### Artwork Studio
12 items — 2 implemented, 3 partial, 7 planned.

| ID | Area | Visual / functional goal | Status | Priority | Acceptance test |
|---|---|---|---|---|---|
| T053 | Library | Search, inspect and filter all 538 image records | implemented | P0 | 172 + 363 + 3 records |
| T054 | Review | Add review status/notes and export decisions JSON | implemented | P0 | Export valid JSON; updates persist where supported |
| T055 | Goal compare | View actual image beside matching goal crop | planned | P0 | Reference/current/assets side-by-side |
| T056 | Quality | Separate featured / standard / fallback / needs replacement | partial | P0 | All records tagged and filtering consistent |
| T057 | Batch | Generate prompt for selected asset from scientific notes | planned | P0 | Prompt links to exact manifest ID |
| T058 | Batch | Copy prompt or export multiple prompts in Markdown/JSON | planned | P0 | Download ready; no API credentials required |
| T059 | Import | Import approved replacement images via user-selected file and validate dimensions | planned | P0 | No silent overwrite; confirmed license and subject |
| T060 | Provenance | Record rights, attribution, source URLs, date and source quality | planned | P0 | Clear license/reuse rights and citation fields |
| T061 | Review | Show fallback/inherited-image chain | planned | P1 | Direct vs inherited transparent |
| T062 | Cards | Improve preview quality, card density, comparison composition | partial | P1 | Readable cards desktop/mobile |
| T063 | Feedback | Persist status changes and import/export decisions across sessions | partial | P0 | Win/Edge test + export/import backup |
| T064 | Queue | Batch status and next-up recommendations | planned | P1 | Queue sortable by tier, source, priority and review status |

Evidence reference: v1.9 Studio and manifest.

### Tree of Life Atlas
3 items — 0 implemented, 0 partial, 3 planned.

| ID | Area | Visual / functional goal | Status | Priority | Acceptance test |
|---|---|---|---|---|---|
| T065 | Expansion | Translate common illustrated-header and story-card language to this widget | planned | P2 | Keep widget-specific visualization and data |
| T066 | Preservation | Preserve existing dataset and interactions while upgrading visual shell | planned | P0 | No regression in current controls |
| T067 | Comparison | Capture new goal reference and actual screenshot at same viewport | planned | P2 | Source goal concept approved before release |

Evidence reference: Goal design direction.

### Muscle Atlas
3 items — 0 implemented, 0 partial, 3 planned.

| ID | Area | Visual / functional goal | Status | Priority | Acceptance test |
|---|---|---|---|---|---|
| T068 | Expansion | Translate common illustrated-header and story-card language to this widget | planned | P2 | Keep widget-specific visualization and data |
| T069 | Preservation | Preserve existing dataset and interactions while upgrading visual shell | planned | P0 | No regression in current controls |
| T070 | Comparison | Capture new goal reference and actual screenshot at same viewport | planned | P2 | Source goal concept approved before release |

Evidence reference: Goal design direction.

### Emergence Atlas
3 items — 0 implemented, 0 partial, 3 planned.

| ID | Area | Visual / functional goal | Status | Priority | Acceptance test |
|---|---|---|---|---|---|
| T071 | Expansion | Translate common illustrated-header and story-card language to this widget | planned | P2 | Keep widget-specific visualization and data |
| T072 | Preservation | Preserve existing dataset and interactions while upgrading visual shell | planned | P0 | No regression in current controls |
| T073 | Comparison | Capture new goal reference and actual screenshot at same viewport | planned | P2 | Source goal concept approved before release |

Evidence reference: Goal design direction.

### Widget Launcher
4 items — 1 implemented, 1 partial, 2 planned.

| ID | Area | Visual / functional goal | Status | Priority | Acceptance test |
|---|---|---|---|---|---|
| T074 | Dashboard | Extend illustrated card gradients and status panel polish | partial | P1 | Same common design without hypothetical metrics |
| T075 | Assets | Support optional external asset manifests and local artwork bundles | planned | P0 | File selection includes dependent image directories or standalone mode |
| T076 | Data | Retain Shared Taxa as nonlaunchable versioned resource | implemented | P0 | Import records hashes and current dependency compatibility |
| T077 | Sync | Regression-test folder sync / imported artwork / IndexedDB in Windows | planned | P0 | Successful refresh and persistence after restart |

Evidence reference: Widget Launcher v1.12.

### Shared Taxa
2 items — 1 implemented, 0 partial, 1 planned.

| ID | Area | Visual / functional goal | Status | Priority | Acceptance test |
|---|---|---|---|---|---|
| T078 | Data | Preserve Shared Taxa v1.0 authoritative dataset unaffected by artwork | implemented | P0 | No scientific data mutations for UI/art updates |
| T079 | Provenance | Link selected taxon from Deep Time representative life view | planned | P1 | Use canonical concept IDs and traceable scientific source |

Evidence reference: Original archive unchanged.

### Goal Tracking Workspace
5 items — 3 implemented, 1 partial, 1 planned.

| ID | Area | Visual / functional goal | Status | Priority | Acceptance test |
|---|---|---|---|---|---|
| T080 | Comparison | Goal image and actual browser screenshot shown side by side | implemented | P0 | Three atlas comparisons in one offline HTML |
| T081 | Checklist | Searchable acceptance-based register with visual/functional axes | implemented | P0 | Filter, edit statuses, export/import decisions |
| T082 | Artwork | Batch 1 prompts keyed to real artwork manifest records | implemented | P0 | 13 intervals, 33 figures, 8 brain render requests |
| T083 | Persistence | Browser-local changes with portable backup and restore | partial | P0 | Export and import round-trip test in Windows Edge |
| T084 | Release QA | Automate fresh screenshot capture and comparison after each release | planned | P1 | Matching viewport, same selected state, repeatable screenshots |

Evidence reference: Goal Board v1.10.
