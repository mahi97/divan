---
name: legacy-rewrite
description: Safely modernize legacy research code while preserving behavior
---

# Legacy Rewrite

## When to Use

- Modernizing old Python code (Python 2 patterns, outdated APIs)
- Cleaning up research code for publication or reuse
- Restructuring a messy prototype into maintainable code

## Inputs

- Target file or directory to modernize
- Specific goals (optional)

## Steps

1. **Assess current state:**
   - Read the target code
   - Identify Python version and patterns used
   - Note existing tests

2. **Write tests first:**
   - If tests are missing, STOP and write tests
   - Tests must capture current behavior before any changes
   - Run tests to confirm they pass

3. **Plan changes:**
   Common modernizations for research code:
   - Replace `os.path` with `pathlib`
   - Add type hints to public functions
   - Replace `.format()` with f-strings
   - Replace `argparse` spaghetti with config files
   - Extract hardcoded values to configs
   - Split monolithic scripts into modules
   - Add proper error handling for data loading

4. **Apply incrementally:**
   - One category of change per commit
   - Run tests after each change
   - Commit after each passing step

5. **Verify:**
   - All tests pass
   - Linter passes
   - Behavior is preserved (run an experiment with known results)

## Output

```
## Legacy Rewrite Report
- Target: src/old_train.py
- Changes: pathlib migration (12 lines), type hints (8 functions), f-strings (15)
- Tests: 10 passing before, 10 passing after
- Behavior: verified with experiment 0001 config
```

## Safety

- NEVER rewrite without tests
- NEVER combine modernization with feature changes
- If refactor changes behavior, stop and confirm
- Commit after each step for easy rollback
- For research code: verify a known experiment still reproduces
