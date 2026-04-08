#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

if command -v ruff &> /dev/null; then
  ruff check "$@" .
else
  echo "ruff not found. Install with: pip install ruff"
  exit 1
fi
