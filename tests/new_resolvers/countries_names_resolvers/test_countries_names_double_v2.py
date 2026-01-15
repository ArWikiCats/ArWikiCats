from __future__ import annotations

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats.new_resolvers.countries_names_resolvers.countries_names_double_v2 import resolve_countries_names_double

ireland_test_data = {
    "russia–south sudan relations": "العلاقات الروسية السودانية الجنوبية",
}

test_data = {
    "bermuda–canada relations": "علاقات برمودا وكندا",
}


@pytest.mark.parametrize("category, expected", ireland_test_data.items(), ids=ireland_test_data.keys())
@pytest.mark.fast
def test_ireland_test_data(category: str, expected: str) -> None:
    label = resolve_countries_names_double(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_work_relations_new(category: str, expected: str) -> None:
    label = resolve_countries_names_double(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_work_relations_new", test_data, resolve_countries_names_double),
    ("test_work_relations_ireland", ireland_test_data, resolve_countries_names_double)
]


@pytest.mark.parametrize("name,data,callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_dump_all(name: str, data: str, callback: str) -> None:
    name = f"{__name__}_{name}"
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, f"test_resolve_relations_label_big_data_{name}")

    # dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
