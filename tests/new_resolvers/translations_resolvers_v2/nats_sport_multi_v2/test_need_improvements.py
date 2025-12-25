#!/usr/bin/python3
"""
TODO: need improvements
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.translations_resolvers_v2.nats_sport_multi_v2 import resolve_nats_sport_multi_v2

data_1 = {
}

nat_p17_oioi_to_check_data = {
    "chinese boxing chairmen and investors": "رؤساء ومسيرو للبوكسينغ الصين",

    "chinese domestic women's boxing clubs": "أندية للبوكسينغ محلية الصين للسيدات",
    "chinese domestic women's boxing coaches": "مدربو للبوكسينغ محلية الصين للسيدات",
    "chinese domestic women's boxing competitions": "منافسات للبوكسينغ محلية الصين للسيدات",
    "chinese domestic women's boxing cups": "كؤوس للبوكسينغ محلية الصين للسيدات",
    "chinese domestic women's boxing leagues": "دوريات للبوكسينغ محلية الصين للسيدات",

    "chinese boxing cups": "كؤوس للبوكسينغ الصين",
    "chinese boxing leagues": "دوريات للبوكسينغ الصين",
    "chinese boxing clubs": "أندية للبوكسينغ الصين",
    "chinese boxing coaches": "مدربو للبوكسينغ الصين",
    "chinese boxing competitions": "منافسات للبوكسينغ الصين",
    "chinese boxing cup competitions": "منافسات كؤوس للبوكسينغ الصين",
    "chinese current boxing seasons": "مواسم للبوكسينغ الصين حالية",
    "chinese defunct indoor boxing clubs": "أندية للبوكسينغ الصين داخل الصالات سابقة",
    "chinese defunct indoor boxing coaches": "مدربو للبوكسينغ الصين داخل الصالات سابقة",
    "chinese defunct indoor boxing competitions": "منافسات للبوكسينغ الصين داخل الصالات سابقة",
    "chinese defunct indoor boxing cups": "كؤوس للبوكسينغ الصين داخل الصالات سابقة",
    "chinese defunct indoor boxing leagues": "دوريات للبوكسينغ الصين داخل الصالات سابقة",
    "chinese defunct boxing clubs": "أندية للبوكسينغ الصين سابقة",
    "chinese defunct boxing coaches": "مدربو للبوكسينغ الصين سابقة",
    "chinese defunct boxing competitions": "منافسات للبوكسينغ الصين سابقة",
    "chinese defunct boxing cup competitions": "منافسات كؤوس للبوكسينغ الصين سابقة",
    "chinese defunct boxing cups": "كؤوس للبوكسينغ الصين سابقة",
    "chinese defunct boxing leagues": "دوريات للبوكسينغ الصين سابقة",
    "chinese defunct outdoor boxing clubs": "أندية للبوكسينغ الصين في الهواء الطلق سابقة",
    "chinese defunct outdoor boxing coaches": "مدربو للبوكسينغ الصين في الهواء الطلق سابقة",
    "chinese defunct outdoor boxing competitions": "منافسات للبوكسينغ الصين في الهواء الطلق سابقة",
    "chinese defunct outdoor boxing cups": "كؤوس للبوكسينغ الصين في الهواء الطلق سابقة",
    "chinese defunct outdoor boxing leagues": "دوريات للبوكسينغ الصين في الهواء الطلق سابقة",
    "chinese domestic boxing": "للبوكسينغ الصين محلية",
    "chinese domestic boxing clubs": "أندية للبوكسينغ الصين محلية",
    "chinese domestic boxing coaches": "مدربو للبوكسينغ الصين محلية",
    "chinese domestic boxing competitions": "منافسات للبوكسينغ الصين محلية",
    "chinese domestic boxing cup": "كؤوس للبوكسينغ الصين محلية",
    "chinese domestic boxing cups": "كؤوس للبوكسينغ الصين محلية",
    "chinese domestic boxing leagues": "دوريات للبوكسينغ الصين محلية",
    "chinese indoor boxing clubs": "أندية للبوكسينغ الصين داخل الصالات",
    "chinese indoor boxing coaches": "مدربو للبوكسينغ الصين داخل الصالات",
    "chinese indoor boxing competitions": "منافسات للبوكسينغ الصين داخل الصالات",
    "chinese indoor boxing cups": "كؤوس للبوكسينغ الصين داخل الصالات",
    "chinese indoor boxing leagues": "دوريات للبوكسينغ الصين داخل الصالات",
    "chinese outdoor boxing coaches": "مدربو للبوكسينغ الصين في الهواء الطلق",
    "chinese outdoor boxing competitions": "منافسات للبوكسينغ الصين في الهواء الطلق",
    "chinese outdoor boxing leagues": "دوريات للبوكسينغ الصين في الهواء الطلق",
    "chinese professional boxing clubs": "أندية للبوكسينغ الصين للمحترفين",
    "chinese professional boxing coaches": "مدربو للبوكسينغ الصين للمحترفين",
    "chinese professional boxing competitions": "منافسات للبوكسينغ الصين للمحترفين",
    "chinese professional boxing cups": "كؤوس للبوكسينغ الصين للمحترفين",
    "chinese outdoor boxing cups": "كؤوس للبوكسينغ الصين في الهواء الطلق",
    "chinese professional boxing leagues": "دوريات للبوكسينغ الصين للمحترفين",
}

data_3 = {
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_need_improvements_1(category: str, expected: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected


@pytest.mark.parametrize("category, expected", nat_p17_oioi_to_check_data.items(), ids=nat_p17_oioi_to_check_data.keys())
@pytest.mark.skip2
def test_need_improvements_2(category: str, expected: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
@pytest.mark.fast
def test_need_improvements_3(category: str, expected: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected


to_test = [
    ("test_need_improvements_1", data_1, resolve_nats_sport_multi_v2),
    ("test_need_improvements_2", nat_p17_oioi_to_check_data, resolve_nats_sport_multi_v2),
    ("test_need_improvements_3", data_3, resolve_nats_sport_multi_v2),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)

    # add_result = {x: v for x, v in data.items() if x in diff_result and "" == diff_result.get(x)}
    # dump_diff(add_result, f"{name}_add")
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
