---
name: graphify
description: Build a queryable knowledge graph from code, docs, and papers in the current project
---

# Skill: Graphify — Knowledge Graph Generation

Use to transform a research codebase, documentation, or paper collection into an interactive,
queryable knowledge graph that reveals relationships between concepts, modules, and results.

## When to Use

- Onboarding to a large, unfamiliar codebase
- Mapping relationships between research papers and code modules
- Exploring which experiments depend on which components
- Generating a visual overview of the project's architecture
- Finding connections between concepts across docs and source files

## Inputs

- **Source**: directory to analyze (default: `.`, the project root)
- **Output directory**: where to write graph files (default: `./graph_output/`)
- **Focus** (optional): subdirectory or file pattern to limit scope

## Steps

### Step 1 — Install graphify

```bash
pip install graphifyy
```

### Step 2 — Generate the knowledge graph

```bash
# Full project graph
graphify --source . --output graph_output/

# Limit to src/ and docs/
graphify --source src/ docs/ --output graph_output/

# Focus on a specific component
graphify --source src/models/ --output graph_output/models/
```

### Step 3 — Review outputs

Graphify produces three artifacts:

| File | Description |
|------|-------------|
| `graph_output/graph.html` | Interactive visual graph (open in browser) |
| `graph_output/GRAPH_REPORT.md` | Markdown summary of nodes, clusters, key connections |
| `graph_output/graph.json` | Raw graph data (nodes + edges) for programmatic use |

Open `graph.html` in a browser to explore interactively. Read `GRAPH_REPORT.md` for
a text summary.

### Step 4 — Use the graph for research tasks

Common queries once the graph is built:
- Find all modules that depend on `src/models/base.py`
- Identify which docs reference experiment `0042`
- List papers connected to a given concept (e.g., "attention")
- Trace the data flow from `data/` to `results/`

### Step 5 — Regenerate as the project grows

Re-run graphify when significant new code or docs are added:

```bash
graphify --source . --output graph_output/
```

Consider adding to `scripts/check.sh` for continuous graph updates.

## Output

```
graph_output/
  graph.html       ← open in browser for interactive exploration
  GRAPH_REPORT.md  ← text summary of the knowledge graph
  graph.json       ← raw graph data (nodes + edges)
```

## Invocation Shortcut

This skill can also be invoked via the `/graphify` command in Claude Code.

## Safety

- Graphify only reads files; it never modifies the project.
- Exclude sensitive directories (e.g., `.env`, credentials) from the source scope.
- `graph.json` may contain source code snippets — treat as internal, do not share publicly.

## Notes

Graphify (`pip install graphifyy`) builds a NetworkX knowledge graph from code structure,
docstrings, comments, and Markdown documents. Particularly useful for ML research repos
where relationships between papers, experiments, and code modules are complex.

See: https://github.com/safishamsi/graphify
