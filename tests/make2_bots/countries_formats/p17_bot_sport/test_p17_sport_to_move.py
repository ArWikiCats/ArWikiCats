"""
Tests
"""

import pytest

from load_one_data import dump_diff, one_dump_test
from ArWikiCats.make_bots.countries_formats.p17_sport_to_move import (
    sport_formts_en_ar_is_p17_label,
    get_con_3_lab_sports,
)

# =========================================================
#           sport_formts_en_ar_is_p17_label
# =========================================================

data_under = {
    "aruba men's under-20 international footballers": "لاعبو منتخب أروبا تحت 20 سنة لكرة القدم للرجال",
    "lithuania men's under-21 international footballers": "لاعبو منتخب ليتوانيا تحت 21 سنة لكرة القدم للرجال",
    "mauritania men's under-20 international footballers": "لاعبو منتخب موريتانيا تحت 20 سنة لكرة القدم للرجال",
    "yemen under-13 international footballers": "لاعبو منتخب اليمن تحت 13 سنة لكرة القدم",
    "yemen under-14 international footballers": "لاعبو منتخب اليمن تحت 14 سنة لكرة القدم",
    "egypt amateur under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للهواة",
    "egypt amateur under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للهواة",
    "egypt amateur under-19 international soccer playerss": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للهواة",
    "egypt amateur under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للهواة",
    "egypt amateur under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للهواة",
    "egypt amateur under-20 international soccer playerss": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للهواة",
    "egypt men's a' under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للرجال للمحليين",
    "egypt men's a' under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للرجال للمحليين",
    "egypt men's a' under-19 international soccer playerss": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للرجال للمحليين",
    "egypt men's a' under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للرجال للمحليين",
    "egypt men's a' under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للرجال للمحليين",
    "egypt men's a' under-20 international soccer playerss": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للرجال للمحليين",
    "egypt men's b under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم الرديف للرجال",
    "egypt men's b under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم الرديف للرجال",
    "egypt men's b under-19 international soccer playerss": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم الرديف للرجال",
    "egypt men's b under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم الرديف للرجال",
    "egypt men's b under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم الرديف للرجال",
    "egypt men's b under-20 international soccer playerss": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم الرديف للرجال",
    "egypt men's under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للرجال",
    "egypt men's under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للرجال",
    "egypt men's under-19 international soccer playerss": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للرجال",
    "egypt men's under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للرجال",
    "egypt men's under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للرجال",
    "egypt men's under-20 international soccer playerss": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للرجال",
    "egypt men's youth under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للشباب",
    "egypt men's youth under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للشباب",
    "egypt men's youth under-19 international soccer playerss": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للشباب",
    "egypt men's youth under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للشباب",
    "egypt men's youth under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للشباب",
    "egypt men's youth under-20 international soccer playerss": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للشباب",
    "egypt under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم",
    "egypt under-19 international managers": "مدربو تحت 19 سنة دوليون من مصر",
    "egypt under-19 international players": "لاعبو تحت 19 سنة دوليون من مصر",
    "egypt under-19 international playerss": "لاعبو تحت 19 سنة دوليون من مصر",
    "egypt under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم",
    "egypt under-19 international soccer playerss": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم",
    "egypt under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم",
    "egypt under-20 international managers": "مدربو تحت 20 سنة دوليون من مصر",
    "egypt under-20 international players": "لاعبو تحت 20 سنة دوليون من مصر",
    "egypt under-20 international playerss": "لاعبو تحت 20 سنة دوليون من مصر",
    "egypt under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم",
    "egypt under-20 international soccer playerss": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم",
    "egypt women's under-19 international footballers": "لاعبات منتخب مصر تحت 19 سنة لكرة القدم للسيدات",
    "egypt women's under-19 international soccer players": "لاعبات منتخب مصر تحت 19 سنة لكرة القدم للسيدات",
    "egypt women's under-19 international soccer playerss": "لاعبات منتخب مصر تحت 19 سنة لكرة القدم للسيدات",
    "egypt women's under-20 international footballers": "لاعبات منتخب مصر تحت 20 سنة لكرة القدم للسيدات",
    "egypt women's under-20 international soccer players": "لاعبات منتخب مصر تحت 20 سنة لكرة القدم للسيدات",
    "egypt women's under-20 international soccer playerss": "لاعبات منتخب مصر تحت 20 سنة لكرة القدم للسيدات",
    "egypt women's youth under-19 international footballers": "لاعبات منتخب مصر تحت 19 سنة لكرة القدم للشابات",
    "egypt women's youth under-19 international soccer players": "لاعبات منتخب مصر تحت 19 سنة لكرة القدم للشابات",
    "egypt women's youth under-19 international soccer playerss": "لاعبات منتخب مصر تحت 19 سنة لكرة القدم للشابات",
    "egypt women's youth under-20 international footballers": "لاعبات منتخب مصر تحت 20 سنة لكرة القدم للشابات",
    "egypt women's youth under-20 international soccer players": "لاعبات منتخب مصر تحت 20 سنة لكرة القدم للشابات",
    "egypt women's youth under-20 international soccer playerss": "لاعبات منتخب مصر تحت 20 سنة لكرة القدم للشابات",
    "egypt youth under-19 international footballers": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للشباب",
    "egypt youth under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للشباب",
    "egypt youth under-19 international soccer playerss": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم للشباب",
    "egypt youth under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للشباب",
    "egypt youth under-20 international soccer players": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للشباب",
    "egypt youth under-20 international soccer playerss": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم للشباب",
}

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
def test_sport_formts_en_ar_is_p17_label_1(category, expected) -> None:
    label = sport_formts_en_ar_is_p17_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_under.items(), ids=list(data_under.keys()))
@pytest.mark.fast
def test_sport_formts_en_ar_is_p17_label_data_under(category, expected) -> None:
    label = sport_formts_en_ar_is_p17_label(category)
    assert label == expected


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
def test_get_con_3_lab_sports(category, expected):
    result = get_con_3_lab_sports(category)
    assert result == expected


# =========================================================
#           DUMP
# =========================================================

TEMPORAL_CASES = [
    ("test_sport_formts_en_ar_is_p17_label_1", data_1, sport_formts_en_ar_is_p17_label),
    ("test_sport_formts_en_ar_is_p17_label_data_under", data_under, sport_formts_en_ar_is_p17_label),
    ("test_get_con_3_lab_sports", test_data_get_con_3_lab, get_con_3_lab_sports),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name, data, callback):
    expected, diff_result = one_dump_test(data, callback, do_strip=False)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
