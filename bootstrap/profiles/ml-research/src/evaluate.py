"""Evaluation entry point for {{PROJECT_NAME}}."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate {{PROJECT_NAME}}")
    parser.add_argument("--config", type=Path, default=Path("configs/base.yaml"))
    parser.add_argument("--checkpoint", type=Path, required=True,
                        help="Path to model checkpoint")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = yaml.safe_load(args.config.read_text())
    print(f"Evaluating from checkpoint: {args.checkpoint}")

    # TODO: Replace with your actual evaluation code


if __name__ == "__main__":
    main()
