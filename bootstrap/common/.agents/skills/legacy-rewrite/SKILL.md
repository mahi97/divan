# Legacy Rewrite

Safely modernize legacy code while preserving behavior.

## When to Use

- Modernizing old Python patterns
- Replacing deprecated APIs or libraries
- Restructuring code to match current conventions

## Steps

1. Read target code, identify Python version and dependencies
2. Check for existing tests — if missing, write tests FIRST
3. Run tests to confirm baseline
4. Plan changes in small independent steps
5. Apply one category of change at a time
6. Run tests after each change, commit after each pass
7. Verify all tests pass and no new warnings

## Output

Report listing: target, changes made, test results before/after, risks.

## Safety

- Never rewrite without tests. Write tests first.
- Never combine modernization with feature changes.
- Commit after each step for easy rollback.
