# Example: Workspace Layout

Divan lives **inside** each project as `project/divan/`.

---

## Single Project

```text
~/research/
  attention_paper/             ← your ML research project (git repo)
    divan/                     ← cloned inside (your toolkit)
      skills/custom/           ← GPU deploy, experiments, paper, etc.
      docs/servers/            ← your server configs
      bootstrap/               ← files copied to parent on init
      tools/init_project.py
    src/
      train.py
      model.py
      data.py
    tests/
    configs/
      base.yaml
      experiment_0001.yaml
    docs/
      architecture.md
      experiments/
        0001-baseline.md
    scripts/
      check.sh
      jobs/
        train.pbs
    paper/
      main.tex
    AGENTS.md                  ← created by init, points to divan/
    CLAUDE.md                  ← created by init
    .gitignore                 ← created by init (includes divan/)
    pyproject.toml
```

## Multiple Projects

```text
~/research/
  attention_paper/
    divan/           ← clone of your divan
    src/
    ...

  scaling_laws/
    divan/           ← same divan repo, independent clone
    src/
    ...

  benchmark_suite/
    divan/           ← same divan repo, independent clone
    src/
    ...
```

Each project gets its own divan clone. Update all at once:

```bash
for dir in ~/research/*/divan; do
  echo "Updating $dir..."
  (cd "$dir" && git pull)
done
```

## Initialization Commands

```bash
# New ML research project
mkdir ~/research/my_experiment && cd ~/research/my_experiment
git init
git clone https://github.com/YOUR_USER/divan.git
cd divan && bash init.sh --profile ml-research

# Existing project (safe — skips existing files)
cd ~/research/existing_project
git clone https://github.com/YOUR_USER/divan.git
cd divan && bash init.sh --profile base --backup

# LLM research project
mkdir ~/research/llm_eval && cd ~/research/llm_eval
git init
git clone https://github.com/YOUR_USER/divan.git
cd divan && bash init.sh --profile llm-research
```

## What Gets Created in the Parent Project

After `bash init.sh --profile ml-research`:

```text
my_project/
  README.md          ← from bootstrap (placeholder-rendered)
  AGENTS.md          ← from bootstrap
  CLAUDE.md          ← from bootstrap
  .gitignore         ← from bootstrap (includes divan/)
  .editorconfig
  .gitattributes
  pyproject.toml     ← from ml-research profile
  src/
    __init__.py
    train.py
    evaluate.py
    utils/config.py
  tests/
    test_smoke.py
  configs/
    base.yaml
    sweeps/
      template.yaml
  docs/
    architecture.md
    commands.md
    roadmap.md
    decisions/README.md
    experiments/README.md
    literature/README.md
  scripts/
    check.sh / check.ps1
    test.sh  / test.ps1
    lint.sh  / lint.ps1
    jobs/
      train.pbs
  paper/
    main.tex
    references.bib
  .claude/
    settings.json
    skills/...
  .agents/skills/...
  .codex/config.toml
```
