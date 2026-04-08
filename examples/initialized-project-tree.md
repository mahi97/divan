# Example: Initialized Project Tree

This shows the full file tree of a project initialized with the
`research-python` profile.

## Command

```bash
python tools/init_project.py \
  --target ../my_experiment \
  --profile research-python \
  --project-name my_experiment \
  --owner research-lab \
  --description "Transformer attention pattern analysis"
```

## Resulting Tree

```
my_experiment/
├── .agents/
│   └── skills/
│       ├── README.md
│       ├── experiment-runner/
│       │   └── SKILL.md
│       ├── legacy-rewrite/
│       │   └── SKILL.md
│       ├── literature-scan/
│       │   └── SKILL.md
│       └── repo-onboarding/
│           └── SKILL.md
├── .claude/
│   ├── settings.json
│   └── skills/
│       ├── README.md
│       ├── experiment-runner/
│       │   └── SKILL.md
│       ├── legacy-rewrite/
│       │   └── SKILL.md
│       ├── literature-scan/
│       │   └── SKILL.md
│       └── repo-onboarding/
│           └── SKILL.md
├── .codex/
│   └── config.toml
├── .editorconfig
├── .gitattributes
├── .gitignore
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── docs/
│   ├── architecture.md
│   ├── commands.md
│   ├── decisions/
│   │   └── README.md
│   ├── experiments/
│   │   └── README.md
│   ├── literature/
│   │   └── README.md
│   └── roadmap.md
├── pyproject.toml
├── scripts/
│   ├── check.ps1
│   ├── check.sh
│   ├── lint.ps1
│   ├── lint.sh
│   ├── test.ps1
│   └── test.sh
├── src/
│   └── __init__.py
└── tests/
    └── test_smoke.py
```

## Sample File Content After Placeholder Rendering

### README.md (excerpt)

```markdown
# my_experiment

Transformer attention pattern analysis

## Quick Start

git clone https://github.com/research-lab/my_experiment.git
cd my_experiment
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
scripts/check.sh
```

### CLAUDE.md (excerpt)

```markdown
# CLAUDE.md — my_experiment

Transformer attention pattern analysis

## Quick Reference

- Language: Python
- Test: scripts/test.sh or pytest
- Lint: scripts/lint.sh or ruff check .
- Check all: scripts/check.sh
```

### pyproject.toml (excerpt)

```toml
[project]
name = "my_experiment"
version = "0.1.0"
description = "Transformer attention pattern analysis"
requires-python = ">=3.12"
license = "MIT"
authors = [
    { name = "research-lab" },
]
```

## Initialization Report

```
## Initialization Report
- Target: /home/user/research/my_experiment
- Profile: research-python
- Files created: 31
- Files skipped (already exist): 0
- Files overwritten: 0
- Files backed up: 0
- Placeholders: {{DESCRIPTION}} -> Transformer attention pattern analysis, ...
- Errors: none
```
