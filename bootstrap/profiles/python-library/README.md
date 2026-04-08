# Profile: python-library

For reusable Python packages intended to be installed via pip.

## When to Use

- Building a library or SDK
- Creating a CLI tool
- Publishing to PyPI or a private index

## Files Added (on top of common)

This profile is a lightweight overlay. It primarily sets conventions — most
library-specific config should be customized after initialization.

## Conventions

- Package code goes in `src/<package_name>/`
- Use `pyproject.toml` for all metadata (no `setup.py`)
- Include a `py.typed` marker for type-checked packages
- Write a `CHANGELOG.md` for release notes
- Use semantic versioning

## Recommended Structure After Init

```
my_library/
  src/
    my_library/
      __init__.py
      py.typed
  tests/
  docs/
  CHANGELOG.md
  pyproject.toml
```

## Publishing Checklist

- [ ] Version bumped in pyproject.toml
- [ ] CHANGELOG.md updated
- [ ] All tests pass
- [ ] `python -m build` succeeds
- [ ] `twine check dist/*` passes
