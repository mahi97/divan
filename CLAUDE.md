# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Repo Is

**Divan** is a curated collection of Claude Code plugins, skills, hooks, agents, and workflows. It serves as a one-stop install for a complete Claude Code power-user setup.

## Key Files

- `stack.yaml` - The master manifest listing all components (plugins, MCP servers, settings, custom components)
- `install.sh` - The installer script (user-level, project-level, or both)
- `skills/` - Custom skill definitions (markdown files with YAML frontmatter)
- `hooks/` - Custom hook configurations and scripts
- `agents/` - Custom agent definitions
- `commands/` - Custom slash commands
- `workflows/` - Multi-step workflow templates
- `profiles/` - Installation profiles (full, minimal, ml, web, devtools)

## Architecture

The stack is organized in layers:
1. **External plugins** (24 from claude-plugins-official marketplace) - managed via `stack.yaml`
2. **MCP servers** (6 external services) - configured automatically by plugins
3. **Custom components** (skills, hooks, agents, commands) - defined in this repo
4. **Profiles** - subsets of the stack for different use cases

## Commands

```bash
./install.sh --user             # Install at user level
./install.sh --project          # Install at project level
./install.sh --dry-run          # Preview without changes
./install.sh --uninstall        # Remove settings
```

## Conventions

- All custom skills go in `skills/` as `.md` files with YAML frontmatter
- All custom hooks go in `hooks/` with `.yaml` config + `hooks/scripts/` for implementations
- All agent definitions go in `agents/` as `.md` files with YAML frontmatter
- `stack.yaml` is the single source of truth for what's in the stack
- Never commit credentials or `.env` files
- Profiles reference plugins by name from `stack.yaml`
