#!/usr/bin/python3
"""
TODO: need improvements
"""

import pytest

from ArWikiCats.new_resolvers.sports_resolvers.nationalities_and_sports import resolve_nats_sport_multi_v2
from utils.dump_runner import make_dump_test_name_data_callback

data_1 = {
    "yemeni domestic basketball": "كرة سلة يمنية محلية",
    "yemeni domestic womens basketball": "كرة سلة يمنية محلية للسيدات",
    "chinese indoor boxing clubs": "أندية بوكسينغ صينية داخل الصالات",
    "chinese indoor boxing coaches": "مدربو بوكسينغ صينية داخل الصالات",
    "chinese indoor boxing competitions": "منافسات بوكسينغ صينية داخل الصالات",
    "chinese indoor boxing leagues": "دوريات بوكسينغ صينية داخل الصالات",
    "chinese outdoor boxing coaches": "مدربو بوكسينغ صينية في الهواء الطلق",
    "chinese outdoor boxing competitions": "منافسات بوكسينغ صينية في الهواء الطلق",
    "chinese outdoor boxing leagues": "دوريات بوكسينغ صينية في الهواء الطلق",
}

nat_p17_oioi_to_check_data = {
    "chinese current boxing seasons": "مواسم بوكسينغ صينية حالية",
    "chinese defunct indoor boxing clubs": "أندية بوكسينغ صينية داخل الصالات سابقة",
    "chinese defunct indoor boxing coaches": "مدربو بوكسينغ صينية داخل الصالات سابقة",
    "chinese defunct indoor boxing competitions": "منافسات بوكسينغ صينية داخل الصالات سابقة",
    "chinese defunct indoor boxing leagues": "دوريات بوكسينغ صينية داخل الصالات سابقة",
    "chinese defunct boxing clubs": "أندية بوكسينغ صينية سابقة",
    "chinese defunct boxing coaches": "مدربو بوكسينغ صينية سابقة",
    "chinese defunct boxing competitions": "منافسات بوكسينغ صينية سابقة",
    "chinese defunct boxing leagues": "دوريات بوكسينغ صينية سابقة",
    "chinese defunct outdoor boxing clubs": "أندية بوكسينغ صينية في الهواء الطلق سابقة",
    "chinese defunct outdoor boxing coaches": "مدربو بوكسينغ صينية في الهواء الطلق سابقة",
    "chinese defunct outdoor boxing competitions": "منافسات بوكسينغ صينية في الهواء الطلق سابقة",
    "chinese defunct outdoor boxing leagues": "دوريات بوكسينغ صينية في الهواء الطلق سابقة",
    "chinese professional boxing clubs": "أندية بوكسينغ صينية للمحترفين",
    "chinese professional boxing coaches": "مدربو بوكسينغ صينية للمحترفين",
    "chinese professional boxing competitions": "منافسات بوكسينغ صينية للمحترفين",
    "chinese professional boxing leagues": "دوريات بوكسينغ صينية للمحترفين",
    "chinese boxing chairmen and investors": "رؤساء ومسيرو البوكسينغ الصينية",
    "chinese boxing leagues": "دوريات البوكسينغ الصينية",
    "chinese boxing clubs": "أندية البوكسينغ الصينية",
    "chinese boxing coaches": "مدربو البوكسينغ الصينية",
    "chinese boxing competitions": "منافسات البوكسينغ الصينية",
    "chinese domestic women's boxing clubs": "أندية بوكسينغ صينية محلية للسيدات",
    "chinese domestic women's boxing coaches": "مدربو بوكسينغ صينية محلية للسيدات",
    "chinese domestic women's boxing competitions": "منافسات بوكسينغ صينية محلية للسيدات",
    "chinese domestic women's boxing leagues": "دوريات بوكسينغ صينية محلية للسيدات",
    "chinese domestic boxing": "بوكسينغ صينية محلية",
    "chinese domestic boxing clubs": "أندية بوكسينغ صينية محلية",
    "chinese domestic boxing coaches": "مدربو بوكسينغ صينية محلية",
    "chinese domestic boxing competitions": "منافسات بوكسينغ صينية محلية",
    "chinese domestic boxing leagues": "دوريات بوكسينغ صينية محلية",
}

data_3 = {}

to_test = [
    ("test_need_improvements_1", data_1, resolve_nats_sport_multi_v2),
    ("test_need_improvements_2", nat_p17_oioi_to_check_data, resolve_nats_sport_multi_v2),
    ("test_need_improvements_3", data_3, resolve_nats_sport_multi_v2),
]


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_need_improvements_1(category: str, expected: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected


@pytest.mark.parametrize(
    "category, expected", nat_p17_oioi_to_check_data.items(), ids=nat_p17_oioi_to_check_data.keys()
)
@pytest.mark.fast
def test_need_improvements_2(category: str, expected: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
@pytest.mark.fast
def test_need_improvements_3(category: str, expected: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected


test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
