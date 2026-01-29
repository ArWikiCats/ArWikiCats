# -*- coding: utf-8 -*-
"""
Unit tests for the filter_en module.
"""

import pytest

from ArWikiCats.fix.filter_en import CATEGORY_BLACKLIST, CATEGORY_PREFIX_BLACKLIST, MONTH_NAMES, filter_cat


class TestFilterCatBlacklist:
    """Tests for filter_cat with blacklisted terms."""

    def test_blocks_disambiguation_categories(self) -> None:
        """Should block categories containing 'Disambiguation'."""
        # The blacklist contains "Disambiguation" which needs to match substring
        assert filter_cat("Test disambiguation test") is False
        assert filter_cat("disambiguation") is False
        assert filter_cat("DISAMBIGUATION") is False

    def test_blocks_wikiproject_categories(self) -> None:
        """Should block categories containing 'wikiproject'."""
        assert filter_cat("WikiProject Test") is False
        assert filter_cat("Test wikiproject page") is False

    def test_blocks_sockpuppets_categories(self) -> None:
        """Should block categories containing 'sockpuppets'."""
        assert filter_cat("Suspected sockpuppets") is False
        assert filter_cat("Sockpuppets of User") is False

    def test_blocks_without_source_categories(self) -> None:
        """Should block categories containing 'without a source'."""
        assert filter_cat("Articles without a source") is False

    def test_blocks_images_for_deletion(self) -> None:
        """Should block categories containing 'images for deletion'."""
        assert filter_cat("Images for deletion") is False

    def test_case_insensitive_blacklist_matching(self) -> None:
        """Should perform case-insensitive matching for blacklist."""
        assert filter_cat("test disambiguation test") is False
        assert filter_cat("test wikiproject test") is False
        assert filter_cat("test sockpuppets test") is False


class TestFilterCatPrefixBlacklist:
    """Tests for filter_cat with prefix blacklist."""

    def test_blocks_cleanup_prefix(self) -> None:
        """Should block categories starting with 'Clean-up' or 'Cleanup'."""
        assert filter_cat("Clean-up articles") is False
        assert filter_cat("Cleanup from 2020") is False

    def test_blocks_uncategorized_prefix(self) -> None:
        """Should block categories starting with 'Uncategorized'."""
        assert filter_cat("Uncategorized pages") is False

    def test_blocks_unreferenced_prefix(self) -> None:
        """Should block categories starting with 'Unreferenced'."""
        assert filter_cat("Unreferenced articles") is False

    def test_blocks_unverifiable_prefix(self) -> None:
        """Should block categories starting with 'Unverifiable'."""
        assert filter_cat("Unverifiable content") is False

    def test_blocks_unverified_prefix(self) -> None:
        """Should block categories starting with 'Unverified'."""
        assert filter_cat("Unverified claims") is False

    def test_blocks_wikipedia_prefix(self) -> None:
        """Should block categories starting with 'Wikipedia'."""
        assert filter_cat("Wikipedia articles") is False
        assert filter_cat("Wikipedia templates") is False

    def test_blocks_articles_about_prefix(self) -> None:
        """Should block categories starting with 'Articles about'."""
        assert filter_cat("Articles about living people") is False

    def test_blocks_articles_containing_prefix(self) -> None:
        """Should block categories starting with 'Articles containing'."""
        assert filter_cat("Articles containing Arabic text") is False

    def test_blocks_articles_needing_prefix(self) -> None:
        """Should block categories starting with 'Articles needing'."""
        assert filter_cat("Articles needing cleanup") is False

    def test_blocks_articles_with_prefix(self) -> None:
        """Should block categories starting with 'Articles with'."""
        assert filter_cat("Articles with unsourced statements") is False

    def test_blocks_use_prefix(self) -> None:
        """Should block categories starting with 'use '."""
        assert filter_cat("use dmy dates") is False
        assert filter_cat("Use American English") is False

    def test_blocks_user_pages_prefix(self) -> None:
        """Should block categories starting with 'User pages'."""
        assert filter_cat("User pages with test") is False

    def test_blocks_userspace_prefix(self) -> None:
        """Should block categories starting with 'Userspace'."""
        assert filter_cat("Userspace drafts") is False

    def test_case_insensitive_prefix_matching(self) -> None:
        """Should perform case-insensitive matching for prefixes."""
        assert filter_cat("CLEANUP ARTICLES") is False
        assert filter_cat("cleanup articles") is False
        assert filter_cat("Cleanup Articles") is False

    def test_strips_category_prefix_before_checking(self) -> None:
        """Should strip 'Category:' before checking prefixes."""
        assert filter_cat("Category:Wikipedia articles") is False
        assert filter_cat("Category:Cleanup pages") is False


class TestFilterCatMonthPatterns:
    """Tests for filter_cat with month-based date patterns."""

    def test_blocks_from_january_pattern(self) -> None:
        """Should block 'from January YYYY' patterns."""
        assert filter_cat("Articles from January 2020") is False
        assert filter_cat("Something from january 2021") is False

    def test_blocks_from_february_pattern(self) -> None:
        """Should block 'from February YYYY' patterns."""
        assert filter_cat("Articles from February 2020") is False

    def test_blocks_from_march_pattern(self) -> None:
        """Should block 'from March YYYY' patterns."""
        assert filter_cat("Articles from March 2019") is False

    def test_blocks_all_month_patterns(self) -> None:
        """Should block patterns for all months."""
        for month in MONTH_NAMES:
            assert filter_cat(f"Articles from {month} 2020") is False
            assert filter_cat(f"Test from {month.lower()} 2021") is False

    def test_requires_year_in_pattern(self) -> None:
        """Should require a year after the month."""
        # Without year, should pass
        assert filter_cat("Articles from January") is True
        assert filter_cat("From March something") is True

    def test_case_insensitive_month_matching(self) -> None:
        """Should perform case-insensitive matching for months."""
        assert filter_cat("articles from JANUARY 2020") is False
        assert filter_cat("Articles from january 2020") is False


class TestFilterCatAllowedCategories:
    """Tests for categories that should pass the filter."""

    def test_allows_normal_categories(self) -> None:
        """Should allow normal category names."""
        assert filter_cat("History of Egypt") is True
        assert filter_cat("American writers") is True
        assert filter_cat("21st-century philosophers") is True

    def test_allows_categories_with_similar_terms(self) -> None:
        """Should allow categories with terms similar to blacklist but not exact."""
        assert filter_cat("Disambiguated topics") is True  # Not "Disambiguation"
        assert filter_cat("Wiki history") is True  # Not "WikiProject"

    def test_allows_empty_string(self) -> None:
        """Should handle empty string (returns True as not blocked)."""
        assert filter_cat("") is True

    def test_allows_categories_with_months_not_in_pattern(self) -> None:
        """Should allow categories mentioning months but not matching the pattern."""
        assert filter_cat("January events") is True
        assert filter_cat("March 2020") is True  # No "from" prefix
        assert filter_cat("In January") is True


class TestFilterCatEdgeCases:
    """Edge case tests for filter_cat."""

    def test_handles_category_prefix(self) -> None:
        """Should handle 'Category:' prefix correctly."""
        assert filter_cat("Category:History") is True
        assert filter_cat("Category:Wikipedia articles") is False

    def test_handles_mixed_case(self) -> None:
        """Should handle mixed case inputs."""
        assert filter_cat("test disambiguation test") is False
        assert filter_cat("Cleanup articles") is False

    def test_handles_whitespace(self) -> None:
        """Should handle categories with extra whitespace."""
        assert filter_cat("  Disambiguation  ") is False
        assert filter_cat("  History of Egypt  ") is True

    def test_handles_unicode_characters(self) -> None:
        """Should handle Unicode characters."""
        assert filter_cat("تاريخ مصر") is True
        assert filter_cat("Disambiguation تصنيف") is False

    def test_partial_matches_for_blacklist(self) -> None:
        """Should match blacklist terms even as substrings."""
        assert filter_cat("Test disambiguation test") is False
        assert filter_cat("Before sockpuppets after") is False


class TestFilterCatConstants:
    """Tests for module constants."""

    def test_category_blacklist_is_list(self) -> None:
        """CATEGORY_BLACKLIST should be a list."""
        assert isinstance(CATEGORY_BLACKLIST, list)
        assert len(CATEGORY_BLACKLIST) > 0

    def test_category_prefix_blacklist_is_list(self) -> None:
        """CATEGORY_PREFIX_BLACKLIST should be a list."""
        assert isinstance(CATEGORY_PREFIX_BLACKLIST, list)
        assert len(CATEGORY_PREFIX_BLACKLIST) > 0

    def test_month_names_is_list(self) -> None:
        """MONTH_NAMES should be a list of 12 months."""
        assert isinstance(MONTH_NAMES, list)
        assert len(MONTH_NAMES) == 12

    def test_month_names_contains_all_months(self) -> None:
        """MONTH_NAMES should contain all month names."""
        expected_months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        assert MONTH_NAMES == expected_months


class TestFilterCatRegressionTests:
    """Regression tests to prevent known issues."""

    def test_does_not_block_legitimate_use_cases(self) -> None:
        """Should not block legitimate categories that might contain similar words."""
        assert filter_cat("Uses of technology") is True
        assert filter_cat("Historical disambiguation") is True  # If it's in a valid context

    def test_consistent_behavior_with_repeated_calls(self) -> None:
        """Should return consistent results for the same input."""
        category = "History of Egypt"
        assert filter_cat(category) == filter_cat(category)
        assert filter_cat(category) == filter_cat(category)

    def test_handles_special_regex_characters(self) -> None:
        """Should handle categories with special regex characters."""
        assert filter_cat("Articles (test)") is True
        assert filter_cat("Items [test]") is True
        assert filter_cat("Test * category") is True