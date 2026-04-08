"""Training entry point for {{PROJECT_NAME}}."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


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

    config = yaml.safe_load(args.config.read_text())
    print(f"Starting run: {config.get('experiment', {}).get('name', 'unnamed')}")

    # TODO: Replace with your actual training code
    # Example structure:
    #   model = build_model(config["model"])
    #   data = load_data(config["data"])
    #   trainer = Trainer(model, data, config["training"])
    #   trainer.train()


if __name__ == "__main__":
    main()
