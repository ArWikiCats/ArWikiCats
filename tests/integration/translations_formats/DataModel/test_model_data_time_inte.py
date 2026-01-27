"""
Integration tests for model_data_time.py module.

This module provides integration tests for YearFormatData factory function
which creates formatters for year, decade, and century patterns.
"""

import pytest

from ArWikiCats.translations_formats.DataModel.model_data_time import (
    YearFormatData,
)


class TestYearFormatDataIntegration:
    """Integration tests for YearFormatData."""

    @pytest.fixture
    def year_bot(self):
        """Create a YearFormatData instance."""
        return YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )

    def test_search_year(self, year_bot):
        """Test search with plain year."""
        result = year_bot.search("2020")
        assert result == "2020"

    def test_search_decade(self, year_bot):
        """Test search with decade pattern."""
        result = year_bot.search("1990s")
        assert result == "عقد 1990"

    def test_search_century(self, year_bot):
        """Test search with century pattern."""
        result = year_bot.search("14th-century")
        assert result == "القرن 14"

    def test_search_millennium(self, year_bot):
        """Test search with millennium pattern."""
        result = year_bot.search("3rd millennium")
        assert result == "الألفية 3"

    def test_search_bc_year(self, year_bot):
        """Test search with BC year."""
        result = year_bot.search("500 BC")
        assert result == "500 ق م"

    def test_search_bc_century(self, year_bot):
        """Test search with BC century."""
        result = year_bot.search("5th century BC")
        assert result == "القرن 5 ق م"

    def test_search_bc_decade(self, year_bot):
        """Test search with BC decade."""
        result = year_bot.search("500s BC")
        assert result == "عقد 500 ق م"

    def test_search_no_match(self, year_bot):
        """Test search returns empty string for non-time patterns."""
        result = year_bot.search("no time pattern")
        assert result == ""

    def test_match_key_century(self, year_bot):
        """Test match_key extracts century from text."""
        result = year_bot.match_key("14th-century writers")
        assert result == "14th-century"

    def test_match_key_decade(self, year_bot):
        """Test match_key extracts decade from text."""
        result = year_bot.match_key("1990s films")
        assert result == "1990s"

    def test_match_key_year(self, year_bot):
        """Test match_key extracts year from text."""
        result = year_bot.match_key("2020 events")
        assert result == "2020"

    def test_match_key_no_match(self, year_bot):
        """Test match_key returns empty string when no match."""
        result = year_bot.match_key("no time pattern here")
        assert result == ""

    def test_normalize_category_with_key(self, year_bot):
        """Test normalize_category_with_key replaces time with placeholder."""
        key, normalized = year_bot.normalize_category_with_key("14th-century writers")
        assert key == "14th-century"
        assert normalized == "{year1} writers"

    def test_get_key_label_century(self, year_bot):
        """Test get_key_label converts century to Arabic."""
        result = year_bot.get_key_label("14th-century")
        assert result == "القرن 14"

    def test_get_key_label_decade(self, year_bot):
        """Test get_key_label converts decade to Arabic."""
        result = year_bot.get_key_label("1990s")
        assert result == "عقد 1990"


class TestYearFormatDataVariousCenturies:
    """Integration tests for YearFormatData with various century formats."""

    @pytest.fixture
    def year_bot(self):
        """Create a YearFormatData instance."""
        return YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )

    @pytest.mark.parametrize(
        "century,expected",
        [
            ("1st-century", "القرن 1"),
            ("2nd-century", "القرن 2"),
            ("3rd-century", "القرن 3"),
            ("4th-century", "القرن 4"),
            ("10th-century", "القرن 10"),
            ("21st-century", "القرن 21"),
        ],
    )
    def test_various_centuries(self, year_bot, century, expected):
        """Test various century patterns."""
        result = year_bot.search(century)
        assert result == expected


class TestYearFormatDataVariousDecades:
    """Integration tests for YearFormatData with various decade formats."""

    @pytest.fixture
    def year_bot(self):
        """Create a YearFormatData instance."""
        return YearFormatData(
            key_placeholder="{year1}",
            value_placeholder="{year1}",
        )

    @pytest.mark.parametrize(
        "decade,expected",
        [
            ("1950s", "عقد 1950"),
            ("1960s", "عقد 1960"),
            ("1970s", "عقد 1970"),
            ("1980s", "عقد 1980"),
            ("2000s", "عقد 2000"),
            ("2010s", "عقد 2010"),
            ("2020s", "عقد 2020"),
        ],
    )
    def test_various_decades(self, year_bot, decade, expected):
        """Test various decade patterns."""
        result = year_bot.search(decade)
        assert result == expected
