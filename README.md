# Widget Lab

Standalone Atlas and Quiz widgets, scientific data, and reviewed specifications managed in Git. **Atlas is the current priority.** Deep Time 1.19.0, Mythology 1.14.0, and Brain 1.22.0 now have goal-directed visual updates; other builds and the imported v1.21 dashboard are preserved. Quiz remains an unverified scaffold.

From the repository root, start Atlas with:

```sh
just serve
```

Run `just` to list commands, `just build` to rebuild current standalone widgets and the launch page, and `just check` for audits, unit tests, and project consistency. Install [just](https://github.com/casey/just) separately; direct Python commands remain available in [developer tooling](tools/README.md). `just deps` installs Python development dependencies into your active environment. Override the interpreter with `just python=/path/to/venv/bin/python check`.

Open <http://localhost:8765/current.html> for current builds. The [original master dashboard](atlas/index.html) remains available at <http://localhost:8765/> with the artwork tools and goal tracker. Serving only `atlas/` keeps private migration folders outside the web root. Browser storage is origin-specific: use a stable port and export existing decisions before changing origins. No cloud deployment or progress synchronization is configured.

The visual direction is [goal_1.png](atlas/images/goal_1.png) and [goal_2.png](atlas/images/goal_2.png). Read the [Atlas context](docs/context/atlas_master.md), [visual specification](atlas/specs/visual-direction.md), and [latest handoff](docs/handoffs/latest.md) before making changes. The pictures define direction; their sample versions, counts, and anatomical imagery are not verified application data.

Verified imported source identities are recorded in [project_manifest.json](project_manifest.json). The seven original widget HTML files remain in `atlas/widgets/` with their delivered names and layout so existing paths work. Deep Time, Mythology and Brain presentation sources live in their component `src/` folders; build standalone HTML with `python3 tools/build_deep_time.py`, `python3 tools/build_mythology.py`, or `python3 tools/build_brain.py`. Other component `src/` placeholders remain empty. `python3 tools/build_atlas_index.py` refreshes the current-build launch page from the manifest. Historical changelogs remain embedded in the original HTML and in `atlas/docs/`.

Repository version is in [VERSION](VERSION); dated changes are in [CHANGELOG.md](CHANGELOG.md). Releases use annotated `vX.Y.Z` GitHub tags. The [live TODO](TODO.md) tracks categories, priorities, acceptance criteria, issues, and proposed suggestions. See the [batch workflow](docs/development-workflow.md) for task/spec synchronization and authorized commit/tag/push behavior.

Every Atlas update produces fresh browser actual-versus-goal comparison images with completed/pending sidebars and automatically opens them with `feh`. Initial captures for all seven components are in the [visual review](docs/visual-reviews/0.1.0/index.html). Run `python3 tools/capture_atlas_comparisons.py --widgets deep-time brain mythology` for an affected batch; advance VERSION first so earlier evidence is preserved.

Install check/capture dependencies with `python3 -m pip install -r requirements-dev.txt`. Chrome/Chromium and `feh` are also needed for the visual workflow.

Run checks from the repository root:

```sh
python3 tools/verify_migration.py
python3 tools/verify_atlas.py
python3 tools/check_project.py
python3 -m unittest discover -s tests -v
```

Run `just artwork-test` for exhaustive Deep Time/Mythology offline image coverage and embedded/adjacent byte parity; the [0.4.2 report](docs/artwork-tests/0.4.2/README.md) verifies all 535 indexed IDs and 1,070 images.

Run `python3 tools/test_atlas_browser.py` for the real-input Chrome regression matrix across Deep Time, Brain, and Mythology at 390/768/1440px. The [0.4.2 results](docs/browser-tests/0.4.2/README.md) pass all 45 scenario checks, including the three primary widgets’ presentation assertions, and retain selected-state screenshots. Project checks reject incomplete matrices or reports for outdated source hashes. Storage, Windows, full accessibility, and scientific reviews remain separate.

Python 3.9+, Node.js, and Python `jsonschema` are needed for all checks. Without `jsonschema` or Node, the respective audit reports incomplete validation and exits nonzero. These tools check file integrity, schemas, source identity, and JavaScript syntax. Interactive browser, accessibility, folder-picker, persistence, and scientific review remain separate work.

`shared/taxa/` is the canonical imported Shared Taxa v1.0 package. The identical delivered copy in `atlas/data/Shared_Taxa_v1.0/` is preserved for the original dashboard's links. Do not edit either published dataset in place or change stable IDs. Distribution ZIPs remain in ignored `incoming/`; original dashboard package-download actions are unavailable until packaging is implemented. Two small original source ZIPs are retained as manifest checksum evidence.

`incoming/` and `.local/` remain ignored. The user authorized inspecting relevant migration artifacts and curating project context in this session; raw chats, account exports, and personal progress must stay private. The user authorizes committing, annotated tagging, and pushing completed validated batches. Source deletion, deployment, and publishing GitHub Releases still require separate instruction.
