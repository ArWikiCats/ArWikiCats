"""
Tests
"""

import pytest
from typing import Callable

from load_one_data import dump_diff, one_dump_test
from ArWikiCats.translations_resolvers_v2.nats_v2 import (
    resolve_by_nats,
)

main_data_2 = {
    # males - en_is_nat_ar_is_mens
    "yemeni non profit publishers": "ناشرون غير ربحيون يمنيون",
    "yemeni non-profit publishers": "ناشرون غير ربحيون يمنيون",
    "yemeni government officials": "مسؤولون حكوميون يمنيون",
    "saudi non profit publishers": "ناشرون غير ربحيون سعوديون",
    "egyptian government officials": "مسؤولون حكوميون مصريون",

    # ar - en_is_nat_ar_is_P17
    "Bahraini King's Cup": "كأس ملك البحرين",
    "Yemeni King's Cup": "كأس ملك اليمن",
    "French Grand Prix": "جائزة فرنسا الكبرى",
    "Italian Grand Prix": "جائزة إيطاليا الكبرى",
    "French Open": "فرنسا المفتوحة",
    "Australian Open": "أستراليا المفتوحة",
    "French Ladies Open": "فرنسا المفتوحة للسيدات",
    "Canadian Cup": "كأس كندا",
    "Egyptian Independence": "استقلال مصر",
    "Syrian Independence": "استقلال سوريا",
    "Canadian National University": "جامعة كندا الوطنية",
    "Egyptian National University": "جامعة مصر الوطنية",
    "Canadian National University Alumni": "خريجو جامعة كندا الوطنية",
    "Egyptian National University Alumni": "خريجو جامعة مصر الوطنية",
    "Japanese national women's motorsports racing team": "منتخب اليابان لسباق رياضة المحركات للسيدات",
    "French national women's motorsports racing team": "منتخب فرنسا لسباق رياضة المحركات للسيدات",

    # the_male - en_is_nat_ar_is_al_mens
    "Iraqi President Cup": "كأس الرئيس العراقي",
    "Egyptian President Cup": "كأس الرئيس المصري",
    "Iraqi Federation Cup": "كأس الاتحاد العراقي",
    "Saudi Federation Cup": "كأس الاتحاد السعودي",
    "Iraqi FA Cup": "كأس الاتحاد العراقي",
    "Egyptian FA Cup": "كأس الاتحاد المصري",
    "Iraqi Occupation": "الاحتلال العراقي",
    "American Occupation": "الاحتلال الأمريكي",
    "Iraqi Super Cup": "كأس السوبر العراقي",
    "Egyptian Super Cup": "كأس السوبر المصري",
    "Saudi Elite Cup": "كأس النخبة السعودي",
    "Iraqi Referendum": "الاستفتاء العراقي",
    "Syrian Referendum": "الاستفتاء السوري",
    "American Involvement": "التدخل الأمريكي",
    "French Involvement": "التدخل الفرنسي",
    "Egyptian Census": "التعداد المصري",
    "Iraqi Census": "التعداد العراقي",
    "Iraqi Professional Football League": "دوري كرة القدم العراقي للمحترفين",
    "Saudi Professional Football League": "دوري كرة القدم السعودي للمحترفين",
    "Iraqi Premier Football League": "الدوري العراقي الممتاز لكرة القدم",
    "Egyptian Premier Football League": "الدوري المصري الممتاز لكرة القدم",
    "Iraqi National Super League": "دوري السوبر العراقي",
    "Egyptian National Super League": "دوري السوبر المصري",
    "Iraqi Super League": "دوري السوبر العراقي",
    "Saudi Super League": "دوري السوبر السعودي",
    "Iraqi Premier League": "الدوري العراقي الممتاز",
    "Egyptian Premier League": "الدوري المصري الممتاز",
    "Iraqi Premier Division": "الدوري العراقي الممتاز",
    "Saudi Premier Division": "الدوري السعودي الممتاز",
    "Iraqi amateur football league": "الدوري العراقي لكرة القدم للهواة",
    "Egyptian amateur football league": "الدوري المصري لكرة القدم للهواة",
    "Iraqi football league": "الدوري العراقي لكرة القدم",
    "Saudi football league": "الدوري السعودي لكرة القدم",
    "Egyptian Population Census": "التعداد السكاني المصري",
    "Iraqi Population Census": "التعداد السكاني العراقي",
    "Egyptian population and housing census": "التعداد المصري للسكان والمساكن",
    "Iraqi population and housing census": "التعداد العراقي للسكان والمساكن",
    "Egyptian National Party": "الحزب الوطني المصري",
    "Iraqi National Party": "الحزب الوطني العراقي",
    "Egyptian Criminal Law": "القانون الجنائي المصري",
    "Iraqi Criminal Law": "القانون الجنائي العراقي",
    "Egyptian Family Law": "قانون الأسرة المصري",
    "Iraqi Family Law": "قانون الأسرة العراقي",
    "Egyptian Labour Law": "قانون العمل المصري",
    "Iraqi Labour Law": "قانون العمل العراقي",
    "Egyptian Abortion Law": "قانون الإجهاض المصري",
    "American Abortion Law": "قانون الإجهاض الأمريكي",
    "French Rugby Union Leagues": "اتحاد دوري الرجبي الفرنسي",
    "Australian Rugby Union Leagues": "اتحاد دوري الرجبي الأسترالي",
    "French Women's Rugby Union": "اتحاد الرجبي الفرنسي للنساء",
    "Australian Women's Rugby Union": "اتحاد الرجبي الأسترالي للنساء",
    "French Rugby Union": "اتحاد الرجبي الفرنسي",
    "Australian Rugby Union": "اتحاد الرجبي الأسترالي",
    "American Presidential Pardons": "العفو الرئاسي الأمريكي",
    "Egyptian Presidential Pardons": "العفو الرئاسي المصري",
    "American Pardons": "العفو الأمريكي",
    "Egyptian Pardons": "العفو المصري",
}


@pytest.mark.parametrize("category, expected", main_data_2.items(), ids=list(main_data_2.keys()))
@pytest.mark.fast
def test_resolve_by_all(category: str, expected: str) -> None:
    label = resolve_by_nats(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_resolve_by_all", main_data_2, resolve_by_nats),
]


@pytest.mark.dump
@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
