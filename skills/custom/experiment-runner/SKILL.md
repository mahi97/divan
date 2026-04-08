---
name: experiment-runner
description: Run an experiment with structured config and logging
---

# Experiment Runner

## When to Use

- Running a new experiment (training, evaluation, benchmark)
- Comparing results against a baseline
- The operator says "run experiment X" or "try Y and see what happens"

## Inputs

- Experiment description or hypothesis
- Config file (from `configs/`) or parameters to configure
- Baseline to compare against (optional)
- Target server: local, bare-gpu, or hpc (default: local)

## Steps

1. **Create experiment log:**
   - Scan `docs/experiments/` for next number (NNNN)
   - Create `docs/experiments/NNNN-short-title.md`
   - Fill in hypothesis and setup

2. **Create or verify config:**
   - Write `configs/experiment_NNNN.yaml` if it doesn't exist
   - Include all hyperparameters, data paths, seeds
   - Commit the config

3. **Record environment:**
   - Python version, key dependency versions
   - Git commit hash
   - Target server and GPU type

4. **Commit code:**
   - Ensure all code changes are committed
   - Record commit hash in experiment log

5. **Run experiment:**
   - **Local:** `python src/train.py --config configs/experiment_NNNN.yaml`
   - **Bare GPU:** Follow `gpu-deploy` skill
   - **HPC:** Follow `hpc-submit` skill

6. **Monitor:**
   - Watch for crashes, NaN loss, OOM in early epochs
   - Check W&B/TensorBoard if configured

7. **Record results:**
   - Update experiment log with metrics
   - Compare against baseline if provided
   - Update status to completed/failed

## Output

Experiment log at `docs/experiments/NNNN-title.md` plus summary:

```
## Experiment NNNN — Title
- Status: completed | failed
- Key metric: [value] (baseline: [value], delta: [+/-]%)
- Config: configs/experiment_NNNN.yaml
- Commit: [hash]
- Server: [where it ran]
- Log: docs/experiments/NNNN-title.md
```

## Safety

- Always commit code before running
- Record exact commit hash
- Never modify completed experiment logs — create a new experiment
- Set timeouts and checkpoints for long runs
- If running on shared resources, check availability first
