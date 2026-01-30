#!/usr/bin/python3
"""
Unit tests for data_new_model.py module.

This module provides tests for format_films_country_data factory function
which creates MultiDataFormatterDataDouble instances for film category translations.
"""

from ArWikiCats.translations_formats.data_new_model import (
    format_films_country_data,
)
from ArWikiCats.translations_formats.DataModel import FormatData
from ArWikiCats.translations_formats.DataModelDouble import FormatDataDouble, MultiDataFormatterDataDouble


class TestFormatFilmsCountryData:
    """Tests for format_films_country_data factory function."""

    def test_returns_multi_data_formatter_data_double(self):
        """Test that format_films_country_data returns a MultiDataFormatterDataDouble instance."""
        formatted_data = {"{nat_en} films": "أفلام {nat_ar}"}
        data_list = {"british": "بريطانية"}

        bot = format_films_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
        )

        assert isinstance(bot, MultiDataFormatterDataDouble)

    def test_default_placeholders(self):
        """Test default placeholders are used correctly."""
        formatted_data = {"{nat_en} films": "أفلام {nat_ar}"}
        data_list = {"british": "بريطانية"}

        bot = format_films_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
        )

        assert bot.country_bot.key_placeholder == "{nat_en}"
        assert bot.country_bot.value_placeholder == "{nat_ar}"
        assert bot.other_bot.key_placeholder == "{film_key}"
        assert bot.other_bot.value_placeholder == "{film_ar}"

    def test_custom_placeholders(self):
        """Test custom placeholders are used correctly."""
        formatted_data = {"{country} films": "أفلام {country_label}"}
        data_list = {"british": "بريطانية"}

        bot = format_films_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
            value_placeholder="{country_label}",
            key2_placeholder="{genre}",
            value2_placeholder="{genre_label}",
        )

        assert bot.country_bot.key_placeholder == "{country}"
        assert bot.country_bot.value_placeholder == "{country_label}"
        assert bot.other_bot.key_placeholder == "{genre}"
        assert bot.other_bot.value_placeholder == "{genre_label}"

    def test_data_list2_passed_to_other_bot(self):
        """Test data_list2 is used for the other_bot (genre bot)."""
        formatted_data = {"{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}"}
        data_list = {"british": "بريطانية"}
        data_list2 = {"action": "أكشن", "drama": "دراما"}

        bot = format_films_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
            data_list2=data_list2,
        )

        # Check that data_list2 is passed to other_bot
        assert "action" in bot.other_bot.data_list_ci
        assert "drama" in bot.other_bot.data_list_ci

    def test_other_formatted_data_passed_to_other_bot(self):
        """Test other_formatted_data is used for the other_bot."""
        formatted_data = {"{nat_en} films": "أفلام {nat_ar}"}
        data_list = {"british": "بريطانية"}
        data_list2 = {"action": "أكشن"}
        other_formatted_data = {"{film_key} films": "أفلام {film_ar}"}

        bot = format_films_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
            data_list2=data_list2,
            other_formatted_data=other_formatted_data,
        )

        # Check that other_formatted_data is passed to other_bot
        assert "{film_key} films" in bot.other_bot.formatted_data

    def test_text_before_and_after(self):
        """Test text_before and text_after are passed to country_bot."""
        formatted_data = {"{nat_en} films": "أفلام {nat_ar}"}
        data_list = {"british": "بريطانية"}

        bot = format_films_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
            text_before="the ",
            text_after=" !",
        )

        assert bot.country_bot.text_before == "the "
        assert bot.country_bot.text_after == " !"

    def test_data_to_find(self):
        """Test data_to_find is stored correctly."""
        formatted_data = {"{nat_en} films": "أفلام {nat_ar}"}
        data_list = {"british": "بريطانية"}
        data_to_find = {"direct lookup": "نتيجة مباشرة"}

        bot = format_films_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
            data_to_find=data_to_find,
        )

        assert bot.data_to_find == data_to_find

    def test_country_bot_is_format_data(self):
        """Test that country_bot is a FormatData instance."""
        formatted_data = {"{nat_en} films": "أفلام {nat_ar}"}
        data_list = {"british": "بريطانية"}

        bot = format_films_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
        )

        assert isinstance(bot.country_bot, FormatData)

    def test_other_bot_is_format_data_double(self):
        """Test that other_bot is a FormatDataDouble instance."""
        formatted_data = {"{nat_en} films": "أفلام {nat_ar}"}
        data_list = {"british": "بريطانية"}
        data_list2 = {"action": "أكشن"}

        bot = format_films_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
            data_list2=data_list2,
        )

        assert isinstance(bot.other_bot, FormatDataDouble)
