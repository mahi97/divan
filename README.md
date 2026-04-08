# Divan

Personal AI research toolkit — skills, agents, workflows, and project
scaffolding for ML/AI research projects.

## What This Is

Divan is cloned **inside** your project and acts as your portable research
operations layer. It provides:

- **Skills** for Claude Code and Codex — GPU deployment, experiment running,
  hyperparameter sweeps, monitoring, visualization, LaTeX paper writing
- **Bootstrap files** copied into the parent project (AGENTS.md, CLAUDE.md,
  scripts, docs structure)
- **Standards and conventions** for consistent research across all projects
- **Server profiles** for bare GPU servers (SSH) and HPC clusters (PBS/Torque)
- **Workflows** for common research pipelines (train → evaluate → visualize → paper)

## What This Is Not

- Not a Python package or library — it's an operations toolkit
- Not a framework — it doesn't impose runtime dependencies on your code
- Not project-specific — it works across any ML/AI research project

## Layout

```
my_project/                    ← your research project
  divan/                       ← this repo, cloned inside
    skills/                    ← skills for AI agents
    workflows/                 ← research pipeline definitions
    bootstrap/                 ← files copied to parent project
    docs/                      ← standards and server guides
    tools/                     ← init, fetch, validate scripts
  src/                         ← your project code (created by init)
  tests/                       ← your tests
  configs/                     ← experiment configs
  docs/                        ← project docs
  scripts/                     ← build/test/lint/deploy scripts
  AGENTS.md                    ← agent instructions (created by init)
  CLAUDE.md                    ← Claude instructions (created by init)
```

## Quick Start

### New project

```bash
mkdir my_project && cd my_project
git init
git clone https://github.com/YOUR_USER/divan.git
cd divan && bash init.sh
```

### Existing project

```bash
cd my_project
git clone https://github.com/YOUR_USER/divan.git
cd divan && bash init.sh --backup
```

### With a specific profile

```bash
bash init.sh --profile ml-research
bash init.sh --profile llm-research
bash init.sh --profile general-python
```

### Preview first

```bash
bash init.sh --dry-run
```

## Profiles

| Profile           | Use case                                            |
|-------------------|-----------------------------------------------------|
| `base`            | Common files only — docs, scripts, agent configs     |
| `ml-research`     | Full ML setup — configs, data dirs, experiment tracking |
| `llm-research`    | LLM-specific — prompts, eval harness, model management |
| `general-python`  | Python package/app — pyproject.toml, src layout      |

## Skills

Skills live in `divan/skills/` and are available to AI agents working on the
parent project. Custom skills are in `skills/custom/`, external skills are
fetched via `skills/external/manifest.yml`.

| Skill              | Purpose                                            |
|--------------------|----------------------------------------------------|
| `gpu-deploy`       | Deploy and run on bare GPU servers via SSH          |
| `hpc-submit`       | Submit and manage jobs on HPC/PBS clusters          |
| `experiment-runner` | Run experiments with structured logging             |
| `sweep-runner`     | Hyperparameter sweeps (grid, random, Bayesian)      |
| `monitoring-setup` | Set up experiment monitoring (W&B, TensorBoard)     |
| `results-viz`      | Visualize and compare experiment results            |
| `latex-paper`      | Write, compile, and manage LaTeX papers             |
| `project-setup`    | Set up Python project environment and dependencies  |
| `repo-onboarding`  | Understand an existing codebase quickly             |
| `legacy-rewrite`   | Safely modernize legacy research code               |

## Server Access

Divan supports two GPU server types. See `docs/servers/` for details.

| Server Type     | Access Method    | Job Management        |
|-----------------|------------------|-----------------------|
| Bare GPU        | SSH direct       | tmux/screen, manual   |
| HPC Cluster     | SSH to login node | PBS/Torque (qsub, qstat, qdel) |

## How Agents Use Divan

When an AI agent (Claude Code, Codex) opens your project, it reads:

1. `AGENTS.md` or `CLAUDE.md` in the project root (created by init)
2. These files point to `divan/` for skills, standards, and workflows
3. The agent uses skills from `divan/skills/` to perform tasks
4. The agent follows standards from `divan/docs/standards/`

## Structure

```
divan/
  README.md                    # This file
  init.sh / init.ps1           # Quick init wrappers
  AGENTS.md                    # Agent instructions for divan itself
  CLAUDE.md                    # Claude instructions for divan itself
  PROJECT_INIT_PLAYBOOK.md     # Step-by-step init guide for agents
  skills/
    custom/                    # Your custom skills (10 starter skills)
    external/                  # External skills + fetch manifest
  agents/                      # Agent definitions
  workflows/                   # Research pipeline workflows
  bootstrap/
    common/                    # Files copied to parent project
    profiles/                  # Profile overlays
  docs/
    standards/                 # Canonical standards
    servers/                   # GPU server guides
    templates/                 # Document templates
  tools/
    init_project.py            # Main initializer
    validate_template.py       # Self-validator
    fetch_skills.py            # External skill fetcher
    render_templates.py        # Placeholder rendering
  configs/                     # Reusable config templates
  examples/                    # Reference layouts
```

## License

MIT — see [LICENSE](LICENSE).
