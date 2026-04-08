---
name: experiment-runner
description: Run an experiment and produce a structured log entry
---

# Experiment Runner

## When to Use

Use this skill when:
- Running a new experiment
- Comparing results against a baseline
- The operator asks to "try X and see what happens"

## Inputs

- Experiment description or hypothesis
- Configuration (parameters, dataset, etc.)
- Baseline to compare against (optional)

## Steps

1. **Create experiment log:**
   - Determine the next experiment number (scan `docs/experiments/`)
   - Create `docs/experiments/NNNN-short-title.md`
   - Fill in hypothesis and setup sections

2. **Record environment:**
   - Python version
   - Key dependency versions
   - Hardware details (if relevant)
   - Current git commit hash

3. **Run the experiment:**
   - Execute the specified command or script
   - Capture stdout/stderr
   - Record timing

4. **Record results:**
   - Update the experiment log with results
   - Add metrics table
   - Compare against baseline if provided

5. **Conclude:**
   - Update status (completed/failed)
   - Write conclusion
   - Suggest follow-up experiments if appropriate

## Output Format

The experiment log file (`docs/experiments/NNNN-title.md`) serves as the output.
Additionally, print a summary:

```
## Experiment NNNN — Title
- Status: completed
- Key metric: X (baseline: Y, delta: +Z%)
- Conclusion: one sentence
- Log: docs/experiments/NNNN-title.md
```

## Safety Notes

- Always commit code before running experiments.
- Record the exact commit hash in the experiment log.
- Never modify experiment logs after completion — add a new experiment instead.
- If the experiment modifies data files, note it in the log.
