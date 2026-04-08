"""Smoke tests to verify the project is set up correctly."""

import os
from pathlib import Path
import sys

import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = PROJECT_ROOT / "configs/base.yaml"
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def test_configs_exist():
    assert CONFIG_PATH.exists(), "base.yaml config missing"


def test_import_src():
    import src  # noqa: F401


def test_config_loading():
    from src.utils.config import load_config

    config = load_config(CONFIG_PATH)
    assert "experiment" in config


def test_base_config_exposes_data_and_gpu_controls():
    config = yaml.safe_load(CONFIG_PATH.read_text())

    paths = config["paths"]
    assert "data_root" in paths
    assert "hf_home" in paths
    assert "hf_datasets_cache" in paths
    assert "hf_hub_cache" in paths

    compute = config["compute"]
    assert "gpu_devices" in compute
    assert "gpu_count" in compute


def test_runtime_environment_uses_configured_paths_and_gpus(monkeypatch):
    from src.utils.config import configure_runtime_environment, load_config

    monkeypatch.delenv("HF_HOME", raising=False)
    monkeypatch.delenv("HF_DATASETS_CACHE", raising=False)
    monkeypatch.delenv("HF_HUB_CACHE", raising=False)
    monkeypatch.delenv("TRANSFORMERS_CACHE", raising=False)
    monkeypatch.delenv("CUDA_VISIBLE_DEVICES", raising=False)

    config = load_config(CONFIG_PATH)
    configure_runtime_environment(config, project_root=PROJECT_ROOT)

    assert os.environ["HF_HOME"].endswith(".cache/huggingface")
    assert os.environ["HF_DATASETS_CACHE"].endswith(".cache/huggingface/datasets")
    assert os.environ["HF_HUB_CACHE"].endswith(".cache/huggingface/hub")
    assert os.environ["TRANSFORMERS_CACHE"].endswith(
        ".cache/huggingface/transformers"
    )
    assert os.environ["CUDA_VISIBLE_DEVICES"] == "0"
