#!/usr/bin/python3
"""

"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.sports_resolvers.nationalities_and_sports import resolve_nats_sport_multi_v2

data_1 = {
    "chinese outdoor boxing clubs": "أندية بوكسينغ صينية في الهواء الطلق",
    "chinese outdoor boxing": "بوكسينغ صينية في الهواء الطلق",
    "chinese women's boxing": "بوكسينغ صينية للسيدات",
    "chinese indoor boxing": "بوكسينغ صينية داخل الصالات",
}

data_3 = {
    "chinese men's boxing championship": "بطولة الصين للبوكسينغ للرجال",
    "chinese amateur boxing championship": "بطولة الصين للبوكسينغ للهواة",
    "chinese amateur boxing championships": "بطولة الصين للبوكسينغ للهواة",
    "chinese championships boxing": "بطولة الصين للبوكسينغ",
    "chinese men's boxing championships": "بطولة الصين للبوكسينغ للرجال",
    "chinese men's boxing national team": "منتخب الصين للبوكسينغ للرجال",
    "chinese men's u23 national boxing team": "منتخب الصين للبوكسينغ تحت 23 سنة للرجال",
    "chinese boxing championship": "بطولة الصين للبوكسينغ",
    "chinese boxing championships": "بطولة الصين للبوكسينغ",
    "chinese boxing indoor championship": "بطولة الصين للبوكسينغ داخل الصالات",
    "chinese boxing indoor championships": "بطولة الصين للبوكسينغ داخل الصالات",
    "chinese boxing junior championships": "بطولة الصين للبوكسينغ للناشئين",
    "chinese boxing national team": "منتخب الصين للبوكسينغ",
    "chinese boxing u-13 championships": "بطولة الصين للبوكسينغ تحت 13 سنة",
    "chinese boxing u-14 championships": "بطولة الصين للبوكسينغ تحت 14 سنة",
    "chinese boxing u-15 championships": "بطولة الصين للبوكسينغ تحت 15 سنة",
    "chinese boxing u-16 championships": "بطولة الصين للبوكسينغ تحت 16 سنة",
    "chinese boxing u-17 championships": "بطولة الصين للبوكسينغ تحت 17 سنة",
    "chinese boxing u-18 championships": "بطولة الصين للبوكسينغ تحت 18 سنة",
    "chinese boxing u-19 championships": "بطولة الصين للبوكسينغ تحت 19 سنة",
    "chinese boxing u-20 championships": "بطولة الصين للبوكسينغ تحت 20 سنة",
    "chinese boxing u-21 championships": "بطولة الصين للبوكسينغ تحت 21 سنة",
    "chinese boxing u-23 championships": "بطولة الصين للبوكسينغ تحت 23 سنة",
    "chinese boxing u-24 championships": "بطولة الصين للبوكسينغ تحت 24 سنة",
    "chinese boxing u13 championships": "بطولة الصين للبوكسينغ تحت 13 سنة",
    "chinese boxing u14 championships": "بطولة الصين للبوكسينغ تحت 14 سنة",
    "chinese boxing u15 championships": "بطولة الصين للبوكسينغ تحت 15 سنة",
    "chinese boxing u16 championships": "بطولة الصين للبوكسينغ تحت 16 سنة",
    "chinese boxing u17 championships": "بطولة الصين للبوكسينغ تحت 17 سنة",
    "chinese boxing u18 championships": "بطولة الصين للبوكسينغ تحت 18 سنة",
    "chinese boxing u19 championships": "بطولة الصين للبوكسينغ تحت 19 سنة",
    "chinese boxing u20 championships": "بطولة الصين للبوكسينغ تحت 20 سنة",
    "chinese boxing u21 championships": "بطولة الصين للبوكسينغ تحت 21 سنة",
    "chinese boxing u23 championships": "بطولة الصين للبوكسينغ تحت 23 سنة",
    "chinese boxing u24 championships": "بطولة الصين للبوكسينغ تحت 24 سنة",
    "chinese open boxing": "الصين المفتوحة للبوكسينغ",
    "chinese outdoor boxing championship": "بطولة الصين للبوكسينغ في الهواء الطلق",
    "chinese outdoor boxing championships": "بطولة الصين للبوكسينغ في الهواء الطلق",
    "chinese women's boxing championship": "بطولة الصين للبوكسينغ للسيدات",
    "chinese women's boxing championships": "بطولة الصين للبوكسينغ للسيدات",
    "chinese youth boxing championship": "بطولة الصين للبوكسينغ للشباب",
    "chinese youth boxing championships": "بطولة الصين للبوكسينغ للشباب",
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_sport_lab_oioioi_load_1(category: str, expected: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
@pytest.mark.fast
def test_sport_lab_oioioi_load_3(category: str, expected: str) -> None:
    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected


to_test = [
    ("test_sport_lab_oioioi_load_1", data_1, resolve_nats_sport_multi_v2),
    ("test_sport_lab_oioioi_load_3", data_3, resolve_nats_sport_multi_v2),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)

    # add_result = {x: v for x, v in data.items() if x in diff_result and "" == diff_result.get(x)}
    # dump_diff(add_result, f"{name}_add")
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
