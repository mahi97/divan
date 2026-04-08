# Workflow: New Project Setup

Complete setup sequence for a new ML research project.

---

## Steps

1. **Clone divan into project**
   ```bash
   mkdir my_project && cd my_project
   git init
   git clone https://github.com/YOUR_USER/divan.git
   ```

2. **Run init** → `PROJECT_INIT_PLAYBOOK.md`
   ```bash
   cd divan && bash init.sh --profile ml-research
   ```
   This copies docs, scripts, AGENTS.md, CLAUDE.md to `../`

3. **Fill in server details**
   - Edit `divan/docs/servers/bare-gpu.md` with your server info
   - Edit `divan/docs/servers/hpc-pbs.md` with your cluster info

4. **Set up Python environment** → `skills/custom/project-setup`
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -e ".[dev]"
   ```

5. **Create initial project structure**
   - Write `docs/architecture.md` — what this project will build
   - Create `configs/base.yaml` — base experiment config
   - Create `src/__init__.py` and entry point

6. **Set up monitoring** → `skills/custom/monitoring-setup`
   - Configure W&B project
   - Set up `.env` with API keys

7. **First smoke test**
   ```bash
   scripts/check.sh
   ```

8. **First commit**
   ```bash
   git add -A && git commit -m "Initialize project from divan template"
   ```

## Checklist

- [ ] divan cloned inside project
- [ ] init.sh run (AGENTS.md, CLAUDE.md, scripts created in parent)
- [ ] Server docs filled in
- [ ] Python environment working
- [ ] Monitoring configured
- [ ] `scripts/check.sh` passes
- [ ] Initial commit made
