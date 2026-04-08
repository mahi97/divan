# Documentation Standards

These standards define what documentation every project must have and how it
should be written.

---

## Required Documents

| Document                | Location                  | Purpose                               |
|-------------------------|---------------------------|---------------------------------------|
| Project README          | `README.md`               | Purpose, setup, quick start           |
| Architecture overview   | `docs/architecture.md`    | System design, components, data flow  |
| Commands reference      | `docs/commands.md`        | Every developer command, copy-paste   |

These three files are non-negotiable. A project without them is not ready for
collaboration.

## Optional Documents

| Document              | Location                          | When to create                    |
|-----------------------|-----------------------------------|-----------------------------------|
| Roadmap               | `docs/roadmap.md`                 | When planning future work         |
| Decision records      | `docs/decisions/NNNN-title.md`    | When making architectural choices |
| Experiment logs       | `docs/experiments/NNNN-title.md`  | When running experiments          |
| Literature notes      | `docs/literature/NNNN-title.md`   | When reading papers/references    |

## Writing Style

1. **Be concise.** Say what needs to be said, then stop.
2. **Be specific.** Use exact file paths, command lines, and version numbers.
3. **Be current.** Outdated docs are worse than no docs. Delete or update.
4. **Use examples.** A single concrete example beats a paragraph of explanation.
5. **Use copy-paste commands.** Readers should be able to run commands directly.

## README Structure

Every README should have these sections, in order:

```markdown
# Project Name

One-line description.

## Overview

2-3 sentences about what this project does and why it exists.

## Quick Start

Step-by-step setup instructions with copy-paste commands.

## Usage

How to use the project after setup.

## Development

How to run tests, lint, and contribute.

## License

License identifier and link.
```

## Architecture Document

`docs/architecture.md` should contain:

1. **System overview** — what the system does, at a high level.
2. **Component diagram** — text-based (Mermaid or ASCII) showing major parts.
3. **Key decisions** — why the system is structured this way.
4. **Data flow** — how data moves through the system.
5. **Dependencies** — external services, databases, APIs.

Keep it under 300 lines. Link to decision records for detailed rationale.

## Commands Document

`docs/commands.md` is a flat list of every command a developer needs:

```markdown
## Setup
pip install -e ".[dev]"

## Run tests
pytest

## Lint
ruff check .

## Format
ruff format .

## Build
python -m build
```

No prose between commands. Group by task. Use headings as labels.

## Decision Records

Format for `docs/decisions/NNNN-title.md`:

```markdown
# NNNN — Title

**Date:** YYYY-MM-DD
**Status:** accepted | superseded by NNNN | deprecated

## Context

What is the situation that requires a decision?

## Decision

What did we decide?

## Consequences

What are the expected effects — positive and negative?
```

## Experiment Logs

Format for `docs/experiments/NNNN-title.md`:

```markdown
# NNNN — Title

**Date:** YYYY-MM-DD
**Status:** running | completed | failed | abandoned

## Hypothesis

What are we testing?

## Setup

How to reproduce this experiment.

## Results

What happened?

## Conclusion

What did we learn? What's next?
```

## Literature Notes

Format for `docs/literature/NNNN-title.md`:

```markdown
# NNNN — Short Title

**Citation:** Author(s), "Title", Venue, Year. [link]

## Key Takeaways

- Bullet points of the most important ideas.

## Relevance

How does this relate to our project?

## Notes

Any additional observations.
```
