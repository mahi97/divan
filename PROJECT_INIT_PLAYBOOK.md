# Project Initialization Playbook

This is a step-by-step guide for AI agents. Follow it exactly.

---

## Prerequisites

- You are working inside a target project directory (e.g., `../project_1`).
- The divan template repo is a sibling (e.g., `../divan`).
- You know the project name, owner, and desired profile.

## Step 1: Locate Divan

```bash
ls ../divan/PROJECT_INIT_PLAYBOOK.md
```

If this file does not exist, ask the operator where the template repo is.

## Step 2: Read Standards

Read these files (in order):
1. `../divan/docs/standards/agent-standards.md`
2. `../divan/docs/standards/documentation-standards.md`

## Step 3: Choose Mode

- **New project (empty directory):** proceed to Step 4.
- **Existing project (has code):** proceed to Step 4 but use RETROFIT rules in
  Step 5.

## Step 4: Choose Profile

| Profile            | When to use                              |
|--------------------|------------------------------------------|
| `base`             | General project, unknown type            |
| `research-python`  | Experiments, papers, benchmarks          |
| `python-library`   | Reusable pip-installable package         |
| `llm-research`     | LLM/ML work with models and GPUs        |

If unsure, use `base`.

## Step 5: Copy Files

### 5a: Common files

Copy all files from `../divan/bootstrap/common/` into the project root,
preserving directory structure.

**RETROFIT RULE:** If a file already exists in the target, DO NOT overwrite it.
Skip it and record it in your report.

### 5b: Profile overlay

Copy files from `../divan/bootstrap/profiles/<chosen-profile>/` into the
project root, preserving directory structure. Skip `README.md` in the profile
directory (it documents the profile, not the project).

**RETROFIT RULE:** Same as 5a — do not overwrite existing files.

## Step 6: Replace Placeholders

In every file you copied, replace:

| Placeholder            | Value                                   |
|------------------------|-----------------------------------------|
| `{{PROJECT_NAME}}`     | The project directory name              |
| `{{OWNER}}`            | The GitHub org or username              |
| `{{DESCRIPTION}}`      | One-line project description            |
| `{{PRIMARY_LANGUAGE}}` | Main language (default: Python)         |
| `{{PYTHON_VERSION}}`   | Python version (default: 3.12)         |
| `{{LICENSE}}`          | License type (default: MIT)            |
| `{{YEAR}}`             | Current year                           |

Ask the operator for values you cannot infer.

## Step 7: Verify

Check that:
- [ ] No `{{…}}` placeholders remain in any copied file
- [ ] `README.md` exists and has real content
- [ ] `docs/architecture.md` exists
- [ ] `docs/commands.md` exists
- [ ] `scripts/check.sh` exists and is executable
- [ ] `.gitignore` exists

## Step 8: Report

Produce this report:

```
## Initialization Report
- Target: <path>
- Profile: <name>
- Mode: new | retrofit
- Files created: <count>
- Files skipped (already exist): <count>
- Placeholders replaced: <list>
- Warnings: <any issues or none>
```

## Quick Reference: File Sources

```
bootstrap/common/           → copied to every project
bootstrap/profiles/<name>/  → overlaid on top of common
docs/templates/             → human-readable reference (not copied by script)
docs/standards/             → read for reference (not copied)
```
