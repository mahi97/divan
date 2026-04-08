# Profile: research-python

The most complete profile. Designed for Python-based research projects involving
experiments, papers, notebooks, prototypes, and benchmarks.

## When to Use

- Running ML/statistical experiments
- Writing research papers with code
- Prototyping and benchmarking
- Notebook-heavy exploratory work

## Files Added (on top of common)

```
pyproject.toml      — Python project config with dev dependencies
src/__init__.py     — Package placeholder
tests/test_smoke.py — Smoke test to verify setup works
```

## Conventions

- Source code goes in `src/` (or rename the package after init)
- Experiments are logged in `docs/experiments/`
- Notebooks live in `notebooks/` (create as needed)
- Large data goes in `data/` (gitignored by default)
- Results go in `results/` (gitignored by default)

## Recommended Dev Dependencies

The `pyproject.toml.template` includes:
- pytest — testing
- ruff — linting and formatting
- mypy — type checking

Add domain-specific dependencies (torch, numpy, etc.) as needed.
