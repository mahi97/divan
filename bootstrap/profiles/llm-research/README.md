# Profile: llm-research

LLM/generative AI work — prompts, evals, model management, inference pipelines.

## When to Use

- Fine-tuning or evaluating LLMs
- Prompt engineering and systematic evaluation
- RAG, agents, or tool-use research
- Inference pipelines and benchmarking models

## Files Added (on top of common + ml-research)

This profile layers on top of `ml-research`. Apply `ml-research` first if
you want both. Or use `llm-research` standalone for lighter setups.

```
configs/llm_base.yaml       — LLM-specific config template
src/prompts/                — Prompt template directory
src/eval_harness.py         — Evaluation harness template
```

## Conventions

- Prompt templates live in `src/prompts/` as `.txt` or `.jinja2` files
- Never hardcode API keys — use `.env`
- Pin model versions/revisions in configs
- Store model weights outside the repo (use HF model IDs or paths)
- Eval results go in `results/evals/`

## Required Environment Variables

```
WANDB_API_KEY=...
HF_TOKEN=...         # Hugging Face access token (for gated models)
OPENAI_API_KEY=...   # If using OpenAI models
ANTHROPIC_API_KEY=... # If using Claude
```

## Skills to Use

- `divan/skills/custom/experiment-runner/`
- `divan/skills/custom/monitoring-setup/`
- `divan/skills/custom/hpc-submit/` (for large model runs)
