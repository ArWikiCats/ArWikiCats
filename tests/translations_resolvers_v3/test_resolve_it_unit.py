#!/usr/bin/python3
"""Integration tests for format_films_country_data and """

import pytest
import re

from ArWikiCats.new_resolvers.translations_formats import FormatData, YearFormatData, MultiDataFormatterBase, V3Formats, MultiDataFormatterBaseYearV3
from ArWikiCats.new_resolvers.new_jobs_resolver.mens import mens_resolver_labels
from ArWikiCats.time_resolvers import fixing


class FormatDataXX:
    """
    A dynamic wrapper that allows FormatData to handle year patterns.
    It mimics FormatData behavior but for time values extracted by regex.
    """

    def __init__(self, key_placeholder: str, value_placeholder: str) -> None:
        self.key_placeholder = key_placeholder
        self.value_placeholder = value_placeholder

    def match_key(self, text: str) -> str:
        """Extract English year/decade and return it as the key."""
        return text.replace(" from {en}", "")

    def get_key_label(self, key: str) -> str:
        """Convert the year expression to Arabic."""
        if not key:
            return ""
        result = mens_resolver_labels(key)
        return result

    def normalize_category(self, text: str, key: str) -> str:
        """Replace matched year with placeholder."""
        if not key:
            return text
        return re.sub(re.escape(key), self.key_placeholder, text, flags=re.IGNORECASE)

    def normalize_category_with_key(self, category: str) -> tuple[str, str]:
        """
        Normalize nationality placeholders within a category string.

        Example:
            category:"Yemeni national football teams", result: "natar national football teams"
        """
        key = self.match_key(category)
        result = ""
        if key:
            result = self.normalize_category(category, key)
        return key, result

    def replace_value_placeholder(self, label: str, value: str) -> str:
        # Replace placeholder
        result = label.replace(self.value_placeholder, value)
        result = fixing(result)
        return result

    def search(self, text: str) -> str:
        """place holders"""
        return ""


@pytest.fixture
def multi_bot() -> MultiDataFormatterBase:
    """Create a format_multi_data instance for testing."""

    # Sample data for nationality translations
    nationality_data = {
        "yemen": "اليمن",
        "Crown of Aragon": "تاج أرغون",
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

    other_bot = FormatDataXX(
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
