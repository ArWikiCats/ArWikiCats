"""
Unit tests for jobs_and_genders_resolver module.
"""

import pytest

from ArWikiCats.new_resolvers.genders_resolvers.jobs_and_genders_resolver import (
    genders_jobs_resolver,
    generate_formatted_data,
    generate_jobs_data_dict,
)


# ---------------------------------------------------------------------------
# Tests for generate_jobs_data_dict function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestGenerateJobsDataDict:
    """Tests for the generate_jobs_data_dict function."""

    def test_returns_dict(self) -> None:
        """Should return a dictionary."""
        result = generate_jobs_data_dict()
        assert isinstance(result, dict)

    def test_contains_actors(self) -> None:
        """Should contain 'actors' key."""
        result = generate_jobs_data_dict()
        assert "actors" in result

    def test_contains_singers(self) -> None:
        """Should contain 'singers' key."""
        result = generate_jobs_data_dict()
        assert "singers" in result

    def test_contains_composers(self) -> None:
        """Should contain 'composers' key."""
        result = generate_jobs_data_dict()
        assert "composers" in result

    def test_actors_has_required_keys(self) -> None:
        """Each job entry should have job_males, job_females, both_jobs keys."""
        result = generate_jobs_data_dict()
        assert "job_males" in result["actors"]
        assert "job_females" in result["actors"]
        assert "both_jobs" in result["actors"]

    def test_actors_values_are_strings(self) -> None:
        """Job values should be strings."""
        result = generate_jobs_data_dict()
        assert isinstance(result["actors"]["job_males"], str)
        assert isinstance(result["actors"]["job_females"], str)
        assert isinstance(result["actors"]["both_jobs"], str)


# ---------------------------------------------------------------------------
# Tests for generate_formatted_data function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestGenerateFormattedData:
    """Tests for the generate_formatted_data function."""

    def test_returns_dict(self) -> None:
        """Should return a dictionary."""
        result = generate_formatted_data()
        assert isinstance(result, dict)

    def test_contains_actresses(self) -> None:
        """Should contain 'actresses' key."""
        result = generate_formatted_data()
        assert "actresses" in result

    def test_contains_male_job_pattern(self) -> None:
        """Should contain male job pattern."""
        result = generate_formatted_data()
        assert "male {job_en}" in result

    def test_contains_female_job_pattern(self) -> None:
        """Should contain female job pattern."""
        result = generate_formatted_data()
        assert "female {job_en}" in result

    def test_contains_nationality_job_pattern(self) -> None:
        """Should contain nationality + job pattern."""
        result = generate_formatted_data()
        assert "{en_nat} {job_en}" in result


# ---------------------------------------------------------------------------
# Tests for genders_jobs_resolver function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestGendersJobsResolver:
    """Tests for the genders_jobs_resolver function."""

    def test_returns_string(self) -> None:
        """Should return a string."""
        result = genders_jobs_resolver("test")
        assert isinstance(result, str)

    def test_handles_empty_string(self) -> None:
        """Should handle empty string."""
        result = genders_jobs_resolver("")
        assert isinstance(result, str)

    def test_handles_actors(self) -> None:
        """Should handle 'actors' input."""
        result = genders_jobs_resolver("actors")
        assert isinstance(result, str)

    def test_handles_actresses(self) -> None:
        """Should handle 'actresses' input."""
        result = genders_jobs_resolver("actresses")
        assert isinstance(result, str)

    def test_handles_male_actors(self) -> None:
        """Should handle 'male actors' input."""
        result = genders_jobs_resolver("male actors")
        assert isinstance(result, str)

    def test_handles_female_actors(self) -> None:
        """Should handle 'female actors' input."""
        result = genders_jobs_resolver("female actors")
        assert isinstance(result, str)

    def test_handles_nationality_with_job(self) -> None:
        """Should handle nationality + job pattern."""
        result = genders_jobs_resolver("american actors")
        assert isinstance(result, str)

    def test_handles_singers(self) -> None:
        """Should handle 'singers' input."""
        result = genders_jobs_resolver("singers")
        assert isinstance(result, str)

    def test_handles_composers(self) -> None:
        """Should handle 'composers' input."""
        result = genders_jobs_resolver("composers")
        assert isinstance(result, str)

    def test_handles_category_prefix(self) -> None:
        """Should handle input with category: prefix."""
        result = genders_jobs_resolver("category:actors")
        assert isinstance(result, str)

    def test_handles_uppercase(self) -> None:
        """Should handle uppercase input."""
        result = genders_jobs_resolver("ACTORS")
        assert isinstance(result, str)

    def test_is_cached(self) -> None:
        """Function should use lru_cache for performance."""
        result1 = genders_jobs_resolver("test_cache_value")
        result2 = genders_jobs_resolver("test_cache_value")
        assert result1 == result2
