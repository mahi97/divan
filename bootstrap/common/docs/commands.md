# Commands — {{PROJECT_NAME}}

All commands run from the project root.

## Setup

```bash
uv sync --extra dev
# Add profile extras as needed, for example:
uv sync --extra dev --extra ml
```

## Test

```bash
uv run pytest
# or
scripts/test.sh
```

## Lint

```bash
uv run ruff check .
# or
scripts/lint.sh
```

## Format

```bash
uv run ruff format .
```

## Check All

```bash
scripts/check.sh
```
