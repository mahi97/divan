# CLAUDE.md — {{PROJECT_NAME}}

{{DESCRIPTION}}

## Quick Reference

- Language: {{PRIMARY_LANGUAGE}}
- Test: `scripts/test.sh` or `pytest`
- Lint: `scripts/lint.sh` or `ruff check .`
- Check all: `scripts/check.sh`

## Toolkit

This project uses divan (`divan/` directory). Key locations:

- `divan/skills/custom/` — skills for GPU deploy, experiments, sweeps, LaTeX
- `divan/docs/standards/` — coding and research standards
- `divan/docs/servers/` — bare GPU and HPC access guides
- `divan/workflows/` — research pipeline definitions

## Key Files

- `docs/architecture.md` — system design
- `docs/commands.md` — all developer commands
- `configs/` — experiment configurations

## Rules

- Read `divan/docs/standards/agent-standards.md` for full rules
- Run `scripts/check.sh` before committing
- Commit code before running experiments
- Log experiments in `docs/experiments/`
- Never commit secrets, never push unless asked
- Never modify `divan/` unless working on divan itself
