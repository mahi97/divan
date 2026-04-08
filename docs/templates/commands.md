# Commands — {{PROJECT_NAME}}

All commands are run from the project root.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\Activate.ps1   # Windows
pip install -e ".[dev]"
```

## Run

```bash
python -m {{PROJECT_NAME}}
```

## Test

```bash
pytest
# or
scripts/test.sh
```

## Lint

```bash
ruff check .
# or
scripts/lint.sh
```

## Format

```bash
ruff format .
```

## Check (lint + test)

```bash
scripts/check.sh
```

## Build

```bash
python -m build
```
