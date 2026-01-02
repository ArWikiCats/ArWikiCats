#!/usr/bin/python3
"""Integration tests for format_multi_data  """

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.translations_formats import (
    MultiDataFormatterBase,
    format_multi_data,
)


@pytest.fixture
def multi_bot() -> MultiDataFormatterBase:
    under_data = {
        "under-20": "تحت 20 سنة",
        "under-15": "تحت 15 سنة",
    }
    formatted_data = {
        "{en} {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم ",
        "{en} {under_en} amateur international soccer players": "لاعبو منتخب {ar} {under_ar} لكرة القدم للهواة",
        "{en} men's {under_en} international footballers": "لاعبو منتخب {ar} {under_ar} لكرة القدم للرجال",
        "national {under_en} football team": "منتخب كرة القدم {under_ar}",
        "{en} national football team managers": "مدربو منتخب {ar} لكرة القدم",
        "{en} sports templates": "قوالب {ar} الرياضية",
        "{en} amateur international soccer players": "لاعبو منتخب {ar} لكرة القدم للهواة",
        "{en} men's a' international footballers": "لاعبو منتخب {ar} لكرة القدم للرجال للمحليين",
    }
    countries_from_nat = {
        "armenia": "أرمينيا",
        "chad": "تشاد",
        "mauritania": "موريتانيا",
        "yemen": "اليمن",
    }
    return format_multi_data(
        formatted_data=formatted_data,
        data_list=under_data,
        key_placeholder="{under_en}",
        value_placeholder="{under_ar}",
        data_list2=countries_from_nat,
        key2_placeholder="{en}",
        value2_placeholder="{ar}",
        use_other_formatted_data=True,
    )


# =========================================================
#           data_compare
# =========================================================

data_compare = {
    "armenia national football team managers": "مدربو منتخب أرمينيا لكرة القدم",
    "chad sports templates": "قوالب تشاد الرياضية",
    "yemen amateur international soccer players": "لاعبو منتخب اليمن لكرة القدم للهواة",
    "yemen men's a' international footballers": "لاعبو منتخب اليمن لكرة القدم للرجال للمحليين",
    "mauritania men's under-20 international footballers": "لاعبو منتخب موريتانيا تحت 20 سنة لكرة القدم للرجال",
    "national under-15 football team": "منتخب كرة القدم تحت 15 سنة",
}


@pytest.mark.fast
def test_data_compare_one(multi_bot: MultiDataFormatterBase) -> None:
    category = "national under-15 football team"
    expected = "منتخب كرة القدم تحت 15 سنة"

    label2 = multi_bot.search_all(category)

    assert label2 == expected


@pytest.mark.parametrize("category, expected", data_compare.items(), ids=data_compare.keys())
@pytest.mark.fast
def test_data_compare_multi(multi_bot: MultiDataFormatterBase, category: str, expected: str) -> None:
    label2 = multi_bot.search_all(category)

    assert label2 == expected


# =========================================================
#           DUMP
# =========================================================


TEMPORAL_CASES = [
    ("test_data_compare", data_compare),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(multi_bot: MultiDataFormatterBase, name: str, data: dict[str, str]) -> None:
    callback = multi_bot.search_all
    expected, diff_result = one_dump_test(data, callback, do_strip=False)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
