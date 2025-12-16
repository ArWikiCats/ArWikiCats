#!/usr/bin/python3
"""Integration tests for format_films_country_data and """

import pytest
import re

from ArWikiCats.translations_formats import FormatData, YearFormatData, MultiDataFormatterBase, V3Formats, MultiDataFormatterBaseYearV3


@pytest.fixture
def multi_bot() -> MultiDataFormatterBase:
    """Create a format_multi_data instance for testing."""

    # Sample data for nationality translations
    nationality_data = {
        "yemen": "اليمن",
        "Crown of Aragon": "تاج أرغون",
    }

    # Sample data for job translations
    job_data = {
        "writers": "كتاب",
        "actors": "ممثلون",
        "directors": "مخرجون",
    }

    # Template data with both nationality and job placeholders
    formatted_data = {
        "{en_job} from {en}": "{job_ar} من {ar}",
    }
    country_bot = FormatData(
        formatted_data=formatted_data,
        data_list=nationality_data,
        key_placeholder="{en}",
        value_placeholder="{ar}",
    )

    other_bot = FormatData(
        {},
        job_data,
        key_placeholder="{en_job}",
        value_placeholder="{job_ar}",
    )
    return MultiDataFormatterBase(
        country_bot=country_bot,
        other_bot=other_bot,
    )


@pytest.fixture
def yc_bot2(multi_bot: MultiDataFormatterBase) -> MultiDataFormatterBaseYearV3:

    other_bot = YearFormatData(
        key_placeholder="{year1}",
        value_placeholder="{year1}",
    )
    formatted_data = {
        "{year1} {country1}": "{country1} في {year1}",
    }
    country_bot = V3Formats(
        formatted_data=formatted_data,
        bot=multi_bot,
        key_placeholder="{country1}",
        value_placeholder="{country1}",
    )
    return MultiDataFormatterBaseYearV3(
        country_bot=country_bot,
        other_bot=other_bot,
        other_key_first=True,
    )


class TestPart1:

    test_data_standard = {
        "writers from Crown of Aragon": "كتاب من تاج أرغون",
        "writers from yemen": "كتاب من اليمن",
    }

    @pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
    def test_country_combinations(self, multi_bot: MultiDataFormatterBase, category: str, expected: str) -> None:
        """
        Test
        """
        result = multi_bot.search_all(category)
        assert result == expected


class TestPart2:
    test_data_standard = {
        "14th-century writers from Crown of Aragon": "كتاب من تاج أرغون في القرن 14",
        "14th-century writers from yemen": "كتاب من اليمن في القرن 14",
    }

    @pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
    def test_year_country_combinations(self, yc_bot2: MultiDataFormatterBaseYearV3, category: str, expected: str) -> None:
        """
        Test
        """
        result = yc_bot2.search_all(category)
        assert result == expected
