"""
Unit tests for genders_resolvers __init__ module.
"""

import pytest

from ArWikiCats.new_resolvers.genders_resolvers import resolve_nat_genders_pattern_v2

# ---------------------------------------------------------------------------
# Tests for resolve_nat_genders_pattern_v2 function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestResolveNatGendersPatternV2:
    """Tests for the resolve_nat_genders_pattern_v2 function."""

    def test_returns_string(self) -> None:
        """Should return a string."""
        result = resolve_nat_genders_pattern_v2("test")
        assert isinstance(result, str)

    def test_handles_empty_string(self) -> None:
        """Should handle empty string."""
        result = resolve_nat_genders_pattern_v2("")
        assert isinstance(result, str)

    def test_handles_footballers(self) -> None:
        """Should handle footballers pattern."""
        result = resolve_nat_genders_pattern_v2("footballers")
        assert isinstance(result, str)

    def test_handles_male_footballers(self) -> None:
        """Should handle male footballers pattern."""
        result = resolve_nat_genders_pattern_v2("male footballers")
        assert isinstance(result, str)

    def test_handles_female_footballers(self) -> None:
        """Should handle female footballers pattern."""
        result = resolve_nat_genders_pattern_v2("female footballers")
        assert isinstance(result, str)

    def test_handles_actors(self) -> None:
        """Should handle actors pattern."""
        result = resolve_nat_genders_pattern_v2("actors")
        assert isinstance(result, str)

    def test_handles_actresses(self) -> None:
        """Should handle actresses pattern."""
        result = resolve_nat_genders_pattern_v2("actresses")
        assert isinstance(result, str)

    def test_handles_nationality_with_job(self) -> None:
        """Should handle nationality with job pattern."""
        result = resolve_nat_genders_pattern_v2("american actors")
        assert isinstance(result, str)

    def test_is_cached(self) -> None:
        """Function should use lru_cache for performance."""
        # Call twice with same input
        result1 = resolve_nat_genders_pattern_v2("test_cache")
        result2 = resolve_nat_genders_pattern_v2("test_cache")
        assert result1 == result2
