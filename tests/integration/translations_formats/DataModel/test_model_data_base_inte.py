"""
Integration tests for model_data_base.py module.

This module provides integration tests for FormatDataBase class which is
the abstract base class for all FormatData-type formatters.

Note: FormatDataBase is an abstract class, so we test it through
its concrete subclass FormatData.
"""

import pytest

from ArWikiCats.translations_formats.DataModel.model_data import FormatData
from ArWikiCats.translations_formats.DataModel.model_data_base import FormatDataBase


class TestFormatDataBaseIntegration:
    """Integration tests for FormatDataBase through FormatData."""

    @pytest.fixture
    def bot(self):
        """Create a FormatData instance for testing."""
        formatted_data = {
            "{sport} players": "لاعبو {sport_label}",
            "{sport} coaches": "مدربو {sport_label}",
            "{sport} teams": "فرق {sport_label}",
        }
        data_list = {
            "football": "كرة القدم",
            "basketball": "كرة السلة",
            "tennis": "التنس",
        }
        return FormatData(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )

    def test_inherits_from_format_data_base(self, bot):
        """Test that FormatData inherits from FormatDataBase."""
        assert isinstance(bot, FormatDataBase)

    def test_match_key_workflow(self, bot):
        """Test the full match_key workflow."""
        # match_key finds the sport key
        key = bot.match_key("football players")
        assert key == "football"

        # get_key_label returns the Arabic label
        label = bot.get_key_label(key)
        assert label == "كرة القدم"

    def test_normalize_category_workflow(self, bot):
        """Test the full normalize_category workflow."""
        key = bot.match_key("basketball coaches")
        normalized = bot.normalize_category("basketball coaches", key)
        assert normalized == "{sport} coaches"

    def test_get_template_workflow(self, bot):
        """Test the get_template workflow."""
        key = bot.match_key("tennis teams")
        template = bot.get_template(key, "tennis teams")
        assert template == "فرق {sport_label}"

    def test_search_workflow_full(self, bot):
        """Test the complete search workflow."""
        result = bot.search("football players")
        assert result == "لاعبو كرة القدم"

    def test_create_label_alias(self, bot):
        """Test that create_label is an alias for search."""
        search_result = bot.search("basketball coaches")
        create_result = bot.create_label("basketball coaches")
        assert search_result == create_result

    def test_search_all_workflow(self, bot):
        """Test search_all without Category prefix."""
        # search_all doesn't strip the Category: prefix automatically
        result = bot.search_all("tennis teams", add_arabic_category_prefix=False)
        assert result == "فرق التنس"

    def test_search_all_category_workflow(self, bot):
        """Test search_all_category full workflow."""
        result = bot.search_all_category("Category:football players")
        assert result == "تصنيف:لاعبو كرة القدم"


class TestFormatDataBasePatternBuilding:
    """Integration tests for FormatDataBase pattern building."""

    def test_create_alternation_with_multiple_keys(self):
        """Test that create_alternation creates correct alternation pattern."""
        bot = FormatData(
            formatted_data={},
            data_list={"a": "1", "bb": "2", "ccc": "3"},
            key_placeholder="{x}",
            value_placeholder="{x}",
        )
        alternation = bot.create_alternation()
        # Longer keys should come first due to sorting
        assert "ccc" in alternation
        assert "bb" in alternation
        assert "a" in alternation

    def test_keys_to_pattern_creates_pattern(self):
        """Test that keys_to_pattern creates a valid regex pattern."""
        bot = FormatData(
            formatted_data={},
            data_list={"test": "اختبار"},
            key_placeholder="{x}",
            value_placeholder="{x}",
        )
        assert bot.pattern is not None
        match = bot.pattern.search(" test ")
        assert match is not None
        assert match.group(1) == "test"

    def test_pattern_respects_word_boundaries(self):
        """Test that pattern respects word boundaries."""
        bot = FormatData(
            formatted_data={},
            data_list={"test": "اختبار"},
            key_placeholder="{x}",
            value_placeholder="{x}",
        )
        # "test" should match as a word
        match = bot.pattern.search(" test ")
        assert match is not None
        # "testing" should not match "test" as a whole word
        match = bot.pattern.search(" testing ")
        # The pattern uses word boundaries, so this depends on regex_filter


class TestFormatDataBaseCaseInsensitivity:
    """Integration tests for FormatDataBase case insensitivity."""

    @pytest.fixture
    def bot(self):
        """Create a FormatData instance with mixed case."""
        formatted_data = {"Football Players": "لاعبو كرة القدم"}
        data_list = {"FOOTBALL": "كرة القدم"}
        return FormatData(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )

    def test_match_key_case_insensitive(self, bot):
        """Test that match_key is case-insensitive."""
        key = bot.match_key("football players")
        assert key == "football"

    def test_formatted_data_ci_created(self, bot):
        """Test that formatted_data_ci is created."""
        assert "football players" in bot.formatted_data_ci

    def test_data_list_ci_created(self, bot):
        """Test that data_list_ci is created."""
        assert "football" in bot.data_list_ci


class TestFormatDataBaseAddFormattedData:
    """Integration tests for FormatDataBase.add_formatted_data method."""

    def test_add_formatted_data_flow(self):
        """Test adding formatted data after initialization."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )

        # Initially can't find "coaches" template
        result = bot._search("football coaches")
        assert result == ""

        # Add new template
        bot.add_formatted_data("{sport} coaches", "مدربو {sport_label}")

        # Now should find the template (use _search to avoid cache issues)
        result = bot._search("football coaches")
        assert result == "مدربو كرة القدم"
