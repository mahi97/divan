# Divan

**A curated Claude Code super collection** -- every plugin, skill, hook, agent, and workflow you need, installable by use case.

Divan (Persian: a collected works) bundles 24 official marketplace plugins, 6 MCP servers, custom skills, hooks, and workflows into a single CLI. Initialize any project with the right subset for your work.

## Install

**One-liner** (no manual clone needed):

```bash
curl -fsSL https://raw.githubusercontent.com/mahi97/divan/main/install.sh | bash
```

This clones to `~/.divan`, links the CLI to `~/.local/bin/divan`, and you're done.

**Or clone and install manually:**

```bash
git clone https://github.com/mahi97/divan.git ~/.divan
cd ~/.divan && ./divan self-install
```

**Customize install location:**

```bash
# Change where divan lives and where the binary goes
DIVAN_HOME=~/my-tools/divan BIN_DIR=~/bin curl -fsSL https://raw.githubusercontent.com/mahi97/divan/main/install.sh | bash

# Or after cloning
./divan self-install --bin-dir ~/bin --divan-home ~/my-tools/divan
```

## Quick Start

```bash
# Initialize a project with a profile
divan init --profile web --target ~/my-app

# Or pick interactively
divan init

# Browse what's available
divan profiles
divan list --profile ml
```

## The `divan` CLI

```bash
divan self-install                               # install CLI to PATH
divan init [--profile <name>] [--target <dir>]   # initialize a project
divan add <plugin|tag>                            # add a component
divan remove <plugin>                             # remove a component
divan list [--profile <name>]                     # browse the collection
divan profiles                                    # list all profiles
divan status                                      # show current project config
divan sync                                        # re-sync from profile
divan user-install [--profile <name>]             # install at user level
divan uninstall                                   # reset Claude Code settings
divan self-uninstall                              # remove divan from PATH
```

## Profiles

Each profile selects a subset of the collection tuned for a use case:

| Profile | Plugins | Use Case |
|---------|---------|----------|
| `full` | 24 | Everything -- power users |
| `minimal` | 6 | Core essentials only |
| `web` | 15 | Next.js, Vercel, Supabase, frontend |
| `ml` | 14 | HuggingFace, training, datasets, Python |
| `research` | 14 | Papers, experiments, documentation |
| `devtools` | 14 | Building plugins, skills, agents |
| `embedded` | 12 | C/C++ with clangd LSP |

```bash
# Preview what a profile includes
./divan list --profile ml

# See all profiles with their plugin lists
./divan profiles
```

## What's in the Collection

### Plugins (24)

| Category | Plugins |
|----------|---------|
| **Core** | superpowers, github, commit-commands, context7, ralph-loop, remember |
| **Git & Quality** | code-review, code-simplifier, qodo-skills |
| **Workflow** | feature-dev, hookify |
| **Frontend** | frontend-design |
| **Platforms** | vercel, supabase, huggingface-skills |
| **Code Intel** | greptile |
| **Dev Tools** | plugin-dev, skill-creator, agent-sdk-dev, claude-code-setup, claude-md-management |
| **Communication** | telegram |
| **LSP** | clangd-lsp, pyright-lsp |

### MCP Servers (6)

GitHub Copilot, Vercel, Supabase, Hugging Face, Greptile, Context7 -- configured automatically by their plugins.

### Custom Components

```
skills/       # Your custom Claude Code skills
hooks/        # Custom hook configs + scripts
agents/       # Custom agent definitions
commands/     # Custom slash commands
workflows/    # Multi-step workflow templates
```

## How It Works

### Project Initialization

`divan init` does the following:

1. **Selects a profile** (interactive picker or `--profile` flag)
2. **Resolves plugins** from profile tags + extras + required core
3. **Creates `.divan.yaml`** -- lockfile tracking what's installed
4. **Updates `~/.claude/settings.json`** -- enables plugins globally
5. **Creates `.claude/settings.json`** -- project-level config
6. **Generates `CLAUDE.md`** -- with profile-specific guidance
7. **Copies custom skills/hooks/commands** from this repo

### Adding & Removing

After init, modify your project's stack:

```bash
# Add a single plugin
divan add frontend-design

# Add all plugins with a tag
divan add ai-ml

# Remove a plugin (core plugins can't be removed)
divan remove telegram
```

### Tag System

Every plugin has tags. Profiles select by tag, so adding a new plugin to `stack.yaml` with the right tags automatically includes it in matching profiles.

Available tags: `core`, `git`, `code-quality`, `workflow`, `frontend`, `backend`, `ai-ml`, `platform`, `code-intel`, `devtools`, `communication`, `lsp`, `session`, `safety`, `python`, `cpp`, `automation`

## Creating Custom Profiles

Add a YAML file to `profiles/`:

```yaml
name: my-profile
description: "My custom setup"
icon: "MY"
tags: [core, git, workflow, python]
extras:
  - pyright-lsp
  - greptile
settings:
  model: "opus[1m]"
claude_md:
  append: |
    ## Divan Profile: my-profile
    Your project-specific guidance here.
```

## Contributing Custom Components

### Skills

```markdown
<!-- skills/my-skill.md -->
---
name: my-skill
description: What this skill does
---
Skill instructions here...
```

### Hooks

```yaml
# hooks/my-hook.yaml
event: PreToolUse
matcher: Bash
script: hooks/scripts/my-hook.sh
```

### Agents

```markdown
<!-- agents/my-agent.md -->
---
name: my-agent
description: Agent purpose
model: sonnet
tools: [Read, Grep, Glob, Bash]
---
Agent system prompt here...
```

## Updating

```bash
# Update the divan collection itself
cd ~/.divan && git pull

# Then re-sync any initialized project
cd ~/my-app && divan sync
```

## Uninstalling

```bash
# Reset Claude Code settings (disables all plugins)
divan uninstall

# Remove divan CLI from PATH
divan self-uninstall

# Fully remove (optional)
rm -rf ~/.divan
```

A backup is created automatically before any settings changes.

## License

MIT
