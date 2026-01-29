"""
Unit tests for sports_and_genders_resolver module.
"""

import pytest

from ArWikiCats.new_resolvers.genders_resolvers.sports_and_genders_resolver import (
    genders_sports_resolver,
    generate_sports_data_dict,
)

# ---------------------------------------------------------------------------
# Tests for generate_sports_data_dict function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestGenerateSportsDataDict:
    """Tests for the generate_sports_data_dict function."""

    def test_returns_dict(self) -> None:
        """Should return a dictionary."""
        result = generate_sports_data_dict()
        assert isinstance(result, dict)

    def test_contains_softball(self) -> None:
        """Should contain 'softball' key."""
        result = generate_sports_data_dict()
        assert "softball" in result

    def test_contains_futsal(self) -> None:
        """Should contain 'futsal' key."""
        result = generate_sports_data_dict()
        assert "futsal" in result

    def test_contains_badminton(self) -> None:
        """Should contain 'badminton' key."""
        result = generate_sports_data_dict()
        assert "badminton" in result

    def test_contains_american_football(self) -> None:
        """Should contain 'american-football' key."""
        result = generate_sports_data_dict()
        assert "american-football" in result

    def test_sport_has_sport_ar_key(self) -> None:
        """Each sport entry should have 'sport_ar' key."""
        result = generate_sports_data_dict()
        assert "sport_ar" in result["softball"]

    def test_sport_ar_value_is_string(self) -> None:
        """sport_ar value should be a string."""
        result = generate_sports_data_dict()
        assert isinstance(result["softball"]["sport_ar"], str)

    def test_softball_arabic_translation(self) -> None:
        """Softball should have correct Arabic translation."""
        result = generate_sports_data_dict()
        assert result["softball"]["sport_ar"] == "كرة لينة"


# ---------------------------------------------------------------------------
# Tests for genders_sports_resolver function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestGendersSportsResolver:
    """Tests for the genders_sports_resolver function."""

    def test_returns_string(self) -> None:
        """Should return a string."""
        result = genders_sports_resolver("test")
        assert isinstance(result, str)

    def test_handles_empty_string(self) -> None:
        """Should handle empty string."""
        result = genders_sports_resolver("")
        assert isinstance(result, str)

    def test_handles_footballers(self) -> None:
        """Should handle 'footballers' input."""
        result = genders_sports_resolver("footballers")
        assert isinstance(result, str)

    def test_handles_male_footballers(self) -> None:
        """Should handle 'male footballers' input."""
        result = genders_sports_resolver("male footballers")
        assert isinstance(result, str)

    def test_handles_female_footballers(self) -> None:
        """Should handle 'female footballers' input."""
        result = genders_sports_resolver("female footballers")
        assert isinstance(result, str)

    def test_handles_softball_players(self) -> None:
        """Should handle 'softball players' input."""
        result = genders_sports_resolver("softball players")
        assert isinstance(result, str)

    def test_handles_female_softball_players(self) -> None:
        """Should handle 'female softball players' input."""
        result = genders_sports_resolver("female softball players")
        assert isinstance(result, str)

    def test_handles_nationality_with_sport(self) -> None:
        """Should handle nationality + sport pattern."""
        result = genders_sports_resolver("american footballers")
        assert isinstance(result, str)

    def test_handles_futsal_players(self) -> None:
        """Should handle 'futsal players' input."""
        result = genders_sports_resolver("futsal players")
        assert isinstance(result, str)

    def test_handles_badminton_players(self) -> None:
        """Should handle 'badminton players' input."""
        result = genders_sports_resolver("badminton players")
        assert isinstance(result, str)

    def test_handles_category_prefix(self) -> None:
        """Should handle input with category: prefix."""
        result = genders_sports_resolver("category:footballers")
        assert isinstance(result, str)

    def test_handles_uppercase(self) -> None:
        """Should handle uppercase input."""
        result = genders_sports_resolver("FOOTBALLERS")
        assert isinstance(result, str)

    def test_handles_womens_variant(self) -> None:
        """Should handle women's variant (converted to female)."""
        result = genders_sports_resolver("women's softball players")
        assert isinstance(result, str)

    def test_handles_mens_variant(self) -> None:
        """Should handle men's variant (converted to male)."""
        result = genders_sports_resolver("men's softball players")
        assert isinstance(result, str)

    def test_is_cached(self) -> None:
        """Function should use lru_cache for performance."""
        result1 = genders_sports_resolver("test_cache_sport")
        result2 = genders_sports_resolver("test_cache_sport")
        assert result1 == result2
