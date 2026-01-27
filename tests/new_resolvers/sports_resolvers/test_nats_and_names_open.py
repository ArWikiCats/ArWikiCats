#!/usr/bin/python3
""" """

import pytest

from ArWikiCats.new_resolvers.sports_resolvers.countries_names_and_sports import resolve_countries_names_sport
from ArWikiCats.new_resolvers.sports_resolvers.nationalities_and_sports import resolve_nats_sport_multi_v2
from utils.dump_runner import make_dump_test_name_data_callback

data_nats_0 = {}
data_nats_1 = {
    "australian open (tennis)": "بطولة أستراليا المفتوحة لكرة المضرب",
    "australian open tennis": "بطولة أستراليا المفتوحة لكرة المضرب",
    "canadian open (tennis)": "بطولة كندا المفتوحة لكرة المضرب",
    "italian open (tennis)": "بطولة إيطاليا المفتوحة لكرة المضرب",
    "mexican open (tennis)": "بطولة المكسيك المفتوحة لكرة المضرب",
    "canadian open tennis": "بطولة كندا المفتوحة لكرة المضرب",
    "italian open tennis": "بطولة إيطاليا المفتوحة لكرة المضرب",
    "mexican open tennis": "بطولة المكسيك المفتوحة لكرة المضرب",
}

data_names_0 = {}

data_names_3 = {
    "chile open (tennis)": "بطولة تشيلي المفتوحة لكرة المضرب",
    "china open (tennis)": "بطولة الصين المفتوحة لكرة المضرب",
    "qatar open (tennis)": "بطولة قطر المفتوحة لكرة المضرب",
    "chile open tennis": "بطولة تشيلي المفتوحة لكرة المضرب",
    "china open tennis": "بطولة الصين المفتوحة لكرة المضرب",
    "qatar open tennis": "بطولة قطر المفتوحة لكرة المضرب",
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
test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
