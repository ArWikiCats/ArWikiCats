"""
Tests
"""

from typing import Callable

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.nationalities_resolvers.nationalities_v2 import resolve_by_nats

test_data_males = {
    "christian religious orders": "أخويات دينية مسيحية",
    "christian political parties": "أحزاب سياسية مسيحية",
    "jewish political parties": "أحزاب سياسية يهودية",
    "palestinian political parties": "أحزاب سياسية فلسطينية",
    "Yemeni expatriates": "يمنيون مغتربون",
    "Yemeni emigrants": "يمنيون مهاجرون",
}


@pytest.mark.parametrize("category, expected", test_data_males.items(), ids=test_data_males.keys())
@pytest.mark.fast
def test_resolve_males(category: str, expected: str) -> None:
    label = resolve_by_nats(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_resolve_males", test_data_males, resolve_by_nats),
    x]


@pytest.mark.dump
@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
