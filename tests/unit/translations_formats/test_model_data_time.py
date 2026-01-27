#!/usr/bin/python3
"""
Tests for model_data_time.py module.

This module provides tests for:
1. YearFormatData class - deprecated legacy class for year pattern handling
2. YearFormatData factory function - preferred way to create year formatters
"""

import pytest

from ArWikiCats.translations_formats.DataModel.model_data_time import (
    YearFormatData,
    # YearFormatData,
)


class TestYearFormatDataLegacyInit:
    """Tests for YearFormatData initialization."""

    def test_init_default_placeholders(self):
        """Test initialization with custom placeholders."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        assert bot.key_placeholder == "{year1}"
        assert bot.value_placeholder == "{year1}"

    def test_init_custom_placeholders(self):
        """Test initialization with different key and value placeholders."""
        bot = YearFormatData(
            key_placeholder="{time_key}",
            value_placeholder="{time_value}",
        )
        assert bot.key_placeholder == "{time_key}"
        assert bot.value_placeholder == "{time_value}"


class TestYearFormatDataLegacyMatchKey:
    """Tests for YearFormatData.match_key method."""

    def test_match_key_century(self):
        """Test matching century pattern."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.match_key("14th-century writers")
        assert result == "14th-century"

    def test_match_key_decade(self):
        """Test matching decade pattern."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.match_key("1990s films")
        assert result == "1990s"

    def test_match_key_year(self):
        """Test matching year pattern."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.match_key("2020 events")
        assert result == "2020"

    def test_match_key_no_match(self):
        """Test match_key returns empty string when no match."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.match_key("no time pattern here")
        assert result == ""

    def test_match_key_millennium(self):
        """Test matching millennium pattern."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.match_key("3rd millennium BC")
        assert result == "3rd millennium BC"

    def test_match_key_bc(self):
        """Test matching BC patterns."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.match_key("500 BC kings")
        assert result == "500 BC"


class TestYearFormatDataLegacyNormalizeCategory:
    """Tests for YearFormatData.normalize_category method."""

    def test_normalize_category_with_key(self):
        """Test normalize_category replaces matched year with placeholder."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.normalize_category("14th-century writers", "14th-century")
        assert result == "{year1} writers"

    def test_normalize_category_case_insensitive(self):
        """Test normalize_category is case-insensitive."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.normalize_category("14th-Century Writers", "14th-century")
        assert result == "{year1} Writers"

    def test_normalize_category_empty_key(self):
        """Test normalize_category returns original text when key is empty."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.normalize_category("14th-century writers", "")
        assert result == "14th-century writers"

    def test_normalize_category_multiple_occurrences(self):
        """Test normalize_category only replaces first occurrence."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.normalize_category("14th-century 14th-century", "14th-century")
        # Should replace first occurrence only (re.sub default behavior with count=1?)
        # Actually looking at the code, it uses re.sub without count parameter, so all occurrences
        assert result == "{year1} {year1}"

    def test_normalize_category_decade(self):
        """Test normalize_category with decade pattern."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.normalize_category("1990s films", "1990s")
        assert result == "{year1} films"


class TestYearFormatDataLegacyNormalizeCategoryWithKey:
    """Tests for YearFormatData.normalize_category_with_key method."""

    def test_normalize_category_with_key_both(self):
        """Test normalize_category_with_key returns key and normalized category."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        key, result = bot.normalize_category_with_key("14th-century writers")
        assert key == "14th-century"
        assert result == "{year1} writers"

    def test_normalize_category_with_key_no_match(self):
        """Test normalize_category_with_key when no key matches."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        key, result = bot.normalize_category_with_key("no time pattern")
        assert key == ""
        assert result == ""

    def test_normalize_category_with_key_decade(self):
        """Test normalize_category_with_key with decade pattern."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        key, result = bot.normalize_category_with_key("1990s films")
        assert key == "1990s"
        assert result == "{year1} films"


class TestYearFormatDataLegacyReplaceValuePlaceholder:
    """Tests for YearFormatData.replace_value_placeholder method."""

    def test_replace_value_placeholder_basic(self):
        """Test replace_value_placeholder replaces placeholder with value."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.replace_value_placeholder("القرن {year1}", "14")
        assert result == "القرن 14"

    def test_replace_value_placeholder_standardize_time(self):
        """Test replace_value_placeholder standardizes time phrases."""
        from ArWikiCats.time_formats.utils_time import standardize_time_phrases

        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        # This should call standardize_time_phrases
        result = bot.replace_value_placeholder("تأسيسات سنة القرن {year1}", "14")
        # standardize_time_phrases converts "تأسيسات سنة القرن" -> "تأسيسات القرن"
        expected = standardize_time_phrases("تأسيسات سنة القرن 14")
        assert result == expected

    def test_replace_value_placeholder_no_placeholder(self):
        """Test replace_value_placeholder when placeholder not in label."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.replace_value_placeholder("القرن 14", "14")
        assert result == "القرن 14"


class TestYearFormatDataLegacyGetKeyLabel:
    """Tests for YearFormatData.get_key_label method."""

    def test_get_key_label_with_key(self):
        """Test get_key_label returns Arabic conversion for the key."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.get_key_label("14th-century")
        assert result == "القرن 14"

    def test_get_key_label_empty_key(self):
        """Test get_key_label returns empty string when key is empty."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.get_key_label("")
        assert result == ""

    def test_get_key_label_decade(self):
        """Test get_key_label with decade pattern."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.get_key_label("1990s")
        assert result == "عقد 1990"


class TestYearFormatDataLegacySearch:
    """Tests for YearFormatData.search method."""

    def test_search_century(self):
        """Test search converts century to Arabic."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.search("14th-century")
        assert result == "القرن 14"

    def test_search_decade(self):
        """Test search converts decade to Arabic."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.search("1990s")
        assert result == "عقد 1990"

    def test_search_year(self):
        """Test search with plain year."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.search("2020")
        assert result == "2020"

    def test_search_millennium(self):
        """Test search converts millennium to Arabic."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.search("3rd millennium")
        assert result == "الألفية 3"

    def test_search_bc_century(self):
        """Test search with BC century."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.search("5th century BC")
        assert result == "القرن 5 ق م"

    def test_search_bc_decade(self):
        """Test search with BC decade."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.search("500s BC")
        assert result == "عقد 500 ق م"

    def test_search_bc_year(self):
        """Test search with BC year."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.search("500 BC")
        assert result == "500 ق م"


class TestYearFormatDataLegacySearchAll:
    """Tests for YearFormatData.search_all method."""

    def test_search_all_century(self):
        """Test search_all converts century to Arabic."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.search_all("14th-century")
        assert result == "القرن 14"

    def test_search_all_decade(self):
        """Test search_all converts decade to Arabic."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.search_all("1990s")
        assert result == "عقد 1990"

    def test_search_all_year(self):
        """Test search_all with plain year."""
        bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = bot.search_all("2020")
        assert result == "2020"


class TestYearFormatDataFactory:
    """Tests for YearFormatData factory function."""

    def test_year_format_data_returns_format_data_from(self):
        """Test YearFormatData returns a FormatDataFrom instance."""
        from ArWikiCats.translations_formats.DataModel.model_multi_data_year_from import (
            FormatDataFrom,
        )

        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        assert isinstance(year_bot, FormatDataFrom)

    def test_year_format_data_search_century(self):
        """Test YearFormatData factory search with century."""
        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = year_bot.search("14th-century")
        assert result == "القرن 14"

    def test_year_format_data_search_decade(self):
        """Test YearFormatData factory search with decade."""
        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = year_bot.search("1990s")
        assert result == "عقد 1990"

    def test_year_format_data_match_key(self):
        """Test YearFormatData factory match_key method."""
        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = year_bot.match_key("14th-century writers")
        assert result == "14th-century"

    def test_year_format_data_no_match(self):
        """Test YearFormatData factory with no match."""
        year_bot = YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )
        result = year_bot.search("no time pattern")
        assert result == ""
