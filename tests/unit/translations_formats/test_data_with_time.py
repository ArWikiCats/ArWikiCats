#!/usr/bin/python3
"""
Unit tests for data_with_time.py module.

This module provides tests for format_year_country_data and format_year_country_data_v2
factory functions which create MultiDataFormatterBaseYear and MultiDataFormatterBaseYearV2 instances.
"""

import pytest

from ArWikiCats.translations_formats.data_with_time import (
    COUNTRY_PARAM,
    YEAR_PARAM,
    format_year_country_data,
    format_year_country_data_v2,
)
from ArWikiCats.translations_formats.DataModelMulti import (
    MultiDataFormatterBaseYear,
    MultiDataFormatterBaseYearV2,
)


class TestFormatYearCountryData:
    """Tests for format_year_country_data factory function."""

    def test_returns_multi_data_formatter_base_year(self):
        """Test that format_year_country_data returns a MultiDataFormatterBaseYear instance."""
        formatted_data = {"{year1} {country1} events": "{country1} أحداث في {year1}"}
        data_list = {"british": "بريطانية"}

        bot = format_year_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
        )

        assert isinstance(bot, MultiDataFormatterBaseYear)

    def test_default_placeholders(self):
        """Test default placeholders are used correctly."""
        formatted_data = {"{year1} {country1} events": "{country1} أحداث في {year1}"}
        data_list = {"british": "بريطانية"}

        bot = format_year_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
        )

        assert bot.country_bot.key_placeholder == COUNTRY_PARAM
        assert bot.country_bot.value_placeholder == COUNTRY_PARAM
        assert bot.other_bot.key_placeholder == YEAR_PARAM
        assert bot.other_bot.value_placeholder == YEAR_PARAM

    def test_custom_placeholders(self):
        """Test custom placeholders are used correctly."""
        formatted_data = {"{time} {nat} writers": "{nat_ar} كتاب في {time_ar}"}
        data_list = {"yemen": "يمنية"}

        bot = format_year_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{nat}",
            value_placeholder="{nat_ar}",
            key2_placeholder="{time}",
            value2_placeholder="{time_ar}",
        )

        assert bot.country_bot.key_placeholder == "{nat}"
        assert bot.country_bot.value_placeholder == "{nat_ar}"
        assert bot.other_bot.key_placeholder == "{time}"
        assert bot.other_bot.value_placeholder == "{time_ar}"

    def test_text_before_and_after(self):
        """Test text_before and text_after are passed to country_bot."""
        formatted_data = {"{year1} {country1} events": "{country1} أحداث في {year1}"}
        data_list = {"british": "بريطانية"}

        bot = format_year_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
            text_before="the ",
            text_after=" !",
        )

        assert bot.country_bot.text_before == "the "
        assert bot.country_bot.text_after == " !"

    def test_data_to_find(self):
        """Test data_to_find is stored correctly."""
        formatted_data = {"{year1} {country1} events": "{country1} أحداث في {year1}"}
        data_list = {"british": "بريطانية"}
        data_to_find = {"direct lookup": "نتيجة مباشرة"}

        bot = format_year_country_data(
            formatted_data=formatted_data,
            data_list=data_list,
            data_to_find=data_to_find,
        )

        assert bot.data_to_find == data_to_find


class TestFormatYearCountryDataV2:
    """Tests for format_year_country_data_v2 factory function."""

    def test_returns_multi_data_formatter_base_year_v2(self):
        """Test that format_year_country_data_v2 returns a MultiDataFormatterBaseYearV2 instance."""
        formatted_data = {"{year1} {country1} writers": "{demonym} كتاب في {year1}"}
        data_list = {"yemen": {"demonym": "يمنيون"}}

        bot = format_year_country_data_v2(
            formatted_data=formatted_data,
            data_list=data_list,
        )

        assert isinstance(bot, MultiDataFormatterBaseYearV2)

    def test_default_placeholders(self):
        """Test default placeholders are used correctly."""
        formatted_data = {"{year1} {country1} writers": "{demonym} كتاب في {year1}"}
        data_list = {"yemen": {"demonym": "يمنيون"}}

        bot = format_year_country_data_v2(
            formatted_data=formatted_data,
            data_list=data_list,
        )

        assert bot.country_bot.key_placeholder == COUNTRY_PARAM
        assert bot.other_bot.key_placeholder == YEAR_PARAM
        assert bot.other_bot.value_placeholder == YEAR_PARAM

    def test_custom_placeholders(self):
        """Test custom placeholders are used correctly."""
        formatted_data = {"{time} {nat} writers": "{demonym} كتاب في {time_ar}"}
        data_list = {"yemen": {"demonym": "يمنيون"}}

        bot = format_year_country_data_v2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{nat}",
            key2_placeholder="{time}",
            value2_placeholder="{time_ar}",
        )

        assert bot.country_bot.key_placeholder == "{nat}"
        assert bot.other_bot.key_placeholder == "{time}"
        assert bot.other_bot.value_placeholder == "{time_ar}"

    def test_text_before_and_after(self):
        """Test text_before and text_after are passed to country_bot."""
        formatted_data = {"{year1} {country1} writers": "{demonym} كتاب في {year1}"}
        data_list = {"yemen": {"demonym": "يمنيون"}}

        bot = format_year_country_data_v2(
            formatted_data=formatted_data,
            data_list=data_list,
            text_before="the ",
            text_after=" !",
        )

        assert bot.country_bot.text_before == "the "
        assert bot.country_bot.text_after == " !"

    def test_data_to_find(self):
        """Test data_to_find is stored correctly."""
        formatted_data = {"{year1} {country1} writers": "{demonym} كتاب في {year1}"}
        data_list = {"yemen": {"demonym": "يمنيون"}}
        data_to_find = {"direct lookup": "نتيجة مباشرة"}

        bot = format_year_country_data_v2(
            formatted_data=formatted_data,
            data_list=data_list,
            data_to_find=data_to_find,
        )

        assert bot.data_to_find == data_to_find


class TestConstants:
    """Tests for module constants."""

    def test_year_param(self):
        """Test YEAR_PARAM constant."""
        assert YEAR_PARAM == "{year1}"

    def test_country_param(self):
        """Test COUNTRY_PARAM constant."""
        assert COUNTRY_PARAM == "{country1}"
