# {{PROJECT_NAME}}

{{DESCRIPTION}}

## Overview

Brief description of what this project does and why it exists.

## Quick Start

```bash
# Clone
git clone https://github.com/{{OWNER}}/{{PROJECT_NAME}}.git
cd {{PROJECT_NAME}}

# Setup
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# Verify
scripts/check.sh
```

## Usage

How to use this project after setup.

## Development

```bash
# Run tests
scripts/test.sh

# Lint
scripts/lint.sh

# Full check (lint + test)
scripts/check.sh
```

See `docs/commands.md` for the complete command reference.

## Project Structure

```
{{PROJECT_NAME}}/
  src/               # Source code
  tests/             # Tests
  docs/              # Documentation
  scripts/           # Build/test/lint scripts
```

## License

{{LICENSE}} — see [LICENSE](LICENSE).
