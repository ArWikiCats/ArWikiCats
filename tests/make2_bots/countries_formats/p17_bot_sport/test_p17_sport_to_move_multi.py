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
    # "egypt under-19 international players": "لاعبون تحت 19 سنة دوليون من مصر",
    # "egypt under-19 international playerss": "لاعبون تحت 19 سنة دوليون من مصر",
    # "egypt under-20 international playerss": "لاعبون تحت 20 سنة دوليون من مصر",
    # "egypt under-20 international players": "لاعبون تحت 20 سنة دوليون من مصر",

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
    "egypt under-19 international managers": "مدربون تحت 19 سنة دوليون من مصر",
    "egypt under-19 international soccer players": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم",
    "egypt under-19 international soccer playerss": "لاعبو منتخب مصر تحت 19 سنة لكرة القدم",
    "egypt under-20 international footballers": "لاعبو منتخب مصر تحت 20 سنة لكرة القدم",
    "egypt under-20 international managers": "مدربون تحت 20 سنة دوليون من مصر",
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


@pytest.mark.parametrize("category, expected", data_under.items(), ids=list(data_under.keys()))
@pytest.mark.fast
def test_under(category, expected) -> None:
    label1 = sport_formts_en_ar_is_p17_label(category)
    assert label1 == expected

    label2 = sport_formts_en_ar_is_p17_label(category, use_multi=True)
    assert label2 == expected


# =========================================================
#           DUMP
# =========================================================

TEMPORAL_CASES = [
    ("test_under", data_under, sport_formts_en_ar_is_p17_label),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name, data, callback):
    expected, diff_result = one_dump_test(data, callback, do_strip=False)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
