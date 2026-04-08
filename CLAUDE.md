# CLAUDE.md — Divan Toolkit

This is `divan/`, a personal ML/AI research toolkit. It lives inside a project
directory and provides skills, standards, and workflows.

**The actual project is `../` (the parent directory).** Divan is the toolkit.

## Quick Orientation

- `skills/custom/` — task-specific skills (GPU deploy, experiments, LaTeX, etc.)
- `docs/standards/agent-standards.md` — canonical rules
- `docs/servers/` — bare GPU and HPC cluster access
- `workflows/` — research pipeline definitions
- `bootstrap/` — files copied to parent project on init

## Initialize Parent Project

```bash
bash init.sh --profile ml-research
```
Or follow `PROJECT_INIT_PLAYBOOK.md` step by step.

## When Working on the Parent Project

Read `../CLAUDE.md` — it points back here for skills and standards.

Key skills:
- `skills/custom/gpu-deploy/` — deploy to bare GPU server
- `skills/custom/hpc-submit/` — submit to HPC/PBS cluster
- `skills/custom/experiment-runner/` — run + log experiments
- `skills/custom/sweep-runner/` — hyperparameter sweeps
- `skills/custom/monitoring-setup/` — W&B, TensorBoard setup
- `skills/custom/results-viz/` — visualize results
- `skills/custom/latex-paper/` — LaTeX paper workflow
- `skills/custom/project-setup/` — Python env setup

## Rules

- Never modify divan/ files unless explicitly working on divan itself
- Never commit secrets
- Never run GPU jobs without confirming server + resources
- Never delete experiment logs
- Always commit code before running experiments
