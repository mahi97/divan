# Divan

**A curated Claude Code stack** -- plugins, skills, hooks, agents, and workflows in one installable collection.

Divan (Persian: a collection of poems/works) is a batteries-included setup for Claude Code that combines 24 official marketplace plugins, custom skills, hooks, and workflows into a single repo you can install at user or project level.

## Quick Start

```bash
# Clone
git clone https://github.com/Mahi97/divan.git
cd divan

# Install everything at user level
./install.sh --user

# Or interactive mode
./install.sh
```

## What's Included

### External Plugins (24)

| Category | Plugins | Description |
|----------|---------|-------------|
| **Workflow** | superpowers, feature-dev, hookify | Planning, TDD, debugging, brainstorming, parallel agents |
| **Git** | github, commit-commands, code-review | Full GitHub integration, commit/push/PR, code review |
| **Code Quality** | code-simplifier, qodo-skills | Cleanup, rule enforcement, PR feedback |
| **AI/ML Platforms** | vercel, huggingface-skills, supabase | Deployment, ML training, database/auth |
| **Code Intelligence** | context7, greptile | Live docs lookup, semantic search |
| **Frontend** | frontend-design | Production-grade UI generation |
| **Development** | plugin-dev, skill-creator, agent-sdk-dev, claude-code-setup, claude-md-management | Build your own plugins, skills, agents |
| **Communication** | telegram | Chat-based interactions via Telegram bot |
| **LSP** | clangd-lsp, pyright-lsp | C/C++ and Python language servers |
| **Session** | remember | Persistent state across sessions |
| **Safety** | ralph-loop | Self-referential loop prevention |

### MCP Servers

| Server | Endpoint | Purpose |
|--------|----------|---------|
| GitHub | `api.githubcopilot.com/mcp/` | Issues, PRs, code search |
| Vercel | `mcp.vercel.com` | Deployments, logs, projects |
| Supabase | `mcp.supabase.com/mcp` | Database, auth, storage |
| Hugging Face | `huggingface.co/mcp` | Models, datasets, spaces |
| Greptile | `api.greptile.com/mcp` | Semantic code search |
| Context7 | *(embedded)* | Library documentation |

### Custom Components

```
skills/       # Custom Claude Code skills
hooks/        # Custom hook scripts
agents/       # Custom agent definitions
commands/     # Custom slash commands
workflows/    # Multi-step workflow definitions
profiles/     # Installation profiles (minimal, full, ml, web, etc.)
```

## Installation Modes

### User-Level (Global)

Configures `~/.claude/settings.json` with all plugins enabled:

```bash
./install.sh --user           # Full stack (24 plugins)
./install.sh --user --minimal # Required plugins only (5 plugins)
```

### Project-Level

Copies skills, hooks, commands, and CLAUDE.md into a target project:

```bash
./install.sh --project                     # Current directory
./install.sh --project --target ~/my-app   # Specific directory
```

### Both

```bash
./install.sh --user --project   # or interactive mode option 3
```

### Dry Run

```bash
./install.sh --user --dry-run   # Preview changes without applying
```

## Profiles

Profiles let you install a subset of the stack tuned for a specific workflow:

| Profile | Plugins | Use Case |
|---------|---------|----------|
| `full` | All 24 | Everything, for power users |
| `minimal` | 5 required | Lightweight, essential only |
| `ml` | minimal + huggingface, vercel | Machine learning projects |
| `web` | minimal + vercel, frontend-design, supabase | Web development |
| `devtools` | minimal + plugin-dev, skill-creator, agent-sdk-dev | Building Claude Code extensions |

```bash
./install.sh --user --profile ml
```

## Custom Skills

Add your own skills in `skills/`:

```markdown
<!-- skills/my-skill.md -->
---
name: my-skill
description: What this skill does
---

Skill instructions here...
```

## Custom Hooks

Add hooks in `hooks/`:

```yaml
# hooks/pre-commit-check.yaml
event: PreToolUse
matcher: Bash
script: hooks/scripts/pre-commit-check.sh
```

## Custom Agents

Define agents in `agents/`:

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

## Project Structure

```
divan/
  stack.yaml          # Stack manifest - all components listed here
  install.sh          # Installer script
  README.md           # This file
  CLAUDE.md           # Agent-facing project documentation
  skills/             # Custom skills
    README.md         # Skill authoring guide
  hooks/              # Custom hooks
    README.md         # Hook authoring guide
    scripts/          # Hook script implementations
  agents/             # Custom agent definitions
    README.md         # Agent authoring guide
  commands/           # Custom slash commands
  workflows/          # Multi-step workflow definitions
  profiles/           # Installation profiles
    full.yaml
    minimal.yaml
    ml.yaml
    web.yaml
    devtools.yaml
  docs/               # Extended documentation
    plugin-guide.md   # Detailed plugin descriptions
    mcp-setup.md      # MCP server configuration
    troubleshooting.md
```

## Updating

Pull the latest and re-run install:

```bash
cd divan
git pull
./install.sh --user
```

## Uninstalling

```bash
./install.sh --uninstall   # Resets settings, keeps plugin cache
```

A backup is automatically created before any changes.

## Contributing

1. Fork this repo
2. Add your skills/hooks/agents/commands
3. Update `stack.yaml` with new components
4. Submit a PR

## License

MIT
