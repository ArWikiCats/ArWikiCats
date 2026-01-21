"""Tests for :mod:`make_bots.bys`."""

from __future__ import annotations

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.legacy_bots.legacy_resolvers_bots.bys import make_new_by_label

make_new_by_label_data = {
    "by ali khamenei": "بواسطة علي خامنئي",
}

to_test = [
    ("test_make_new_by_label", make_new_by_label_data, make_new_by_label),
]


@pytest.mark.parametrize("category, expected", make_new_by_label_data.items(), ids=make_new_by_label_data.keys())
@pytest.mark.fast
def test_make_new_by_label(category: str, expected: str) -> None:
    label = make_new_by_label(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("name,data, callback", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
