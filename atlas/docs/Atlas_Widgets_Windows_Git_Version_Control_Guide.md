# Atlas Widgets — Local Version Control and Backup on Windows

For the **Atlas Widgets** project, I recommend using **GitHub Desktop on Windows**. It provides Git version control through a graphical interface, so you can track changes between versions, restore earlier releases, and optionally back up your work to a private GitHub repository.

## 1. Install GitHub Desktop

**GitHub Desktop** is free and runs on Windows.

- Download: [desktop.github.com](https://desktop.github.com/)
- You can start using Git locally without uploading anything online.
- GitHub Desktop lets you review changes, create commits, and manage release tags without memorizing command-line instructions.

## 2. Create your local Atlas Widgets repository

1. Open **GitHub Desktop**.
2. Choose **File → New repository**.
3. Set the repository name to `Atlas-Widgets`.
4. Set the local path to `C:\Projects` (create this folder if necessary).
5. Check **Initialize this repository with a README**.
6. Click **Create repository**.

Your new project folder will be:

```text
C:\Projects\Atlas-Widgets\
```

Git maintains a hidden `.git` directory inside that folder containing your local version history. **Do not delete or manually edit `.git`.**

## 3. Organize your Atlas Widgets files

Recommended folder structure:

```text
Atlas-Widgets/
├── widgets/
│   ├── deep-time/
│   ├── tree-of-life/
│   ├── brain/
│   ├── muscle/
│   ├── mythology/
│   └── emergence/
├── launchers/
├── shared-taxa/
├── docs/
├── releases/
├── source-exports/
└── README.md
```

| Folder or file | Purpose |
|---|---|
| `widgets/` | Current standalone atlas HTML and JavaScript files |
| `launchers/` | Widget Launcher and, optionally, Quiz Launcher |
| `shared-taxa/` | Canonical JSON data, schemas, migration guides, and validation reports |
| `docs/` | Master specifications, design comparisons, and changelogs |
| `releases/` | Selected finished release ZIP files |
| `source-exports/` | Original unreconciled Tree of Life and Deep Time inputs |
| `README.md` | Project overview and release index |

Keep **working files** in individual folders. For example:

```text
widgets/brain/brain_atlas.html
```

You can reuse the same working filename across releases and update the widget's **internal version number**. Git will retain the earlier content in its history.

You can also save distributed ZIPs in `releases/`, but avoid storing every very large generated archive in ordinary Git history. Use a separate archive backup or Git LFS when appropriate.

## 4. Save your first version

After copying the current Atlas Widgets files into your new folder:

1. Return to **GitHub Desktop**.
2. Open the **Changes** tab to review the files Git detected.
3. Enter a commit summary such as:

   ```text
   Initial Atlas Widgets archive — October 2026
   ```

4. Click **Commit to main**.

A **commit** is a saved checkpoint in the project's history. It records the files' contents at that point so you can compare or recover previous versions.

## 5. Record each widget release independently

For example, suppose you update **Brain Atlas from v1.11 to v1.12**.

| Step | Action |
|---|---|
| 1 | Download the new HTML or ZIP generated in ChatGPT. |
| 2 | Replace `widgets/brain/brain_atlas.html` with the new version. |
| 3 | Review the differences under **Changes** in GitHub Desktop. |
| 4 | Commit with a message such as `Brain Atlas v1.12 — UI refinements`. |
| 5 | Create a Git tag named `brain-atlas-v1.12`. |
| 6 | Push to your private GitHub backup, if configured. |

### Git tags for independent widget versions

**Git tags** label particular commits so you can locate important releases. This works even when all the widgets share one Git repository.

In GitHub Desktop, open **History**, right-click the appropriate commit, and select **Create Tag**.

Illustrative tag names (create only the ones corresponding to releases actually in your repository):

```text
deep-time-v1.8
tree-of-life-v1.9
brain-atlas-v1.11
muscle-atlas-v1.3
shared-taxa-v1.0
widget-launcher-v1.8
```

Each atlas and dataset can therefore retain its **independent version history**.

## 6. Set up an additional backup

Local Git provides version history, **but it does not protect against losing the entire computer or drive**.

### Private GitHub repository

1. In GitHub Desktop, click **Publish repository**.
2. Enable **Keep this code private**.
3. Click **Publish Repository**.
4. After future commits, use **Push origin** to send them to the private online repository.

A private GitHub repository is an additional copy, not a replacement for all backups. Ordinary GitHub repositories also have file-size limits (files over 100 MiB are blocked); store oversized archives separately or use Git LFS where appropriate.

### External-drive backup

Periodically copy the entire directory to an external drive:

```text
C:\Projects\Atlas-Widgets\
```

Include hidden files so the **`.git` directory** is copied as well. This preserves the local version history alongside the source files.

## 7. Recover an older version

Suppose a Brain Atlas update accidentally removes a feature.

1. Open the repository in **GitHub Desktop**.
2. Select the **History** tab.
3. Locate the commit that introduced the unwanted change.
4. Right-click it and choose **Revert Changes in Commit**.

GitHub Desktop creates a new commit reversing that commit's changes, while retaining the earlier history. Review the proposed reversal before committing, especially if the original commit changed several widgets.

If you need to inspect or retrieve a specific *older version* rather than reverse a later change, use the relevant commit or release tag to locate it.

## 8. Recommended ongoing workflow

```text
ChatGPT — Atlas Widgets Master Development
        |
        v
Generate and validate an updated widget
        |
        v
Save the new working files in Windows
        |
        v
GitHub Desktop: review changes → commit → tag release
        |
        v
Push to private GitHub repository
        |
        v
Periodically copy repository to external drive
```

**The main habit:** Make a commit for every completed, validated release. This creates a reliable checkpoint even if a later update accidentally breaks the interface or alters scientific data.

## 9. Suggested project-specific release checklist

- [ ] Confirm the widget loads and its interactive features work.
- [ ] Confirm existing scientific data and Shared Taxa compatibility are preserved.
- [ ] Update the widget's independent version, release date, and changelog.
- [ ] Save the latest working HTML, JSON, and documentation in the corresponding folders.
- [ ] Review changes in GitHub Desktop.
- [ ] Commit the verified release with a descriptive message.
- [ ] Create a unique release tag, such as `brain-atlas-v1.12`.
- [ ] Push to the private remote repository (if enabled).
- [ ] Periodically make an external backup of the complete repository.

## Useful links

- [GitHub Desktop](https://desktop.github.com/)
- [GitHub Desktop documentation](https://docs.github.com/en/desktop)
- [About GitHub file-size limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)

---

*Prepared for the Atlas Widgets project. This guide describes a recommended workflow rather than an automatically configured backup.*
