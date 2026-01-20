"""
tests
"""

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats.new_resolvers.relations_resolver.nationalities_double_v2 import resolve_by_nats_double_v2

nats_1 = {
    "yemeni–lebanese conflict": "الصراع اللبناني اليمني",
    "zimbabwean–palestinian conflict legal issues": "قضايا قانونية في الصراع الزيمبابوي الفلسطيني",
    "zimbabwean–palestinian conflict video games": "ألعاب فيديو الصراع الزيمبابوي الفلسطيني",
    "zimbabwean–palestinian conflict": "الصراع الزيمبابوي الفلسطيني",
    "zimbabwean–palestinian joint economic efforts": "الجهود الاقتصادية المشتركة الزيمبابوية الفلسطينية",
}

nats_2 = {}


@pytest.mark.parametrize("category, expected", nats_1.items(), ids=nats_1.keys())
@pytest.mark.fast
def test_nats_1(category: str, expected: str) -> None:
    label = resolve_by_nats_double_v2(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", nats_2.items(), ids=nats_2.keys())
@pytest.mark.fast
def test_nats_2(category: str, expected: str) -> None:
    label = resolve_by_nats_double_v2(category)
    assert label == expected


TEMPORAL_CASES = [("nats_1", nats_1, resolve_by_nats_double_v2), ("nats_2", nats_2, resolve_by_nats_double_v2)]


@pytest.mark.parametrize("name,data,callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_dump_all(name: str, data: str, callback: str) -> None:
    name = f"{__name__}_{name}"
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, f"test_resolve_resolve_by_nats_double_v2_{name}")

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
