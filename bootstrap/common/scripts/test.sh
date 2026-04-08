#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

if command -v uv &> /dev/null; then
  uv run pytest "$@"
elif command -v pytest &> /dev/null; then
  pytest "$@"
else
  echo "pytest not found. Install with: uv sync --extra dev"
  exit 1
fi
