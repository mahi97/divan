---
name: latex-paper
description: Write, compile, and manage LaTeX research papers
---

# LaTeX Paper

## When to Use

- Starting a new research paper
- Adding results or sections to an existing paper
- Compiling and checking the paper
- Managing references and figures

## Inputs

- Paper title and target venue (conference/journal)
- Results to include (from experiment logs)
- Figures to include (from `paper/figures/`)

## Steps

### Setting Up a New Paper

1. **Create paper directory:**
   ```
   paper/
     main.tex            # Main LaTeX file
     references.bib      # BibTeX references
     figures/             # Paper figures
     sections/            # Optional: split sections into files
       introduction.tex
       method.tex
       experiments.tex
       results.tex
       conclusion.tex
   ```

2. **Use a standard template:**
   Start with the target venue's template (NeurIPS, ICML, ACL, etc.).
   Or use a minimal template:
   ```latex
   \documentclass{article}
   \usepackage{amsmath,graphicx,hyperref,booktabs}
   \title{{{PAPER_TITLE}}}
   \author{{{AUTHOR}}}
   \begin{document}
   \maketitle
   \begin{abstract}
   ...
   \end{abstract}
   \input{sections/introduction}
   \input{sections/method}
   \input{sections/experiments}
   \input{sections/results}
   \input{sections/conclusion}
   \bibliographystyle{plain}
   \bibliography{references}
   \end{document}
   ```

### Adding Results

3. **Generate tables from data:**
   Write a script to generate LaTeX tables from result files:
   ```python
   # scripts/generate_tables.py
   # Reads results/ and outputs paper/tables/results.tex
   ```
   Use `\input{tables/results.tex}` in the paper.

4. **Reference figures:**
   ```latex
   \begin{figure}[t]
     \centering
     \includegraphics[width=\linewidth]{figures/loss_curves.pdf}
     \caption{Training loss curves comparing...}
     \label{fig:loss-curves}
   \end{figure}
   ```

### Compiling

5. **Compile the paper:**
   ```bash
   cd paper
   pdflatex main.tex
   bibtex main
   pdflatex main.tex
   pdflatex main.tex
   ```
   Or with latexmk:
   ```bash
   latexmk -pdf main.tex
   ```

6. **Check for issues:**
   - Missing references (look for `??` in output)
   - Overfull hboxes
   - Missing figures

### Managing References

7. **Add BibTeX entries:**
   - Use Google Scholar "Cite" → BibTeX
   - Use `divan/skills/custom/literature-scan/` to find papers
   - Keep `references.bib` sorted by citation key

## Output

```
## Paper Status Report
- Title: [paper title]
- Pages: [count]
- Sections complete: intro ✓, method ✓, experiments ~, results ✗
- Figures: 5 included, 2 pending
- References: 23
- Compilation: clean (no warnings)
- PDF: paper/main.pdf
```

## Safety

- Never delete paper source files
- Commit frequently — LaTeX is hard to recover from mistakes
- Do not regenerate figures without confirmation
- Keep backup of references.bib
- Track paper drafts in git, not with filename versioning (no `main_v2_final.tex`)
