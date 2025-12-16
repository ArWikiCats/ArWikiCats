#!/usr/bin/python3
"""Integration tests for format_films_country_data and """

import pytest
from ArWikiCats.translations_resolvers_v3.resolve_v33 import multi_bot_v3


class TestCountriesPart:

    test_data_standard = {
        "writers from Crown of Aragon": "كتاب من تاج أرغون",
        "writers from yemen": "كتاب من اليمن",
    }

    @pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
    def test_country_combinations(self, category: str, expected: str) -> None:
        """
        Test
        """
        bot = multi_bot_v3()
        result = bot.country_bot.search(category)
        assert result == expected


class TestYearPart:

    test_data_standard = {
        "100s": "عقد 100",
    }

    @pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
    def test_year_combinations(self, category: str, expected: str) -> None:
        """
        Test
        """
        bot = multi_bot_v3()
        result = bot.other_bot.search_all(category)
        assert result == expected


class TestAllParts:
    test_data_standard = {
        "14th-century writers from Crown of Aragon": "كتاب من تاج أرغون في القرن 14",
        "14th-century writers from yemen": "كتاب من اليمن في القرن 14",
    }

    @pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
    def test_year_country_combinations(self, category: str, expected: str) -> None:
        """
        Test
        """
        bot = multi_bot_v3()
        result = bot.search_all(category)
        assert result == expected
