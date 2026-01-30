"""
Tests
"""

import pytest
from load_one_data import dump_same_and_not_same, one_dump_test

from ArWikiCats.new_resolvers.nationalities_resolvers.nationalities_v2 import resolve_by_nats

nat_match_data = {
    "Thai remakes of foreign films": "أفلام تايلندية مأخوذة من أفلام أجنبية",
    "Spanish remakes of foreign films": "أفلام إسبانية مأخوذة من أفلام أجنبية",
    "Taiwanese remakes of foreign films": "أفلام تايوانية مأخوذة من أفلام أجنبية",
    "South Korean remakes of foreign films": "أفلام كورية جنوبية مأخوذة من أفلام أجنبية",
    "Pakistani remakes of foreign films": "أفلام باكستانية مأخوذة من أفلام أجنبية",
    "Philippine remakes of foreign films": "أفلام فلبينية مأخوذة من أفلام أجنبية",
    "Japanese remakes of foreign films": "أفلام يابانية مأخوذة من أفلام أجنبية",
    "Indian remakes of foreign films": "أفلام هندية مأخوذة من أفلام أجنبية",
    "Iranian remakes of foreign films": "أفلام إيرانية مأخوذة من أفلام أجنبية",
    "Italian remakes of foreign films": "أفلام إيطالية مأخوذة من أفلام أجنبية",
    "Chinese remakes of foreign films": "أفلام صينية مأخوذة من أفلام أجنبية",
    "Dutch remakes of foreign films": "أفلام هولندية مأخوذة من أفلام أجنبية",
    "Bangladeshi remakes of foreign films": "أفلام بنغلاديشية مأخوذة من أفلام أجنبية",
    "American remakes of foreign films": "أفلام أمريكية مأخوذة من أفلام أجنبية",
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
def test_nat_match_data(category: str, expected: str) -> None:
    label = resolve_by_nats(category)
    assert label == expected


ENTERTAINMENT_CASES = [
    ("test_nat_match_data", nat_match_data, resolve_by_nats),
]


@pytest.mark.parametrize("name,data,callback", ENTERTAINMENT_CASES)
@pytest.mark.dump
def test_entertainment(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    # dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
