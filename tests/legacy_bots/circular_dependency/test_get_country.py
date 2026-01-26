"""
TODO: write tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.legacy_bots.resolvers.country_resolver import get_country

data_1 = {}


data_2 = {}


def test_get_country() -> None:
    # Test with a basic input
    result = get_country("test country")
    assert isinstance(result, str)

    # Test with different parameter
    result_with_country2 = get_country("test country", False)
    assert isinstance(result_with_country2, str)

    # Test with empty string
    result_empty = get_country("")
    assert isinstance(result_empty, str)


TEMPORAL_CASES = [
    ("test_get_country_1", data_1),
    ("test_get_country_2", data_2),
]


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_get_country_1(category: str, expected: str) -> None:
    label = get_country(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_get_country_2(category: str, expected: str) -> None:
    label = get_country(category)
    assert label == expected


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, get_country)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
