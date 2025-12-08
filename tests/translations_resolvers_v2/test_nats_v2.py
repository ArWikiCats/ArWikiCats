"""
Tests
"""

import pytest
from typing import Callable

from load_one_data import dump_diff, one_dump_test
from ArWikiCats.translations_resolvers_v2.nats_v2 import (
    resolve_by_nats,
)

main_data_2 = {
    # males
    "yemeni non profit publishers": "ناشرون غير ربحيون يمنيون",
    "yemeni non-profit publishers": "ناشرون غير ربحيون يمنيون",
    "yemeni government officials": "مسؤولون حكوميون يمنيون",

    # ar
    "Bahraini King's Cup": "كأس ملك البحرين",
    "French Open": "فرنسا المفتوحة",
    "Canadian National University Alumni": "خريجو جامعة كندا الوطنية",
    "Japanese national women's motorsports racing team": "منتخب اليابان لسباق رياضة المحركات للسيدات",

    # the_male
    "Iraqi Premier League": "الدوري العراقي الممتاز",
    "Iraqi amateur football league": "الدوري العراقي لكرة القدم للهواة",
}


@pytest.mark.parametrize("category, expected", main_data_2.items(), ids=list(main_data_2.keys()))
@pytest.mark.fast
def test_resolve_by_all(category: str, expected: str) -> None:
    label = resolve_by_nats(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_resolve_by_all", main_data_2, resolve_by_nats),
]


@pytest.mark.dump
@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
