# Example: Workspace Layout

This shows how a typical divan workspace looks on disk.

## Fresh Workspace

```
~/research/
  divan/                          ← template repo (cloned once)
    README.md
    AGENTS.md
    CLAUDE.md
    TEMPLATE_USAGE.md
    PROJECT_INIT_PLAYBOOK.md
    docs/
      standards/                  ← canonical rules
      templates/                  ← document templates
    bootstrap/
      common/                     ← files for every project
      profiles/                   ← project-type overlays
    tools/
      init_project.py             ← initializer
      validate_template.py        ← self-checker
```

## After Initializing Two Projects

```
~/research/
  divan/                          ← template repo (unchanged)

  image_classifier/               ← initialized with research-python
    README.md
    AGENTS.md
    CLAUDE.md
    pyproject.toml
    src/
      __init__.py
    tests/
      test_smoke.py
    docs/
      architecture.md
      commands.md
      roadmap.md
      experiments/
      literature/
      decisions/
    scripts/
      check.sh
      test.sh
      lint.sh
    .claude/
    .agents/

  prompt_eval/                    ← initialized with llm-research
    README.md
    AGENTS.md
    CLAUDE.md
    docs/
      architecture.md
      commands.md
      experiments/
      literature/
    scripts/
      check.sh
      test.sh
      lint.sh
    .claude/
    .agents/
```

## Retrofitted Legacy Project

```
~/research/
  divan/

  old_scraper/                    ← existing project, retrofitted with base
    scraper.py                    ← existing code (untouched)
    utils.py                      ← existing code (untouched)
    requirements.txt              ← existing file (untouched)
    README.md                     ← ADDED by divan
    AGENTS.md                     ← ADDED
    CLAUDE.md                     ← ADDED
    docs/
      architecture.md             ← ADDED
      commands.md                 ← ADDED
    scripts/
      check.sh                    ← ADDED
      test.sh                     ← ADDED
      lint.sh                     ← ADDED
    .claude/                      ← ADDED
    .agents/                      ← ADDED
```

## Commands Used

```bash
# Initialize image_classifier
python divan/tools/init_project.py \
  --target image_classifier \
  --profile research-python \
  --project-name image_classifier \
  --owner mylab

# Initialize prompt_eval
python divan/tools/init_project.py \
  --target prompt_eval \
  --profile llm-research \
  --project-name prompt_eval \
  --owner mylab

# Retrofit old_scraper
python divan/tools/init_project.py \
  --target old_scraper \
  --profile base \
  --project-name old_scraper \
  --owner mylab \
  --backup
```
