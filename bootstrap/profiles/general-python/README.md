# Profile: general-python

Generic Python package or application — pip-installable, with standard tooling.

## When to Use

- Building a reusable Python library
- Creating a CLI tool
- A Python application that is not ML-research-focused

## Files Added (on top of common)

```
pyproject.toml      — Python project config
src/__init__.py     — Package placeholder
tests/test_smoke.py — Basic smoke test
```

## Conventions

- Source code in `src/<package_name>/`
- Use `uv` with `pyproject.toml` for dependency management and command execution
- Follow test-driven development by default
- Semantic versioning
- CHANGELOG.md for release notes (create manually)
