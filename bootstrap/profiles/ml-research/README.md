# Profile: ml-research

Full ML research setup — training, experiments, sweeps, monitoring, paper.

## When to Use

- Training neural networks or running ML experiments
- Projects involving benchmarks, ablations, sweeps
- Work that produces papers or reports

## Files Added (on top of common)

```
pyproject.toml          — Python project config with ML dependencies
src/__init__.py         — Package placeholder
src/train.py            — Training entry point template
src/evaluate.py         — Evaluation entry point template
src/utils/config.py     — Config loading utility
tests/test_smoke.py     — Smoke test
configs/base.yaml       — Base experiment config
configs/sweeps/         — Sweep config directory
scripts/jobs/train.pbs  — HPC PBS job script template
paper/main.tex          — LaTeX paper template
paper/references.bib    — BibTeX references file
```

## Conventions

- Configs in `configs/`, never hardcoded hyperparameters
- Results in `results/` (gitignored)
- Data in `data/` (gitignored)
- Experiment logs in `docs/experiments/`
- Paper in `paper/`

## Skills to Use

- `divan/skills/custom/experiment-runner/`
- `divan/skills/custom/sweep-runner/`
- `divan/skills/custom/gpu-deploy/`
- `divan/skills/custom/hpc-submit/`
- `divan/skills/custom/monitoring-setup/`
- `divan/skills/custom/results-viz/`
- `divan/skills/custom/latex-paper/`
