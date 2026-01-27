"""Test configuration for the test-suite."""

import os
import random

import pytest


def pytest_configure(config: pytest.Config) -> None:
    """
    Global test-suite normalization.
    - Force UTF-8 I/O (important on Windows for Arabic output)
    - Make random deterministic (avoid flaky order / generation)
    """
    os.environ.setdefault("PYTHONUTF8", "1")
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")

    # Make randomness deterministic across workers/processes
    random.seed(0)
