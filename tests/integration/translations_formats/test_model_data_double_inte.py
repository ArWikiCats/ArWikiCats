#!/usr/bin/python3
"""

Integration tests

TODO: write tests for the parameters:
        splitter: str = " ",
        sort_ar_labels: bool = False,
"""

import pytest

from ArWikiCats.translations_formats import FormatDataDouble


@pytest.fixture
def bot() -> FormatDataDouble:
    # Template data with both nationality and sport placeholders
    formatted_data = {
        "{film_key} films": "أفلام {film_ar}",
        "{film_key} television commercials": "إعلانات تجارية تلفزيونية {film_ar}",
    }

    # film_keys_for_female
    data_list2 = {
        "action comedy": "حركة كوميدية",
        "action thriller": "إثارة حركة",
        "action": "حركة",
        "drama": "درامية",
        "upcoming": "قادمة",
        "horror": "رعب",
        "black": "سوداء",
        "black-and-white": "أبيض وأسود",
        "psychological horror": "رعب نفسي",
    }

    # Create an instance of the FormatDataDouble class with the formatted data and data list
    _bot = FormatDataDouble(
        formatted_data=formatted_data,
        data_list=data_list2,
        key_placeholder="{film_key}",
        value_placeholder="{film_ar}",
    )

    put_label_last = {
        "low-budget",
        "christmas",
        "lgbtq-related",
        "upcoming",
    }
    _bot.update_put_label_last(put_label_last)
    return _bot


test_data = {
    "black-and-white films": "أفلام أبيض وأسود",
    "black-and-white action films": "أفلام أبيض وأسود حركة",
    "drama action television commercials": "إعلانات تجارية تلفزيونية درامية حركة",
    "horror upcoming films": "أفلام رعب قادمة",
    "psychological horror films": "أفلام رعب نفسي",
    "psychological horror black-and-white films": "أفلام رعب نفسي أبيض وأسود",
    "horror horror films": "أفلام رعب رعب",
}


@pytest.mark.parametrize("category,expected", test_data.items(), ids=test_data.keys())
def test_year_country_combinations(bot: FormatDataDouble, category: str, expected: str) -> None:
    """
    Test
    """
    result = bot.search(category)
    assert result == expected


test_match_key_data = {
    "Yemeni action films": "action",
    "Yemeni action drama films": "action drama",
    "Yemeni upcoming horror films": "upcoming horror",
    "Yemeni black-and-white films": "black-and-white",
    "psychological horror black-and-white films": "psychological horror black-and-white",
}


@pytest.mark.parametrize("category, expected", test_match_key_data.items(), ids=test_match_key_data.keys())
@pytest.mark.fast
def test_match_key(bot: FormatDataDouble, category: str, expected: str) -> None:
    result = bot.match_key(category)
    assert result == expected
