# {{PROJECT_NAME}}

{{DESCRIPTION}}

## Overview

Brief description of what this project does and why it exists.

## Quick Start

```bash
git clone https://github.com/{{OWNER}}/{{PROJECT_NAME}}.git
cd {{PROJECT_NAME}}

# Clone divan toolkit
git clone https://github.com/{{OWNER}}/divan.git

# Set up environment
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# Verify
scripts/check.sh
```

## Usage

How to run the main code.

## Training / Experiments

```bash
# Run an experiment
python src/train.py --config configs/experiment_0001.yaml

# Deploy to GPU server
# See divan/skills/custom/gpu-deploy/ for instructions
```

## Development

```bash
scripts/test.sh      # Run tests
scripts/lint.sh      # Lint
scripts/check.sh     # Both
```

See `docs/commands.md` for the complete command reference.

## Project Structure

```
{{PROJECT_NAME}}/
  divan/             # Toolkit — skills, standards, workflows
  src/               # Source code
  tests/             # Tests
  configs/           # Experiment configs
  docs/              # Documentation
  scripts/           # Build/test/lint/deploy scripts
  data/              # Data (gitignored)
  results/           # Results (gitignored)
```

## License

{{LICENSE}} — see [LICENSE](LICENSE).
