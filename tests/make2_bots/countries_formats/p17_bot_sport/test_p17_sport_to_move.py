"""
Tests
"""

import pytest

from load_one_data import dump_diff, one_dump_test
from ArWikiCats.make_bots.countries_formats.p17_sport_to_move import (
    get_en_ar_is_p17_label,
    get_con_3_lab_sports,
)

# =========================================================
#           get_en_ar_is_p17_label
# =========================================================

data_1 = {
    "armenia national football team managers": "مدربو منتخب أرمينيا لكرة القدم",
    "kosovo national football team managers": "مدربو منتخب كوسوفو لكرة القدم",
    "trinidad and tobago national football team managers": "مدربو منتخب ترينيداد وتوباغو لكرة القدم",

    "bolivia men's international footballers": "لاعبو منتخب بوليفيا لكرة القدم للرجال",
    "bulgaria women's international footballers": "لاعبات منتخب بلغاريا لكرة القدم للسيدات",
    "chad sports templates": "قوالب تشاد الرياضية",
    "costa rica sports templates": "قوالب كوستاريكا الرياضية",
    "croatia men's international footballers": "لاعبو منتخب كرواتيا لكرة القدم للرجال",
    "cyprus women's international footballers": "لاعبات منتخب قبرص لكرة القدم للسيدات",
    "czech republic men's youth international footballers": "لاعبو منتخب التشيك لكرة القدم للشباب",
    "democratic-republic-of-the-congo amateur international soccer players": "لاعبو منتخب جمهورية الكونغو الديمقراطية لكرة القدم للهواة",
    "democratic-republic-of-the-congo men's a' international footballers": "لاعبو منتخب جمهورية الكونغو الديمقراطية لكرة القدم للرجال للمحليين",
    "guam men's international footballers": "لاعبو منتخب غوام لكرة القدم للرجال",
    "guam women's international footballers": "لاعبات منتخب غوام لكرة القدم للسيدات",
    "guinea-bissau women's international footballers": "لاعبات منتخب غينيا بيساو لكرة القدم للسيدات",
    "iceland women's youth international footballers": "لاعبات منتخب آيسلندا لكرة القدم للشابات",
    "latvia men's youth international footballers": "لاعبو منتخب لاتفيا لكرة القدم للشباب",
    "malawi men's international footballers": "لاعبو منتخب مالاوي لكرة القدم للرجال",
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
    "angola men's international footballers": "لاعبو منتخب أنغولا لكرة القدم للرجال",
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=list(data_1.keys()))
@pytest.mark.fast
def test_get_en_ar_is_p17_label_1(category: str, expected: str) -> None:
    label1 = get_en_ar_is_p17_label(category)
    assert label1 == expected

# =========================================================
#           get_con_3_lab_sports
# =========================================================


test_data_get_con_3_lab = {
    "{en} amateur international footballers": "لاعبو منتخب {ar} لكرة القدم للهواة",
    "{en} amateur international soccer players": "لاعبو منتخب {ar} لكرة القدم للهواة",
    "{en} international footballers": "لاعبو منتخب {ar} لكرة القدم",
    "{en} international soccer players": "لاعبو منتخب {ar} لكرة القدم",
    "{en} men's a' international footballers": "لاعبو منتخب {ar} لكرة القدم للرجال للمحليين",
    "{en} men's international footballers": "لاعبو منتخب {ar} لكرة القدم للرجال",
    "{en} men's international soccer players": "لاعبو منتخب {ar} لكرة القدم للرجال",
    "{en} men's under-20 international footballers": "لاعبو منتخب {ar} تحت 20 سنة لكرة القدم للرجال",
    "{en} men's under-21 international footballers": "لاعبو منتخب {ar} تحت 21 سنة لكرة القدم للرجال",
    "{en} men's youth international footballers": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} national football team managers": "مدربو منتخب {ar} لكرة القدم",
    "{en} national team": "منتخبات {ar} الوطنية",
    "{en} national teams": "منتخبات {ar} الوطنية",
    "{en} rally championship": "بطولة {ar} للراليات",
    "{en} sports templates": "قوالب {ar} الرياضية",
    "{en} under-13 international footballers": "لاعبو منتخب {ar} تحت 13 سنة لكرة القدم",
    "{en} under-14 international footballers": "لاعبو منتخب {ar} تحت 14 سنة لكرة القدم",
    "{en} women's international footballers": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's youth international footballers": "لاعبات منتخب {ar} لكرة القدم للشابات",
}


@pytest.mark.parametrize("category, expected", test_data_get_con_3_lab.items(), ids=list(test_data_get_con_3_lab.keys()))
@pytest.mark.fast
def test_get_con_3_lab_sports(category: str, expected: str) -> None:
    result = get_con_3_lab_sports(category)
    assert result == expected


# =========================================================
#           DUMP
# =========================================================

TEMPORAL_CASES = [
    ("test_get_en_ar_is_p17_label_1", data_1, get_en_ar_is_p17_label),
    ("test_get_con_3_lab_sports", test_data_get_con_3_lab, get_con_3_lab_sports),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name, data, callback) -> None:
    expected, diff_result = one_dump_test(data, callback, do_strip=False)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
