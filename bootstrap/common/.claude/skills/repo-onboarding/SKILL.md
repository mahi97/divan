---
name: repo-onboarding
description: Help a new contributor understand this project's structure, conventions, and key files
---

# Repo Onboarding

## When to Use

Use this skill when:
- A new contributor asks "how does this project work?"
- You need to orient yourself in an unfamiliar codebase
- Someone asks for a project walkthrough

## Inputs

- The project root directory (current working directory)

## Steps

1. **Read core docs:**
   - `README.md` — project purpose and setup
   - `docs/architecture.md` — system design
   - `docs/commands.md` — developer commands

2. **Scan project structure:**
   - List top-level directories and their purpose
   - Identify the main source directory
   - Identify the test directory

3. **Identify key files:**
   - Entry point (main.py, app.py, etc.)
   - Configuration files (pyproject.toml, setup.cfg, etc.)
   - CI configuration (.github/workflows/)

4. **Check health:**
   - Are tests present? Do they pass?
   - Is a linter configured?
   - Are there any obvious issues (missing docs, broken imports)?

5. **Produce onboarding summary.**

## Output Format

```
## Onboarding Summary — {{PROJECT_NAME}}

### Purpose
One-line description.

### Structure
- src/ — source code (X modules)
- tests/ — tests (Y test files)
- docs/ — documentation

### Key Files
- Entry point: src/main.py
- Config: pyproject.toml
- CI: .github/workflows/ci.yml

### Getting Started
1. command to setup
2. command to test
3. command to run

### Health Check
- Tests: pass/fail/missing
- Lint: pass/fail/missing
- Docs: complete/incomplete
```

## Safety Notes

- This is a read-only skill. It should not modify any files.
- If docs are missing, note it in the summary but do not create them here.
