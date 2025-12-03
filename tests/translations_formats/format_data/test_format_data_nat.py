#!/usr/bin/python3
"""Integration tests for :mod:`teamsnew_bot` lazy resolver."""

import re

import pytest

from ArWikiCats.translations_formats import FormatData


@pytest.fixture
def bot() -> FormatData:
    formatted_data = {
        "{en_nat} people": "{nat_men1}",  # 187
        "{en_nat} people by occupation": "{nat_men1} حسب المهنة",  # 182
        "{en_nat} sportspeople": "رياضيون {nat_men1}",  # 174
        "{en_nat} men": "رجال {nat_men1}",  # 183
        "{en_nat} sportsmen": "رياضيون رجال {nat_men1}",  # 182
    }

    data_list = {
        "welsh": "ويلزيون",
        "abkhazian": "أبخازيون",
        "yemeni": "يمنيون",
        "afghan": "أفغان",
        "african": "أفارقة",
        "ancient-roman": "رومان قدماء",
    }
    _bot = FormatData(formatted_data, data_list, "{en_nat}", "{nat_men1}")
    return _bot


test_data = {
    "welsh people": "ويلزيون",
    "yemeni people": "يمنيون",
    "yemeni men": "رجال يمنيون",
}


@pytest.mark.parametrize("category,expected", test_data.items(), ids=test_data.keys())
def test_search(bot: FormatData, category: str, expected: str) -> None:
    assert bot.search(category) == expected
