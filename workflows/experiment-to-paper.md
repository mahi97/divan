# Workflow: Experiment → Paper Section

Turn completed experiment results into a paper section with figures and tables.

---

## Prerequisites

- At least one completed experiment with results
- Paper LaTeX source exists in `paper/`

## Steps

1. **Gather results**
   - Identify which experiments to include
   - Load metrics from `results/` or W&B
   - Compare experiments to baseline

2. **Generate figures** → `skills/custom/results-viz`
   - Training curves
   - Metric comparison bar chart
   - Any ablation study plots
   - Save to `paper/figures/`

3. **Generate tables**
   - Write `scripts/generate_tables.py` if not exists
   - Run to produce `paper/tables/results.tex`
   - Include error bars / std across seeds

4. **Write paper section** → `skills/custom/latex-paper`
   - Write results section in `paper/sections/results.tex`
   - Reference figures and tables
   - Describe findings without over-interpreting

5. **Compile paper**
   - `cd paper && latexmk -pdf main.tex`
   - Check for missing references, overfull boxes

6. **Review**
   - Verify all claims are supported by the data
   - Check figure captions are complete
   - Ensure reproducibility details are included

## Checklist

- [ ] All relevant experiments completed
- [ ] Figures generated and saved to `paper/figures/`
- [ ] Tables generated and saved to `paper/tables/`
- [ ] Results section written
- [ ] Paper compiles cleanly
- [ ] Claims are supported by data
