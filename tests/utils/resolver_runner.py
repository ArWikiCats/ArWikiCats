# tests/utils/resolver_runner.py
from __future__ import annotations

from collections.abc import Callable, Mapping

import pytest


def make_resolver_test(
    *,
    resolver: Callable[[str], str],
    data: Mapping[str, str],
    test_name: str = "test_resolver_data",
    marks: list[pytest.MarkDecorator] = [],
):
    """
    Factory to generate a parametrized pytest test for a resolver.

    - resolver: function under test
    - data: mapping {category: expected}
    - ids: use the dict keys to keep Arabic readable
    """

    @pytest.mark.parametrize("category, expected", list(data.items()), ids=list(data.keys()))
    def _test(category: str, expected: str) -> None:
        assert resolver(category) == expected

    # Apply mark(s)
    for m in marks:
        _test = m(_test)

    # Give it a stable pytest test name
    _test.__name__ = test_name

    return _test


def make_resolver_fast_test(
    *, resolver: Callable[[str], str], data: Mapping[str, str], test_name: str = "test_resolver_data"
):
    return make_resolver_test(
        resolver=resolver,
        data=data,
        test_name=test_name,
        marks=[pytest.mark.fast],
    )
