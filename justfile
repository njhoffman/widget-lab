# Run from any directory with: just --justfile /path/to/widget-lab/justfile
set positional-arguments

python := "python3"

# List available development commands.
default:
    @just --list

# Install Python development dependencies (Chrome, Node.js and feh are separate).
deps:
    "{{ python }}" -m pip install -r requirements-dev.txt

# Build current standalone widgets and the manifest-driven launch page.
build: build-deep-time build-mythology build-brain build-index

# Build Deep Time from its preserved baseline and presentation sources.
build-deep-time:
    "{{ python }}" tools/build_deep_time.py

# Build Mythology from its preserved baseline and verified featured artwork.
build-mythology:
    "{{ python }}" tools/build_mythology.py

# Build Brain from its preserved baseline and presentation sources.
build-brain:
    "{{ python }}" tools/build_brain.py

# Refresh atlas/current.html from registered component sources.
build-index:
    "{{ python }}" tools/build_atlas_index.py

# Audit imported data, artwork, source integrity and inline JavaScript syntax.
verify:
    "{{ python }}" tools/verify_migration.py
    "{{ python }}" tools/verify_atlas.py

# Run the unit and source-preservation suite without launching a browser.
test:
    "{{ python }}" -m unittest discover -s tests -v

# Run audits, unit tests, and release/task/registered-evidence consistency checks.
check: verify test
    "{{ python }}" tools/check_project.py

# Serve only atlas/ on localhost; open http://localhost:8765/current.html.
serve port="8765":
    "{{ python }}" -m http.server "$1" --bind 127.0.0.1 --directory atlas

# Run the full browser matrix; forward options, e.g. --output /tmp/atlas-tests.
browser-test *args:
    "{{ python }}" tools/test_atlas_browser.py "$@"

# Capture comparisons and open in feh; e.g. just compare --widgets brain.
compare *args:
    "{{ python }}" tools/capture_atlas_comparisons.py "$@"
