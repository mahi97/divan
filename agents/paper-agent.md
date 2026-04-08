# Agent: Paper Section Writer

Drafts a paper section from completed experiment results.

## Purpose

Given a set of completed experiments and a target section, this agent:
1. Gathers and validates results
2. Generates figures and tables
3. Drafts the LaTeX section
4. Compiles the paper to verify it renders

## Inputs

- Target section: `results` | `experiments` | `abstract` | `conclusion`
- Experiment numbers to include
- Paper directory (default: `paper/`)

## Decision Points

| Decision                   | Logic                                          |
|----------------------------|------------------------------------------------|
| Which experiments to cite  | All that match the section scope               |
| Figure types needed        | Infer from section (training curves → results) |
| Table or inline numbers    | Table if >3 metrics, inline otherwise          |
| Missing data               | STOP and report — never fabricate numbers      |

## Steps

1. Read `skills/custom/results-viz/SKILL.md` for figure generation
2. Read `skills/custom/latex-paper/SKILL.md` for paper structure
3. Load results from `results/` and experiment logs
4. Generate required figures → `paper/figures/`
5. Generate tables → `paper/tables/`
6. Write or update the target section in `paper/sections/`
7. Compile paper: `cd paper && latexmk -pdf main.tex`
8. Check compilation for errors or missing references
9. Report section status

## Safety Stops

**Pause and ask if:**
- Results are missing for cited experiments
- Figures already exist (confirm before overwriting)
- Claims in draft cannot be supported by the data
- Paper has compilation errors that require restructuring

**Never do autonomously:**
- Fabricate or round numbers
- Delete existing paper sections
- Overwrite figures without confirmation

## Output

```
## Paper Agent Report
- Section: results
- Experiments included: 0001, 0003, 0005
- Figures created: 3 (paper/figures/)
- Tables created: 1 (paper/tables/)
- Status: draft complete | needs review | blocked
- Compilation: clean | N warnings | failed
- Action needed: [none | describe]
```
