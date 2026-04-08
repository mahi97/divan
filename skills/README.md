# Divan Skills

Skills are structured instructions that AI agents follow to perform specific
research tasks. They live in this directory and are referenced by the project's
`AGENTS.md` and `CLAUDE.md`.

## Custom Skills (skills/custom/)

Your own skills, maintained in this repo:

| Skill              | Purpose                                         |
|--------------------|-------------------------------------------------|
| `gpu-deploy`       | Deploy and run code on bare GPU servers via SSH  |
| `hpc-submit`       | Submit and manage jobs on HPC/PBS clusters       |
| `experiment-runner` | Run experiments with structured logging          |
| `sweep-runner`     | Hyperparameter sweeps                            |
| `monitoring-setup` | Set up experiment monitoring                     |
| `results-viz`      | Visualize and compare results                    |
| `latex-paper`      | Write, compile, manage LaTeX papers              |
| `project-setup`    | Set up Python project environment                |
| `repo-onboarding`  | Understand an existing codebase                  |
| `legacy-rewrite`   | Safely modernize legacy code                     |

## External Skills (skills/external/)

Skills from other sources, fetched via `manifest.yml`. Run:
```bash
python tools/fetch_skills.py
```

## Skill Format

Each skill has a `SKILL.md` file with:

1. **When to use** — trigger conditions
2. **Inputs** — what the skill needs
3. **Steps** — the procedure
4. **Output** — expected result format
5. **Safety** — things to be careful about

## Adding a New Skill

1. Create `skills/custom/my-skill/SKILL.md`
2. Follow the format of existing skills
3. Update this README
