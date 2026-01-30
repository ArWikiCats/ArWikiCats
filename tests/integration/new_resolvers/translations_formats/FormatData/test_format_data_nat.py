#!/usr/bin/python3
"""Integration tests for :mod:`FormatData` with nationality data."""


import pytest

from ArWikiCats.translations_formats import FormatData


@pytest.fixture
def bot() -> FormatData:
    formatted_data = {
        "{en_nat} people": "{males}",  # 187
        "{en_nat} people by occupation": "{males} حسب المهنة",  # 182
        "{en_nat} sports-people": "رياضيون {males}",  # 174
        "{en_nat} men": "رجال {males}",  # 183
        "{en_nat} sportsmen": "رياضيون رجال {males}",  # 182
    }

    data_list = {
        "welsh": "ويلزيون",
        "abkhazian": "أبخازيون",
        "yemeni": "يمنيون",
        "afghan": "أفغان",
        "african": "أفارقة",
        "ancient-roman": "رومان قدماء",
    }
    _bot = FormatData(formatted_data, data_list, "{en_nat}", "{males}")
    return _bot


test_data = {
    "welsh people": "ويلزيون",
    "yemeni people": "يمنيون",
    "yemeni men": "رجال يمنيون",
}


@pytest.mark.parametrize("category,expected", test_data.items(), ids=test_data.keys())
def test_search(bot: FormatData, category: str, expected: str) -> None:
    assert bot.search(category) == expected
