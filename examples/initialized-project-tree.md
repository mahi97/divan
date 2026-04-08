# Example: Initialized Project Tree

Full tree after `bash divan/init.sh --profile ml-research --project-name attention_study --owner mahi`

## Command Run

```bash
cd ~/research/attention_study
git clone https://github.com/mahi/divan.git
cd divan && bash init.sh \
  --profile ml-research \
  --project-name attention_study \
  --owner mahi \
  --description "Attention pattern analysis in transformer models"
```

## Resulting Tree

```text
attention_study/
├── divan/                             ← your toolkit (stays here)
│   ├── init.sh
│   ├── skills/custom/
│   │   ├── gpu-deploy/SKILL.md
│   │   ├── hpc-submit/SKILL.md
│   │   ├── experiment-runner/SKILL.md
│   │   ├── sweep-runner/SKILL.md
│   │   ├── monitoring-setup/SKILL.md
│   │   ├── results-viz/SKILL.md
│   │   ├── latex-paper/SKILL.md
│   │   └── ...
│   ├── docs/servers/
│   │   ├── bare-gpu.md   ← fill in your server details
│   │   └── hpc-pbs.md    ← fill in your cluster details
│   └── workflows/
│       ├── train-evaluate.md
│       ├── sweep-and-select.md
│       └── experiment-to-paper.md
│
├── AGENTS.md                          ← created by init
├── CLAUDE.md                          ← created by init
├── README.md                          ← created by init
├── .gitignore                         ← created by init (divan/ is excluded)
├── .editorconfig
├── .gitattributes
│
├── pyproject.toml                     ← ml-research profile
├── src/
│   ├── __init__.py
│   ├── train.py                       ← training entry point
│   ├── evaluate.py                    ← evaluation entry point
│   └── utils/
│       └── config.py
│
├── tests/
│   └── test_smoke.py
│
├── configs/
│   ├── base.yaml                      ← base experiment config
│   └── sweeps/
│       └── template.yaml
│
├── docs/
│   ├── architecture.md
│   ├── commands.md
│   ├── roadmap.md
│   ├── decisions/README.md
│   ├── experiments/README.md          ← logs go here
│   └── literature/README.md
│
├── scripts/
│   ├── check.sh  / check.ps1
│   ├── test.sh   / test.ps1
│   ├── lint.sh   / lint.ps1
│   └── jobs/
│       └── train.pbs                  ← HPC job script
│
├── paper/
│   ├── main.tex
│   └── references.bib
│
├── .claude/
│   ├── settings.json
│   └── skills/
│       ├── repo-onboarding/SKILL.md
│       ├── experiment-runner/SKILL.md
│       └── ...
│
├── .agents/skills/
│   └── ...
│
└── .codex/config.toml
```

## Initialization Report

```text
## Initialization Report
- Target: /home/mahi/research/attention_study
- Profile: ml-research
- Files created: 43
- Files skipped (already exist): 0
- Files overwritten: 0
- Files backed up: 0
- Placeholders: {{PROJECT_NAME}}=attention_study, {{OWNER}}=mahi,
                {{DESCRIPTION}}=Attention pattern analysis..., {{YEAR}}=2026
- Errors: none
```

## What to Do Next

1. Fill in server details in `divan/docs/servers/bare-gpu.md` (your GPU server)
   and `divan/docs/servers/hpc-pbs.md` (your HPC cluster).

2. Set up Python environment:
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -e ".[ml]"
   ```

3. Configure monitoring:
   ```bash
   cp .env.example .env   # create if needed
   echo "WANDB_API_KEY=your_key" >> .env
   ```

4. Run smoke test:
   ```bash
   scripts/check.sh
   ```

5. Start first experiment:
   ```bash
   # Follow divan/workflows/train-evaluate.md
   # or ask your AI agent to use the experiment-runner skill
   ```
