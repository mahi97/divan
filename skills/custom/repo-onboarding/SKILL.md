---
name: repo-onboarding
description: Quickly understand an existing codebase's structure and conventions
---

# Repo Onboarding

## When to Use

- First time working on a project
- A new contributor asks "how does this project work?"
- You need to orient yourself before making changes

## Inputs

- The project root directory (usually `../` from divan)

## Steps

1. **Read core docs:**
   - `README.md` — purpose and setup
   - `docs/architecture.md` — system design
   - `docs/commands.md` — developer commands
   - `CLAUDE.md` or `AGENTS.md` — agent-specific context

2. **Scan project structure:**
   - List top-level directories and their purpose
   - Identify source directory (`src/` or package name)
   - Identify test directory
   - Note config files (pyproject.toml, configs/, etc.)

3. **Identify key files:**
   - Entry point (train.py, main.py, app.py)
   - Model definition (if ML project)
   - Data loading code
   - Config handling

4. **Check project health:**
   - Are tests present? Run `scripts/test.sh`
   - Is lint configured? Run `scripts/lint.sh`
   - Are there recent experiments in `docs/experiments/`?
   - Is there a paper in `paper/`?

5. **Understand compute setup:**
   - Check `divan/docs/servers/` for server access
   - Check for PBS job scripts in `scripts/jobs/`
   - Check for deployment configs

## Output

```
## Onboarding Summary — {{PROJECT_NAME}}

### Purpose
One-line description.

### Structure
- src/ — source code (X modules)
- tests/ — tests (Y test files)
- configs/ — experiment configs
- docs/ — documentation

### Key Files
- Entry point: src/train.py
- Model: src/model.py
- Data: src/data.py
- Config: configs/base.yaml

### Commands
1. Setup: pip install -e ".[dev]"
2. Test: scripts/test.sh
3. Train: python src/train.py --config configs/base.yaml

### Health
- Tests: [pass/fail/missing]
- Lint: [pass/fail/missing]
- Recent experiments: [count or none]
- Paper: [exists/missing]
```

## Safety

- Read-only skill. Do not modify files.
- If docs are missing, note it but do not create them here.
