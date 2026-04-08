# Commands — {{PROJECT_NAME}}

All commands run from the project root.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\Activate.ps1   # Windows
pip install -e ".[dev]"
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

## Check All

```bash
scripts/check.sh
```
