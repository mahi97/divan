---
name: sweep-runner
description: Run hyperparameter sweeps with structured tracking
---

# Sweep Runner

## When to Use

- Searching for optimal hyperparameters
- Comparing multiple configurations systematically
- The operator says "sweep over X" or "find the best learning rate"

## Inputs

- Base config (from `configs/`)
- Parameters to sweep and their ranges
- Sweep strategy: grid, random, or bayesian
- Number of trials (for random/bayesian)
- Resource constraints (GPU hours budget)

## Steps

1. **Define sweep config:**
   Create `configs/sweeps/sweep_NNNN.yaml`:

   ```yaml
   sweep:
     name: learning_rate_sweep
     strategy: grid  # grid | random | bayesian
     base_config: configs/experiment_0001.yaml

   parameters:
     training.learning_rate:
       values: [1e-5, 3e-5, 1e-4, 3e-4, 1e-3]
     training.batch_size:
       values: [16, 32, 64]

   metric:
     name: val_loss
     goal: minimize

   budget:
     max_trials: 15
     max_gpu_hours: 24
   ```

2. **Create experiment log:**
   Create `docs/experiments/NNNN-sweep-title.md` documenting the sweep.

3. **Generate trial configs:**
   - Grid: enumerate all combinations
   - Random: sample from ranges
   - Bayesian: use W&B sweep or Optuna

4. **Run trials:**
   - Launch trials sequentially or in parallel
   - Track each trial's metrics
   - Use early stopping for clearly bad configs

5. **Collect results:**
   - Gather metrics from all trials
   - Identify best configuration
   - Save best config as `configs/best_NNNN.yaml`

6. **Update experiment log:**
   - Add results table with all trials
   - Note the winner and its metrics
   - Compare against previous best

## Output

```
## Sweep NNNN — Title
- Strategy: grid (15 trials)
- Best config: lr=3e-4, batch=32
- Best metric: val_loss=0.342 (baseline: 0.401, -14.7%)
- GPU hours used: 18.5
- Full results: docs/experiments/NNNN-sweep-title.md
- Best config saved: configs/best_NNNN.yaml
```

## Safety

- Set a GPU hours budget and respect it
- Use early stopping to avoid wasting compute
- Always save the best config to a file
- Record all trials, not just the best
- If using W&B sweeps, ensure the API key is configured (not committed)
