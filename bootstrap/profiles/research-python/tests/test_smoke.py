"""Smoke test to verify the project is set up correctly."""


def test_import():
    """Verify the main package can be imported."""
    import src  # noqa: F401


def test_true():
    """Baseline test that always passes."""
    assert True
