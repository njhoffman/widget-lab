# Widget Lab

A private Git monorepo for standalone **Atlas Widgets**, **Quiz Widgets**, and versioned **Shared Taxa**. Migration scaffold only: **sources and release versions are NOT considered imported or verified** until you inspect them.

Start with [docs/migration/MANUAL_STEPS.md](docs/migration/MANUAL_STEPS.md), then fill `incoming/` according to its folder map and run `import-files`. This project separates source code and scientific data (Git), private user progress (future cloud backend), and discussion archives (private local storage).

Key locations:
- `atlas/widgets/*/src/` and `quiz/widgets/*/src/`: implementation files
- `atlas/specs/` and `quiz/specs/`: reviewed feature specifications
- `shared/taxa/`: verified Shared Taxa source
- `docs/context/`: reviewed, committed summaries of conversations
- `docs/decisions/`: approved architectural and UI decisions
- `docs/architecture/`: proposed PWA/cloud/offline architecture
- `docs/handoffs/`: Codex task reports
- `AGENTS.md`: persistent implementation instructions
- `project_manifest.json`: component registry; version fields initially null

Private `incoming/` and `.local/` are **intentionally ignored** by Git. Never push raw ChatGPT exports or files containing account information.
