# Template Usage Guide

Divan supports multiple usage modes depending on your situation and preferences.

---

## Mode 1: Script-Based Initialization

The fastest way. Run the initializer with your target path and profile.

```bash
# New project
python tools/init_project.py \
  --target ../my_project \
  --profile research-python \
  --project-name my_project \
  --owner myorg

# Preview first
python tools/init_project.py \
  --target ../my_project \
  --profile research-python \
  --project-name my_project \
  --owner myorg \
  --dry-run
```

### Flags

| Flag              | Description                                     |
|-------------------|-------------------------------------------------|
| `--target`        | Path to target project directory                 |
| `--profile`       | Profile name: base, research-python, etc.        |
| `--project-name`  | Name for `{{PROJECT_NAME}}` substitution         |
| `--owner`         | Name for `{{OWNER}}` substitution                |
| `--dry-run`       | Show what would happen without making changes    |
| `--force`         | Overwrite existing files                         |
| `--backup`        | Create .bak copies before overwriting            |

---

## Mode 2: Agent-Guided Initialization

Have an AI agent (Claude Code, Codex, etc.) read and follow the playbook.

1. Open the target project in your editor or terminal.
2. Tell the agent: "Read `../divan/PROJECT_INIT_PLAYBOOK.md` and initialize
   this project."
3. The agent will follow the step-by-step instructions, copying and adapting
   files as needed.

This mode is useful when you want the agent to make judgment calls about which
files to skip or adapt.

---

## Mode 3: Manual Copy

For full control, copy files yourself.

1. Copy everything from `bootstrap/common/` into your project root.
2. Copy files from `bootstrap/profiles/<your-profile>/` on top.
3. Search and replace all `{{PLACEHOLDER}}` tokens.
4. Review and adjust each file.

### Placeholder reference

| Placeholder            | Replace with                    |
|------------------------|---------------------------------|
| `{{PROJECT_NAME}}`     | Your project directory name     |
| `{{OWNER}}`            | Your GitHub org or username     |
| `{{DESCRIPTION}}`      | One-line project description    |
| `{{PRIMARY_LANGUAGE}}` | Main language (e.g., Python)    |
| `{{PYTHON_VERSION}}`   | Python version (e.g., 3.12)    |
| `{{LICENSE}}`          | License name (e.g., MIT)       |
| `{{YEAR}}`             | Current year (e.g., 2026)      |

---

## Mode 4: Retrofit an Existing Repo

For projects that already have code but lack standard structure.

### With the script

```bash
python tools/init_project.py \
  --target ../legacy_project \
  --profile base \
  --project-name legacy_project \
  --owner myorg \
  --backup
```

The script will:
- Skip files that already exist (unless `--force` is used)
- Create backups of overwritten files when `--backup` is used
- Report what was created, skipped, and backed up

### With an agent

Tell the agent:
"Read `../divan/PROJECT_INIT_PLAYBOOK.md`. This is an existing project — use
retrofit mode. Do not restructure existing code. Only add missing standard files."

### Manual retrofit checklist

1. Add `AGENTS.md` and `CLAUDE.md` if missing
2. Add `docs/architecture.md` if missing
3. Add `docs/commands.md` if missing
4. Add `scripts/check.sh`, `scripts/test.sh`, `scripts/lint.sh` if missing
5. Add `.editorconfig` and `.gitattributes` if missing
6. Add `.claude/` and `.agents/` directories if missing
7. Do NOT move or rename existing files
8. Document any deviations in `docs/architecture.md`

---

## Mode 5: Greenfield New Repo

Starting completely from scratch.

```bash
# Create the directory
mkdir ../my_new_project
cd ../my_new_project
git init

# Initialize from divan
python ../divan/tools/init_project.py \
  --target . \
  --profile research-python \
  --project-name my_new_project \
  --owner myorg

# First commit
git add -A
git commit -m "Initialize project from divan template"
```

---

## Choosing a Profile

| Question                                        | Profile           |
|-------------------------------------------------|-------------------|
| Just need standard docs and scripts?            | `base`            |
| Running experiments, writing papers?             | `research-python` |
| Building a reusable Python package?              | `python-library`  |
| Working with LLMs, models, GPUs?                 | `llm-research`    |
| Not sure?                                        | `base`            |

Start with `base` if uncertain. You can always add profile-specific files later.
