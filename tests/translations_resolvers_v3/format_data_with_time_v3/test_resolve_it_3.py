#!/usr/bin/python3
"""Integration tests for format_films_country_data and """

import pytest
from ArWikiCats.translations_resolvers_v3.resolve_v3 import resolve_job_from_country, resolve_yearjob_from_country


class TestPart1:

    test_data_standard = {
        "writers from Crown of Aragon": "كتاب من تاج أرغون",
        "writers from yemen": "كتاب من اليمن",
    }

    @pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
    def test_country_combinations(self, category: str, expected: str) -> None:
        """
        Test
        """
        result = resolve_job_from_country(category)
        assert result == expected


class TestPart2:
    test_data_standard = {
        "14th-century writers from Crown of Aragon": "كتاب من تاج أرغون في القرن 14",
        "14th-century writers from yemen": "كتاب من اليمن في القرن 14",
    }

    @pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
    def test_year_country_combinations(self, category: str, expected: str) -> None:
        """
        Test
        """
        result = resolve_yearjob_from_country(category)
        assert result == expected
