"""
Unit tests for genders_resolvers utils module.
"""

import pytest

from ArWikiCats.new_resolvers.genders_resolvers.utils import (
    REGEX_MENS,
    REGEX_WOMENS,
    fix_keys,
)

# ---------------------------------------------------------------------------
# Tests for fix_keys function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestFixKeys:
    """Tests for the fix_keys function."""

    def test_lowercase_conversion(self) -> None:
        """Should convert input to lowercase."""
        result = fix_keys("AMERICAN FOOTBALL")
        assert "american" in result

    def test_removes_category_prefix(self) -> None:
        """Should remove 'category:' prefix."""
        result = fix_keys("category:test")
        assert "category:" not in result

    def test_removes_apostrophe(self) -> None:
        """Should remove apostrophes."""
        result = fix_keys("women's sports")
        assert "'" not in result

    def test_replaces_expatriates(self) -> None:
        """Should replace 'expatriates' with 'expatriate'."""
        result = fix_keys("american expatriates")
        assert "expatriate" in result
        assert "expatriates" not in result

    def test_replaces_canadian_football(self) -> None:
        """Should replace 'canadian football' with 'canadian-football'."""
        result = fix_keys("canadian football players")
        assert "canadian-football" in result

    def test_replaces_american_football(self) -> None:
        """Should replace 'american football' with 'american-football'."""
        result = fix_keys("american football players")
        assert "american-football" in result

    def test_replaces_womens_with_female(self) -> None:
        """Should replace 'women's' and 'women' with 'female'."""
        result = fix_keys("women's basketball")
        assert "female" in result
        assert "women" not in result

    def test_replaces_mens_with_male(self) -> None:
        """Should replace 'men's' and 'men' with 'male'."""
        result = fix_keys("men's basketball")
        assert "male" in result
        assert "men" not in result

    def test_strips_whitespace(self) -> None:
        """Should strip leading/trailing whitespace."""
        result = fix_keys("  test category  ")
        assert result == "test category"

    def test_empty_string(self) -> None:
        """Should handle empty string."""
        result = fix_keys("")
        assert result == ""


# ---------------------------------------------------------------------------
# Tests for regex patterns
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestRegexPatterns:
    """Tests for regex patterns."""

    def test_regex_womens_matches_womens(self) -> None:
        """REGEX_WOMENS should match 'womens'."""
        assert REGEX_WOMENS.search("womens basketball") is not None

    def test_regex_womens_matches_women(self) -> None:
        """REGEX_WOMENS should match 'women'."""
        assert REGEX_WOMENS.search("women basketball") is not None

    def test_regex_mens_matches_mens(self) -> None:
        """REGEX_MENS should match 'mens'."""
        assert REGEX_MENS.search("mens basketball") is not None

    def test_regex_mens_matches_men(self) -> None:
        """REGEX_MENS should match 'men'."""
        assert REGEX_MENS.search("men basketball") is not None

    def test_regex_womens_case_insensitive(self) -> None:
        """REGEX_WOMENS should be case insensitive."""
        assert REGEX_WOMENS.search("WOMEN basketball") is not None

    def test_regex_mens_case_insensitive(self) -> None:
        """REGEX_MENS should be case insensitive."""
        assert REGEX_MENS.search("MEN basketball") is not None
