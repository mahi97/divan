# Agent: Experiment Runner

Autonomously runs an experiment from config to logged results.

## Purpose

Given a hypothesis and config, this agent:
1. Creates the experiment log
2. Validates and commits code
3. Deploys and runs on the appropriate server
4. Monitors for completion or failure
5. Pulls results and updates the log

## Inputs

- Experiment hypothesis (or config file path)
- Target server: `local` | `bare-gpu` | `hpc`
- Resource requirements (if non-default)

## Decision Points

| Decision                  | Logic                                         |
|---------------------------|-----------------------------------------------|
| Which server to use       | Check input; if unspecified, ask operator     |
| Config exists?            | If yes, use it; if no, create from hypothesis |
| Tests passing?            | If not, STOP and report                       |
| Job finished?             | Poll every 10 min; timeout after walltime     |
| Results look valid?       | Check for NaN, all-zero metrics, no output    |

## Steps

1. Read `skills/custom/experiment-runner/SKILL.md`
2. Create experiment log (steps 1-3 of skill)
3. Ensure code is committed
4. Select and run deploy skill based on target server
5. Monitor until complete or failed (check logs, qstat, tmux)
6. Pull results to local `results/`
7. Update experiment log with metrics and status
8. Produce summary report

## Safety Stops

**Pause and ask the operator if:**
- Tests are failing before the experiment starts
- GPU memory is insufficient for the config
- Walltime estimate exceeds 24 hours without confirmation
- Results contain NaN or obviously invalid metrics
- The job was killed or failed unexpectedly

**Never do autonomously:**
- Delete experiment data
- Commit and push code
- Run compute on an HPC login node
- Overwrite a running experiment's config

## Output

```
## Experiment Agent Report
- Experiment: NNNN
- Status: completed | failed | aborted
- Key metric: [value]
- Server used: [name]
- Job ID: [if HPC]
- Log: docs/experiments/NNNN-title.md
- Action needed: [none | describe what operator should do]
```
