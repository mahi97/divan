# Project Initialization Playbook

Step-by-step guide for AI agents. Follow exactly.

---

## Context

You are inside `divan/` which is a subdirectory of the target project.
The parent directory (`../`) is the project you are initializing.

## Step 1: Confirm Location

```bash
ls ../  # Should be the project root
ls ./bootstrap/common/  # Should exist (you're in divan/)
```

If not in divan/, navigate there first.

## Step 2: Determine Mode

- **New project** (parent is empty or nearly empty): proceed normally.
- **Existing project** (parent has code): use RETROFIT rules — do not
  overwrite existing files.

## Step 3: Choose Profile

| Profile          | When to use                              |
|------------------|------------------------------------------|
| `base`           | General project, unknown type            |
| `ml-research`    | ML experiments, training, benchmarks     |
| `llm-research`   | LLM work — prompts, evals, models       |
| `general-python` | Python package or application            |

Default: `ml-research`

## Step 4: Run Init

### Option A: Script
```bash
bash init.sh --profile ml-research
```

### Option B: Manual

Copy all files from `bootstrap/common/` to `../`, preserving structure:
```bash
cp -rn bootstrap/common/. ../
```

Then copy profile overlay (skip profile's README.md):
```bash
# For ml-research:
cp -rn bootstrap/profiles/ml-research/. ../
```

**RETROFIT RULE:** If a file already exists in `../`, DO NOT overwrite.
Skip it and note it in your report.

## Step 5: Replace Placeholders

In every file copied to `../`, replace:

| Placeholder            | Value                              |
|------------------------|------------------------------------|
| `{{PROJECT_NAME}}`     | Parent directory name              |
| `{{OWNER}}`            | GitHub username (ask if unknown)   |
| `{{DESCRIPTION}}`      | One-line description (ask or infer)|
| `{{PRIMARY_LANGUAGE}}` | Python (default)                   |
| `{{PYTHON_VERSION}}`   | 3.12 (default, check .python-version) |
| `{{LICENSE}}`          | MIT (default)                      |
| `{{YEAR}}`             | Current year                       |

## Step 6: Verify

- [ ] No `{{…}}` placeholders remain in `../`
- [ ] `../README.md` exists with real content
- [ ] `../AGENTS.md` exists and references `divan/`
- [ ] `../CLAUDE.md` exists and references `divan/`
- [ ] `../docs/architecture.md` exists
- [ ] `../docs/commands.md` exists
- [ ] `../scripts/check.sh` exists
- [ ] `../.gitignore` exists and includes `divan/` entry

## Step 7: Report

```
## Initialization Report
- Target: ../ (parent project)
- Profile: [name]
- Mode: new | retrofit
- Files created: [count]
- Files skipped: [count]
- Placeholders replaced: [list]
- Warnings: [any issues or none]
```

## File Sources

```
bootstrap/common/           → copied to ../
bootstrap/profiles/<name>/  → overlaid on ../
skills/                     → stays in divan/, read by agents on demand
docs/standards/             → stays in divan/, referenced by ../CLAUDE.md
docs/servers/               → stays in divan/, read by deploy skills
```
