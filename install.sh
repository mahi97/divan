#!/usr/bin/env bash
set -euo pipefail

# ─── Divan Installer ─────────────────────────────────────────────────────────
# Installs the complete Claude Code stack at user or project level.
#
# Usage:
#   ./install.sh                    # Interactive mode
#   ./install.sh --user             # User-level install (all plugins)
#   ./install.sh --project          # Project-level install (copy configs to cwd)
#   ./install.sh --user --minimal   # Only required plugins
#   ./install.sh --dry-run          # Show what would be installed
#   ./install.sh --uninstall        # Remove divan-managed settings

DIVAN_ROOT="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_DIR="${HOME}/.claude"
SETTINGS_FILE="${CLAUDE_DIR}/settings.json"
BACKUP_DIR="${CLAUDE_DIR}/backups/divan-$(date +%Y%m%d-%H%M%S)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Defaults
MODE=""
MINIMAL=false
DRY_RUN=false
UNINSTALL=false
TARGET_DIR="$(pwd)"

# ─── Parse arguments ─────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case $1 in
    --user)     MODE="user"; shift ;;
    --project)  MODE="project"; shift ;;
    --minimal)  MINIMAL=true; shift ;;
    --dry-run)  DRY_RUN=true; shift ;;
    --uninstall) UNINSTALL=true; shift ;;
    --target)   TARGET_DIR="$2"; shift 2 ;;
    -h|--help)
      echo "Divan - Claude Code Stack Installer"
      echo ""
      echo "Usage: ./install.sh [OPTIONS]"
      echo ""
      echo "Options:"
      echo "  --user          Install at user level (~/.claude/)"
      echo "  --project       Install at project level (current directory)"
      echo "  --minimal       Only install required plugins"
      echo "  --dry-run       Show what would be installed without making changes"
      echo "  --uninstall     Remove divan-managed settings"
      echo "  --target DIR    Target directory for project-level install"
      echo "  -h, --help      Show this help message"
      exit 0
      ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

# ─── Helper functions ────────────────────────────────────────────────────────

log_info()    { echo -e "${BLUE}[INFO]${NC} $1"; }
log_success() { echo -e "${GREEN}[OK]${NC} $1"; }
log_warn()    { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error()   { echo -e "${RED}[ERROR]${NC} $1"; }
log_dry()     { echo -e "${CYAN}[DRY-RUN]${NC} $1"; }

banner() {
  echo -e "${BOLD}"
  echo "╔══════════════════════════════════════════════════════════════╗"
  echo "║                                                              ║"
  echo "║     ██████╗ ██╗██╗   ██╗ █████╗ ███╗   ██╗                 ║"
  echo "║     ██╔══██╗██║██║   ██║██╔══██╗████╗  ██║                 ║"
  echo "║     ██║  ██║██║██║   ██║███████║██╔██╗ ██║                 ║"
  echo "║     ██║  ██║██║╚██╗ ██╔╝██╔══██║██║╚██╗██║                 ║"
  echo "║     ██████╔╝██║ ╚████╔╝ ██║  ██║██║ ╚████║                 ║"
  echo "║     ╚═════╝ ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝                 ║"
  echo "║                                                              ║"
  echo "║          Claude Code Stack Installer v1.0.0                  ║"
  echo "║                                                              ║"
  echo "╚══════════════════════════════════════════════════════════════╝"
  echo -e "${NC}"
}

ensure_jq() {
  if ! command -v jq &>/dev/null; then
    log_error "jq is required but not installed. Install it with: sudo apt install jq"
    exit 1
  fi
}

ensure_claude() {
  if ! command -v claude &>/dev/null; then
    log_warn "Claude Code CLI not found. Install it first: npm install -g @anthropic-ai/claude-code"
    log_warn "Continuing with file-based installation..."
  fi
}

backup_settings() {
  if [[ -f "$SETTINGS_FILE" ]]; then
    mkdir -p "$BACKUP_DIR"
    cp "$SETTINGS_FILE" "$BACKUP_DIR/settings.json"
    log_info "Backed up settings to $BACKUP_DIR/settings.json"
  fi
}

# ─── Plugin lists ────────────────────────────────────────────────────────────

REQUIRED_PLUGINS=(
  "superpowers"
  "ralph-loop"
  "context7"
  "github"
  "commit-commands"
)

ALL_PLUGINS=(
  "superpowers"
  "commit-commands"
  "code-review"
  "code-simplifier"
  "feature-dev"
  "frontend-design"
  "hookify"
  "ralph-loop"
  "vercel"
  "huggingface-skills"
  "supabase"
  "context7"
  "greptile"
  "qodo-skills"
  "github"
  "plugin-dev"
  "skill-creator"
  "agent-sdk-dev"
  "claude-code-setup"
  "claude-md-management"
  "telegram"
  "clangd-lsp"
  "pyright-lsp"
  "remember"
)

# ─── Interactive mode ────────────────────────────────────────────────────────

interactive_menu() {
  echo ""
  echo -e "${BOLD}Choose installation scope:${NC}"
  echo ""
  echo "  1) User-level   - Install plugins and settings globally (~/.claude/)"
  echo "  2) Project-level - Copy configs, skills, hooks to current project"
  echo "  3) Both          - Full user setup + project configs"
  echo ""
  read -rp "Selection [1-3]: " choice
  case $choice in
    1) MODE="user" ;;
    2) MODE="project" ;;
    3) MODE="both" ;;
    *) log_error "Invalid choice"; exit 1 ;;
  esac

  echo ""
  echo -e "${BOLD}Plugin set:${NC}"
  echo ""
  echo "  1) Full     - All 24 plugins (recommended)"
  echo "  2) Minimal  - Only required plugins (${#REQUIRED_PLUGINS[@]} plugins)"
  echo ""
  read -rp "Selection [1-2]: " choice
  case $choice in
    1) MINIMAL=false ;;
    2) MINIMAL=true ;;
    *) log_error "Invalid choice"; exit 1 ;;
  esac
}

# ─── User-level install ─────────────────────────────────────────────────────

install_user() {
  log_info "Installing at user level..."

  local plugins=()
  if $MINIMAL; then
    plugins=("${REQUIRED_PLUGINS[@]}")
  else
    plugins=("${ALL_PLUGINS[@]}")
  fi

  # Build the enabledPlugins JSON
  local plugins_json="{"
  local first=true
  for plugin in "${plugins[@]}"; do
    if $first; then first=false; else plugins_json+=","; fi
    plugins_json+="\"${plugin}@claude-plugins-official\":true"
  done
  plugins_json+="}"

  # Build settings
  local settings_json
  settings_json=$(jq -n \
    --argjson plugins "$plugins_json" \
    '{
      model: "opus[1m]",
      enabledPlugins: $plugins,
      skipDangerousModePermissionPrompt: true
    }')

  if $DRY_RUN; then
    log_dry "Would write to $SETTINGS_FILE:"
    echo "$settings_json" | jq .
    log_dry "Would enable ${#plugins[@]} plugins"
    return
  fi

  backup_settings
  mkdir -p "$CLAUDE_DIR"
  echo "$settings_json" | jq . > "$SETTINGS_FILE"
  log_success "Wrote settings with ${#plugins[@]} plugins enabled"

  # Install plugins via CLI if available
  if command -v claude &>/dev/null; then
    log_info "Installing plugins via Claude Code CLI..."
    for plugin in "${plugins[@]}"; do
      log_info "  Installing ${plugin}..."
      claude plugins install "${plugin}" 2>/dev/null || log_warn "  Could not install ${plugin} via CLI"
    done
    log_success "Plugin installation complete"
  else
    log_warn "Claude CLI not found - plugins will be installed on next Claude Code launch"
  fi
}

# ─── Project-level install ───────────────────────────────────────────────────

install_project() {
  local target="$TARGET_DIR"
  log_info "Installing at project level in ${target}..."

  if $DRY_RUN; then
    log_dry "Would create:"
    log_dry "  ${target}/CLAUDE.md"
    log_dry "  ${target}/.claude/settings.json (project-level)"
    log_dry "  ${target}/skills/ (custom skills)"
    log_dry "  ${target}/hooks/ (custom hooks)"
    return
  fi

  # Copy CLAUDE.md if one exists in divan
  if [[ -f "${DIVAN_ROOT}/CLAUDE.md" ]] && [[ ! -f "${target}/CLAUDE.md" ]]; then
    cp "${DIVAN_ROOT}/CLAUDE.md" "${target}/CLAUDE.md"
    log_success "Copied CLAUDE.md"
  elif [[ -f "${target}/CLAUDE.md" ]]; then
    log_warn "CLAUDE.md already exists, skipping (use --force to overwrite)"
  fi

  # Copy project-level settings
  mkdir -p "${target}/.claude"
  if [[ -f "${DIVAN_ROOT}/profiles/default/settings.json" ]]; then
    cp "${DIVAN_ROOT}/profiles/default/settings.json" "${target}/.claude/settings.json"
    log_success "Copied project settings"
  fi

  # Copy custom skills
  if [[ -d "${DIVAN_ROOT}/skills" ]]; then
    mkdir -p "${target}/.claude/skills"
    cp -r "${DIVAN_ROOT}/skills/"* "${target}/.claude/skills/" 2>/dev/null || true
    log_success "Copied custom skills"
  fi

  # Copy custom hooks
  if [[ -d "${DIVAN_ROOT}/hooks" ]]; then
    mkdir -p "${target}/.claude/hooks"
    cp -r "${DIVAN_ROOT}/hooks/"* "${target}/.claude/hooks/" 2>/dev/null || true
    log_success "Copied custom hooks"
  fi

  # Copy custom commands
  if [[ -d "${DIVAN_ROOT}/commands" ]]; then
    mkdir -p "${target}/.claude/commands"
    cp -r "${DIVAN_ROOT}/commands/"* "${target}/.claude/commands/" 2>/dev/null || true
    log_success "Copied custom commands"
  fi

  log_success "Project-level install complete"
}

# ─── Uninstall ───────────────────────────────────────────────────────────────

uninstall() {
  log_warn "Uninstalling divan-managed settings..."

  if $DRY_RUN; then
    log_dry "Would reset $SETTINGS_FILE to defaults"
    return
  fi

  backup_settings

  # Reset to minimal settings
  jq -n '{model: "opus[1m]", enabledPlugins: {}}' > "$SETTINGS_FILE"
  log_success "Settings reset. Backup saved to $BACKUP_DIR"
  log_info "Plugins remain cached but are disabled. Re-run install.sh to restore."
}

# ─── Main ────────────────────────────────────────────────────────────────────

banner
ensure_jq

if $UNINSTALL; then
  uninstall
  exit 0
fi

if [[ -z "$MODE" ]]; then
  interactive_menu
fi

ensure_claude

case $MODE in
  user)    install_user ;;
  project) install_project ;;
  both)    install_user; install_project ;;
esac

echo ""
echo -e "${GREEN}${BOLD}Installation complete!${NC}"
echo ""
echo "Next steps:"
echo "  - Start Claude Code to activate plugins"
echo "  - Run 'claude plugins list' to verify installed plugins"
echo "  - Check docs at: https://github.com/Mahi97/divan"
echo ""
