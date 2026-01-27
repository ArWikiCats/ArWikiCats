#!/usr/bin/python3
"""
Tests for MultiDataFormatterYearAndFrom2 class with translation_category_relations integration.

This module tests the new methods added to MultiDataFormatterYearAndFrom2:
- get_relation_word: Find relation words in categories
- resolve_relation_label: Append Arabic relation words to labels
- get_relation_mapping: Access the translation_category_relations dictionary

Tests follow existing project conventions and use pytest parametrize for data-driven testing.

TODO: use MultiDataFormatterYearAndFrom2 in workflows.
"""

import pytest

from ArWikiCats.format_bots.relation_mapping import translation_category_relations
from ArWikiCats.time_formats.time_to_arabic import convert_time_to_arabic, match_time_en_first
from ArWikiCats.translations_formats import FormatDataFrom, MultiDataFormatterYearAndFrom2


def get_label(text: str) -> str:
    """Mock label lookup function for testing."""
    data = {
        "writers from Hong Kong": "كتاب من هونغ كونغ",
        "writers from yemen": "كتاب من اليمن",
        "writers from Crown of Aragon": "كتاب من تاج أرغون",
        "writers gg yemen": "كتاب من اليمن",
        "people from germany": "أشخاص من ألمانيا",
        "buildings in france": "مباني في فرنسا",
    }
    return data.get(text.lower(), "")


@pytest.fixture
def multi_bot() -> MultiDataFormatterYearAndFrom2:
    """Create a MultiDataFormatterYearAndFrom2 instance for testing."""
    formatted_data = {
        "{year1} {country1}": "{country1} في {year1}",
    }
    country_bot = FormatDataFrom(
        formatted_data=formatted_data,
        key_placeholder="{country1}",
        value_placeholder="{country1}",
        search_callback=get_label,
        match_key_callback=lambda x: x.replace("{year1}", "").strip(),
    )
    year_bot = FormatDataFrom(
        formatted_data={},
        key_placeholder="{year1}",
        value_placeholder="{year1}",
        search_callback=convert_time_to_arabic,
        match_key_callback=match_time_en_first,
    )
    return MultiDataFormatterYearAndFrom2(
        country_bot=country_bot,
        year_bot=year_bot,
        category_relation_mapping=translation_category_relations,
        other_key_first=True,
    )


class TestGetRelationWord:
    """Tests for get_relation_word method."""

    # Test data: (category, expected_key, expected_arabic)
    test_data = [
        ("People from Germany", "from", "من"),
        ("Buildings in France", "in", "في"),
        ("Works published by Oxford", "published by", "نشرتها"),
        ("Films directed by Spielberg", "directed by", "أخرجها"),
        ("Ships launched in 1910", "launched in", "أطلقت في"),
        ("Cities established in 1750", "established in", "أسست في"),
        ("Books written by Dickens", "written by", "كتبها"),
        ("Items manufactured in China", "manufactured in", "صنعت في"),
        ("Treaties concluded in Vienna", "concluded in", "أبرمت في"),
    ]

    @pytest.mark.parametrize(
        "category,expected_key,expected_arabic",
        test_data,
        ids=[t[0] for t in test_data],
    )
    def test_get_relation_word(
        self, multi_bot: MultiDataFormatterYearAndFrom2, category: str, expected_key: str, expected_arabic: str
    ) -> None:
        """Test that get_relation_word correctly identifies relation words."""
        key, arabic = multi_bot.get_relation_word(category)
        assert key == expected_key
        assert arabic == expected_arabic

    def test_no_relation_word(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that get_relation_word returns empty tuple when no relation found."""
        key, arabic = multi_bot.get_relation_word("Random category without relation")
        assert key == ""
        assert arabic == ""

    def test_relation_word_requires_spaces(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that relation words must be surrounded by spaces."""
        # "builtin" should not match "built in"
        key, arabic = multi_bot.get_relation_word("Somethingbuiltin somewhere")
        assert key == ""
        assert arabic == ""


class TestResolveRelationLabel:
    """Tests for resolve_relation_label method."""

    # Test data: (category, base_label, expected_result)
    test_data = [
        ("Writers from Yemen", "كتاب", "كتاب من"),
        ("People in Germany", "أشخاص", "أشخاص في"),
        ("Buildings built in France", "مباني", "مباني بنيت في"),
        ("Films directed by Spielberg", "أفلام", "أفلام أخرجها"),
        ("Works published by Oxford", "أعمال", "أعمال نشرتها"),
    ]

    @pytest.mark.parametrize(
        "category,base_label,expected",
        test_data,
        ids=[t[0] for t in test_data],
    )
    def test_resolve_relation_label(
        self, multi_bot: MultiDataFormatterYearAndFrom2, category: str, base_label: str, expected: str
    ) -> None:
        """Test that resolve_relation_label correctly appends Arabic relation words."""
        result = multi_bot.resolve_relation_label(category, base_label)
        assert result == expected

    def test_empty_base_label(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that resolve_relation_label handles empty base_label."""
        result = multi_bot.resolve_relation_label("Writers from Yemen", "")
        assert result == ""

    def test_empty_category(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that resolve_relation_label handles empty category."""
        result = multi_bot.resolve_relation_label("", "كتاب")
        assert result == "كتاب"

    def test_no_relation_in_category(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that resolve_relation_label returns original label when no relation found."""
        result = multi_bot.resolve_relation_label("Random text", "كتاب")
        assert result == "كتاب"

    def test_avoid_duplicate_relation(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that resolve_relation_label avoids adding duplicate relation words."""
        # "من" is already at the end of the base_label
        result = multi_bot.resolve_relation_label("Writers from Yemen", "كتاب من")
        assert result == "كتاب من"

    def test_avoid_duplicate_relation_with_country(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that resolve_relation_label avoids duplicates when relation is in middle."""
        # "من" appears in the middle followed by country
        result = multi_bot.resolve_relation_label("Writers from Yemen", "كتاب من اليمن")
        assert result == "كتاب من اليمن"

    def test_no_false_positive_duplicate_detection(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that substring matches don't produce false positives."""
        # "من" is part of "من الكتاب" but not as a standalone relation word
        # The method should still add "من" because it's not at word boundaries
        result = multi_bot.resolve_relation_label("Writers from Yemen", "أشخاص")
        assert result == "أشخاص من"


class TestGetRelationMapping:
    """Tests for get_relation_mapping method."""

    def test_get_relation_mapping_contains_expected_keys(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that get_relation_mapping contains expected relation words."""
        mapping = multi_bot.get_relation_mapping()
        # Check some expected keys
        assert "from" in mapping
        assert "in" in mapping
        assert "by" in mapping
        assert "published by" in mapping
        assert "directed by" in mapping

    def test_get_relation_mapping_contains_expected_values(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that get_relation_mapping contains expected Arabic translations."""
        mapping = multi_bot.get_relation_mapping()
        assert mapping["from"] == "من"
        assert mapping["in"] == "في"
        assert mapping["by"] == "حسب"
        assert mapping["published by"] == "نشرتها"


class TestIntegrationWithExistingFunctionality:
    """Integration tests to ensure new methods work with existing functionality."""

    def test_create_label_still_works(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that create_label still works after adding new methods."""
        result = multi_bot.create_label("14th-century writers from yemen")
        assert result == "كتاب من اليمن في القرن 14"

    def test_search_all_still_works(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that search_all still works after adding new methods."""
        result = multi_bot.search_all("14th-century writers from yemen")
        assert result == "كتاب من اليمن في القرن 14"

    def test_normalize_both_new_still_works(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that normalize_both_new still works after adding new methods."""
        result = multi_bot.normalize_both_new("14th-century writers from yemen")
        assert result.nat_key == "writers from yemen"
        assert result.other_key == "14th-century"


class TestEdgeCases:
    """Edge case tests for robust handling."""

    def test_multiple_relation_words(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test category with multiple relation words returns first match."""
        # "from" appears before "in" in translation_category_relations
        key, arabic = multi_bot.get_relation_word("People from Germany in Europe")
        # Should match the first relation word found in the mapping
        assert key in ["from", "in"]

    def test_case_sensitivity(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test that relation word matching is case-sensitive."""
        # The current implementation is case-sensitive
        key, arabic = multi_bot.get_relation_word("People FROM Germany")
        # Should not match because "FROM" != "from"
        assert key == ""
        assert arabic == ""

    def test_special_characters_in_relation(self, multi_bot: MultiDataFormatterYearAndFrom2) -> None:
        """Test relation words with special characters like hyphens."""
        key, arabic = multi_bot.get_relation_word("Schools for-deaf in New York")
        assert key == "for-deaf"
        assert arabic == "للصم"


class TestFormatDataFromClass:
    """Tests for the FormatDataFrom class."""

    def test_format_data_from_init(self) -> None:
        """Test FormatDataFrom initialization."""
        bot = FormatDataFrom(
            formatted_data={"test": "اختبار"},
            key_placeholder="{key}",
            value_placeholder="{value}",
            search_callback=lambda x: x,
            match_key_callback=lambda x: x,
        )
        assert bot.key_placeholder == "{key}"
        assert bot.value_placeholder == "{value}"
        assert bot.formatted_data == {"test": "اختبار"}
        assert "test" in bot.formatted_data_ci

    def test_format_data_from_match_key(self) -> None:
        """Test FormatDataFrom.match_key method."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{key}",
            value_placeholder="{value}",
            search_callback=lambda x: x,
            match_key_callback=lambda x: x.upper(),
        )
        result = bot.match_key("test")
        assert result == "TEST"

    def test_format_data_from_search(self) -> None:
        """Test FormatDataFrom.search method."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{key}",
            value_placeholder="{value}",
            search_callback=lambda x: f"searched: {x}",
            match_key_callback=lambda x: x,
        )
        result = bot.search("test")
        assert result == "searched: test"

    def test_format_data_from_normalize_category(self) -> None:
        """Test FormatDataFrom.normalize_category method."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{placeholder}",
            value_placeholder="{value}",
            search_callback=lambda x: x,
            match_key_callback=lambda x: x,
        )
        result = bot.normalize_category("category with key here", "key")
        assert result == "category with {placeholder} here"

    def test_format_data_from_get_template_ar(self) -> None:
        """Test FormatDataFrom.get_template_ar method."""
        bot = FormatDataFrom(
            formatted_data={"{year1} {country1}": "{country1} في {year1}"},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: x,
            match_key_callback=lambda x: x,
        )
        result = bot.get_template_ar("{year1} {country1}")
        assert result == "{country1} في {year1}"

    def test_format_data_from_get_template_ar_case_insensitive(self) -> None:
        """Test FormatDataFrom.get_template_ar is case-insensitive."""
        bot = FormatDataFrom(
            formatted_data={"{Year1} {Country1}": "{country1} في {year1}"},
            key_placeholder="{country1}",
            value_placeholder="{country1}",
            search_callback=lambda x: x,
            match_key_callback=lambda x: x,
        )
        result = bot.get_template_ar("{year1} {country1}")
        assert result == "{country1} في {year1}"

    def test_format_data_from_fixing_callback(self) -> None:
        """Test FormatDataFrom with fixing_callback."""
        bot = FormatDataFrom(
            formatted_data={},
            key_placeholder="{key}",
            value_placeholder="{value}",
            search_callback=lambda x: x,
            match_key_callback=lambda x: x,
            fixing_callback=lambda x: x.strip().upper(),
        )
        result = bot.replace_value_placeholder("  test {value}  ", "input")
        assert result == "TEST INPUT"
