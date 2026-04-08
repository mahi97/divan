# Profile: llm-research

For projects involving large language models, generative AI, and ML experiments
with significant compute requirements.

## When to Use

- Fine-tuning or evaluating LLMs
- Running inference pipelines
- Benchmarking model performance
- Prompt engineering and evaluation
- RAG, agents, or tool-use research

## Files Added (on top of common)

This profile is a conventions overlay. It adds guidance rather than heavy
scaffolding, since LLM projects vary widely.

## Conventions

### Directory Layout

```
project/
  src/              # Source code
  tests/            # Tests
  configs/          # Model configs, prompt templates, eval configs
  data/             # Datasets (gitignored if large)
  results/          # Model outputs, eval results (gitignored if large)
  notebooks/        # Exploration notebooks
  models/           # Model checkpoints (gitignored, use symlinks or DVC)
  docs/
    experiments/    # Experiment logs (always committed)
    literature/     # Paper notes
```

### Model Management

- Never commit model weights to git.
- Use symlinks, DVC, or cloud storage for large files.
- Record model source (HuggingFace ID, URL, etc.) in experiment logs.
- Pin model versions/revisions in configs.

### Compute Awareness

- Document GPU/compute requirements in README.
- Use config files for hyperparameters — do not hardcode.
- Support CPU fallback for development/testing.
- Log hardware info in experiment records.

### Evaluation

- Define eval metrics in a config file.
- Use standardized eval harnesses when available.
- Always compare against a documented baseline.
- Record prompt templates alongside results.

### API Keys and Secrets

- Use `.env` files for API keys (gitignored).
- Document required environment variables in README.
- Never log API keys, even partially.

## Recommended Dependencies

Add as needed:
- `transformers`, `torch` — model loading and inference
- `datasets` — data loading
- `evaluate` — metrics
- `vllm` or `litellm` — efficient inference
- `wandb` or `mlflow` — experiment tracking (optional)
