"""Config loading utilities."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml


def load_config(path: str | Path) -> dict[str, Any]:
    """Load a YAML config file."""
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def configure_runtime_environment(
    config: dict[str, Any], *, project_root: str | Path | None = None
) -> None:
    """Apply config-driven cache and device settings to the process environment."""
    root = Path(project_root) if project_root is not None else Path.cwd()

    paths = config.get("paths", {})
    env_mapping = {
        "hf_home": "HF_HOME",
        "hf_datasets_cache": "HF_DATASETS_CACHE",
        "hf_hub_cache": "HF_HUB_CACHE",
        "transformers_cache": "TRANSFORMERS_CACHE",
    }
    for key, env_name in env_mapping.items():
        value = paths.get(key)
        if value:
            os.environ[env_name] = str(_resolve_path(root, value))

    compute = config.get("compute", {})
    gpu_devices = compute.get("gpu_devices")
    if gpu_devices is None:
        return

    if isinstance(gpu_devices, list):
        devices = ",".join(str(device) for device in gpu_devices)
    else:
        devices = str(gpu_devices)
    os.environ["CUDA_VISIBLE_DEVICES"] = devices


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


def _resolve_path(root: Path, value: str | Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    return (root / path).resolve()
