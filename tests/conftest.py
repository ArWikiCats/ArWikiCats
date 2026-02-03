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


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add custom command line options."""
    parser.addoption(
        "--rune2e",
        action="store_true",
        default=False,
        help="Run end-to-end tests (disabled by default in quick mode)",
    )


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """
    Automatically apply markers based on test location.

    Marker rules:
    - tests/unit/* → @pytest.mark.unit
    - tests/integration/* → @pytest.mark.integration
    - tests/e2e/* → @pytest.mark.e2e
    """
    run_e2e = config.getoption("--rune2e")

    for item in items:
        path_str = str(item.fspath)

        # Auto-mark based on file path
        if "tests" + os.sep + "unit" in path_str:
            item.add_marker(pytest.mark.unit)
            item.add_marker(pytest.mark.fast)
        elif "tests" + os.sep + "integration" in path_str:
            item.add_marker(pytest.mark.integration)
        elif "tests" + os.sep + "e2e" in path_str:
            item.add_marker(pytest.mark.e2e)
            if not run_e2e:
                item.add_marker(pytest.mark.skip(reason="E2E tests disabled, use --rune2e"))
