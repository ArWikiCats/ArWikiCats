"""
Tests
"""

import pytest

from load_one_data import dump_diff, one_dump_test
from ArWikiCats.make_bots.countries_formats.p17_sport_to_move import (
    get_en_ar_is_p17_label,
    get_en_ar_is_p17_label_multi,
)

# =========================================================
#           data_compare
# =========================================================

data_compare = {
    "armenia national football team managers": "مدربو منتخب أرمينيا لكرة القدم",
    "chad sports templates": "قوالب تشاد الرياضية",
    "democratic-republic-of-the-congo amateur international soccer players": "لاعبو منتخب جمهورية الكونغو الديمقراطية لكرة القدم للهواة",
    "democratic-republic-of-the-congo men's a' international footballers": "لاعبو منتخب جمهورية الكونغو الديمقراطية لكرة القدم للرجال للمحليين",
    "lithuania men's under-21 international footballers": "لاعبو منتخب ليتوانيا تحت 21 سنة لكرة القدم للرجال",
    "mauritania men's under-20 international footballers": "لاعبو منتخب موريتانيا تحت 20 سنة لكرة القدم للرجال",
}


@pytest.mark.parametrize("category, expected", data_compare.items(), ids=list(data_compare.keys()))
@pytest.mark.skip2
def test_data_compare(category, expected) -> None:
    label1 = get_en_ar_is_p17_label(category)
    assert label1 == expected

    label2 = get_en_ar_is_p17_label_multi(category)
    assert label2 == expected

# =========================================================
#           DUMP
# =========================================================


TEMPORAL_CASES = [
    ("test_data_compare", data_compare, get_en_ar_is_p17_label_multi),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name, data, callback):
    expected, diff_result = one_dump_test(data, callback, do_strip=False)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
