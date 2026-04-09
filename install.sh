#!/usr/bin/env bash
set -euo pipefail

# ═══════════════════════════════════════════════════════════════════════════════
# Divan remote installer
# Usage: curl -fsSL https://raw.githubusercontent.com/mahi97/divan/main/install.sh | bash
# ═══════════════════════════════════════════════════════════════════════════════

DIVAN_HOME="${DIVAN_HOME:-${HOME}/.divan}"
BIN_DIR="${BIN_DIR:-${HOME}/.local/bin}"

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'
BLUE='\033[0;34m'; CYAN='\033[0;36m'; BOLD='\033[1m'; DIM='\033[2m'; NC='\033[0m'

echo -e "${BOLD}${CYAN}"
echo "  ╺━┓╻╻ ╻┏━┓┏┓╻"
echo "  ┏━╸┃┃┗┛┃┣━┫┃┗┫   Claude Code Super Collection"
echo "  ╺━╸╹╹  ╹╹ ╹╹ ╹   Installer"
echo -e "${NC}"

# Check dependencies
for cmd in git jq; do
  if ! command -v "$cmd" &>/dev/null; then
    echo -e "${RED}Error:${NC} ${cmd} is required. Install it first."
    exit 1
  fi
done

# Clone or update
if [[ -d "$DIVAN_HOME" ]]; then
  echo -e "${BLUE}>>>${NC} Updating existing install at ${DIVAN_HOME}..."
  git -C "$DIVAN_HOME" pull --ff-only 2>/dev/null || {
    echo -e "${YELLOW} !${NC} Pull failed. Removing and re-cloning..."
    rm -rf "$DIVAN_HOME"
    git clone --depth 1 https://github.com/mahi97/divan.git "$DIVAN_HOME"
  }
else
  echo -e "${BLUE}>>>${NC} Cloning divan to ${DIVAN_HOME}..."
  git clone --depth 1 https://github.com/mahi97/divan.git "$DIVAN_HOME"
fi

# Run divan install from the clone
exec "${DIVAN_HOME}/divan" install --bin-dir "$BIN_DIR" --divan-home "$DIVAN_HOME"
