"""
Tests
"""

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats.new_resolvers.nationalities_resolvers.nationalities_v2 import resolve_by_nats

nat_match_data = {
    "anti-haitian sentiment": "مشاعر معادية للهايتيون",
    "anti-palestinian sentiment": "مشاعر معادية للفلسطينيون",
    "anti-turkish sentiment": "مشاعر معادية للأتراك",
    "anti-american sentiment": "مشاعر معادية للأمريكيون",
    "anti-czech sentiment": "مشاعر معادية للتشيكيون",
    "anti-japanese sentiment": "مشاعر معادية لليابانيون",
    "anti-asian sentiment": "مشاعر معادية للآسيويون",
    "anti-slovene sentiment": "مشاعر معادية للسلوفينيون",
    "anti-ukrainian sentiment": "مشاعر معادية للأوكرانيون",
    "anti-chechen sentiment": "مشاعر معادية للشيشانيون",
    "anti-mexican sentiment": "مشاعر معادية للمكسيكيون",
    "anti-chinese sentiment": "مشاعر معادية للصينيون",
    "anti-christian sentiment": "مشاعر معادية للمسيحيون",
    "anti-serbian sentiment": "مشاعر معادية للصرب",
    "anti-armenian sentiment": "مشاعر معادية للأرمن",
    "anti-scottish sentiment": "مشاعر معادية للإسكتلنديون",
    "anti-iranian sentiment": "مشاعر معادية للإيرانيون",
    "anti-english sentiment": "مشاعر معادية للإنجليز",
    "anti-hungarian sentiment": "مشاعر معادية للمجريون",
    "anti-greek sentiment": "مشاعر معادية لليونانيون",
}


@pytest.mark.parametrize("category, expected", nat_match_data.items(), ids=nat_match_data.keys())
@pytest.mark.fast
def te_nat_match_data(category: str, expected: str) -> None:
    label = resolve_by_nats(category)
    assert label == expected


ENTERTAINMENT_CASES = [
    ("te_nat_match_data_nats", nat_match_data, resolve_by_nats),
]


@pytest.mark.parametrize("name,data,callback", ENTERTAINMENT_CASES)
@pytest.mark.dump
def test_entertainment(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    # dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
