# CLAUDE.md — Divan Template Repository

This is `divan`, a workspace template repository. Not an application.
It provides standards, scaffolding, and initialization tooling for sibling projects.

## Quick Orientation

- `docs/standards/agent-standards.md` — canonical rules (read this first)
- `PROJECT_INIT_PLAYBOOK.md` — step-by-step project initialization
- `bootstrap/common/` — files copied to every target project
- `bootstrap/profiles/` — optional overlays by project type
- `tools/init_project.py` — automated initializer

## Common Tasks

### Initialize a new project
```bash
python tools/init_project.py --target ../my_project --profile research-python \
  --project-name my_project --owner myorg
```

### Validate the template
```bash
python tools/validate_template.py
```

### Initialize manually
Follow `PROJECT_INIT_PLAYBOOK.md` step by step.

## Rules

- Never overwrite files without `--force` or user confirmation
- Never commit secrets
- Never push without being asked
- Always replace all `{{PLACEHOLDER}}` tokens when initializing
- Dry-run first for bulk operations
- Produce a short report after any significant changes

## Placeholders

Template files use: `{{PROJECT_NAME}}`, `{{OWNER}}`, `{{DESCRIPTION}}`,
`{{PRIMARY_LANGUAGE}}`, `{{PYTHON_VERSION}}`, `{{LICENSE}}`, `{{YEAR}}`

## What Not to Do

- Don't add application code to this repo
- Don't modify bootstrap templates without updating docs/standards/
- Don't strip `{{…}}` placeholders from template files
- Don't restructure existing target projects during initialization

## Project Structure

```
divan/
  docs/standards/          # Canonical standards (source of truth)
  docs/templates/          # Human-readable document templates
  bootstrap/common/        # Files for every project
  bootstrap/profiles/      # Project-type overlays
  tools/                   # Init and validation scripts
  examples/                # Reference layouts
```
