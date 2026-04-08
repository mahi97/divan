# CLAUDE.md — {{PROJECT_NAME}}

{{DESCRIPTION}}

## Quick Reference

- Language: {{PRIMARY_LANGUAGE}}
- Test: `scripts/test.sh` or `uv run pytest`
- Lint: `scripts/lint.sh` or `uv run ruff check .`
- Check all: `scripts/check.sh`

## Toolkit

This project uses divan (`divan/` directory). Key locations:

- `divan/skills/custom/` — skills for GPU deploy, experiments, sweeps, LaTeX, knowledge graphs
- `divan/skills/external/` — engineering workflow and library-specific skills
- `divan/docs/standards/` — coding and research standards
- `divan/docs/servers/` — bare GPU and HPC access guides
- `divan/workflows/` — research pipeline definitions

**Skill discovery rule:** Before starting work with an unfamiliar library or tool, check
`divan/skills/custom/` and `divan/skills/external/`. Run `python divan/tools/fetch_skills.py`
to pull the full catalog. If nothing exists, use `skill-seekers create <url>` to generate a
skill. See `divan/skills/custom/skill-generation/SKILL.md`.

## Key Files

- `docs/architecture.md` — system design
- `docs/commands.md` — all developer commands
- `configs/` — experiment configurations

## Rules

- Read `divan/docs/standards/agent-standards.md` for full rules
- Run `scripts/check.sh` before committing
- Use `uv` and `pyproject.toml` as the default Python workflow
- Write or update a failing test before implementing new behavior
- Commit code before running experiments
- Log experiments in `docs/experiments/`
- Keep data, cache, and checkpoint locations configurable in `configs/`
- Keep GPU selection configurable in `configs/`
- Never commit secrets, never push unless asked
- Never modify `divan/` unless working on divan itself
