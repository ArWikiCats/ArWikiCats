#!/usr/bin/python3
""" """

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.translations_resolvers.sports_formats_oioioi import sport_lab_oioioi_load
from ArWikiCats.translations_resolvers_v2.nats_sport_multi_v2 import resolve_nats_sport_multi_v2

data0 = {
    # "chinese championships (boxing)": "بطولة الصين للبوكسينغ",
    # "chinese open (boxing)": "الصين المفتوحة للبوكسينغ",
    "chinese boxing cups": "كؤوس للبوكسينغ الصين",
    "chinese boxing leagues": "دوريات للبوكسينغ الصين",
    "chinese boxing chairmen and investors": "رؤساء ومسيرو للبوكسينغ الصين",
    "chinese boxing clubs": "أندية للبوكسينغ الصين",
    "chinese boxing coaches": "مدربو للبوكسينغ الصين",
    "chinese boxing competitions": "منافسات للبوكسينغ الصين",
    "chinese boxing cup competitions": "منافسات كؤوس للبوكسينغ الصين",
    "chinese outdoor boxing": "للبوكسينغ الصين في الهواء الطلق",
    "chinese women's boxing": "للبوكسينغ الصين نسائية",
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
    "chinese domestic women's boxing clubs": "أندية للبوكسينغ محلية الصين للسيدات",
    "chinese domestic women's boxing coaches": "مدربو للبوكسينغ محلية الصين للسيدات",
    "chinese domestic women's boxing competitions": "منافسات للبوكسينغ محلية الصين للسيدات",
    "chinese domestic women's boxing cups": "كؤوس للبوكسينغ محلية الصين للسيدات",
    "chinese domestic women's boxing leagues": "دوريات للبوكسينغ محلية الصين للسيدات",
    "chinese indoor boxing": "للبوكسينغ الصين داخل الصالات",
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

data = {
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
    "chinese outdoor boxing clubs": "أندية للبوكسينغ الصين في الهواء الطلق",
    "chinese women's boxing championship": "بطولة الصين للبوكسينغ للسيدات",
    "chinese women's boxing championships": "بطولة الصين للبوكسينغ للسيدات",
    "chinese youth boxing championship": "بطولة الصين للبوكسينغ للشباب",
    "chinese youth boxing championships": "بطولة الصين للبوكسينغ للشباب",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=list(data.keys()))
@pytest.mark.fast
def test_sport_lab_oioioi_load(category: str, expected: str) -> None:
    label1 = sport_lab_oioioi_load(category)
    assert label1 == expected

    label2 = resolve_nats_sport_multi_v2(category)
    assert label2 == expected


to_test = [
    ("test_sport_lab_oioioi_load_0", data0),
    ("test_sport_lab_oioioi_load_1", data),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_nats_sport_multi_v2)
    dump_diff(diff_result, name)

    # add_result = {x: v for x, v in data.items() if x in diff_result and "" == diff_result.get(x)}
    # dump_diff(add_result, f"{name}_add")
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
