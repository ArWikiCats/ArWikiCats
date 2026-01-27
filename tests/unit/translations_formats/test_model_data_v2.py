#!/usr/bin/python3
"""
Tests for model_data_v2.py module.

This module provides tests for:
1. FormatDataV2 class - dictionary-based template-driven translations
2. MultiDataFormatterBaseV2 class - combines two FormatDataV2 instances
"""

import pytest

from ArWikiCats.translations_formats.DataModel.model_data_v2 import (
    FormatDataV2,
    MultiDataFormatterBaseV2,
)


class TestFormatDataV2Init:
    """Tests for FormatDataV2 initialization."""

    def test_init_with_dict_data_list(self):
        """Test initialization with dictionary data_list."""
        formatted_data = {"{country} writers": "{demonym} كتاب"}
        data_list = {
            "yemeni": {"demonym": "يمنيون", "country_ar": "اليمن"},
            "egyptian": {"demonym": "مصريون", "country_ar": "مصر"},
        }
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )
        assert bot.formatted_data == formatted_data
        assert bot.data_list == data_list
        assert bot.key_placeholder == "{country}"

    def test_init_with_mixed_data_list(self):
        """Test initialization with mixed string and dict data_list."""
        formatted_data = {"{country} writers": "{demonym} كتاب"}
        data_list = {
            "yemeni": {"demonym": "يمنيون"},
            "saudi": "سعوديون",
        }
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )
        assert bot.data_list == data_list

    def test_init_with_text_after(self):
        """Test initialization with text_after parameter."""
        formatted_data = {"{country} writers": "{demonym} كتاب"}
        data_list = {"yemeni": {"demonym": "يمنيون"}}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
            text_after="people",
        )
        assert bot.text_after == "people"

    def test_init_with_text_before(self):
        """Test initialization with text_before parameter."""
        formatted_data = {"{country} writers": "{demonym} كتاب"}
        data_list = {"yemeni": {"demonym": "يمنيون"}}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
            text_before="the ",
        )
        assert bot.text_before == "the "

    def test_init_with_regex_filter(self):
        """Test initialization with custom regex_filter."""
        formatted_data = {"{country} writers": "{demonym} كتاب"}
        data_list = {"yemeni": {"demonym": "يمنيون"}}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
            regex_filter=r"[\w-]",
        )
        assert bot.regex_filter == r"[\w-]"


class TestFormatDataV2ApplyPatternReplacement:
    """Tests for FormatDataV2.apply_pattern_replacement method."""

    def test_apply_pattern_replacement_dict(self):
        """Test apply_pattern_replacement with dict value."""
        formatted_data = {"{country} writers": "{demonym} كتاب"}
        data_list = {"yemeni": {"demonym": "يمنيون", "country_ar": "اليمن"}}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

        template_label = "{demonym} كتاب"
        sport_label = {"demonym": "يمنيون", "country_ar": "اليمن"}
        result = bot.apply_pattern_replacement(template_label, sport_label)
        assert result == "يمنيون كتاب"

    def test_apply_pattern_replacement_multiple_placeholders(self):
        """Test apply_pattern_replacement with multiple placeholders."""
        formatted_data = {"{country} writers in {country}": "{demonym} كتاب في {country_ar}"}
        data_list = {"yemeni": {"demonym": "يمنيون", "country_ar": "اليمن"}}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

        template_label = "{demonym} كتاب في {country_ar}"
        sport_label = {"demonym": "يمنيون", "country_ar": "اليمن"}
        result = bot.apply_pattern_replacement(template_label, sport_label)
        assert result == "يمنيون كتاب في اليمن"

    def test_apply_pattern_replacement_string_value(self):
        """Test apply_pattern_replacement with string value returns template unchanged."""
        formatted_data = {"{country} writers": "كتاب"}
        data_list = {"yemeni": "يمنيون"}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

        template_label = "كتاب"
        sport_label = "يمنيون"
        result = bot.apply_pattern_replacement(template_label, sport_label)
        assert result == template_label

    def test_apply_pattern_replacement_empty_dict(self):
        """Test apply_pattern_replacement with empty dict."""
        formatted_data = {"{country} writers": "كتاب"}
        data_list = {"yemeni": {}}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

        template_label = "كتاب"
        sport_label = {}
        result = bot.apply_pattern_replacement(template_label, sport_label)
        assert result == template_label

    def test_apply_pattern_replacement_partial_replacement(self):
        """Test apply_pattern_replacement when not all placeholders are replaced."""
        formatted_data = {"{country} writers": "{demonym} كتاب {country_ar}"}
        data_list = {"yemeni": {"demonym": "يمنيون"}}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

        template_label = "{demonym} كتاب {country_ar}"
        sport_label = {"demonym": "يمنيون"}
        result = bot.apply_pattern_replacement(template_label, sport_label)
        # Should replace only available placeholder, leave {country_ar} as is
        assert result == "يمنيون كتاب {country_ar}"

    def test_apply_pattern_replacement_trims_whitespace(self):
        """Test apply_pattern_replacement trims leading/trailing whitespace."""
        formatted_data = {"{country} writers": "  {demonym} كتاب  "}
        data_list = {"yemeni": {"demonym": "يمنيون"}}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

        template_label = "  {demonym} كتاب  "
        sport_label = {"demonym": "يمنيون"}
        result = bot.apply_pattern_replacement(template_label, sport_label)
        assert result == "يمنيون كتاب"


class TestFormatDataV2ReplaceValuePlaceholder:
    """Tests for FormatDataV2.replace_value_placeholder method."""

    def test_replace_value_placeholder_dict(self):
        """Test replace_value_placeholder with dict value."""
        formatted_data = {"{country} writers": "{demonym} كتاب"}
        data_list = {"yemeni": {"demonym": "يمنيون"}}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

        label = "{demonym} كتاب"
        value = {"demonym": "يمنيون"}
        result = bot.replace_value_placeholder(label, value)
        assert result == "يمنيون كتاب"

    def test_replace_value_placeholder_multiple_keys(self):
        """Test replace_value_placeholder with multiple placeholder keys."""
        formatted_data = {"{country} writers": "{demonym} من {country_ar}"}
        data_list = {"yemeni": {"demonym": "يمنيون", "country_ar": "اليمن"}}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

        label = "{demonym} من {country_ar}"
        value = {"demonym": "يمنيون", "country_ar": "اليمن"}
        result = bot.replace_value_placeholder(label, value)
        assert result == "يمنيون من اليمن"

    def test_replace_value_placeholder_string_value(self):
        """Test replace_value_placeholder with string value returns label unchanged."""
        formatted_data = {"{country} writers": "كتاب"}
        data_list = {"yemeni": "يمنيون"}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

        label = "كتاب"
        value = "يمنيون"
        result = bot.replace_value_placeholder(label, value)
        assert result == label

    def test_replace_value_placeholder_empty_dict(self):
        """Test replace_value_placeholder with empty dict."""
        formatted_data = {"{country} writers": "كتاب"}
        data_list = {"yemeni": {}}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

        label = "كتاب"
        value = {}
        result = bot.replace_value_placeholder(label, value)
        assert result == label


class TestFormatDataV2Search:
    """Tests for FormatDataV2.search method (inherited from FormatDataBase)."""

    def test_search_dict_data_list(self):
        """Test search with dictionary data_list."""
        formatted_data = {"{country} writers": "{demonym} كتاب"}
        data_list = {
            "yemeni": {"demonym": "يمنيون"},
            "egyptian": {"demonym": "مصريون"},
        }
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

        result = bot.search("yemeni writers")
        assert result == "يمنيون كتاب"

    def test_search_no_match(self):
        """Test search with no matching pattern."""
        formatted_data = {"{country} writers": "{demonym} كتاب"}
        data_list = {"yemeni": {"demonym": "يمنيون"}}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

        result = bot.search("no match here")
        assert result == ""

    def test_search_case_insensitive(self):
        """Test search is case-insensitive."""
        formatted_data = {"{country} writers": "{demonym} كتاب"}
        data_list = {"Yemeni": {"demonym": "يمنيون"}}
        bot = FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

        result = bot.search("yemeni writers")
        assert result == "يمنيون كتاب"


class TestMultiDataFormatterBaseV2Init:
    """Tests for MultiDataFormatterBaseV2 initialization."""

    def test_init_default(self):
        """Test initialization with default parameters."""
        country_bot = FormatDataV2(
            formatted_data={"{country}": "{demonym}"},
            data_list={"yemeni": {"demonym": "يمنيون"}},
            key_placeholder="{country}",
        )
        other_bot = FormatDataV2(
            formatted_data={"{job}": "{job_ar}"},
            data_list={"writers": {"job_ar": "كتاب"}},
            key_placeholder="{job}",
        )

        bot = MultiDataFormatterBaseV2(country_bot=country_bot, other_bot=other_bot)

        assert bot.country_bot is country_bot
        assert bot.other_bot is other_bot
        assert bot.search_first_part is False
        assert bot.data_to_find is None

    def test_init_with_search_first_part(self):
        """Test initialization with search_first_part=True."""
        country_bot = FormatDataV2(
            formatted_data={"{country}": "{demonym}"},
            data_list={"yemeni": {"demonym": "يمنيون"}},
            key_placeholder="{country}",
        )
        other_bot = FormatDataV2(
            formatted_data={"{job}": "{job_ar}"},
            data_list={"writers": {"job_ar": "كتاب"}},
            key_placeholder="{job}",
        )

        bot = MultiDataFormatterBaseV2(
            country_bot=country_bot,
            other_bot=other_bot,
            search_first_part=True,
        )

        assert bot.search_first_part is True

    def test_init_with_data_to_find(self):
        """Test initialization with data_to_find dictionary."""
        country_bot = FormatDataV2(
            formatted_data={"{country}": "{demonym}"},
            data_list={"yemeni": {"demonym": "يمنيون"}},
            key_placeholder="{country}",
        )
        other_bot = FormatDataV2(
            formatted_data={"{job}": "{job_ar}"},
            data_list={"writers": {"job_ar": "كتاب"}},
            key_placeholder="{job}",
        )

        data_to_find = {"yemeni writers": "كتاب يمنيون"}
        bot = MultiDataFormatterBaseV2(
            country_bot=country_bot,
            other_bot=other_bot,
            data_to_find=data_to_find,
        )

        assert bot.data_to_find == data_to_find
