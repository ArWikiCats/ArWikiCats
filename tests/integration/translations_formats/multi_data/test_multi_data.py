#!/usr/bin/python3
"""Integration tests for format_multi_data"""

import pytest
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


@pytest.fixture
def multi_bot2() -> MultiDataFormatterBase:
    under_data = {
        "shooting location": "موقع التصوير",
        "developer": "التطوير",
        "location": "الموقع",
        "setting": "الأحداث",
        "disestablishment": "الانحلال",
        "reestablishment": "إعادة التأسيس",
        "establishment": "التأسيس",
        "setting location": "موقع الأحداث",
        "invention": "الاختراع",
        "country": "البلد",
        "introduction": "الاستحداث",
        "formal description": "الوصف",
        "photographing": "التصوير",
        "completion": "الانتهاء",
        "opening": "الافتتاح",
    }

    formatted_data = {
        "by year - {en}": "حسب {ar}",
        "by {en}": "حسب {ar}",
        "by {en2}": "حسب {ar2}",
        "by {en} or {en2}": "حسب {ar} أو {ar2}",
        "by {en} and {en2}": "حسب {ar} و{ar2}",
        "by {en} by {en2}": "حسب {ar} حسب {ar2}",
        "by city of {en}": "حسب مدينة {ar}",
        "by date of {en}": "حسب تاريخ {ar}",
        "by country of {en}": "حسب بلد {ar}",
        "by continent of {en}": "حسب قارة {ar}",
        "by location of {en}": "حسب موقع {ar}",
        "by period of {en}": "حسب حقبة {ar}",
        "by time of {en}": "حسب وقت {ar}",
        "by year of {en}": "حسب سنة {ar}",
        "by decade of {en}": "حسب عقد {ar}",
        "by era of {en}": "حسب عصر {ar}",
        "by millennium of {en}": "حسب ألفية {ar}",
        "by century of {en}": "حسب قرن {ar}",
        "by {en} and city of {en2}": "حسب {ar} ومدينة {ar2}",
    }

    return format_multi_data(
        formatted_data=formatted_data,
        data_list=under_data,
        key_placeholder="{en}",
        value_placeholder="{ar}",
        data_list2=under_data,
        key2_placeholder="{en2}",
        value2_placeholder="{ar2}",
        search_first_part=True,
        use_other_formatted_data=True,
    )


# =========================================================
#           data_compare
# =========================================================

data_compare2 = {
    "by country and country": "حسب البلد والبلد",
    "by shooting location": "حسب موقع التصوير",
    "by date of developer": "حسب تاريخ التطوير",
    "by city of disestablishment": "حسب مدينة الانحلال",
    "by city of reestablishment": "حسب مدينة إعادة التأسيس",
    "by city of establishment": "حسب مدينة التأسيس",
    "by country and city of setting": "حسب البلد ومدينة الأحداث",
    "by country and city of developer": "حسب البلد ومدينة التطوير",
}


@pytest.mark.parametrize("category, expected", data_compare2.items(), ids=data_compare2.keys())
@pytest.mark.fast
def test_data_compare_multi2(multi_bot2: MultiDataFormatterBase, category: str, expected: str) -> None:
    label2 = multi_bot2.search_all(category)

    assert label2 == expected
