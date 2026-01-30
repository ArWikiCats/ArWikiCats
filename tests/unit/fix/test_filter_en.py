"""
Unit tests for the filter_en module.
"""

import pytest

from ArWikiCats.fix.filter_en import CATEGORY_BLACKLIST, CATEGORY_PREFIX_BLACKLIST, MONTH_NAMES, is_category_allowed


class TestFilterCatBlacklist:
    """Tests for is_category_allowed with blacklisted terms."""

    def test_blocks_disambiguation_categories(self) -> None:
        """Should block categories containing 'Disambiguation'."""
        # The blacklist contains "Disambiguation" which needs to match substring
        assert is_category_allowed("Test disambiguation test") is False
        assert is_category_allowed("disambiguation") is False
        assert is_category_allowed("DISAMBIGUATION") is False

    def test_blocks_wikiproject_categories(self) -> None:
        """Should block categories containing 'wikiproject'."""
        assert is_category_allowed("WikiProject Test") is False
        assert is_category_allowed("Test wikiproject page") is False

    def test_blocks_sockpuppets_categories(self) -> None:
        """Should block categories containing 'sockpuppets'."""
        assert is_category_allowed("Suspected sockpuppets") is False
        assert is_category_allowed("Sockpuppets of User") is False

    def test_blocks_without_source_categories(self) -> None:
        """Should block categories containing 'without a source'."""
        assert is_category_allowed("Articles without a source") is False

    def test_blocks_images_for_deletion(self) -> None:
        """Should block categories containing 'images for deletion'."""
        assert is_category_allowed("Images for deletion") is False

    def test_case_insensitive_blacklist_matching(self) -> None:
        """Should perform case-insensitive matching for blacklist."""
        assert is_category_allowed("test disambiguation test") is False
        assert is_category_allowed("test wikiproject test") is False
        assert is_category_allowed("test sockpuppets test") is False


class TestFilterCatPrefixBlacklist:
    """Tests for is_category_allowed with prefix blacklist."""

    def test_blocks_cleanup_prefix(self) -> None:
        """Should block categories starting with 'Clean-up' or 'Cleanup'."""
        assert is_category_allowed("Clean-up articles") is False
        assert is_category_allowed("Cleanup from 2020") is False

    def test_blocks_uncategorized_prefix(self) -> None:
        """Should block categories starting with 'Uncategorized'."""
        assert is_category_allowed("Uncategorized pages") is False

    def test_blocks_unreferenced_prefix(self) -> None:
        """Should block categories starting with 'Unreferenced'."""
        assert is_category_allowed("Unreferenced articles") is False

    def test_blocks_unverifiable_prefix(self) -> None:
        """Should block categories starting with 'Unverifiable'."""
        assert is_category_allowed("Unverifiable content") is False

    def test_blocks_unverified_prefix(self) -> None:
        """Should block categories starting with 'Unverified'."""
        assert is_category_allowed("Unverified claims") is False

    def test_blocks_wikipedia_prefix(self) -> None:
        """Should block categories starting with 'Wikipedia'."""
        assert is_category_allowed("Wikipedia articles") is False
        assert is_category_allowed("Wikipedia templates") is False

    def test_blocks_articles_about_prefix(self) -> None:
        """Should block categories starting with 'Articles about'."""
        assert is_category_allowed("Articles about living people") is False

    def test_blocks_articles_containing_prefix(self) -> None:
        """Should block categories starting with 'Articles containing'."""
        assert is_category_allowed("Articles containing Arabic text") is False

    def test_blocks_articles_needing_prefix(self) -> None:
        """Should block categories starting with 'Articles needing'."""
        assert is_category_allowed("Articles needing cleanup") is False

    def test_blocks_articles_with_prefix(self) -> None:
        """Should block categories starting with 'Articles with'."""
        assert is_category_allowed("Articles with unsourced statements") is False

    def test_blocks_use_prefix(self) -> None:
        """Should block categories starting with 'use '."""
        assert is_category_allowed("use dmy dates") is False
        assert is_category_allowed("Use American English") is False

    def test_blocks_user_pages_prefix(self) -> None:
        """Should block categories starting with 'User pages'."""
        assert is_category_allowed("User pages with test") is False

    def test_blocks_userspace_prefix(self) -> None:
        """Should block categories starting with 'Userspace'."""
        assert is_category_allowed("Userspace drafts") is False

    def test_case_insensitive_prefix_matching(self) -> None:
        """Should perform case-insensitive matching for prefixes."""
        assert is_category_allowed("CLEANUP ARTICLES") is False
        assert is_category_allowed("cleanup articles") is False
        assert is_category_allowed("Cleanup Articles") is False

    def test_strips_category_prefix_before_checking(self) -> None:
        """Should strip 'Category:' before checking prefixes."""
        assert is_category_allowed("Category:Wikipedia articles") is False
        assert is_category_allowed("Category:Cleanup pages") is False


class TestFilterCatMonthPatterns:
    """Tests for is_category_allowed with month-based date patterns."""

    def test_blocks_from_january_pattern(self) -> None:
        """Should block 'from January YYYY' patterns."""
        assert is_category_allowed("Articles from January 2020") is False
        assert is_category_allowed("Something from january 2021") is False

    def test_blocks_from_february_pattern(self) -> None:
        """Should block 'from February YYYY' patterns."""
        assert is_category_allowed("Articles from February 2020") is False

    def test_blocks_from_march_pattern(self) -> None:
        """Should block 'from March YYYY' patterns."""
        assert is_category_allowed("Articles from March 2019") is False

    def test_blocks_all_month_patterns(self) -> None:
        """Should block patterns for all months."""
        for month in MONTH_NAMES:
            assert is_category_allowed(f"Articles from {month} 2020") is False
            assert is_category_allowed(f"Test from {month.lower()} 2021") is False

    def test_requires_year_in_pattern(self) -> None:
        """Should require a year after the month."""
        # Without year, should pass
        assert is_category_allowed("Articles from January") is True
        assert is_category_allowed("From March something") is True

    def test_case_insensitive_month_matching(self) -> None:
        """Should perform case-insensitive matching for months."""
        assert is_category_allowed("articles from JANUARY 2020") is False
        assert is_category_allowed("Articles from january 2020") is False


class TestFilterCatAllowedCategories:
    """Tests for categories that should pass the filter."""

    def test_allows_normal_categories(self) -> None:
        """Should allow normal category names."""
        assert is_category_allowed("History of Egypt") is True
        assert is_category_allowed("American writers") is True
        assert is_category_allowed("21st-century philosophers") is True

    def test_allows_categories_with_similar_terms(self) -> None:
        """Should allow categories with terms similar to blacklist but not exact."""
        assert is_category_allowed("Disambiguated topics") is True  # Not "Disambiguation"
        assert is_category_allowed("Wiki history") is True  # Not "WikiProject"

    def test_allows_empty_string(self) -> None:
        """Should handle empty string (returns True as not blocked)."""
        assert is_category_allowed("") is True

    def test_allows_categories_with_months_not_in_pattern(self) -> None:
        """Should allow categories mentioning months but not matching the pattern."""
        assert is_category_allowed("January events") is True
        assert is_category_allowed("March 2020") is True  # No "from" prefix
        assert is_category_allowed("In January") is True


class TestFilterCatEdgeCases:
    """Edge case tests for is_category_allowed."""

    def test_handles_category_prefix(self) -> None:
        """Should handle 'Category:' prefix correctly."""
        assert is_category_allowed("Category:History") is True
        assert is_category_allowed("Category:Wikipedia articles") is False

    def test_handles_mixed_case(self) -> None:
        """Should handle mixed case inputs."""
        assert is_category_allowed("test disambiguation test") is False
        assert is_category_allowed("Cleanup articles") is False

    def test_handles_whitespace(self) -> None:
        """Should handle categories with extra whitespace."""
        assert is_category_allowed("  Disambiguation  ") is False
        assert is_category_allowed("  History of Egypt  ") is True

    def test_handles_unicode_characters(self) -> None:
        """Should handle Unicode characters."""
        assert is_category_allowed("تاريخ مصر") is True
        assert is_category_allowed("Disambiguation تصنيف") is False

    def test_partial_matches_for_blacklist(self) -> None:
        """Should match blacklist terms even as substrings."""
        assert is_category_allowed("Test disambiguation test") is False
        assert is_category_allowed("Before sockpuppets after") is False


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
        assert is_category_allowed("Uses of technology") is True
        assert is_category_allowed("Historical disambiguation") is False  # If it's in a valid context

    def test_consistent_behavior_with_repeated_calls(self) -> None:
        """Should return consistent results for the same input."""
        category = "History of Egypt"
        assert is_category_allowed(category) == is_category_allowed(category)
        assert is_category_allowed(category) == is_category_allowed(category)

    def test_handles_special_regex_characters(self) -> None:
        """Should handle categories with special regex characters."""
        assert is_category_allowed("Articles (test)") is True
        assert is_category_allowed("Items [test]") is True
        assert is_category_allowed("Test * category") is True


def test_is_category_allowed() -> None:
    # Test with allowed category
    result_allowed = is_category_allowed("Football players")
    assert result_allowed is True

    # "Disambiguation" in the list is checked against lowercased input, so it never matches
    result_disambig = is_category_allowed("Disambiguation")
    assert result_disambig is False

    # Test with another blacklisted prefix - this should work as it's a prefix check
    result_cleanup = is_category_allowed("Cleanup")
    assert result_cleanup is False

    # Test with Wikipedia prefix
    result_wikipedia = is_category_allowed("Wikipedia articles")
    assert result_wikipedia is False

    # Test with month pattern
    result_month = is_category_allowed("Category:Events from January 2020")
    assert result_month is False

    # Test with category: prefix
    result_category_prefix = is_category_allowed("category:Football")
    assert isinstance(result_category_prefix, bool)


@pytest.mark.parametrize(
    "cat",
    [
        # "Category:Some Disambiguation page",
        "sockpuppets investigation",
        "Category:Images for deletion requests",
        "Something without a source",
        "WikiProject Movies",
    ],
)
def test_is_category_allowed_blacklist(cat) -> None:
    """Should return False when any blacklist fragment exists in the category."""
    assert is_category_allowed(cat) is False


@pytest.mark.parametrize(
    "cat",
    [
        "Category:Cleanup articles",
        "Category:Uncategorized pages",
        "Wikipedia articles about something",
        "Articles lacking sources",
        "use x-template something",
        "User pages for bots",
        "Userspace sandbox",
    ],
)
def test_is_category_allowed_prefix_blacklist(cat) -> None:
    """Should return False when the category starts with a blocked prefix."""
    assert is_category_allowed(cat) is False


@pytest.mark.parametrize(
    "cat",
    [
        "Category:Events from January 2020",
        "Category:something from february 1999",
        "Category:history from march 5",
    ],
)
def test_is_category_allowed_blocked_month_patterns(cat) -> None:
    """Should return False when category ends with 'from <month> <year>'."""
    assert is_category_allowed(cat) is False


@pytest.mark.parametrize(
    "cat",
    [
        "Category:Football players",
        "Category:Cities in Yemen",
        "Category:Films of 2020",
        "My page without issues",
        "Something random",
    ],
)
def test_is_category_allowed_allowed(cat) -> None:
    """Should return True when the category does not match any blocked rule."""
    assert is_category_allowed(cat) is True
