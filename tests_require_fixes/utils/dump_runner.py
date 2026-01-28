# tests/utils/dump_runner.py
from __future__ import annotations

from collections.abc import Iterable

import pytest

ToTest = Iterable[tuple[str, dict[str, str]]]
ToTestCallback = Iterable[tuple[str, dict[str, str], callable]]


def _run_dump_case(name: str, data: dict[str, str], callback: callable, run_same=False, just_dump=False) -> None:
    """
    Common dump test logic shared across many test files.
    """
    from load_one_data import (
        dump_diff,
        dump_same_and_not_same,
        one_dump_test,
    )

    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)

    if run_same:
        dump_same_and_not_same(data, diff_result, name, just_dump=just_dump)

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


def make_dump_test_name_data(to_test: ToTest, callback, run_same=False, just_dump=False):
    """
    Create a parametrized pytest test function.
    """

    @pytest.mark.parametrize("name,data", list(to_test))
    @pytest.mark.dump
    def test_dump_all(name: str, data: dict[str, str]) -> None:
        _run_dump_case(name, data, callback, run_same=run_same, just_dump=just_dump)

    return test_dump_all


def make_dump_test_name_data_callback(to_test: ToTestCallback, run_same=False, just_dump=False):
    """
    Create a parametrized pytest test function.
    """

    @pytest.mark.parametrize("name,data,callback", list(to_test))
    @pytest.mark.dump
    def test_dump_all(name: str, data: dict[str, str], callback) -> None:
        _run_dump_case(name, data, callback, run_same=run_same, just_dump=just_dump)

    return test_dump_all
