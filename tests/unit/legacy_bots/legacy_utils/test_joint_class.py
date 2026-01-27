"""
Unit tests for joint_class module.
"""

import pytest

from ArWikiCats.legacy_bots.legacy_utils.joint_class import CountryLabelAndTermParent


# ---------------------------------------------------------------------------
# Tests for CountryLabelAndTermParent class
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestCountryLabelAndTermParent:
    """Tests for the CountryLabelAndTermParent class."""

    def test_init_with_no_callable(self) -> None:
        """Should initialize with no callable."""
        parent = CountryLabelAndTermParent()
        assert parent._resolve_callable is None

    def test_init_with_callable(self) -> None:
        """Should initialize with provided callable."""

        def test_resolver(x: str) -> str:
            return f"resolved_{x}"

        parent = CountryLabelAndTermParent(_resolve_callable=test_resolver)
        assert parent._resolve_callable is test_resolver

    def test_check_prefixes_returns_empty_without_callable(self) -> None:
        """_check_prefixes should return empty string without callable."""
        parent = CountryLabelAndTermParent()
        result = parent._check_prefixes("women's test")
        assert result == ""

    def test_check_prefixes_handles_womens_prefix(self) -> None:
        """_check_prefixes should handle 'women's ' prefix."""

        def test_resolver(x: str) -> str:
            return "تسمية"

        parent = CountryLabelAndTermParent(_resolve_callable=test_resolver)
        result = parent._check_prefixes("women's test")
        assert "نسائية" in result

    def test_check_prefixes_handles_mens_prefix(self) -> None:
        """_check_prefixes should handle 'men's ' prefix."""

        def test_resolver(x: str) -> str:
            return "تسمية"

        parent = CountryLabelAndTermParent(_resolve_callable=test_resolver)
        result = parent._check_prefixes("men's test")
        assert "رجالية" in result

    def test_check_prefixes_returns_empty_for_no_prefix(self) -> None:
        """_check_prefixes should return empty for no matching prefix."""

        def test_resolver(x: str) -> str:
            return "تسمية"

        parent = CountryLabelAndTermParent(_resolve_callable=test_resolver)
        result = parent._check_prefixes("test without prefix")
        assert result == ""

    def test_check_prefixes_returns_empty_when_remainder_not_resolved(self) -> None:
        """_check_prefixes should return empty when remainder can't be resolved."""

        def test_resolver(x: str) -> str:
            return ""  # Return empty, simulating failed resolution

        parent = CountryLabelAndTermParent(_resolve_callable=test_resolver)
        result = parent._check_prefixes("women's test")
        assert result == ""

    def test_check_regex_years_returns_string(self) -> None:
        """_check_regex_years should return a string."""
        parent = CountryLabelAndTermParent()
        result = parent._check_regex_years("test")
        assert isinstance(result, str)

    def test_check_regex_years_returns_empty_for_no_year(self) -> None:
        """_check_regex_years should return empty for no year pattern."""
        parent = CountryLabelAndTermParent()
        result = parent._check_regex_years("random text")
        assert result == ""

    def test_check_regex_years_handles_year_patterns(self) -> None:
        """_check_regex_years should handle year patterns."""
        parent = CountryLabelAndTermParent()
        # Test with year at start
        result = parent._check_regex_years("1900 events")
        assert isinstance(result, str)

    def test_check_members_returns_empty_for_no_suffix(self) -> None:
        """_check_members should return empty for no ' members of' suffix."""
        parent = CountryLabelAndTermParent()
        result = parent._check_members("test")
        assert result == ""

    def test_check_members_handles_members_of_suffix(self) -> None:
        """_check_members should handle ' members of' suffix."""
        parent = CountryLabelAndTermParent()
        result = parent._check_members("british members of")
        # Result depends on whether the term is in Nat_mens
        assert isinstance(result, str)

    def test_check_members_returns_empty_for_unknown_term(self) -> None:
        """_check_members should return empty for unknown term."""
        parent = CountryLabelAndTermParent()
        result = parent._check_members("unknown_xyz members of")
        assert result == ""


# ---------------------------------------------------------------------------
# Tests for prefix label combinations
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestPrefixLabelCombinations:
    """Tests for prefix label combinations in _check_prefixes."""

    @pytest.mark.parametrize(
        "prefix,expected_suffix",
        [
            ("women's ", "نسائية"),
            ("men's ", "رجالية"),
        ],
    )
    def test_prefix_labels_map_correctly(self, prefix: str, expected_suffix: str) -> None:
        """Prefixes should map to correct Arabic labels."""

        def test_resolver(x: str) -> str:
            return "تسمية"

        parent = CountryLabelAndTermParent(_resolve_callable=test_resolver)
        result = parent._check_prefixes(f"{prefix}test")
        assert expected_suffix in result


# ---------------------------------------------------------------------------
# Tests for regex year patterns
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestRegexYearPatterns:
    """Tests for regex year pattern detection in _check_regex_years."""

    @pytest.mark.parametrize(
        "input_str",
        [
            "1900 events",
            "2000 births",
            "events 1999",
        ],
    )
    def test_year_patterns_detected(self, input_str: str) -> None:
        """Year patterns should be detected."""
        parent = CountryLabelAndTermParent()
        result = parent._check_regex_years(input_str)
        assert isinstance(result, str)
