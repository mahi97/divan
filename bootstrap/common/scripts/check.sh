#!/usr/bin/env bash
set -euo pipefail

# Run lint and tests in sequence.
# Exit on first failure.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

echo "=== Lint ==="
if command -v uv &> /dev/null; then
  uv run ruff check .
elif command -v ruff &> /dev/null; then
  ruff check .
else
  echo "ruff not found — skipping lint"
fi

echo ""
echo "=== Tests ==="
if command -v uv &> /dev/null; then
  uv run pytest
elif command -v pytest &> /dev/null; then
  pytest
else
  echo "pytest not found — skipping tests"
fi

echo ""
echo "=== All checks passed ==="
