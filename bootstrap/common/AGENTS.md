# AGENTS.md — {{PROJECT_NAME}}

## Project

- **Name:** {{PROJECT_NAME}}
- **Owner:** {{OWNER}}
- **Language:** {{PRIMARY_LANGUAGE}}
- **Description:** {{DESCRIPTION}}

## Toolkit

This project uses **divan** (`divan/` directory) for skills, standards, and
workflows. Read `divan/docs/standards/agent-standards.md` for the full rules.

## Skills (in divan/skills/custom/)

| Skill              | When to use                                  |
|--------------------|----------------------------------------------|
| `gpu-deploy`       | Deploy code to bare GPU server               |
| `hpc-submit`       | Submit jobs to HPC/PBS cluster               |
| `experiment-runner` | Run and log an experiment                    |
| `sweep-runner`     | Hyperparameter sweep                          |
| `monitoring-setup` | Set up W&B / TensorBoard                     |
| `results-viz`      | Visualize and compare results                |
| `latex-paper`      | Write/compile LaTeX paper                    |
| `project-setup`    | Set up Python environment                    |
| `repo-onboarding`  | Understand this codebase                     |

## Commands

```bash
scripts/check.sh     # Lint + test
scripts/test.sh      # Tests only
scripts/lint.sh      # Lint only
```

## Rules

- Read `divan/docs/standards/agent-standards.md` for full rules
- Run `scripts/check.sh` before committing
- Write tests for new functionality
- Do not commit secrets
- Do not push unless asked
- Do not modify `divan/` unless working on divan itself
- Commit code before running experiments
- Log experiments in `docs/experiments/`

## Server Access

- Bare GPU: see `divan/docs/servers/bare-gpu.md`
- HPC cluster: see `divan/docs/servers/hpc-pbs.md`
