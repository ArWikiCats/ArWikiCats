#!/usr/bin/python3
"""
Unit tests for model_multi_data.py module.

This module provides tests for MultiDataFormatterBase, MultiDataFormatterBaseYear,
and MultiDataFormatterBaseYearV2 classes which combine two formatter instances
for dual-element category translations.
"""

import pytest

from ArWikiCats.translations_formats.DataModel import FormatData, FormatDataV2, YearFormatData
from ArWikiCats.translations_formats.DataModelMulti import MultiDataFormatterBaseHelpers
from ArWikiCats.translations_formats.DataModelMulti.model_multi_data import (
    MultiDataFormatterBase,
    MultiDataFormatterBaseYear,
    MultiDataFormatterBaseYearV2,
)


class TestMultiDataFormatterBase:
    """Tests for MultiDataFormatterBase class."""

    def test_init_basic(self):
        """Test basic initialization of MultiDataFormatterBase."""
        country_bot = FormatData(
            formatted_data={"{nat} players": "لاعبون {nat_ar}"},
            data_list={"british": "بريطانيون"},
            key_placeholder="{nat}",
            value_placeholder="{nat_ar}",
        )
        sport_bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_ar}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_ar}",
        )

        bot = MultiDataFormatterBase(country_bot, sport_bot)

        assert bot.country_bot is country_bot
        assert bot.other_bot is sport_bot
        assert bot.search_first_part is False
        assert bot.data_to_find is None

    def test_init_with_search_first_part(self):
        """Test initialization with search_first_part=True."""
        country_bot = FormatData(
            formatted_data={},
            data_list={"british": "بريطانيون"},
            key_placeholder="{nat}",
            value_placeholder="{nat_ar}",
        )
        sport_bot = FormatData(
            formatted_data={},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_ar}",
        )

        bot = MultiDataFormatterBase(country_bot, sport_bot, search_first_part=True)

        assert bot.search_first_part is True

    def test_init_with_data_to_find(self):
        """Test initialization with data_to_find."""
        country_bot = FormatData(
            formatted_data={},
            data_list={"british": "بريطانيون"},
            key_placeholder="{nat}",
            value_placeholder="{nat_ar}",
        )
        sport_bot = FormatData(
            formatted_data={},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_ar}",
        )
        data_to_find = {"direct lookup": "نتيجة مباشرة"}

        bot = MultiDataFormatterBase(country_bot, sport_bot, data_to_find=data_to_find)

        assert bot.data_to_find == data_to_find

    def test_inherits_from_base_helpers(self):
        """Test that MultiDataFormatterBase inherits from MultiDataFormatterBaseHelpers."""
        country_bot = FormatData(
            formatted_data={},
            data_list={},
            key_placeholder="{nat}",
            value_placeholder="{nat_ar}",
        )
        sport_bot = FormatData(
            formatted_data={},
            data_list={},
            key_placeholder="{sport}",
            value_placeholder="{sport_ar}",
        )

        bot = MultiDataFormatterBase(country_bot, sport_bot)

        assert isinstance(bot, MultiDataFormatterBaseHelpers)


class TestMultiDataFormatterBaseYear:
    """Tests for MultiDataFormatterBaseYear class."""

    def test_init_basic(self):
        """Test basic initialization of MultiDataFormatterBaseYear."""
        country_bot = FormatData(
            formatted_data={"{year1} {nat} events": "{nat_ar} أحداث في {year1}"},
            data_list={"british": "بريطانية"},
            key_placeholder="{nat}",
            value_placeholder="{nat_ar}",
        )
        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )

        bot = MultiDataFormatterBaseYear(country_bot, year_bot)

        assert bot.country_bot is country_bot
        assert bot.other_bot is year_bot
        assert bot.search_first_part is False
        assert bot.data_to_find is None

    def test_init_with_search_first_part(self):
        """Test initialization with search_first_part=True."""
        country_bot = FormatData(
            formatted_data={},
            data_list={"british": "بريطانية"},
            key_placeholder="{nat}",
            value_placeholder="{nat_ar}",
        )
        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )

        bot = MultiDataFormatterBaseYear(country_bot, year_bot, search_first_part=True)

        assert bot.search_first_part is True

    def test_init_with_data_to_find(self):
        """Test initialization with data_to_find."""
        country_bot = FormatData(
            formatted_data={},
            data_list={"british": "بريطانية"},
            key_placeholder="{nat}",
            value_placeholder="{nat_ar}",
        )
        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        data_to_find = {"direct lookup": "نتيجة مباشرة"}

        bot = MultiDataFormatterBaseYear(country_bot, year_bot, data_to_find=data_to_find)

        assert bot.data_to_find == data_to_find

    def test_inherits_from_base_helpers(self):
        """Test that MultiDataFormatterBaseYear inherits from MultiDataFormatterBaseHelpers."""
        country_bot = FormatData(
            formatted_data={},
            data_list={},
            key_placeholder="{nat}",
            value_placeholder="{nat_ar}",
        )
        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )

        bot = MultiDataFormatterBaseYear(country_bot, year_bot)

        assert isinstance(bot, MultiDataFormatterBaseHelpers)


class TestMultiDataFormatterBaseYearV2:
    """Tests for MultiDataFormatterBaseYearV2 class."""

    def test_init_basic(self):
        """Test basic initialization of MultiDataFormatterBaseYearV2."""
        country_bot = FormatDataV2(
            formatted_data={"{year1} {nat} writers": "{demonym} كتاب في {year1}"},
            data_list={"yemen": {"demonym": "يمنيون"}},
            key_placeholder="{nat}",
        )
        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )

        bot = MultiDataFormatterBaseYearV2(country_bot, year_bot)

        assert bot.country_bot is country_bot
        assert bot.other_bot is year_bot
        assert bot.search_first_part is False
        assert bot.data_to_find is None
        assert bot.other_key_first is False

    def test_init_with_other_key_first(self):
        """Test initialization with other_key_first=True."""
        country_bot = FormatDataV2(
            formatted_data={},
            data_list={"yemen": {"demonym": "يمنيون"}},
            key_placeholder="{nat}",
        )
        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )

        bot = MultiDataFormatterBaseYearV2(country_bot, year_bot, other_key_first=True)

        assert bot.other_key_first is True

    def test_init_with_search_first_part(self):
        """Test initialization with search_first_part=True."""
        country_bot = FormatDataV2(
            formatted_data={},
            data_list={"yemen": {"demonym": "يمنيون"}},
            key_placeholder="{nat}",
        )
        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )

        bot = MultiDataFormatterBaseYearV2(country_bot, year_bot, search_first_part=True)

        assert bot.search_first_part is True

    def test_init_with_data_to_find(self):
        """Test initialization with data_to_find."""
        country_bot = FormatDataV2(
            formatted_data={},
            data_list={"yemen": {"demonym": "يمنيون"}},
            key_placeholder="{nat}",
        )
        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        data_to_find = {"direct lookup": "نتيجة مباشرة"}

        bot = MultiDataFormatterBaseYearV2(country_bot, year_bot, data_to_find=data_to_find)

        assert bot.data_to_find == data_to_find

    def test_inherits_from_base_helpers(self):
        """Test that MultiDataFormatterBaseYearV2 inherits from MultiDataFormatterBaseHelpers."""
        country_bot = FormatDataV2(
            formatted_data={},
            data_list={},
            key_placeholder="{nat}",
        )
        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )

        bot = MultiDataFormatterBaseYearV2(country_bot, year_bot)

        assert isinstance(bot, MultiDataFormatterBaseHelpers)
