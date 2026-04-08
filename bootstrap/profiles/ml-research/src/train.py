"""Training entry point for {{PROJECT_NAME}}."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.utils.config import configure_runtime_environment, load_config


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train {{PROJECT_NAME}}")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/base.yaml"),
        help="Path to experiment config file",
    )
    parser.add_argument(
        "--run-name",
        default=None,
        help="Override run name (default: from config)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    config = load_config(args.config)
    configure_runtime_environment(config, project_root=Path.cwd())
    print(f"Starting run: {config.get('experiment', {}).get('name', 'unnamed')}")

    # TODO: Replace with your actual training code
    # Example structure:
    #   model = build_model(config["model"])
    #   data = load_data(config["data"])
    #   trainer = Trainer(model, data, config["training"])
    #   trainer.train()


if __name__ == "__main__":
    main()
