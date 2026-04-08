# Divan — Overview

Divan is a personal AI research operations toolkit. It lives inside your
project directory and provides skills, standards, workflows, and scaffolding
that AI agents use to help you build, run, and publish research.

## What Divan Is

- A portable skill library for Claude Code and Codex
- A project bootstrapper that sets up docs, scripts, and agent configs
- A standards reference for consistent research practices
- A workflow guide for GPU deployment, experiments, sweeps, and papers
- A bridge between your code and two types of GPU servers

## What Divan Is Not

- Not a Python package — nothing in divan is imported by your project code
- Not a framework — it imposes no runtime dependencies
- Not a monorepo tool — each project gets its own divan clone

## How It Works

```
my_project/
  divan/              ← cloned inside, provides skills + standards
    init.sh           ← run once to set up the parent project
    skills/           ← AI agents read these for task guidance
    bootstrap/        ← files that get copied to parent project
  src/                ← your code (set up by init)
  tests/              ← your tests
  CLAUDE.md           ← points agents to divan/ (created by init)
  AGENTS.md           ← same, for Codex (created by init)
```

1. Clone divan into your project
2. Run `init.sh` — copies docs, scripts, configs, agent files to parent
3. AI agents read `CLAUDE.md`/`AGENTS.md`, which point to `divan/skills/`
4. Agents use skills to deploy code, run experiments, write papers

## Key Directories

| Path                  | Purpose                                            |
|-----------------------|----------------------------------------------------|
| `skills/custom/`      | Your custom skills for ML research                  |
| `skills/external/`    | External skills with fetch manifest                 |
| `workflows/`          | Research pipeline definitions                       |
| `bootstrap/common/`   | Files copied to parent project on init              |
| `bootstrap/profiles/` | Profile overlays (ml-research, llm-research, etc.)  |
| `docs/standards/`     | Canonical coding and research standards              |
| `docs/servers/`       | GPU server access guides (bare metal + HPC)          |
| `tools/`              | Init, validate, fetch scripts                        |

## Profiles

| Profile          | Best for                                           |
|------------------|----------------------------------------------------|
| `base`           | Any project — docs, scripts, agent configs only     |
| `ml-research`    | Full ML setup with experiment tracking               |
| `llm-research`   | LLM work — prompts, evals, model management          |
| `general-python` | Generic Python package or application                |
