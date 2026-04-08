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

1. **Check Python version:**
   ```bash
   python3 --version
   ```
   If wrong version, recommend pyenv or system install.

2. **Create virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   # .venv\Scripts\Activate.ps1  # Windows
   ```

3. **Install project in dev mode:**
   ```bash
   pip install -e ".[dev]"
   ```
   If no pyproject.toml exists, create one (see profile templates).

4. **Install ML dependencies (if ml-research):**
   ```bash
   pip install torch torchvision  # or tensorflow
   pip install numpy pandas scikit-learn
   pip install wandb tensorboard
   pip install matplotlib seaborn
   ```

5. **Install LLM dependencies (if llm-research):**
   ```bash
   pip install transformers datasets evaluate
   pip install accelerate
   pip install openai anthropic  # API clients
   pip install vllm  # or litellm for inference
   ```

6. **Set up dev tools:**
   ```bash
   pip install ruff pytest mypy
   ```

7. **Verify setup:**
   ```bash
   scripts/check.sh  # Should pass lint + tests
   python -c "import torch; print(torch.cuda.is_available())"  # GPU check
   ```

8. **Create .env for secrets (if needed):**
   ```bash
   touch .env
   echo "WANDB_API_KEY=your_key_here" >> .env
   echo "HF_TOKEN=your_token_here" >> .env
   ```
   Ensure `.env` is in `.gitignore`.

## Output

```
## Setup Report
- Python: 3.12.x
- venv: .venv (active)
- Dependencies: installed (X packages)
- Dev tools: ruff, pytest, mypy
- GPU: available (NVIDIA A100, CUDA 12.x) | not available
- Tests: passing
- Lint: clean
```

## Safety

- Never install packages globally (always use venv)
- Never commit `.env` or API keys
- Pin major versions of critical dependencies (torch, transformers)
- Check GPU driver compatibility before installing CUDA-dependent packages
