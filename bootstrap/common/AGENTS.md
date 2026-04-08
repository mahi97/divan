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

| Skill               | When to use                                  |
|---------------------|----------------------------------------------|
| `gpu-deploy`        | Deploy code to bare GPU server               |
| `hpc-submit`        | Submit jobs to HPC/PBS cluster               |
| `experiment-runner` | Run and log an experiment                    |
| `sweep-runner`      | Hyperparameter sweep                         |
| `monitoring-setup`  | Set up W&B / TensorBoard                     |
| `results-viz`       | Visualize and compare results                |
| `latex-paper`       | Write/compile LaTeX paper                    |
| `project-setup`     | Set up Python environment                    |
| `repo-onboarding`   | Understand this codebase                     |
| `skill-generation`  | Find or generate a skill for an unknown tool |
| `graphify`          | Build a knowledge graph from code and docs   |

Additional skills (engineering workflow, debugging, etc.) are available in
`divan/skills/external/` after running `python divan/tools/fetch_skills.py`.

## Commands

```bash
scripts/check.sh     # Lint + test
scripts/test.sh      # Tests only
scripts/lint.sh      # Lint only
uv run pytest        # Direct test command
```

## Rules

- Read `divan/docs/standards/agent-standards.md` for full rules
- **Before working with any unfamiliar library or tool**, check `divan/skills/custom/`,
  then `divan/skills/external/`, then fetch via `python divan/tools/fetch_skills.py`.
  If no skill exists, use `skill-seekers create <url>` to generate one.
- Run `scripts/check.sh` before committing
- Use `uv` and `pyproject.toml` as the default Python workflow
- Write or update a failing test before implementing new functionality or a bug fix
- Do not commit secrets
- Do not push unless asked
- Do not modify `divan/` unless working on divan itself
- Commit code before running experiments
- Log experiments in `docs/experiments/`
- Keep data, cache, and checkpoint locations configurable in `configs/`
- Keep GPU selection configurable in `configs/`

## Server Access

- Bare GPU: see `divan/docs/servers/bare-gpu.md`
- HPC cluster: see `divan/docs/servers/hpc-pbs.md`
