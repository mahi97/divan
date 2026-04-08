# Agent Standards — Canonical Source of Truth

Rules and conventions for AI agents operating on projects that use divan.
All agent-facing files (AGENTS.md, CLAUDE.md) derive from this document.

---

## 1. Safety

- **Never silently overwrite files.** Check if a file exists first. Skip and
  report unless `--force` is explicitly passed.
- **Never delete files** unless explicitly instructed and confirmed.
- **Never commit secrets.** Refuse to stage `.env`, `credentials.json`, `*.pem`,
  `*.key`, SSH keys, API tokens. Warn the operator if asked.
- **Never push to remote** unless explicitly asked. A commit is not a push.
- **Never kill running experiments** unless explicitly asked.
- **Dry-run first** for destructive or large-scale operations.
- **Never run GPU jobs** without confirming the target server and resource request.

## 2. Project Structure

Projects using divan should converge toward this layout:

```
project_root/
  divan/                     # Divan toolkit (do not modify carelessly)
  README.md                  # Required
  AGENTS.md                  # Required — points agents to divan/
  CLAUDE.md                  # Required — points Claude to divan/
  src/ or <package>/         # Source code
  tests/                     # Tests
  configs/                   # Experiment configs (YAML/TOML)
  docs/
    architecture.md          # Required — system design
    commands.md              # Required — developer commands
    experiments/             # Experiment logs
    literature/              # Reading notes
    decisions/               # Architectural decisions
  scripts/
    check.sh / check.ps1    # Lint + test
    test.sh  / test.ps1     # Run tests
    lint.sh  / lint.ps1     # Run linter
  data/                      # Local data (gitignored if large)
  results/                   # Experiment results (gitignored if large)
  notebooks/                 # Jupyter notebooks (optional)
```

## 3. Divan Awareness

Agents must know that `divan/` is a toolkit directory, not project code.

- **Read skills from** `divan/skills/custom/` — these define how to perform tasks
- **Read standards from** `divan/docs/standards/` — these define conventions
- **Read server docs from** `divan/docs/servers/` — these define compute access
- **Read workflows from** `divan/workflows/` — these define multi-step pipelines
- **Never modify divan/ files** unless explicitly working on divan itself
- **Never add project code to divan/**

## 4. Placeholder Conventions

Template files use these placeholders. Agents must replace all of them:

| Placeholder            | Example value          | Description                    |
|------------------------|------------------------|--------------------------------|
| `{{PROJECT_NAME}}`     | `attention_paper`      | Repo/directory name            |
| `{{OWNER}}`            | `mahi`                 | GitHub username or org         |
| `{{DESCRIPTION}}`      | `Attention analysis…`  | One-line project description   |
| `{{PRIMARY_LANGUAGE}}` | `Python`               | Main language                  |
| `{{PYTHON_VERSION}}`   | `3.12`                 | Python version                 |
| `{{LICENSE}}`          | `MIT`                  | License identifier             |
| `{{YEAR}}`             | `2026`                 | Copyright year                 |

After initialization, no `{{…}}` placeholders should remain.

## 5. Coding Standards

- PEP 8 with `ruff` for formatting. Line length: 88.
- Type hints on all public functions.
- Prefer `pathlib` over `os.path`.
- Prefer stdlib. Minimize external dependencies.
- No comments that restate the code. Comment non-obvious decisions only.
- `TODO(name):` for planned work. `HACK:` for intentional workarounds.
- Never leave commented-out code. Delete it.

## 6. Testing

- `tests/` directory, `pytest` as runner.
- Test files mirror source: `src/foo/bar.py` → `tests/foo/test_bar.py`.
- Every module should have at least a smoke test.
- CI runs tests on every push and PR.

## 7. Experiment Management

- Log experiments in `docs/experiments/NNNN-title.md`.
- Record: hypothesis, setup (commit hash, config, hardware), results, conclusion.
- Never delete experiment logs. Mark failed experiments as failed.
- Commit code before running experiments. Record the commit hash.
- Store configs in `configs/` as YAML or TOML.

## 8. GPU Server Rules

### Bare GPU Server (SSH)
- Always check GPU availability before launching (`nvidia-smi`).
- Use `tmux` or `screen` for long-running jobs.
- Clean up after yourself — kill orphan processes, free GPU memory.
- Use environment variables or config files for server-specific paths.

### HPC Cluster (PBS/Torque)
- Always submit jobs via `qsub`. Never run compute on the login node.
- Use job scripts, not interactive commands, for reproducibility.
- Monitor with `qstat`. Clean up with `qdel` when needed.
- Respect queue policies — check node availability before large submissions.
- Store job scripts in `scripts/jobs/` for reproducibility.

## 9. Safe Refactoring

- Ensure tests exist and pass before refactoring.
- Refactor in small steps. Commit after each.
- Never combine refactoring with feature work.
- For legacy code: preserve behavior first, improve structure second.

## 10. Long-Running Task Rules

- Break work into verifiable steps.
- After each step, verify before proceeding.
- Report progress at checkpoints.
- If stuck for 3+ attempts on the same problem, stop and report.
- For GPU jobs: monitor resource usage, set timeouts, check for hangs.

## 11. Agent Output Format

After any significant operation, produce a short report:

```
## Report
- Action: [what was done]
- Files created: [count]
- Files modified: [count]
- Files skipped: [count]
- Server: [if applicable]
- Warnings: [any issues or none]
```
