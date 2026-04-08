# Research Workflow Standards

Standards for ML/AI research: experiments, sweeps, GPU deployment, monitoring,
results analysis, and paper writing.

---

## Principles

1. **Reproducibility first.** Every experiment must be reproducible from its log.
2. **Log everything.** Failed experiments are data. Never delete logs.
3. **Separate code from results.** Code in `src/`, results in `results/`,
   logs in `docs/experiments/`.
4. **Config-driven experiments.** Hyperparameters live in `configs/`, not in code.
5. **Configurable storage.** Data, cache, checkpoint, and artifact locations must live in config, not library defaults.
6. **Explicit GPU selection.** GPU device choice must be configurable so users can select one GPU or a set of GPUs without editing code.
7. **TDD for research code.** Start new behavior with a failing test or regression case, then implement.
8. **Commit before running.** Always commit before starting an experiment.
9. **Track compute costs.** Note GPU hours, wall time, server used.

## Research Pipeline

```
1. Literature    → Read papers, write notes in docs/literature/
2. Hypothesis    → Write docs/experiments/NNNN-title.md
3. Config        → Create configs/experiment_NNNN.yaml
4. Test          → Write or update a failing test
5. Code          → Implement in src/, commit
6. Deploy        → Push to GPU server (bare or HPC)
7. Run           → Execute with monitoring enabled
8. Monitor       → Watch metrics (W&B, TensorBoard, logs)
9. Analyze       → Pull results, update experiment log
10. Visualize    → Generate plots, compare baselines
11. Paper        → Write up findings in LaTeX
```

## Directory Layout

```
project_root/
  divan/                     # Toolkit (do not mix with project code)
  src/                       # Source code
  tests/                     # Unit tests
  configs/                   # Experiment configs (YAML/TOML)
    sweeps/                  # Sweep configs
  data/                      # Local data (gitignored if large)
  results/                   # Experiment outputs (gitignored if large)
  notebooks/                 # Jupyter notebooks
  scripts/
    jobs/                    # PBS job scripts for HPC
  paper/                     # LaTeX paper
    figures/                 # Figures for paper
  docs/
    experiments/             # Experiment logs (always committed)
    literature/              # Reading notes
    decisions/               # Architectural decisions
```

## Experiment Config Convention

Use YAML configs in `configs/`:

```yaml
# configs/experiment_0001.yaml
experiment:
  name: baseline_transformer
  seed: 42

model:
  type: transformer
  hidden_size: 256
  num_layers: 4

training:
  batch_size: 32
  learning_rate: 1e-4
  epochs: 100
  optimizer: adam

data:
  dataset: wikitext-103
  data_dir: data/datasets/
  split_ratio: [0.8, 0.1, 0.1]

paths:
  cache_root: .cache/
  hf_home: .cache/huggingface/
  hf_datasets_cache: .cache/huggingface/datasets/
  hf_hub_cache: .cache/huggingface/hub/
  checkpoint_dir: results/checkpoints/

compute:
  server: bare-gpu  # or hpc
  gpu_devices: [0]
  gpu_count: 1
  gpu_type: A100
```

Load configs in code:
```python
import yaml
from pathlib import Path

config = yaml.safe_load(Path("configs/experiment_0001.yaml").read_text())
```

## Sweep Workflow

For hyperparameter sweeps:

1. Define sweep space in `configs/sweeps/sweep_NNNN.yaml`
2. Use a sweep runner (W&B sweep, Optuna, or manual grid)
3. Log all trials to the same experiment group
4. Store best config and results
5. Document findings in experiment log

## Reproducibility Checklist

Before declaring an experiment complete:

- [ ] Code is committed, commit hash recorded
- [ ] Config file exists in `configs/` and is committed
- [ ] Dependencies pinned in `uv.lock` or another committed lock file
- [ ] Data and cache locations are configured explicitly, not left to library defaults
- [ ] Dataset source and version documented
- [ ] Random seeds set and recorded
- [ ] GPU selection is configurable and recorded
- [ ] Hardware noted (GPU type, count, server name)
- [ ] Experiment re-runnable from log + config + commit

## Monitoring

- Use W&B, TensorBoard, or similar for live monitoring
- At minimum, log: loss, learning rate, GPU utilization, wall time
- Set up alerts for NaN loss, OOM, job failures
- Save checkpoints at regular intervals

## Results and Visualization

- Raw results in `results/` (gitignored)
- Summary metrics in experiment log (committed)
- Figures in `paper/figures/` or `results/figures/`
- Always compare against a documented baseline
- Include error bars or confidence intervals where applicable

## Paper Writing

- LaTeX source in `paper/`
- Figures generated from scripts, not manually created
- Use `\input{}` for tables generated from results
- Track paper drafts with git, not filename versioning
- BibTeX references in `paper/references.bib`

## Notebook Conventions

- Notebooks are for exploration, not production code
- Extract reusable logic into `src/` modules
- Clear outputs before committing (or use a pre-commit hook)
- Name descriptively: `01-data-exploration.ipynb`, not `Untitled.ipynb`

## Experiment Naming

Sequential numbering with descriptive titles:

```
docs/experiments/
  0001-baseline-transformer.md
  0002-larger-batch-size.md
  0003-learning-rate-sweep.md
  0004-attention-ablation.md
```
