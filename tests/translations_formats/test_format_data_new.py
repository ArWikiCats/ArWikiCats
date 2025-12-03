#!/usr/bin/python3
"""Integration tests for format_films_country_data and """

import pytest

from ArWikiCats.translations import Nat_women
from ArWikiCats.translations_formats import MultiDataFormatterBase, format_films_country_data
from ArWikiCats.make_bots.media_bots.film_keys_bot import get_Films_key_CAO

# Template data with both nationality and sport placeholders
formatted_data = {
    "{nat_en} films": "أفلام {nat_ar}",
    "{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}",
}


@pytest.fixture
def yc_bot() -> MultiDataFormatterBase:
    bot = format_films_country_data(
        formatted_data=formatted_data,
        data_list=Nat_women,
        key_placeholder="{nat_en}",
        value_placeholder="{nat_ar}",
        key2_placeholder="{film_key}",
        value2_placeholder="{film_ar}",
        text_after="",
        text_before="",
        call_back=get_Films_key_CAO
    )

    return bot


test_data = [
    # standard
    ("Yemeni films", "أفلام يمنية"),
    # ("Yemeni action films", "أفلام حركة يمنية"),

]


@pytest.mark.parametrize(
    "category,expected",
    test_data,
    ids=[x[0] for x in test_data]
)
def test_year_country_combinations(yc_bot: MultiDataFormatterBase, category: str, expected: str) -> None:
    """Test all year-country translation patterns."""
    result = yc_bot.search_all(category)
    assert result == expected
