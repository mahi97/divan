# Workflow: Sweep → Select Best → Final Run

Hyperparameter search followed by a final run with the best configuration.

---

## Steps

1. **Define sweep** → `skills/custom/sweep-runner` (steps 1-2)
   - Write `configs/sweeps/sweep_NNNN.yaml`
   - Create experiment log for the sweep

2. **Run sweep trials**
   - Submit all trials (local, GPU, or HPC)
   - Monitor progress

3. **Collect and compare results** → `skills/custom/results-viz`
   - Gather metrics from all trials
   - Produce comparison table

4. **Select best config**
   - Identify winner based on validation metric
   - Save as `configs/best_NNNN.yaml`
   - Document in experiment log

5. **Final training run** → `workflows/train-evaluate`
   - Use best config for a full run (often longer walltime)
   - Apply multiple seeds if needed for statistical robustness

6. **Report**
   - Document sweep results and final run in experiment log
   - Generate figures for paper

## Checklist

- [ ] Sweep config written and committed
- [ ] All trials completed (or stopped early intentionally)
- [ ] Best config saved to `configs/best_NNNN.yaml`
- [ ] Final run completed with best config
- [ ] Results compared to baseline
- [ ] Experiment log updated
