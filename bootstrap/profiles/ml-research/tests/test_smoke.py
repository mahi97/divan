"""Smoke tests to verify the project is set up correctly."""

from pathlib import Path


def test_configs_exist():
    assert Path("configs/base.yaml").exists(), "base.yaml config missing"


def test_import_src():
    import src  # noqa: F401


def test_config_loading():
    from src.utils.config import load_config
    config = load_config("configs/base.yaml")
    assert "experiment" in config
