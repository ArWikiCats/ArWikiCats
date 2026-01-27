"""
Integration tests for model_data_v2.py module.

This module provides integration tests for FormatDataV2 class which handles
dictionary-based template-driven category translations where data_list values
can be dictionaries with multiple placeholder replacements.
"""

import pytest

from ArWikiCats.translations_formats.DataModel.model_data_v2 import FormatDataV2


class TestFormatDataV2Integration:
    """Integration tests for FormatDataV2 class."""

    @pytest.fixture
    def country_bot(self):
        """Create a FormatDataV2 instance for country-related categories."""
        formatted_data = {
            "{country} writers": "كتاب {demonym}",
            "{country} athletes": "رياضيون {demonym}",
            "{country} scientists": "علماء {demonym}",
        }
        data_list = {
            "yemen": {"demonym": "يمنيون", "country_ar": "اليمن"},
            "egypt": {"demonym": "مصريون", "country_ar": "مصر"},
            "france": {"demonym": "فرنسيون", "country_ar": "فرنسا"},
        }
        return FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
        )

    def test_search_with_dict_value(self, country_bot):
        """Test search with dictionary data_list value."""
        result = country_bot.search("yemen writers")
        assert result == "كتاب يمنيون"

    def test_search_multiple_countries(self, country_bot):
        """Test search with different countries."""
        assert country_bot.search("egypt athletes") == "رياضيون مصريون"
        assert country_bot.search("france scientists") == "علماء فرنسيون"

    def test_search_no_match(self, country_bot):
        """Test search returns empty string when no match."""
        result = country_bot.search("unknown country writers")
        assert result == ""

    def test_search_case_insensitive(self, country_bot):
        """Test that search is case-insensitive."""
        result = country_bot.search("YEMEN WRITERS")
        assert result == "كتاب يمنيون"


class TestFormatDataV2MultiplePlaceholders:
    """Integration tests for FormatDataV2 with multiple placeholders."""

    @pytest.fixture
    def bot(self):
        """Create a FormatDataV2 instance with multiple placeholders."""
        formatted_data = {
            "{nat} people in {place}": "شعب {demonym} في {country_ar}",
        }
        data_list = {
            "yemeni": {
                "demonym": "يمني",
                "country_ar": "اليمن",
                "place": "الشرق الأوسط",
            },
        }
        return FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{nat}",
        )

    def test_multiple_placeholders_replaced(self, bot):
        """Test that multiple placeholders are replaced."""
        result = bot.search("yemeni people in {place}")
        # Only {demonym} and {country_ar} are in the template
        assert "يمني" in result
        assert "اليمن" in result


class TestFormatDataV2MatchAndNormalize:
    """Integration tests for FormatDataV2 match and normalize methods."""

    @pytest.fixture
    def bot(self):
        """Create a FormatDataV2 instance for testing."""
        formatted_data = {"{nat} people": "شعب {demonym}"}
        data_list = {"yemen": {"demonym": "يمني"}}
        return FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{nat}",
        )

    def test_match_key(self, bot):
        """Test match_key returns matched key."""
        result = bot.match_key("yemen people")
        assert result == "yemen"

    def test_normalize_category(self, bot):
        """Test normalize_category replaces key with placeholder."""
        result = bot.normalize_category("yemen people", "yemen")
        assert result == "{nat} people"

    def test_normalize_category_with_key(self, bot):
        """Test normalize_category_with_key returns both key and normalized."""
        key, normalized = bot.normalize_category_with_key("yemen people")
        assert key == "yemen"
        assert normalized == "{nat} people"


class TestFormatDataV2ReplaceValuePlaceholder:
    """Integration tests for FormatDataV2.replace_value_placeholder method."""

    def test_replace_value_placeholder_dict(self):
        """Test replace_value_placeholder with dictionary value."""
        bot = FormatDataV2(
            formatted_data={},
            data_list={},
            key_placeholder="{nat}",
        )
        value = {"demonym": "يمني", "country": "اليمن"}
        result = bot.replace_value_placeholder("شعب {demonym} من {country}", value)
        assert result == "شعب يمني من اليمن"

    def test_replace_value_placeholder_partial_dict(self):
        """Test replace_value_placeholder with partial dictionary value."""
        bot = FormatDataV2(
            formatted_data={},
            data_list={},
            key_placeholder="{nat}",
        )
        value = {"demonym": "يمني"}
        result = bot.replace_value_placeholder("شعب {demonym} من {country}", value)
        # Only {demonym} is replaced, {country} remains
        assert "يمني" in result
        assert "{country}" in result

    def test_replace_value_placeholder_non_dict(self):
        """Test replace_value_placeholder with non-dictionary value."""
        bot = FormatDataV2(
            formatted_data={},
            data_list={},
            key_placeholder="{nat}",
        )
        result = bot.replace_value_placeholder("شعب {demonym}", "not a dict")
        # Non-dict values are not processed
        assert result == "شعب {demonym}"


class TestFormatDataV2TextBeforeAfter:
    """Integration tests for FormatDataV2 with text_before and text_after."""

    @pytest.fixture
    def bot(self):
        """Create a FormatDataV2 instance with text_before."""
        formatted_data = {"{nat} people": "شعب {demonym}"}
        data_list = {"yemen": {"demonym": "يمني"}}
        return FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{nat}",
            text_before="the ",
        )

    def test_search_with_text_before(self, bot):
        """Test search handles text_before correctly."""
        result = bot.search("the yemen people")
        assert result == "شعب يمني"


class TestFormatDataV2SearchAll:
    """Integration tests for FormatDataV2.search_all method."""

    @pytest.fixture
    def bot(self):
        """Create a FormatDataV2 instance."""
        formatted_data = {"{nat} writers": "كتاب {demonym}"}
        data_list = {"yemen": {"demonym": "يمنيون"}}
        return FormatDataV2(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{nat}",
        )

    def test_search_all_without_prefix(self, bot):
        """Test search_all without Arabic category prefix."""
        result = bot.search_all("yemen writers")
        assert result == "كتاب يمنيون"

    def test_search_all_with_prefix(self, bot):
        """Test search_all without Category: but with add_arabic_category_prefix flag."""
        # Note: search_all doesn't strip Category: prefix from input
        result = bot.search_all("yemen writers", add_arabic_category_prefix=False)
        assert result == "كتاب يمنيون"

    def test_search_all_category(self, bot):
        """Test search_all_category full workflow."""
        result = bot.search_all_category("Category:yemen writers")
        assert result == "تصنيف:كتاب يمنيون"
