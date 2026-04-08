---
name: project-setup
description: Set up a Python project environment with proper dependencies and tooling
---

# Project Setup

## When to Use

- Setting up a new project from scratch
- Setting up the development environment on a new machine
- The operator says "set up this project" or "install dependencies"

## Inputs

- Python version requirement (default: 3.12)
- Project type: ml-research, llm-research, general-python
- Key dependencies needed

## Steps

1. **Install and verify `uv`:**
   ```bash
   uv --version
   ```
   If missing, install `uv` first. Use `uv` as the default workflow for all Python projects.

2. **Check Python version:**
   ```bash
   uv python list
   ```
   Choose the required interpreter version if it is not already available.

3. **Ensure `pyproject.toml` exists:**
   Keep project metadata, dependencies, and tool configuration in `pyproject.toml`.
   If no `pyproject.toml` exists, create one from the profile templates.

4. **Sync the environment with `uv`:**
   ```bash
   uv sync --extra dev
   ```
   Add profile extras as needed, for example:
   ```bash
   uv sync --extra dev --extra ml
   uv sync --extra dev --extra ml --extra llm
   ```

5. **Install divan meta-tools (optional but recommended):**
   ```bash
   # Skill generation from any doc source (fallback when no skill exists)
   uv tool install skill-seekers

   # Knowledge graph generation for code + docs + papers
   uv tool install graphifyy
   ```

6. **Verify setup:**
   ```bash
   scripts/check.sh  # Should pass lint + tests
   uv run python -c "import torch; print(torch.cuda.is_available())"  # GPU check
   ```

7. **Create `.env` for secrets (if needed):**
   ```bash
   touch .env
   echo "WANDB_API_KEY=your_key_here" >> .env
   echo "HF_TOKEN=your_token_here" >> .env
   ```
   Ensure `.env` is in `.gitignore`.

8. **Adopt TDD from the start:**
   Write or update a failing test before adding new behavior. Keep `pytest` as the default test runner and execute it through `uv run`.

## Output

```
## Setup Report
- Python: 3.12.x
- Environment: managed by uv
- Dependencies: installed (X packages)
- Dev tools: ruff, pytest, mypy
- GPU: available (NVIDIA A100, CUDA 12.x) | not available
- Tests: passing
- Lint: clean
```

## Safety

- Never fall back to ad hoc global `pip install` for project dependencies
- Never commit `.env` or API keys
- Pin major versions of critical dependencies (torch, transformers)
- Check GPU driver compatibility before installing CUDA-dependent packages
