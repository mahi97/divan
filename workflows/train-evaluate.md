# Workflow: Train → Evaluate → Log

Standard cycle for running a single experiment from scratch.

---

## Steps

1. **Setup** → `skills/custom/project-setup`
   - Verify environment is active and deps are installed
   - Verify GPU availability on target server

2. **Create experiment log** → `skills/custom/experiment-runner` (step 1-3)
   - Create `docs/experiments/NNNN-title.md`
   - Write hypothesis and config
   - Commit code

3. **Deploy** → depends on target:
   - Local: skip deploy
   - Bare GPU: `skills/custom/gpu-deploy`
   - HPC: `skills/custom/hpc-submit`

4. **Monitor training** → `skills/custom/monitoring-setup`
   - Confirm monitoring is running (W&B/TensorBoard)
   - Watch for crashes or OOM in first 100 steps

5. **Evaluate**
   - Run evaluation script on best checkpoint
   - Record metrics (loss, accuracy, perplexity, etc.)

6. **Update experiment log** → `skills/custom/experiment-runner` (steps 7-8)
   - Add results to `docs/experiments/NNNN-title.md`
   - Mark status as completed

7. **Visualize** (optional) → `skills/custom/results-viz`
   - Generate comparison plot vs. baseline

## Checklist

- [ ] Environment set up
- [ ] GPU available on target server
- [ ] Config committed
- [ ] Experiment log created
- [ ] Training completed without crash
- [ ] Evaluation run and metrics recorded
- [ ] Experiment log updated and committed
