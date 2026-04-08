#!/usr/bin/env bash
# init.sh — Initialize the parent project from divan bootstrap files.
#
# Run from anywhere inside a project that contains divan/:
#   cd my_project/divan && bash init.sh
#   cd my_project && bash divan/init.sh
#   bash my_project/divan/init.sh
#
# Options are passed through to tools/init_project.py:
#   --profile ml-research   Profile to use (default: ml-research)
#   --dry-run               Show what would happen
#   --force                 Overwrite existing files
#   --backup                Create .bak copies before overwriting
#   --project-name NAME     Override inferred project name
#   --owner NAME            Set owner placeholder
#   --description TEXT      Set description placeholder
#
# Examples:
#   bash init.sh
#   bash init.sh --profile llm-research
#   bash init.sh --dry-run
#   bash init.sh --force --backup

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Ensure we're running from divan root
if [[ ! -f "$SCRIPT_DIR/tools/init_project.py" ]]; then
  echo "ERROR: Cannot find tools/init_project.py. Are you running from divan/?"
  exit 1
fi

# Require python3
if ! command -v python3 &>/dev/null; then
  echo "ERROR: python3 not found. Please install Python 3.8+."
  exit 1
fi

echo "=== Divan Init ==="
echo "Divan root:    $SCRIPT_DIR"
echo "Target project: $(cd "$SCRIPT_DIR/.." && pwd)"
echo ""

python3 "$SCRIPT_DIR/tools/init_project.py" "$@"

STATUS=$?
if [[ $STATUS -eq 0 ]]; then
  echo ""
  echo "=== Done ==="
  echo "Next steps:"
  echo "  1. Fill in your server details in divan/docs/servers/"
  echo "  2. Create a Python venv: python3 -m venv .venv && source .venv/bin/activate"
  echo "  3. Run: scripts/check.sh"
fi

exit $STATUS
