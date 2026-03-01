#!/usr/bin/python3
"""
Tests for mixins.py module.

This module tests the CategoryPrefixMixin class which provides shared
functionality for category prefix handling and placeholder validation.
"""

import pytest

from ArWikiCats.translations_formats.mixins import (
    ARABIC_CATEGORY_PREFIX,
    ENGLISH_CATEGORY_PREFIX,
    CategoryPrefixMixin,
)


class TestCategoryPrefixConstants:
    """Tests for module-level constants."""

    def test_arabic_prefix_constant(self):
        """Test Arabic category prefix constant."""
        assert ARABIC_CATEGORY_PREFIX == "تصنيف:"

    def test_english_prefix_constant(self):
        """Test English category prefix constant."""
        assert ENGLISH_CATEGORY_PREFIX == "category:"


class TestCategoryPrefixMixinPrependPrefix:
    """Tests for prepend_arabic_category_prefix method."""

    def setup_method(self):
        """Create a test instance with the mixin."""
        self.mixin = CategoryPrefixMixin()

    def test_prepend_when_category_has_prefix(self):
        """Test prepending when category has 'category:' prefix."""
        result = self.mixin.prepend_arabic_category_prefix("category:Football", "كرة القدم")
        assert result == "تصنيف:كرة القدم"

    def test_prepend_case_insensitive(self):
        """Test that the prefix check is case-insensitive."""
        result = self.mixin.prepend_arabic_category_prefix("Category:Football", "كرة القدم")
        assert result == "تصنيف:كرة القدم"

        result = self.mixin.prepend_arabic_category_prefix("CATEGORY:Football", "كرة القدم")
        assert result == "تصنيف:كرة القدم"

    def test_no_prepend_when_result_has_prefix(self):
        """Test no prepending when result already has Arabic prefix."""
        result = self.mixin.prepend_arabic_category_prefix("category:Football", "تصنيف:كرة القدم")
        assert result == "تصنيف:كرة القدم"

    def test_no_prepend_when_category_no_prefix(self):
        """Test no prepending when category doesn't have 'category:' prefix."""
        result = self.mixin.prepend_arabic_category_prefix("Football", "كرة القدم")
        assert result == "كرة القدم"

    def test_no_prepend_when_result_empty(self):
        """Test no prepending when result is empty."""
        result = self.mixin.prepend_arabic_category_prefix("category:Football", "")
        assert result == ""


class TestCategoryPrefixMixinCheckPlaceholders:
    """Tests for check_placeholders method."""

    def setup_method(self):
        """Create a test instance with the mixin."""
        self.mixin = CategoryPrefixMixin()

    def test_valid_result_no_placeholders(self):
        """Test that valid results without placeholders are returned."""
        result = self.mixin.check_placeholders("Football", "كرة القدم")
        assert result == "كرة القدم"

    def test_invalid_result_with_placeholder(self):
        """Test that results with placeholders return empty string."""
        result = self.mixin.check_placeholders("Football", "لاعبو {sport}")
        assert result == ""

    def test_empty_result(self):
        """Test that empty results pass through."""
        result = self.mixin.check_placeholders("Football", "")
        assert result == ""


class TestCategoryPrefixMixinStripPrefix:
    """Tests for strip_category_prefix static method."""

    def test_strip_lowercase_prefix(self):
        """Test stripping lowercase 'category:' prefix."""
        result = CategoryPrefixMixin.strip_category_prefix("category:Football")
        assert result == "Football"

    def test_strip_mixed_case_prefix(self):
        """Test stripping mixed case prefix."""
        result = CategoryPrefixMixin.strip_category_prefix("Category:Football")
        assert result == "Football"

        result = CategoryPrefixMixin.strip_category_prefix("CATEGORY:Football")
        assert result == "Football"

    def test_no_prefix_unchanged(self):
        """Test that strings without prefix are unchanged."""
        result = CategoryPrefixMixin.strip_category_prefix("Football")
        assert result == "Football"

    def test_empty_string(self):
        """Test handling of empty string."""
        result = CategoryPrefixMixin.strip_category_prefix("")
        assert result == ""


class TestCategoryPrefixMixinNormalize:
    """Tests for normalize_category_string static method."""

    def test_normalize_collapses_whitespace(self):
        """Test that whitespace is collapsed."""
        result = CategoryPrefixMixin.normalize_category_string("  Football   players  ")
        assert result == "Football players"

    def test_normalize_with_strip_prefix(self):
        """Test normalization with prefix stripping."""
        result = CategoryPrefixMixin.normalize_category_string("category:Football players", strip_prefix=True)
        assert result == "Football players"

    def test_normalize_without_strip_prefix(self):
        """Test normalization without prefix stripping."""
        result = CategoryPrefixMixin.normalize_category_string("category:Football players", strip_prefix=False)
        assert result == "category:Football players"

    def test_normalize_multiple_spaces_and_prefix(self):
        """Test combined normalization with spaces and prefix."""
        result = CategoryPrefixMixin.normalize_category_string("  category:Football   players  ", strip_prefix=True)
        assert result == "Football players"
