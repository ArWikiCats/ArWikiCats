#!/usr/bin/python3
""" """

import pytest
from load_one_data import dump_diff, one_dump_test

# from ArWikiCats.new_resolvers.sports_resolvers.nationalities_and_sports import resolve_nats_sport_multi_v2
# from ArWikiCats.new_resolvers.sports_resolvers.raw_sports import resolve_sport_label_unified
from ArWikiCats.new_resolvers.sports_resolvers.raw_sports_with_suffixes import wrap_team_xo_normal_2025_with_ends

test_find_labels_bot_data_0 = {
    "wheelchair rugby league": "دوري الرجبي على الكراسي المتحركة",
    "rugby": "الرجبي",
    "speed skating": "التزلج السريع",
    "martial arts": "الفنون القتالية",
    "baseball": "كرة القاعدة",
    "basketball": "كرة السلة",
    "chess": "الشطرنج",
    "field hockey": "هوكي الميدان",
    "professional wrestling clubs": "أندية مصارعة محترفين",
    "professional wrestling coaches": "مدربو مصارعة محترفين",
    "wrestling clubs": "أندية مصارعة",
    "wrestling coaches": "مدربو مصارعة",
}

test_find_labels_bot_data = {
    "wheelchair rugby finals": "نهائيات الرجبي على الكراسي المتحركة",
    "wheelchair rugby league finals": "نهائيات دوري الرجبي على الكراسي المتحركة",
    "rugby finals": "نهائيات الرجبي",
    "rugby league finals": "نهائيات دوري الرجبي",
    "baseball finals": "نهائيات كرة القاعدة",
    "olympic gold medalists in baseball": "فائزون بميداليات ذهبية أولمبية في كرة القاعدة",
    "olympic bronze medalists in baseball": "فائزون بميداليات برونزية أولمبية في كرة القاعدة",
    "baseball champions": "أبطال كرة القاعدة",
    "baseball league": "دوري كرة القاعدة",
    "football league": "دوري كرة القدم",
    "hockey league": "دوري هوكي",
    "ice hockey league": "دوري هوكي الجليد",
    "olympics baseball": "كرة القاعدة في الألعاب الأولمبية",
    "rugby league league": "دوري دوري الرجبي",
    "softball league": "دوري الكرة اللينة",
    "summer olympics baseball": "كرة القاعدة في الألعاب الأولمبية الصيفية",
    "summer olympics basketball chairmen and investors": "رؤساء ومسيرو كرة السلة في الألعاب الأولمبية الصيفية",
    "summer olympics basketball": "كرة السلة في الألعاب الأولمبية الصيفية",
    "summer olympics field hockey": "هوكي الميدان في الألعاب الأولمبية الصيفية",
    "summer olympics football": "كرة القدم في الألعاب الأولمبية الصيفية",
    "summer olympics handball": "كرة اليد في الألعاب الأولمبية الصيفية",
    "summer olympics rugby sevens": "سباعيات الرجبي في الألعاب الأولمبية الصيفية",
    "summer olympics volleyball": "كرة الطائرة في الألعاب الأولمبية الصيفية",
    "summer olympics water polo": "كرة الماء في الألعاب الأولمبية الصيفية",
    "winter olympics baseball": "كرة القاعدة في الألعاب الأولمبية الشتوية",
}


@pytest.mark.parametrize("category, expected", test_find_labels_bot_data.items(), ids=test_find_labels_bot_data.keys())
@pytest.mark.fast
def test_Get_New_team_xo_data(category: str, expected: str) -> None:
    label1 = wrap_team_xo_normal_2025_with_ends(category)
    assert isinstance(label1, str)
    assert label1 == expected


@pytest.mark.parametrize(
    "category, expected", test_find_labels_bot_data_0.items(), ids=test_find_labels_bot_data_0.keys()
)
@pytest.mark.fast
def test_test_find_labels_bot_data_0(category: str, expected: str) -> None:
    label1 = wrap_team_xo_normal_2025_with_ends(category)
    assert isinstance(label1, str)
    assert label1 == expected


TEMPORAL_CASES = [
    ("test_find_labels_bot", test_find_labels_bot_data, wrap_team_xo_normal_2025_with_ends),
    ("test_find_labels_bot_2", test_find_labels_bot_data_0, wrap_team_xo_normal_2025_with_ends),
]


@pytest.mark.parametrize("name,data,callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
