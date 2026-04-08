# AGENTS.md — {{PROJECT_NAME}}

## Project

- **Name:** {{PROJECT_NAME}}
- **Owner:** {{OWNER}}
- **Language:** {{PRIMARY_LANGUAGE}}
- **Description:** {{DESCRIPTION}}

## Read First

1. `README.md` — project overview and setup
2. `docs/architecture.md` — system design
3. `docs/commands.md` — how to build, test, lint

## Rules

- Follow existing code conventions. Do not introduce new patterns without reason.
- Run `scripts/check.sh` before committing.
- Write tests for new functionality.
- Do not commit secrets (.env, credentials, keys).
- Do not push to remote unless explicitly asked.
- Produce a short report after significant changes.

## Testing

```bash
scripts/test.sh
```

## Linting

```bash
scripts/lint.sh
```

## Structure

```
{{PROJECT_NAME}}/
  src/               # Source code
  tests/             # Tests
  docs/              # Documentation
  scripts/           # Build/test/lint scripts
```
