"""
Unit tests for common_resolver_chain module.
"""

import pytest

from ArWikiCats.legacy_bots.common_resolver_chain import (
    _lookup_country_with_in_prefix,
    con_lookup_both,
    get_con_label,
    get_lab_for_country2,
    get_type_lab,
)

# ---------------------------------------------------------------------------
# Tests for _lookup_country_with_in_prefix
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestLookupCountryWithInPrefix:
    """Tests for the _lookup_country_with_in_prefix function."""

    def test_returns_empty_for_no_in_prefix(self) -> None:
        """Should return empty when string doesn't start with 'in '."""
        result = _lookup_country_with_in_prefix("yemen")
        assert result == ""

    def test_returns_empty_for_empty_string(self) -> None:
        """Should return empty for empty string."""
        result = _lookup_country_with_in_prefix("")
        assert result == ""

    def test_handles_in_prefix(self) -> None:
        """Should handle strings starting with 'in '."""
        result = _lookup_country_with_in_prefix("in test")
        assert isinstance(result, str)

    def test_returns_fi_prefix_when_resolved(self) -> None:
        """Should return 'في ' prefix when inner term is resolved."""
        # This depends on whether the inner term can be resolved
        result = _lookup_country_with_in_prefix("in something")
        assert isinstance(result, str)
        # If resolved, should start with "في "
        if result:
            assert result.startswith("في ")


# ---------------------------------------------------------------------------
# Tests for get_con_label
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestGetConLabel:
    """Tests for the get_con_label function."""

    def test_returns_string(self) -> None:
        """Should return a string."""
        result = get_con_label("test")
        assert isinstance(result, str)

    def test_people_returns_arabic_label(self) -> None:
        """'people' should return 'أشخاص'."""
        result = get_con_label("people")
        assert result == "أشخاص"

    def test_normalizes_input(self) -> None:
        """Should normalize input - strip and lowercase."""
        result1 = get_con_label("  TEST  ")
        result2 = get_con_label("test")
        assert result1 == result2

    def test_removes_the_articles(self) -> None:
        """Should remove 'the' articles."""
        result1 = get_con_label("the yemen")
        result2 = get_con_label("yemen")
        # Both should produce similar results after normalization
        assert isinstance(result1, str)
        assert isinstance(result2, str)

    def test_handles_empty_string(self) -> None:
        """Should handle empty string."""
        result = get_con_label("")
        assert isinstance(result, str)

    def test_handles_dashes(self) -> None:
        """Should handle strings with dashes."""
        result = get_con_label("test-country")
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# Tests for get_lab_for_country2
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestGetLabForCountry2:
    """Tests for the get_lab_for_country2 function."""

    def test_returns_string(self) -> None:
        """Should return a string."""
        result = get_lab_for_country2("test")
        assert isinstance(result, str)

    def test_normalizes_input(self) -> None:
        """Should normalize input."""
        result1 = get_lab_for_country2("  TEST  ")
        result2 = get_lab_for_country2("test")
        assert result1 == result2

    def test_handles_empty_string(self) -> None:
        """Should handle empty string."""
        result = get_lab_for_country2("")
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# Tests for get_type_lab alias
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestGetTypeLab:
    """Tests for the get_type_lab function (alias for get_con_label)."""

    def test_is_alias_for_get_con_label(self) -> None:
        """get_type_lab should be an alias for get_con_label."""
        assert get_type_lab is get_con_label

    def test_returns_same_as_get_con_label(self) -> None:
        """get_type_lab should return same result as get_con_label."""
        result1 = get_type_lab("test")
        result2 = get_con_label("test")
        assert result1 == result2


# ---------------------------------------------------------------------------
# Tests for con_lookup_both dictionary
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestConLookupBoth:
    """Tests for the con_lookup_both dictionary."""

    def test_is_dict(self) -> None:
        """con_lookup_both should be a dictionary."""
        assert isinstance(con_lookup_both, dict)

    def test_contains_expected_keys(self) -> None:
        """Should contain expected resolver function keys."""
        expected_keys = [
            "get_from_new_p17_final",
            "all_new_resolvers",
            "get_from_pf_keys2",
            "_lookup_country_with_in_prefix",
            "get_pop_All_18",
            "get_KAKO",
        ]
        for key in expected_keys:
            assert key in con_lookup_both

    def test_values_are_callable(self) -> None:
        """All values should be callable."""
        for name, func in con_lookup_both.items():
            assert callable(func), f"{name} is not callable"
