# Experiment Runner

Run an experiment and produce a structured log entry.

## When to Use

- Running a new experiment
- Comparing results against a baseline

## Steps

1. Create `docs/experiments/NNNN-title.md` with hypothesis and setup
2. Record environment (Python version, deps, hardware, git commit)
3. Run the experiment, capture output and timing
4. Record results and metrics in the log
5. Write conclusion, suggest follow-ups

## Output

The experiment log file plus a one-line summary:
`Experiment NNNN — Status: completed — Key metric: X`

## Safety

- Commit code before running experiments
- Record exact commit hash
- Never modify completed experiment logs
