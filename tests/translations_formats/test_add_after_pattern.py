#!/usr/bin/python3
"""Integration tests"""

import pytest

from src.translations_formats.format_data import FormatData


def test_add_after_pattern():

    formated_data = {
        "{nat} cup": "كأس {nat}",
    }

    data_list = {
        "yemeni": "اليمن",
    }

    bot = FormatData(formated_data, data_list, key_placeholder="{nat}", value_placeholder="{nat}", add_after_pattern=" people")
    key = bot.match_key("yemeni cup")
    assert key == "yemeni"

    result = bot.search("yemeni cup")
    assert result == "كأس اليمن"

    normalize = bot.normalize_category("yemeni people cup", "yemeni")
    assert normalize == "{nat} cup"

    result2 = bot.search("yemeni people cup")
    assert result2 == "كأس اليمن"
