# AGENTS.md — Divan Toolkit

You are inside `divan/`, a personal AI research toolkit. This directory lives
inside a project and provides skills, standards, and workflows for ML/AI research.

**Do not treat divan as the project itself.** The actual project is in the
parent directory (`../`).

## Read First

1. `docs/standards/agent-standards.md` — canonical rules
2. `docs/overview.md` — what divan is
3. `PROJECT_INIT_PLAYBOOK.md` — how to initialize the parent project

## If You Are Initializing the Parent Project

Follow `PROJECT_INIT_PLAYBOOK.md` or run:
```bash
bash init.sh --profile ml-research
```

## If You Are Working on the Parent Project

Go to the parent directory. Read `../AGENTS.md` or `../CLAUDE.md` there —
those files will point you back to `divan/skills/` for task-specific guidance.

## Skills

Skills are in `skills/custom/`. Each has a `SKILL.md` with:
- When to use it
- Required inputs
- Step-by-step procedure
- Expected output format
- Safety notes

## Do Not

- Do not add project code to divan
- Do not modify skills without understanding their purpose
- Do not run GPU jobs without confirming server and resources
- Do not delete experiment logs
