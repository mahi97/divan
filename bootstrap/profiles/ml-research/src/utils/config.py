"""Config loading utilities."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def load_config(path: str | Path) -> dict[str, Any]:
    """Load a YAML config file."""
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def merge_configs(*configs: dict[str, Any]) -> dict[str, Any]:
    """Deep-merge multiple config dicts. Later configs override earlier ones."""
    result: dict[str, Any] = {}
    for config in configs:
        _deep_merge(result, config)
    return result


def _deep_merge(base: dict, override: dict) -> None:
    for key, value in override.items():
        if key in base and isinstance(base[key], dict) and isinstance(value, dict):
            _deep_merge(base[key], value)
        else:
            base[key] = value
