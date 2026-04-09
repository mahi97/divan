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

# Symlink
mkdir -p "$BIN_DIR"
ln -sf "${DIVAN_HOME}/divan" "${BIN_DIR}/divan"
echo -e "${GREEN} +${NC} Linked divan → ${BIN_DIR}/divan"

# PATH check
if echo "$PATH" | tr ':' '\n' | grep -qx "$BIN_DIR"; then
  echo -e "${GREEN} +${NC} ${BIN_DIR} is on PATH"
  echo ""
  echo -e "${GREEN}${BOLD}Done!${NC} Run ${BOLD}divan${NC} to get started."
else
  echo -e "${YELLOW} !${NC} ${BIN_DIR} is not on your PATH"
  echo ""

  shell_rc=""
  case "${SHELL:-}" in
    */zsh)  shell_rc="~/.zshrc" ;;
    */bash) shell_rc="~/.bashrc" ;;
    */fish) shell_rc="~/.config/fish/config.fish" ;;
    *)      shell_rc="your shell config" ;;
  esac

  echo "  Add to PATH by running:"
  echo ""
  if [[ "${SHELL:-}" == */fish ]]; then
    echo -e "    ${BOLD}fish_add_path ${BIN_DIR}${NC}"
  else
    echo -e "    ${BOLD}echo 'export PATH=\"${BIN_DIR}:\$PATH\"' >> ${shell_rc}${NC}"
  fi
  echo ""
  echo -e "  Then restart your shell or run: ${BOLD}source ${shell_rc}${NC}"
  echo ""
  echo -e "${GREEN}${BOLD}Done!${NC} After updating PATH, run ${BOLD}divan${NC} to get started."
fi

echo ""
echo -e "${DIM}Quick start:${NC}"
echo -e "  divan profiles             ${DIM}# see available profiles${NC}"
echo -e "  divan init --profile web   ${DIM}# init a web project${NC}"
echo -e "  divan init                 ${DIM}# interactive picker${NC}"
echo ""
