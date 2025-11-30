"""
Tests
"""

import pytest

from load_one_data import dump_diff, one_dump_test
from ArWikiCats.make_bots.countries_formats.p17_sport_to_move import (
    sport_formts_en_ar_is_p17_label,
    sport_formts_en_ar_is_p17_label_new,
    get_con_3_lab_sports,
)

# =========================================================
#           sport_formts_en_ar_is_p17_label
# =========================================================

data_1 = {
    "armenia national football team managers": "مدربو منتخب أرمينيا لكرة القدم",
    "kosovo national football team managers": "مدربو منتخب كوسوفو لكرة القدم",
    "trinidad and tobago national football team managers": "مدربو منتخب ترينيداد وتوباغو لكرة القدم",

    "aruba men's under-20 international footballers": "لاعبو منتخب أروبا تحت 20 سنة لكرة القدم للرجال",
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
    "lithuania men's under-21 international footballers": "لاعبو منتخب ليتوانيا تحت 21 سنة لكرة القدم للرجال",
    "malawi men's international footballers": "لاعبو منتخب مالاوي لكرة القدم للرجال",
    "malaysia women's international footballers": "لاعبات منتخب ماليزيا لكرة القدم للسيدات",
    "mauritania men's under-20 international footballers": "لاعبو منتخب موريتانيا تحت 20 سنة لكرة القدم للرجال",
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
    "venezuela international footballers": "لاعبو منتخب فنزويلا لكرة القدم ",
    "venezuela rally championship": "بطولة فنزويلا للراليات",
    "yemen international footballers": "لاعبو منتخب اليمن لكرة القدم",
    "yemen international soccer players": "لاعبو منتخب اليمن لكرة القدم",
    "yemen rally championship": "بطولة اليمن للراليات",
    "yemen sports templates": "قوالب اليمن الرياضية",
    "yemen under-13 international footballers": "لاعبو منتخب اليمن تحت 13 سنة لكرة القدم ",
    "yemen under-14 international footballers": "لاعبو منتخب اليمن تحت 14 سنة لكرة القدم ",
    "zambia international footballers": "لاعبو منتخب زامبيا لكرة القدم ",
    "zambia men's youth international footballers": "لاعبو منتخب زامبيا لكرة القدم للشباب",
    "zambia rally championship": "بطولة زامبيا للراليات",
    "zambia women's international footballers": "لاعبات منتخب زامبيا لكرة القدم للسيدات",
    "zimbabwe international footballers": "لاعبو منتخب زيمبابوي لكرة القدم ",
    "zimbabwe rally championship": "بطولة زيمبابوي للراليات",
    "angola men's international footballers": "لاعبو منتخب أنغولا لكرة القدم للرجال",
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=list(data_1.keys()))
@pytest.mark.fast
def test_sport_formts_en_ar_is_p17_label_1(category, expected) -> None:
    label = sport_formts_en_ar_is_p17_label(category)
    assert label == expected
    label2 = sport_formts_en_ar_is_p17_label_new(category)
    assert label2 == expected


# =========================================================
#           get_con_3_lab_sports
# =========================================================


test_data_get_con_3_lab = {
    "amateur international footballers": "لاعبو منتخب {} لكرة القدم للهواة",
    "amateur international soccer players": "لاعبو منتخب {} لكرة القدم للهواة",
    "international footballers": "لاعبو منتخب {} لكرة القدم ",
    "international soccer players": "لاعبو منتخب {} لكرة القدم ",
    "men's a' international footballers": "لاعبو منتخب {} لكرة القدم للرجال للمحليين",
    "men's international footballers": "لاعبو منتخب {} لكرة القدم للرجال",
    "men's international soccer players": "لاعبو منتخب {} لكرة القدم للرجال",
    "men's under-20 international footballers": "لاعبو منتخب {} تحت 20 سنة لكرة القدم للرجال",
    "men's under-21 international footballers": "لاعبو منتخب {} تحت 21 سنة لكرة القدم للرجال",
    "men's youth international footballers": "لاعبو منتخب {} لكرة القدم للشباب",
    "national football team managers": "مدربو منتخب {} لكرة القدم",
    "national team": "منتخبات {} الوطنية",
    "national teams": "منتخبات {} الوطنية",
    "rally championship": "بطولة {} للراليات",
    "sports templates": "قوالب {} الرياضية",
    "under-13 international footballers": "لاعبو منتخب {} تحت 13 سنة لكرة القدم ",
    "under-14 international footballers": "لاعبو منتخب {} تحت 14 سنة لكرة القدم ",
    "women's international footballers": "لاعبات منتخب {} لكرة القدم للسيدات",
    "women's youth international footballers": "لاعبات منتخب {} لكرة القدم للشابات",
}


@pytest.mark.parametrize("category, expected", test_data_get_con_3_lab.items(), ids=list(test_data_get_con_3_lab.keys()))
@pytest.mark.fast
def test_get_con_3_lab_sports(category, expected):
    result = get_con_3_lab_sports(category)
    assert result == expected


# =========================================================
#           DUMP
# =========================================================

TEMPORAL_CASES = [
    ("test_sport_formts_en_ar_is_p17_label_1", data_1, sport_formts_en_ar_is_p17_label),
    ("test_sport_formts_en_ar_is_p17_label_new", data_1, sport_formts_en_ar_is_p17_label_new),
    ("test_get_con_3_lab_sports", test_data_get_con_3_lab, get_con_3_lab_sports),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name, data, callback):
    expected, diff_result = one_dump_test(data, callback, do_strip=True)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
