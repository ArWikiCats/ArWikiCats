#!/usr/bin/python3
"""Integration tests"""

import pytest

from ArWikiCats.translations_formats import FormatData

sample_data_type = tuple[dict[str, str], dict[str, str]]


@pytest.fixture
def sample_data() -> sample_data_type:
    formatted_data = {
        "{nat} cup": "كأس {nat}",
    }

    data_list = {
        "yemeni": "اليمن",
    }

    return formatted_data, data_list


def test_text_after(sample_data: sample_data_type) -> None:
    formatted_data, data_list = sample_data

    bot = FormatData(
        formatted_data,
        data_list,
        key_placeholder="{nat}",
        value_placeholder="{nat}",
        text_after=" people",
    )
    key = bot.match_key("yemeni cup")
    assert key == "yemeni"

    result = bot.search("yemeni cup")
    assert result == "كأس اليمن"

    normalize = bot.normalize_category("yemeni people cup", "yemeni")
    assert normalize == "{nat} cup"

    result2 = bot.search("yemeni people cup")
    assert result2 == "كأس اليمن"


def test_text_before(sample_data: sample_data_type) -> None:
    formatted_data, data_list = sample_data

    bot = FormatData(formatted_data, data_list, key_placeholder="{nat}", value_placeholder="{nat}", text_before="the ")

    result3 = bot.search("the yemeni cup")
    assert result3 == "كأس اليمن"

    normalize2 = bot.normalize_category("the yemeni cup", "yemeni")
    assert normalize2 == "{nat} cup"


def test_text_before_text_after(sample_data: sample_data_type) -> None:
    formatted_data, data_list = sample_data

    bot = FormatData(
        formatted_data,
        data_list,
        key_placeholder="{nat}",
        value_placeholder="{nat}",
        text_after=" people",
        text_before="the ",
    )

    normalize2 = bot.normalize_category("the yemeni people cup", "yemeni")
    assert normalize2 == "{nat} cup"

    result4 = bot.search("the yemeni people cup")
    assert result4 == "كأس اليمن"
