# Coding Standards

These standards apply to all projects in this workspace. They are intentionally
opinionated to reduce decision fatigue.

---

## Python

### Style
- Follow PEP 8. Use a formatter (ruff format, black) to enforce it.
- Line length: 88 characters (ruff/black default).
- Use double quotes for strings unless single quotes avoid escaping.

### Type Hints
- Use type hints on all public functions.
- Use `from __future__ import annotations` for forward references.
- Prefer `pathlib.Path` over `os.path` for file operations.
- Prefer `str | None` over `Optional[str]` (Python 3.10+).

### Imports
- Group imports: stdlib, third-party, local — separated by blank lines.
- Use absolute imports. Avoid relative imports except within a package.
- Do not use wildcard imports (`from x import *`).

### Functions
- Keep functions under 40 lines where practical.
- One function, one purpose.
- Prefer returning values over mutating arguments.
- Use `*` to force keyword-only arguments for functions with 3+ parameters.

### Error Handling
- Catch specific exceptions, not bare `except`.
- Let unexpected errors propagate — do not silence them.
- Use `raise ... from err` to preserve exception chains.

### Dependencies
- Minimize external dependencies. Prefer stdlib.
- Manage environments and lockfiles with `uv`.
- Keep dependency declarations in `pyproject.toml`.
- Pin exact versions in lock files, use compatible ranges in `pyproject.toml`.
- Evaluate maintenance status before adding a new dependency.

---

## Shell Scripts

- Use `#!/usr/bin/env bash` as shebang.
- Set `set -euo pipefail` at the top of every script.
- Quote all variable expansions: `"$var"`, not `$var`.
- Prefer long option flags: `--recursive` over `-r`.

---

## General

### Naming
- Files: `snake_case.py`, `kebab-case.sh`, `PascalCase` for classes.
- Variables/functions: `snake_case` in Python, `camelCase` in JS/TS.
- Constants: `UPPER_SNAKE_CASE`.

### Comments
- Do not add comments that restate the code.
- Add comments for non-obvious decisions, workarounds, or external constraints.
- Use `TODO(name):` for planned work. Use `HACK:` for intentional workarounds.
- Never leave commented-out code. Delete it — git has history.

### Testing
- Follow test-driven development when adding features or fixing bugs: start with a failing test or regression case.
- Test files live in `tests/` and mirror the source tree.
- Name test files `test_<module>.py`.
- Name test functions `test_<behavior>`, not `test_<method_name>`.
- One assertion per test is ideal; a few related assertions are acceptable.
- Prefer real implementations over mocks unless external services are involved.
