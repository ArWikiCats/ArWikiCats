from __future__ import annotations

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.relations_resolver.countries_names_double_v2 import resolve_countries_names_double

test_relations_names_v2 = {
    "ireland–republic-of-congo relations": "العلاقات الأيرلندية الكونغوية",
    "russia–south sudan relations": "العلاقات الروسية السودانية الجنوبية",
    "russia-south sudan relations": "العلاقات الروسية السودانية الجنوبية",
    "russia south sudan relations": "العلاقات الروسية السودانية الجنوبية",
    "south sudan russia relations": "العلاقات الروسية السودانية الجنوبية",
    "south sudan russia joint economic efforts": "الجهود الاقتصادية المشتركة الروسية السودانية الجنوبية",
}
#
test_relations_v1 = {
    "bermuda–canada relations": "علاقات برمودا وكندا",
}


@pytest.mark.parametrize("category, expected", test_relations_names_v2.items(), ids=test_relations_names_v2.keys())
@pytest.mark.fast
def test_data_relations_v2(category: str, expected: str) -> None:
    label = resolve_countries_names_double(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_relations_v1.items(), ids=test_relations_v1.keys())
@pytest.mark.fast
def test_data_relations_v1(category: str, expected: str) -> None:
    label = resolve_countries_names_double(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_data_relations_v1", test_relations_v1, resolve_countries_names_double),
    ("test_data_relations_v2", test_relations_names_v2, resolve_countries_names_double),
]


@pytest.mark.parametrize("name,data,callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_dump_all(name: str, data: str, callback: str) -> None:
    name = f"{__name__}_{name}"
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, f"test_resolve_by_nats_double_v2_big_data_{name}")

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
