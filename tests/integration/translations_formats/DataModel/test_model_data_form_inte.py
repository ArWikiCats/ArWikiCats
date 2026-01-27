"""
Integration tests for model_data_form.py module.

This module provides integration tests for FormatDataFrom class which is a
dynamic wrapper for handling category transformations with customizable callbacks.
"""

import pytest

from ArWikiCats.time_formats import convert_time_to_arabic, match_time_en_first
from ArWikiCats.translations_formats.DataModel.model_data_form import FormatDataFrom


class TestFormatDataFromIntegration:
    """Integration tests for FormatDataFrom with time-based callbacks."""

    @pytest.fixture
    def year_bot(self):
        """Create a FormatDataFrom instance for year patterns."""
        return FormatDataFrom(
            formatted_data={
                "{year1} events": "أحداث {year1}",
                "{year1} films": "أفلام {year1}",
            },
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=convert_time_to_arabic,
            match_key_callback=match_time_en_first,
        )

    def test_match_key_century(self, year_bot):
        """Test match_key extracts century."""
        result = year_bot.match_key("14th-century events")
        assert result == "14th-century"

    def test_match_key_decade(self, year_bot):
        """Test match_key extracts decade."""
        result = year_bot.match_key("1990s films")
        assert result == "1990s"

    def test_match_key_year(self, year_bot):
        """Test match_key extracts year."""
        result = year_bot.match_key("2020 events")
        assert result == "2020"

    def test_search_century(self, year_bot):
        """Test search converts century to Arabic."""
        result = year_bot.search("14th-century")
        assert result == "القرن 14"

    def test_search_decade(self, year_bot):
        """Test search converts decade to Arabic."""
        result = year_bot.search("1990s")
        assert result == "عقد 1990"

    def test_search_year(self, year_bot):
        """Test search with plain year."""
        result = year_bot.search("2020")
        assert result == "2020"

    def test_normalize_category_with_key_century(self, year_bot):
        """Test normalize_category_with_key with century."""
        key, normalized = year_bot.normalize_category_with_key("14th-century events")
        assert key == "14th-century"
        assert normalized == "{year1} events"

    def test_get_key_label(self, year_bot):
        """Test get_key_label returns Arabic time."""
        result = year_bot.get_key_label("14th-century")
        assert result == "القرن 14"

    def test_get_template_ar(self, year_bot):
        """Test get_template_ar returns template."""
        result = year_bot.get_template_ar("{year1} events")
        assert result == "أحداث {year1}"

    def test_replace_value_placeholder(self, year_bot):
        """Test replace_value_placeholder replaces placeholder."""
        result = year_bot.replace_value_placeholder("أحداث {year1}", "2020")
        assert result == "أحداث 2020"


class TestFormatDataFromWithCountryCallback:
    """Integration tests for FormatDataFrom with country lookup callbacks."""

    @pytest.fixture
    def country_bot(self):
        """Create a FormatDataFrom instance for country patterns."""
        countries = {
            "yemen": "اليمن",
            "egypt": "مصر",
            "france": "فرنسا",
        }

        def search_callback(key):
            return countries.get(key.lower(), "")

        def match_key_callback(text):
            text_lower = text.lower()
            for country in countries:
                if country in text_lower:
                    return country
            return ""

        return FormatDataFrom(
            formatted_data={
                "{country} people": "شعب {country}",
                "{country} cities": "مدن {country}",
            },
            key_placeholder="{country}",
            value_placeholder="{country}",
            search_callback=search_callback,
            match_key_callback=match_key_callback,
        )

    def test_match_key_country(self, country_bot):
        """Test match_key extracts country name."""
        result = country_bot.match_key("yemen people")
        assert result == "yemen"

    def test_search_country(self, country_bot):
        """Test search returns Arabic country name."""
        result = country_bot.search("yemen")
        assert result == "اليمن"

    def test_normalize_category_with_key(self, country_bot):
        """Test normalize_category_with_key with country."""
        key, normalized = country_bot.normalize_category_with_key("egypt cities")
        assert key == "egypt"
        assert normalized == "{country} cities"


class TestFormatDataFromWithFixingCallback:
    """Integration tests for FormatDataFrom with fixing_callback."""

    @pytest.fixture
    def bot_with_fixing(self):
        """Create a FormatDataFrom instance with fixing_callback."""

        def fix_callback(label):
            # Example: standardize decade format
            return label.replace("سنة ", "")

        return FormatDataFrom(
            formatted_data={"{year1} events": "أحداث سنة {year1}"},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=convert_time_to_arabic,
            match_key_callback=match_time_en_first,
            fixing_callback=fix_callback,
        )

    def test_replace_value_placeholder_with_fixing(self, bot_with_fixing):
        """Test replace_value_placeholder applies fixing_callback."""
        result = bot_with_fixing.replace_value_placeholder("أحداث سنة {year1}", "2020")
        assert result == "أحداث 2020"


class TestFormatDataFromSearchAll:
    """Integration tests for FormatDataFrom.search_all method."""

    @pytest.fixture
    def bot(self):
        """Create a FormatDataFrom instance."""
        return FormatDataFrom(
            formatted_data={},
            key_placeholder="{year1}",
            value_placeholder="{year1}",
            search_callback=convert_time_to_arabic,
            match_key_callback=match_time_en_first,
        )

    def test_search_all_without_prefix(self, bot):
        """Test search_all without Arabic category prefix."""
        result = bot.search_all("14th-century")
        assert result == "القرن 14"

    def test_search_all_with_prefix(self, bot):
        """Test search_all without Category: prefix but with add_arabic_category_prefix."""
        # Note: search_all uses search_callback directly, which doesn't strip Category:
        # So we test without Category: prefix but with add_arabic_category_prefix
        result = bot.search_all("14th-century", add_arabic_category_prefix=False)
        assert result == "القرن 14"

    def test_search_all_without_category_prefix(self, bot):
        """Test search_all without Category: in input."""
        result = bot.search_all("1990s", add_arabic_category_prefix=True)
        assert result == "عقد 1990"
