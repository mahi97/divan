# CLAUDE.md

## What This Repo Is

**Divan** is a super collection of Claude Code plugins, skills, hooks, agents, and workflows. The `divan` CLI initializes projects with use-case-specific subsets.

## Key Files

- `divan` - The CLI script (bash). Subcommands: init, add, remove, list, profiles, status, sync, user-install
- `stack.yaml` - Master manifest. Every plugin with name, description, tags, required flag
- `profiles/*.yaml` - Profile definitions. Each selects plugins by tags + explicit extras
- `skills/`, `hooks/`, `agents/`, `commands/`, `workflows/` - Custom components

## Architecture

1. `stack.yaml` is the single source of truth for all available plugins (24 total)
2. Each plugin has **tags** (e.g., `[core, workflow]`, `[ai-ml, platform]`)
3. **Profiles** select plugins by matching tags + explicit extras list
4. **Core plugins** (tagged `core`, `required: true`) are always included regardless of profile
5. `divan init` resolves a profile into a concrete plugin list, writes `.divan.yaml` lockfile + settings
6. `divan add/remove` modifies the lockfile and settings post-init

## Commands

```bash
divan init --profile web --target ~/app     # Initialize project
divan add ai-ml                             # Add by tag
divan add telegram                          # Add by name
divan remove telegram                       # Remove (not core)
divan list --profile ml                     # Preview a profile
divan profiles                              # List all profiles
divan status                                # Current project info
divan sync                                  # Re-sync from profile
divan user-install --profile full           # User-level install
```

## Installation

- `install.sh` — Remote installer for `curl | bash`. Clones to `~/.divan`, then runs `divan install`
- `install.sh --uninstall` — Removes symlink, removes env block from all shell rcs, resets Claude settings
- `divan install` — Symlinks CLI to `~/.local/bin`, reads `.env`, injects a managed block into shell rc files (`~/.bashrc`, `~/.zshrc`, `~/.profile`)
- `divan uninstall` — Removes symlink, removes env block from all shell rcs, resets Claude settings
- Env block is delimited by `# >>> divan >>>` / `# <<< divan <<<` markers for clean add/remove
- `DIVAN_HOME` and `BIN_DIR` env vars or `--bin-dir`/`--divan-home` flags override defaults

## .env File

- `.env` in the divan repo root defines environment variables to export
- Lines starting with `#` and blank lines are skipped
- Lines with empty values are skipped
- `DIVAN_HOME` is always set automatically (don't duplicate in `.env`)
- Re-run `divan install` after editing `.env` to update shell configs
- `.env` is tracked in git (template with commented-out keys); use `.env.local` for secrets (gitignored)

## Conventions

- Custom skills: `skills/*.md` with YAML frontmatter (name, description)
- Custom hooks: `hooks/*.yaml` config + `hooks/scripts/` implementations
- Custom agents: `agents/*.md` with YAML frontmatter (name, description, model, tools)
- Profiles: `profiles/*.yaml` with name, description, icon, tags, extras, claude_md
- All profile tags must be on a single line in the YAML
- Never commit credentials or `.env` files
