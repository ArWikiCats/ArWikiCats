#
from typing import Callable

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.countries_formats.p17_bot import from_category_relation_mapping, get_con_3_lab_pop_format

test_data_relation_mapping = {}


@pytest.mark.parametrize(
    "category, expected", test_data_relation_mapping.items(), ids=test_data_relation_mapping.keys()
)
@pytest.mark.fast
def test_from_category_relation_mapping(category: str, expected: str) -> None:
    result = from_category_relation_mapping(category)
    assert result == expected


TEMPORAL_CASES = [
    ("test_from_category_relation_mapping", test_data_relation_mapping, from_category_relation_mapping),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
