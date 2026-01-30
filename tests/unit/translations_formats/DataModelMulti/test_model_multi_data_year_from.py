#!/usr/bin/python3
"""
Unit tests for model_multi_data_year_from.py module.

This module provides tests for MultiDataFormatterYearAndFrom class
which combines year-based and "from" relation category translations.
"""

from ArWikiCats.translations_formats.DataModel import FormatDataFrom
from ArWikiCats.translations_formats.DataModelMulti import MultiDataFormatterBaseHelpers
from ArWikiCats.translations_formats.DataModelMulti.model_multi_data_year_from import (
    MultiDataFormatterYearAndFrom,
)


class TestMultiDataFormatterYearAndFrom:
    """Tests for MultiDataFormatterYearAndFrom class."""

    def test_init_basic(self):
        """Test basic initialization of MultiDataFormatterYearAndFrom."""
        country_bot = FormatDataFrom(
            formatted_data={"{year1} {country1}": "{country1} في {year1}"},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "اليمن" if "yemen" in x.lower() else "",
            match_key_callback=lambda x: "yemen" if "yemen" in x.lower() else "",
        )
        year_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=lambda x: "2020" if "2020" in x else "",
            match_key_callback=lambda x: "2020" if "2020" in x else "",
        )

        bot = MultiDataFormatterYearAndFrom(country_bot, year_bot)

        assert bot.country_bot is country_bot
        assert bot.other_bot is year_bot
        assert bot.search_first_part is False
        assert bot.data_to_find is None
        assert bot.other_key_first is False

    def test_init_with_search_first_part(self):
        """Test initialization with search_first_part=True."""
        country_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        year_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        bot = MultiDataFormatterYearAndFrom(country_bot, year_bot, search_first_part=True)

        assert bot.search_first_part is True

    def test_init_with_data_to_find(self):
        """Test initialization with data_to_find."""
        country_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        year_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        data_to_find = {"direct lookup": "نتيجة مباشرة"}

        bot = MultiDataFormatterYearAndFrom(country_bot, year_bot, data_to_find=data_to_find)

        assert bot.data_to_find == data_to_find

    def test_init_with_other_key_first(self):
        """Test initialization with other_key_first=True."""
        country_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        year_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        bot = MultiDataFormatterYearAndFrom(country_bot, year_bot, other_key_first=True)

        assert bot.other_key_first is True

    def test_inherits_from_base_helpers(self):
        """Test that MultiDataFormatterYearAndFrom inherits from MultiDataFormatterBaseHelpers."""
        country_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )
        year_bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=lambda x: "",
            match_key_callback=lambda x: "",
        )

        bot = MultiDataFormatterYearAndFrom(country_bot, year_bot)

        assert isinstance(bot, MultiDataFormatterBaseHelpers)
