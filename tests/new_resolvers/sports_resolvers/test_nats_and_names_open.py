#!/usr/bin/python3
"""

"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.sports_resolvers.countries_names_and_sports import resolve_countries_names_sport
from ArWikiCats.new_resolvers.sports_resolvers.nationalities_and_sports import resolve_nats_sport_multi_v2

data_nats_1 = {
    "australian open (tennis)": "بطولة أستراليا المفتوحة للتنس",
    "australian open tennis": "بطولة أستراليا المفتوحة للتنس",
    "barcelona open (tennis)": "بطولة برشلونة للتنس",
    "canadian open (tennis)": "بطولة كندا للأساتذة",
    "italian open (tennis)": "روما للماسترز",
    "mexican open (tennis)": "بطولة أكابولكو للتنس",
    "barcelona open tennis": "بطولة برشلونة للتنس",
    "canadian open tennis": "بطولة كندا للأساتذة",
    "italian open tennis": "روما للماسترز",
    "madrid open tennis": "مدريد للماسترز",
    "mexican open tennis": "بطولة أكابولكو للتنس",
}

data_names_3 = {
    "chile open (tennis)": "بطولة تشيلي للتنس",
    "china open (tennis)": "بطولة الصين المفتوحة",
    "madrid open (tennis)": "مدريد للماسترز",
    "miami open (tennis)": "ميامي للماسترز",
    "qatar open (tennis)": "بطولة قطر المفتوحة للتنس",
    "chile open tennis": "بطولة تشيلي للتنس",
    "china open tennis": "بطولة الصين المفتوحة",
    "miami open tennis": "ميامي للماسترز",
    "qatar open tennis": "بطولة قطر المفتوحة للتنس",
}


@pytest.mark.parametrize("category, expected", data_nats_1.items(), ids=data_nats_1.keys())
@pytest.mark.fast
def test_nas_open_1(category: str, expected: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected


@pytest.mark.parametrize("category, expected", data_names_3.items(), ids=data_names_3.keys())
@pytest.mark.fast
def test_nas_open_3(category: str, expected: str) -> None:
    label2 = resolve_countries_names_sport(category)
    assert label2 == expected


to_test = [
    ("test_nas_open_1", data_nats_1, resolve_nats_sport_multi_v2),
    ("test_nas_open_3", data_names_3, resolve_countries_names_sport),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
