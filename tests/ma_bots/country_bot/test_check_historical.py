"""
TODO: write tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.legacy_bots.ma_bots.country_bot import check_historical_prefixes

historical_data = {
    "Defunct national legislatures": "هيئات تشريعية وطنية سابقة",
    "Defunct national football teams": "فرق كرة قدم وطنية سابقة",
    "Defunct National Hockey League teams": "فرق دوري هوكي وطنية سابقة",
    "defunct national basketball league teams": "فرق دوري كرة سلة وطنية سابقة",
}


TEMPORAL_CASES = [
    ("test_yemen_2", historical_data),
]


@pytest.mark.parametrize("category, expected", historical_data.items(), ids=historical_data.keys())
@pytest.mark.fast
def test_historical_data(category: str, expected: str) -> None:
    label = check_historical_prefixes(category)
    assert label == expected


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, check_historical_prefixes)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
