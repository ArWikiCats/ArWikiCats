#!/usr/bin/python3
"""
Unit tests for model_multi_data_base.py module.

This module provides tests for NormalizeResult dataclass which stores
the results of category normalization.
"""


from ArWikiCats.translations_formats.DataModelMulti.model_multi_data_base import (
    MultiDataFormatterBaseHelpers,
    NormalizeResult,
)


class TestNormalizeResult:
    """Tests for NormalizeResult dataclass."""

    def test_init_basic(self):
        """Test basic initialization of NormalizeResult."""
        result = NormalizeResult(
            template_key_first="{nat} football championships",
            category="british football championships",
            template_key="{nat} {sport} championships",
            nat_key="british",
            other_key="football",
        )

        assert result.template_key_first == "{nat} football championships"
        assert result.category == "british football championships"
        assert result.template_key == "{nat} {sport} championships"
        assert result.nat_key == "british"
        assert result.other_key == "football"

    def test_init_empty_values(self):
        """Test initialization with empty values."""
        result = NormalizeResult(
            template_key_first="",
            category="",
            template_key="",
            nat_key="",
            other_key="",
        )

        assert result.template_key_first == ""
        assert result.category == ""
        assert result.template_key == ""
        assert result.nat_key == ""
        assert result.other_key == ""

    def test_attributes_are_strings(self):
        """Test that all attributes are strings."""
        result = NormalizeResult(
            template_key_first="test1",
            category="test2",
            template_key="test3",
            nat_key="test4",
            other_key="test5",
        )

        assert isinstance(result.template_key_first, str)
        assert isinstance(result.category, str)
        assert isinstance(result.template_key, str)
        assert isinstance(result.nat_key, str)
        assert isinstance(result.other_key, str)

    def test_equality(self):
        """Test equality between two NormalizeResult instances."""
        result1 = NormalizeResult(
            template_key_first="first",
            category="cat",
            template_key="key",
            nat_key="nat",
            other_key="other",
        )
        result2 = NormalizeResult(
            template_key_first="first",
            category="cat",
            template_key="key",
            nat_key="nat",
            other_key="other",
        )

        assert result1 == result2

    def test_inequality(self):
        """Test inequality between two NormalizeResult instances."""
        result1 = NormalizeResult(
            template_key_first="first",
            category="cat",
            template_key="key",
            nat_key="nat",
            other_key="other",
        )
        result2 = NormalizeResult(
            template_key_first="different",
            category="cat",
            template_key="key",
            nat_key="nat",
            other_key="other",
        )

        assert result1 != result2


class TestMultiDataFormatterBaseHelpersInit:
    """Tests for MultiDataFormatterBaseHelpers __init__ method."""

    def test_init_sets_data_to_find_to_none(self):
        """Test that __init__ sets data_to_find to None."""
        helper = MultiDataFormatterBaseHelpers()
        assert helper.data_to_find is None


class TestMultiDataFormatterBaseHelpersCheckPlaceholders:
    """Tests for MultiDataFormatterBaseHelpers.check_placeholders method."""

    def test_check_placeholders_no_placeholders(self):
        """Test check_placeholders when no unprocessed placeholders."""
        helper = MultiDataFormatterBaseHelpers()
        result = helper.check_placeholders("category", "لاعبو كرة القدم")
        assert result == "لاعبو كرة القدم"

    def test_check_placeholders_with_unprocessed(self):
        """Test check_placeholders when unprocessed placeholders present."""
        helper = MultiDataFormatterBaseHelpers()
        result = helper.check_placeholders("category", "لاعبو {unprocessed}")
        assert result == ""

    def test_check_placeholders_empty_result(self):
        """Test check_placeholders with empty result."""
        helper = MultiDataFormatterBaseHelpers()
        result = helper.check_placeholders("category", "")
        assert result == ""


class TestMultiDataFormatterBaseHelpersPrependArabicCategoryPrefix:
    """Tests for MultiDataFormatterBaseHelpers.prepend_arabic_category_prefix method."""

    def test_prepend_with_category_prefix(self):
        """Test prepend_arabic_category_prefix with category: prefix."""
        helper = MultiDataFormatterBaseHelpers()
        result = helper.prepend_arabic_category_prefix("Category:test", "نتيجة")
        assert result == "تصنيف:نتيجة"

    def test_prepend_without_category_prefix(self):
        """Test prepend_arabic_category_prefix without category: prefix."""
        helper = MultiDataFormatterBaseHelpers()
        result = helper.prepend_arabic_category_prefix("test", "نتيجة")
        assert result == "نتيجة"

    def test_prepend_already_has_arabic_prefix(self):
        """Test prepend_arabic_category_prefix when result already has prefix."""
        helper = MultiDataFormatterBaseHelpers()
        result = helper.prepend_arabic_category_prefix("Category:test", "تصنيف:نتيجة")
        assert result == "تصنيف:نتيجة"

    def test_prepend_empty_result(self):
        """Test prepend_arabic_category_prefix with empty result."""
        helper = MultiDataFormatterBaseHelpers()
        result = helper.prepend_arabic_category_prefix("Category:test", "")
        assert result == ""

    def test_prepend_case_insensitive(self):
        """Test prepend_arabic_category_prefix is case-insensitive."""
        helper = MultiDataFormatterBaseHelpers()
        result = helper.prepend_arabic_category_prefix("CATEGORY:test", "نتيجة")
        assert result == "تصنيف:نتيجة"
