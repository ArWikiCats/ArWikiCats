""" """

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

test_0 = {
    "Defunct national legislatures": "هيئات تشريعية وطنية سابقة",
    "Defunct National Hockey League teams": "فرق دوري هوكي وطنية سابقة",
    "Members of defunct national legislatures": "أعضاء هيئات تشريعية وطنية سابقة",
    "defunct national basketball league teams": "فرق دوري كرة سلة وطنية سابقة",
}

test_1 = {
    "Defunct national football teams": "منتخبات كرة قدم وطنية سابقة",
    "Defunct national sports teams": "منتخبات رياضية وطنية سابقة",
}


TEMPORAL_CASES = [
    ("test_yemen_2", test_1),
]


@pytest.mark.parametrize("category, expected", test_1.items(), ids=test_1.keys())
@pytest.mark.fast
def test_historical_data(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
