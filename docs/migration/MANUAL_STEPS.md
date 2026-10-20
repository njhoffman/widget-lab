# Widget Lab migration — manual steps & exact commands

> **Important:** This scaffold intentionally does not download ChatGPT conversations, infer authoritative versions, or push sensitive files. GitHub receives nothing until you run `publish` and explicitly confirm.

## 1. Tools to install (manually)
Install Git and Python 3.9+; install [GitHub CLI](https://cli.github.com/) for remote creation; optionally install Codex CLI (`npm install -g @openai/codex`).

Sign in to GitHub in the terminal: `gh auth login`. Configure author identity as needed: `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`.

## 2. Export ChatGPT history (manually)
In ChatGPT.com, use **Settings → Data controls → Export data → Confirm export**. When ready, download your account export ZIP privately. An export is account-wide and may include sensitive information. The ZIP may contain `conversations.json` or multiple numbered JSON files. It is NOT guaranteed to contain every widget artifact in immediately usable form.

Run from the directory containing `widget_lab_bootstrap.py`:

```bash
python3 widget_lab_bootstrap.py extract-chats ~/Downloads/chatgpt-export.zip ./widget-lab
```

The script creates an **ignored** `.local/chat_index.csv`, `.local/chat_selection.txt` and `.local/chat_review/`. The initial selection terms cover Atlas, Quiz, Shared Taxa, and several master-workspace title patterns. Check the index for missing conversations (e.g., generic titles), edit `.local/chat_selection.txt` with more exact title fragments, and rerun `extract-chats`. Re-exporting may replace private local transcripts with the same identifier; it never writes raw transcripts to tracked docs.

**Manual curation required:** For branching ChatGPT conversations, exported Markdown follows the selected/current message branch when available; inspect the original chat/export for alternative branches you still want to preserve. Read selected private conversations and write concise approved, up-to-date summaries into `docs/context/atlas_master.md`, `docs/context/quiz_master.md`, and `docs/context/shared_taxa.md`. Transfer current authoritative requirements into the appropriate `atlas/specs/*.md` and `quiz/specs/*.md`; preserve decision rationale in `docs/decisions/`. Mark statuses APPROVED only after verification. Resolve conflicting versions/branches against actual source artifacts; no content is automatically accepted as authoritative.

### Recommended extraction from each relevant chat
- Project identity, chat title, date range, and link (if available)
- Last **verified** release and location of source files
- Accepted requirements versus suggestions and abandoned experiments
- UI/layout decisions, scientific/quiz data requirements and identifiers
- Outstanding work and dependencies, compatibility and tests
- Decisions worth preserving and the reason for them

Do not include full personal conversations, credentials, access tokens, student information, or unrelated content in Git. Store raw export outside the repo as an additional backup.

## 3. Download real widget files (manually)
Download authoritative `.html`, `.js`, `.css`, datasets, question banks, images/diagram files, and manifest files from your current Atlas / Quiz master ChatGPT chats, Library, previous ZIP attachments, or existing local folders. Review code branch comparisons first; the newest filename is not proof of a current release. Save your large historical ZIPs and media archives separately; attach releases via GitHub Releases or Git LFS when appropriate, rather than blindly committing big binaries.

Copy files into the **ignored** `incoming/` folders created by `init`. Examples:

```text
incoming/atlas/brain/Brain_Atlas_v1.11.html
incoming/atlas/deep-time/Deep_Time_Atlas_v1.8.html
incoming/atlas/tree-of-life/Tree_of_Life_v1.9.html
incoming/quiz/geologic-time/Geologic_Quiz_v1.2.html
incoming/quiz/launcher/Quiz_Launcher.html
incoming/shared/taxa/manifest.json
incoming/shared/taxa/taxonomy.json
incoming/docs/architecture/widget_lab_git_cloud_offline_architecture_v1.0.md
incoming/app/prototypes/widget_lab_architecture_explorer_v1.0.html
```

You can use any exact filenames. Folders identify the destination; the script **does not guess** scientific authority from file names. If datasets use other source files, keep them within their appropriate incoming folder. Missing filenames in the examples are fine.

## 4. Copy files into tracked locations (automated)

```bash
python3 widget_lab_bootstrap.py import-files ./widget-lab
```

Import routes files to `atlas/widgets/<name>/src/`, `quiz/widgets/<name>/src/`, `shared/taxa/`, `docs/architecture/`, or `app/prototypes/`.

It skips collisions without overwriting and logs SHA-256/size/path to `docs/migration/import_inventory.csv`. Unsupported/oversize files remain in the ignored inbox for review. Do not consider import completion to be release verification.

## 5. Verify and curate before GitHub (manual)

```bash
python3 widget_lab_bootstrap.py status ./widget-lab
cd widget-lab && git status --short
```

Open `project_manifest.json`; fill **only independently verified** release numbers, dates, and matching files. Update the master context files, specifications, release changelogs, and decision records. Decide which media belong in Git, Git LFS, an object-store/CDN, or a GitHub Release. Ensure no passwords, private chat messages, or unrelated attachments have crossed into tracked docs.

**Do not start automatic public/cloud deployments or data synchronization at this stage.** PWA, Supabase auth/data sync, and Cloudflare hosting are future implementation phases documented separately in the architecture plan.

## 6. Create private GitHub repository (explicit opt-in)

```bash
gh auth login
python3 widget_lab_bootstrap.py publish ./widget-lab YOUR_GITHUB_USERNAME/widget-lab
```

This checks authentication, lets you inspect `git status`, asks you to type a confirmation phrase, stages tracked files, commits them, and runs `gh repo create OWNER/REPO --private --source=. --remote=origin --push`. `publish` refuses to overwrite an existing `origin` remote. Nothing is pushed without confirmation; if an error occurs, review `git status` and `git remote -v` before retrying. **Private** is the default by design.

## 7. Day-to-day spec handoff (manual approval)
1. Discuss features in ChatGPT.com. Ask for a spec patch in Markdown plus acceptance criteria.
2. Save it to the corresponding `*/specs/*.md`, initially marked DRAFT, and review/approve it; alternatively hand the patch to Codex CLI for an explicitly reviewed commit/PR.
3. Commit and push the **approved specification**. Regular ChatGPT chat messages do not automatically update Git.
4. Run Codex from repository root, e.g.: `codex "Read AGENTS.md and quiz/specs/tree-of-life.md; implement only APPROVED requirements, run tests, update changelog and docs/handoffs/latest.md; do not commit or push."`
5. Review changed files, tests, manifest and changelog; then commit and push. Use the GitHub ChatGPT connection to inspect pushed updates when connected.

For future near-automatic publishing, add an approved pull-request workflow or Git-writing app. The standard GitHub reader alone is not a write path into this repo.

## 8. Future offline/cloud architecture
Start with a web-first, offline-first PWA. GitHub holds versioned code, public content, specs; devices cache Shared Taxa and frequently used artwork using IndexedDB/Cache API; private progress uses authenticated sync with local outbox/retry/conflict resolution. Consider Cloudflare Workers static hosting, Supabase Auth/Postgres, object storage for heavy artwork, then Tauri/Capacitor only if device features justify wrappers. Git is **not** a per-user progress database.
