# Commands — {{PROJECT_NAME}}

All commands are run from the project root.

## Setup

```bash
uv sync --extra dev
```

## Run

```bash
uv run python -m {{PROJECT_NAME}}
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

## Check (lint + test)

```bash
scripts/check.sh
```

## Build

```bash
uv run python -m build
```
