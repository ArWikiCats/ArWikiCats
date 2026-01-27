#!/usr/bin/python3
"""
Tests for model_data_base.py module.

This module provides tests for FormatDataBase class which is the abstract
base class for all FormatData-type formatters.

Note: FormatDataBase is an abstract class, so we test it through a
concrete subclass (FormatData).
"""

import pytest

from ArWikiCats.translations_formats.DataModel.model_data import FormatData


class TestFormatDataBaseAddFormattedData:
    """Tests for FormatDataBase.add_formatted_data method."""

    def test_add_formatted_data(self):
        """Test adding a new formatted data entry."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        bot.add_formatted_data("{sport} coaches", "مدربو {sport_label}")

        assert "{sport} coaches" in bot.formatted_data
        assert bot.formatted_data["{sport} coaches"] == "مدربو {sport_label}"
        assert "{sport} coaches" in bot.formatted_data_ci

    def test_add_formatted_data_case_insensitive(self):
        """Test that added formatted_data is case-insensitive."""
        bot = FormatData(
            formatted_data={},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        bot.add_formatted_data("{Sport} Players", "لاعبو {sport_label}")

        # Should be accessible with lowercase key
        assert "{sport} players" in bot.formatted_data_ci


class TestFormatDataBaseCreateAlternation:
    """Tests for FormatDataBase.create_alternation method."""

    def test_create_alternation_empty(self):
        """Test create_alternation with empty data_list."""
        bot = FormatData(
            formatted_data={},
            data_list={},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.create_alternation()
        assert result == ""

    def test_create_alternation_single_key(self):
        """Test create_alternation with single key."""
        bot = FormatData(
            formatted_data={},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.create_alternation()
        assert result == "football"

    def test_create_alternation_multiple_keys(self):
        """Test create_alternation with multiple keys."""
        bot = FormatData(
            formatted_data={},
            data_list={"football": "كرة القدم", "basketball": "كرة السلة"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.create_alternation()
        # Should contain both keys, sorted by space count then length
        assert "football" in result
        assert "basketball" in result


class TestFormatDataBaseMatchKeyNoPattern:
    """Tests for FormatDataBase.match_key when pattern is None."""

    def test_match_key_no_pattern(self):
        """Test match_key returns empty string when pattern is None."""
        bot = FormatData(
            formatted_data={},
            data_list={},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        # With empty data_list, pattern will be None
        result = bot.match_key("football players")
        assert result == ""


class TestFormatDataBaseHandleTextsBeforeAfter:
    """Tests for FormatDataBase.handle_texts_before_after method."""

    def test_handle_texts_no_text_before_after(self):
        """Test handle_texts_before_after when no text_before or text_after."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.handle_texts_before_after("{sport} players")
        assert result == "{sport} players"

    def test_handle_texts_with_text_before(self):
        """Test handle_texts_before_after with text_before - not found in formatted_data_ci."""
        bot = FormatData(
            # The formatted_data doesn't contain "the {sport} players"
            formatted_data={"players": "لاعبو"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
            text_before="the ",
        )
        result = bot.handle_texts_before_after("the {sport} players")
        # Should replace "the {sport}" with "{sport}"
        assert result == "{sport} players"

    def test_handle_texts_with_text_after(self):
        """Test handle_texts_before_after with text_after."""
        bot = FormatData(
            # The formatted_data doesn't contain "{sport} people"
            formatted_data={"players": "لاعبو"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
            text_after=" people",
        )
        result = bot.handle_texts_before_after("{sport} people")
        # Should replace "{sport} people" with "{sport}"
        assert result == "{sport}"

    def test_handle_texts_found_directly(self):
        """Test handle_texts_before_after when normalized found directly without text_before/after."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
            text_before="the ",
        )
        result = bot.handle_texts_before_after("{sport} players")
        # Found directly in formatted_data_ci and doesn't need processing
        # (no "the {sport}" in the input)
        assert result == "{sport} players"

    def test_handle_texts_with_both_before_and_after(self):
        """Test handle_texts_before_after with both text_before and text_after."""
        bot = FormatData(
            formatted_data={"players": "لاعبو"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
            text_before="the ",
            text_after=" category",
        )
        result = bot.handle_texts_before_after("the {sport} category")
        # Should handle both text_before and text_after
        assert result == "{sport}"


class TestFormatDataBaseGetTemplateAr:
    """Tests for FormatDataBase.get_template_ar method."""

    def test_get_template_ar_simple(self):
        """Test get_template_ar with simple template."""
        bot = FormatData(
            formatted_data={"football players": "لاعبو كرة القدم"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.get_template_ar("football players")
        assert result == "لاعبو كرة القدم"

    def test_get_template_ar_with_category_prefix(self):
        """Test get_template_ar with 'category:' prefix."""
        bot = FormatData(
            formatted_data={"football players": "لاعبو كرة القدم"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.get_template_ar("category:football players")
        assert result == "لاعبو كرة القدم"

    def test_get_template_ar_without_category_prefix_adds_it(self):
        """Test get_template_ar adds 'category:' prefix if needed."""
        bot = FormatData(
            formatted_data={"category:football players": "لاعبو كرة القدم"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.get_template_ar("football players")
        assert result == "لاعبو كرة القدم"

    def test_get_template_ar_case_insensitive(self):
        """Test get_template_ar is case-insensitive."""
        bot = FormatData(
            formatted_data={"Football Players": "لاعبو كرة القدم"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.get_template_ar("football players")
        assert result == "لاعبو كرة القدم"


class TestFormatDataBaseSearch:
    """Tests for FormatDataBase._search method."""

    def test_search_exact_match_in_formatted_data(self):
        """Test _search with exact match in formatted_data_ci."""
        bot = FormatData(
            formatted_data={"football players": "لاعبو كرة القدم"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot._search("football players")
        assert result == "لاعبو كرة القدم"

    def test_search_no_sport_key_match(self):
        """Test _search when no sport key matches."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot._search("no match players")
        assert result == ""

    def test_search_no_sport_label_match(self):
        """Test _search when key matches but no label found."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={},  # Empty data_list
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot._search("football players")
        assert result == ""

    def test_search_no_template_match(self):
        """Test _search when key and label match but no template found."""
        bot = FormatData(
            formatted_data={},  # Empty formatted_data
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot._search("football players")
        assert result == ""


class TestFormatDataBaseCreateLabel:
    """Tests for FormatDataBase.create_label method."""

    def test_create_label(self):
        """Test create_label is an alias for search."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.create_label("football players")
        assert result == "لاعبو كرة القدم"


class TestFormatDataBasePrependArabicCategoryPrefix:
    """Tests for FormatDataBase.prepend_arabic_category_prefix method."""

    def test_prepend_arabic_category_prefix_with_category_prefix(self):
        """Test prepend_arabic_category_prefix with category: prefix."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.prepend_arabic_category_prefix("Category:football players", "لاعبو كرة القدم")
        assert result == "تصنيف:لاعبو كرة القدم"

    def test_prepend_arabic_category_prefix_without_category_prefix(self):
        """Test prepend_arabic_category_prefix without category: prefix."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.prepend_arabic_category_prefix("football players", "لاعبو كرة القدم")
        assert result == "لاعبو كرة القدم"

    def test_prepend_arabic_category_prefix_already_has_prefix(self):
        """Test prepend_arabic_category_prefix when result already has prefix."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.prepend_arabic_category_prefix("Category:football players", "تصنيف:لاعبو كرة القدم")
        # Should not duplicate the prefix
        assert result == "تصنيف:لاعبو كرة القدم"

    def test_prepend_arabic_category_prefix_empty_result(self):
        """Test prepend_arabic_category_prefix with empty result."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.prepend_arabic_category_prefix("Category:football players", "")
        assert result == ""

    def test_prepend_arabic_category_prefix_case_insensitive(self):
        """Test prepend_arabic_category_prefix is case-insensitive for category:."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.prepend_arabic_category_prefix("CATEGORY:football players", "لاعبو كرة القدم")
        assert result == "تصنيف:لاعبو كرة القدم"


class TestFormatDataBaseSearchAll:
    """Tests for FormatDataBase.search_all method."""

    def test_search_all_without_prefix(self):
        """Test search_all without add_arabic_category_prefix."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.search_all("football players", add_arabic_category_prefix=False)
        assert result == "لاعبو كرة القدم"

    def test_search_all_with_prefix(self):
        """Test search_all with add_arabic_category_prefix=True."""
        bot = FormatData(
            formatted_data={"category:{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.search_all("Category:football players", add_arabic_category_prefix=True)
        assert result == "تصنيف:لاعبو كرة القدم"

    def test_search_all_no_match(self):
        """Test search_all when no match found."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.search_all("no match")
        assert result == ""


class TestFormatDataBaseCheckPlaceholders:
    """Tests for FormatDataBase.check_placeholders method."""

    def test_check_placeholders_no_placeholders(self):
        """Test check_placeholders with no unprocessed placeholders."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.check_placeholders("football players", "لاعبو كرة القدم")
        assert result == "لاعبو كرة القدم"

    def test_check_placeholders_with_unprocessed(self):
        """Test check_placeholders with unprocessed placeholders."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.check_placeholders("football players", "لاعبو {unprocessed}")
        assert result == ""

    def test_check_placeholders_empty_result(self):
        """Test check_placeholders with empty result."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.check_placeholders("football players", "")
        assert result == ""


class TestFormatDataBaseSearchAllCategory:
    """Tests for FormatDataBase.search_all_category method."""

    def test_search_all_category_full_flow(self):
        """Test search_all_category full normalization flow."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.search_all_category("Category:football players")
        assert result == "تصنيف:لاعبو كرة القدم"

    def test_search_all_category_without_category_prefix(self):
        """Test search_all_category without Category: prefix."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.search_all_category("football players")
        # Should still add Arabic prefix since original didn't have it
        assert result == "لاعبو كرة القدم"

    def test_search_all_category_case_insensitive(self):
        """Test search_all_category is case-insensitive."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.search_all_category("CATEGORY:Football Players")
        assert result == "تصنيف:لاعبو كرة القدم"

    def test_search_all_category_no_match(self):
        """Test search_all_category when no match found."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.search_all_category("no match")
        assert result == ""

    def test_search_all_category_with_unprocessed_placeholders(self):
        """Test search_all_category returns empty for unprocessed placeholders."""
        bot = FormatData(
            # This will leave {sport_label} in the result if no data_list matches
            formatted_data={"players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        # Since "players" has {sport_label} but no sport matched, it won't be replaced
        result = bot.search_all_category("players")
        # Should return empty due to unprocessed placeholder
        assert result == ""

    def test_search_all_category_extra_spaces(self):
        """Test search_all_category normalizes extra spaces."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.search_all_category("Category:football    players")
        assert result == "تصنيف:لاعبو كرة القدم"
