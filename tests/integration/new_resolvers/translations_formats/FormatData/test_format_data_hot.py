#!/usr/bin/python3
"""Integration tests"""


import pytest

from ArWikiCats.translations_formats import FormatData


@pytest.fixture
def bot() -> FormatData:
    formatted_data = {
        "{en} records": "سجلات {ar}",
        "{en} house-of-representatives elections": "انتخابات مجلس نواب ولاية {ar}",
        "{en} in the War of 1812": "{ar} في حرب 1812",
        "{en} independent voters associations": "أعضاء رابطة الناخبين المستقلين في {ar}",
        "{en} independents": "مستقلون من ولاية {ar}",
    }

    data_list = {
        "georgia (u.s. state)": "ولاية جورجيا",
        "georgia": "جورجيا",
        "new york (state)": "ولاية نيويورك",
        "new york": "نيويورك",
        "virginia": "فرجينيا",
        "washington (state)": "ولاية واشنطن",
        "washington": "واشنطن",
        "washington, d.c.": "واشنطن العاصمة",
        "west virginia": "فرجينيا الغربية",
    }
    _bot = FormatData(formatted_data, data_list, key_placeholder="{en}", value_placeholder="{ar}")

    return _bot


def test_match_key(bot) -> None:
    result1 = bot.match_key("georgia (u.s. state) independents")
    assert result1 == "georgia (u.s. state)"

    result2 = bot.match_key("georgia independents")

    assert result2 == "georgia"


def test_search(bot) -> None:
    result1 = bot.search("georgia (u.s. state) independents")
    result2 = bot.search("georgia independents")

    assert result1 == "مستقلون من ولاية ولاية جورجيا"
    assert result2 == "مستقلون من ولاية جورجيا"


def test_case(bot) -> None:
    result = bot.search("washington, d.c. house-of-representatives elections")
    assert result == "انتخابات مجلس نواب ولاية واشنطن العاصمة"

    result2 = bot.search("washington house-of-representatives elections")
    assert result2 == "انتخابات مجلس نواب ولاية واشنطن"
