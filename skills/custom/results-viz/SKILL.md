---
name: results-viz
description: Visualize and compare experiment results
---

# Results Visualization

## When to Use

- Comparing results across experiments
- Creating figures for a paper or presentation
- The operator asks to "plot the results" or "compare experiments"

## Inputs

- Experiment numbers or result files to compare
- Metrics to visualize
- Output format: png, pdf, or interactive
- Destination: `results/figures/` or `paper/figures/`

## Steps

1. **Gather results:**
   - Read experiment logs from `docs/experiments/`
   - Load result data from `results/` or W&B
   - Identify common metrics across experiments

2. **Create comparison table:**
   ```
   | Experiment | Model    | Val Loss | Accuracy | GPU Hours |
   |------------|----------|----------|----------|-----------|
   | 0001       | baseline | 0.401    | 85.2%    | 4.2       |
   | 0002       | large    | 0.342    | 87.8%    | 12.1      |
   ```

3. **Generate plots:**

   Standard plot types:
   - **Training curves:** loss/metric vs. epoch for each experiment
   - **Bar chart:** final metric comparison across experiments
   - **Scatter plot:** metric vs. compute cost
   - **Box plot:** metric distribution across runs/seeds

   Use matplotlib or seaborn:
   ```python
   import matplotlib.pyplot as plt
   import seaborn as sns

   fig, ax = plt.subplots(figsize=(8, 5))
   # ... plot code ...
   fig.savefig("paper/figures/comparison.pdf", bbox_inches="tight", dpi=300)
   ```

4. **Save figures:**
   - For paper: `paper/figures/` in PDF format, 300+ DPI
   - For reports: `results/figures/` in PNG format
   - Name descriptively: `loss_comparison_0001_vs_0002.pdf`

5. **Update experiment log:**
   - Reference figures in the relevant experiment log
   - Add to paper if applicable

## Output

```
## Visualization Report
- Experiments compared: 0001, 0002, 0003
- Plots created:
  - paper/figures/loss_curves.pdf
  - paper/figures/metric_comparison.pdf
  - paper/figures/compute_scaling.pdf
- Key finding: Model 0002 achieves best accuracy with moderate compute
```

## Safety

- Do not overwrite existing figures without confirmation
- Use deterministic colors/styles for consistency across figures
- Always include axis labels, legends, and titles
- For paper figures: use vector format (PDF/SVG) for line plots
- Include error bars or confidence intervals where applicable
