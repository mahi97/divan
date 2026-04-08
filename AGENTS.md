# AGENTS.md — Divan Template Repository

You are inside `divan`, a workspace template repository. This repo is NOT an
application. It provides standards, scaffolding, and tooling to initialize
sibling projects.

## Read First

1. `docs/overview.md` — what this repo is
2. `docs/workspace-model.md` — how divan relates to projects
3. `docs/standards/agent-standards.md` — canonical rules (source of truth)
4. `PROJECT_INIT_PLAYBOOK.md` — step-by-step initialization guide

## Your Primary Task

If you are here to initialize a project, follow `PROJECT_INIT_PLAYBOOK.md`.

If you are here to modify the template itself, read `docs/standards/` first.

## How to Initialize a Sibling Project

### Option A: Run the script
```bash
python tools/init_project.py --target ../project_name --profile research-python \
  --project-name project_name --owner owner_name
```

### Option B: Follow the playbook
Read `PROJECT_INIT_PLAYBOOK.md` and execute each step.

## Safety Rules

- Never overwrite existing files without `--force` or explicit confirmation.
- Never commit secrets (.env, credentials, keys).
- Never push to remote unless explicitly asked.
- Always dry-run before destructive operations.
- Produce an initialization report after making changes.

## Do Not

- Do not treat this repo as an application.
- Do not add domain-specific code here.
- Do not modify bootstrap files without updating corresponding standards docs.
- Do not remove placeholder syntax (`{{...}}`) from template files.

## Standards Location

All canonical standards live in `docs/standards/`:
- `agent-standards.md` — agent behavior rules
- `coding-standards.md` — code style and practices
- `documentation-standards.md` — what docs are required
- `research-workflow.md` — experiment and research conventions
- `project-lifecycle.md` — how projects are created and maintained

## After Making Changes

Produce a report:
```
## Report
- Action: [what you did]
- Files created: [count]
- Files modified: [count]
- Files skipped: [count]
- Warnings: [any issues]
```
