#!/usr/bin/python3
"""
Unit tests for model_multi_data_double.py module.

This module provides tests for MultiDataFormatterDataDouble class
which combines FormatData with FormatDataDouble for double-key category translations.
"""

from ArWikiCats.translations_formats.DataModel import FormatData
from ArWikiCats.translations_formats.DataModelDouble import FormatDataDouble
from ArWikiCats.translations_formats.DataModelDouble.model_multi_data_double import (
    MultiDataFormatterDataDouble,
)
from ArWikiCats.translations_formats.DataModelMulti import MultiDataFormatterBaseHelpers


class TestMultiDataFormatterDataDouble:
    """Tests for MultiDataFormatterDataDouble class."""

    def test_init_basic(self):
        """Test basic initialization of MultiDataFormatterDataDouble."""
        country_bot = FormatData(
            formatted_data={"{nat_en} films": "أفلام {nat_ar}"},
            data_list={"british": "بريطانية"},
            key_placeholder="{nat_en}",
            value_placeholder="{nat_ar}",
        )
        genre_bot = FormatDataDouble(
            formatted_data={"{film_key} films": "أفلام {film_ar}"},
            data_list={"action": "أكشن"},
            key_placeholder="{film_key}",
            value_placeholder="{film_ar}",
        )

        bot = MultiDataFormatterDataDouble(country_bot, genre_bot)

        assert bot.country_bot is country_bot
        assert bot.other_bot is genre_bot
        assert bot.search_first_part is False
        assert bot.data_to_find is None

    def test_init_with_search_first_part(self):
        """Test initialization with search_first_part=True."""
        country_bot = FormatData(
            formatted_data={},
            data_list={"british": "بريطانية"},
            key_placeholder="{nat_en}",
            value_placeholder="{nat_ar}",
        )
        genre_bot = FormatDataDouble(
            formatted_data={},
            data_list={"action": "أكشن"},
            key_placeholder="{film_key}",
            value_placeholder="{film_ar}",
        )

        bot = MultiDataFormatterDataDouble(country_bot, genre_bot, search_first_part=True)

        assert bot.search_first_part is True

    def test_init_with_data_to_find(self):
        """Test initialization with data_to_find."""
        country_bot = FormatData(
            formatted_data={},
            data_list={"british": "بريطانية"},
            key_placeholder="{nat_en}",
            value_placeholder="{nat_ar}",
        )
        genre_bot = FormatDataDouble(
            formatted_data={},
            data_list={"action": "أكشن"},
            key_placeholder="{film_key}",
            value_placeholder="{film_ar}",
        )
        data_to_find = {"direct lookup": "نتيجة مباشرة"}

        bot = MultiDataFormatterDataDouble(country_bot, genre_bot, data_to_find=data_to_find)

        assert bot.data_to_find == data_to_find

    def test_inherits_from_base_helpers(self):
        """Test that MultiDataFormatterDataDouble inherits from MultiDataFormatterBaseHelpers."""
        country_bot = FormatData(
            formatted_data={},
            data_list={},
            key_placeholder="{nat_en}",
            value_placeholder="{nat_ar}",
        )
        genre_bot = FormatDataDouble(
            formatted_data={},
            data_list={},
            key_placeholder="{film_key}",
            value_placeholder="{film_ar}",
        )

        bot = MultiDataFormatterDataDouble(country_bot, genre_bot)

        assert isinstance(bot, MultiDataFormatterBaseHelpers)

    def test_country_bot_is_format_data(self):
        """Test that country_bot is a FormatData instance."""
        country_bot = FormatData(
            formatted_data={},
            data_list={"british": "بريطانية"},
            key_placeholder="{nat_en}",
            value_placeholder="{nat_ar}",
        )
        genre_bot = FormatDataDouble(
            formatted_data={},
            data_list={"action": "أكشن"},
            key_placeholder="{film_key}",
            value_placeholder="{film_ar}",
        )

        bot = MultiDataFormatterDataDouble(country_bot, genre_bot)

        assert isinstance(bot.country_bot, FormatData)

    def test_other_bot_is_format_data_double(self):
        """Test that other_bot is a FormatDataDouble instance."""
        country_bot = FormatData(
            formatted_data={},
            data_list={"british": "بريطانية"},
            key_placeholder="{nat_en}",
            value_placeholder="{nat_ar}",
        )
        genre_bot = FormatDataDouble(
            formatted_data={},
            data_list={"action": "أكشن"},
            key_placeholder="{film_key}",
            value_placeholder="{film_ar}",
        )

        bot = MultiDataFormatterDataDouble(country_bot, genre_bot)

        assert isinstance(bot.other_bot, FormatDataDouble)
