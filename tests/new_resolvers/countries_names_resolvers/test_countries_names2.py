"""
Tests
"""

from typing import Callable

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.countries_names_resolvers.countries_names import resolve_by_countries_names

data_1 = {
    "university of china": "جامعة الصين",
    "politics of yemen": "سياسة اليمن",
    "military installations of yemen": "منشآت اليمن العسكرية",
    "foreign relations of yemen": "علاقات اليمن الخارجية",
    "national symbols of yemen": "رموز اليمن الوطنية",
    "university of yemen": "جامعة اليمن",
    "university of arts of yemen": "جامعة اليمن للفنون",
    "politics of venezuela": "سياسة فنزويلا",
    "politics of zambia": "سياسة زامبيا",
    "politics of zimbabwe": "سياسة زيمبابوي",
    "umayyad governors of yemen": "ولاة اليمن الأمويون",
    "angola men's international footballers": "لاعبو منتخب أنغولا لكرة القدم للرجال",
    "armenia national football team managers": "مدربو منتخب أرمينيا لكرة القدم",
    "bolivia men's international footballers": "لاعبو منتخب بوليفيا لكرة القدم للرجال",
    "bulgaria women's international footballers": "لاعبات منتخب بلغاريا لكرة القدم للسيدات",
    "chad sports templates": "قوالب تشاد الرياضية",
    "costa rica sports templates": "قوالب كوستاريكا الرياضية",
    "croatia men's international footballers": "لاعبو منتخب كرواتيا لكرة القدم للرجال",
    "cyprus women's international footballers": "لاعبات منتخب قبرص لكرة القدم للسيدات",
    "czech republic men's youth international footballers": "لاعبو منتخب التشيك لكرة القدم للشباب",
    "democratic-republic-of-congo amateur international soccer players": "لاعبو منتخب جمهورية الكونغو الديمقراطية لكرة القدم للهواة",
    "democratic-republic-of-congo men's a' international footballers": "لاعبو منتخب جمهورية الكونغو الديمقراطية لكرة القدم للرجال للمحليين",
    "guam men's international footballers": "لاعبو منتخب غوام لكرة القدم للرجال",
    "guam women's international footballers": "لاعبات منتخب غوام لكرة القدم للسيدات",
    "guinea-bissau women's international footballers": "لاعبات منتخب غينيا بيساو لكرة القدم للسيدات",
    "iceland women's youth international footballers": "لاعبات منتخب آيسلندا لكرة القدم للشابات",
    "kosovo national football team managers": "مدربو منتخب كوسوفو لكرة القدم",
    "latvia men's youth international footballers": "لاعبو منتخب لاتفيا لكرة القدم للشباب",
    "malawi men's international footballers": "لاعبو منتخب ملاوي لكرة القدم للرجال",
    "malaysia women's international footballers": "لاعبات منتخب ماليزيا لكرة القدم للسيدات",
    "mauritania sports templates": "قوالب موريتانيا الرياضية",
    "mexico women's international footballers": "لاعبات منتخب المكسيك لكرة القدم للسيدات",
    "north korea men's international footballers": "لاعبو منتخب كوريا الشمالية لكرة القدم للرجال",
    "peru men's youth international footballers": "لاعبو منتخب بيرو لكرة القدم للشباب",
    "poland men's international footballers": "لاعبو منتخب بولندا لكرة القدم للرجال",
    "san marino men's international footballers": "لاعبو منتخب سان مارينو لكرة القدم للرجال",
    "slovakia sports templates": "قوالب سلوفاكيا الرياضية",
    "switzerland men's youth international footballers": "لاعبو منتخب سويسرا لكرة القدم للشباب",
    "tanzania sports templates": "قوالب تنزانيا الرياضية",
    "trinidad and tobago national football team managers": "مدربو منتخب ترينيداد وتوباغو لكرة القدم",
    "tunisia men's a' international footballers": "لاعبو منتخب تونس لكرة القدم للرجال للمحليين",
    "tunisia national team": "منتخبات تونس الوطنية",
    "tunisia national teams": "منتخبات تونس الوطنية",
    "tunisia rally championship": "بطولة تونس للراليات",
    "tunisia sports templates": "قوالب تونس الرياضية",
    "ukraine women's international footballers": "لاعبات منتخب أوكرانيا لكرة القدم للسيدات",
    "venezuela international footballers": "لاعبو منتخب فنزويلا لكرة القدم",
    "venezuela rally championship": "بطولة فنزويلا للراليات",
    "yemen international footballers": "لاعبو منتخب اليمن لكرة القدم",
    "yemen international soccer players": "لاعبو منتخب اليمن لكرة القدم",
    "yemen rally championship": "بطولة اليمن للراليات",
    "yemen sports templates": "قوالب اليمن الرياضية",
    "zambia international footballers": "لاعبو منتخب زامبيا لكرة القدم",
    "zambia men's youth international footballers": "لاعبو منتخب زامبيا لكرة القدم للشباب",
    "zambia rally championship": "بطولة زامبيا للراليات",
    "zambia women's international footballers": "لاعبات منتخب زامبيا لكرة القدم للسيدات",
    "zimbabwe international footballers": "لاعبو منتخب زيمبابوي لكرة القدم",
    "zimbabwe rally championship": "بطولة زيمبابوي للراليات",
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_resolve_by_countries_names_1(category: str, expected: str) -> None:
    label1 = resolve_by_countries_names(category)
    assert label1 == expected


# =========================================================
#           DUMP
# =========================================================


TEMPORAL_CASES = [
    ("test_resolve_by_countries_names_1", data_1, resolve_by_countries_names),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback, do_strip=False)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
