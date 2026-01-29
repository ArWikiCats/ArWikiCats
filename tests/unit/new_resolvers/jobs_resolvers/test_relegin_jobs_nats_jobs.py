"""
Unit tests for relegin_jobs_nats_jobs module.
"""

import pytest

from ArWikiCats.new_resolvers.jobs_resolvers.relegin_jobs_nats_jobs import (
    PAINTER_ROLE_LABELS,
    resolve_nats_jobs,
)

# ---------------------------------------------------------------------------
# Tests for PAINTER_ROLE_LABELS constant
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestPainterRoleLabels:
    """Tests for the PAINTER_ROLE_LABELS constant."""

    def test_is_dict(self) -> None:
        """Should be a dictionary."""
        assert isinstance(PAINTER_ROLE_LABELS, dict)

    def test_contains_painters(self) -> None:
        """Should contain 'painters' key."""
        assert "painters" in PAINTER_ROLE_LABELS

    def test_contains_artists(self) -> None:
        """Should contain 'artists' key."""
        assert "artists" in PAINTER_ROLE_LABELS

    def test_painters_has_males_and_females(self) -> None:
        """painters should have males and females keys."""
        assert "males" in PAINTER_ROLE_LABELS["painters"]
        assert "females" in PAINTER_ROLE_LABELS["painters"]

    def test_artists_has_males_and_females(self) -> None:
        """artists should have males and females keys."""
        assert "males" in PAINTER_ROLE_LABELS["artists"]
        assert "females" in PAINTER_ROLE_LABELS["artists"]


# ---------------------------------------------------------------------------
# Tests for resolve_nats_jobs function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestResolveNatsJobs:
    """Tests for the resolve_nats_jobs function."""

    def test_returns_string(self) -> None:
        """Should return a string."""
        result = resolve_nats_jobs("test")
        assert isinstance(result, str)

    def test_handles_empty_string(self) -> None:
        """Should handle empty string."""
        result = resolve_nats_jobs("")
        assert isinstance(result, str)

    def test_handles_lowercase_input(self) -> None:
        """Should handle lowercase input."""
        result = resolve_nats_jobs("christians")
        assert isinstance(result, str)

    def test_handles_uppercase_input(self) -> None:
        """Should handle uppercase input."""
        result = resolve_nats_jobs("CHRISTIANS")
        assert isinstance(result, str)

    def test_handles_mixed_case_input(self) -> None:
        """Should handle mixed case input."""
        result = resolve_nats_jobs("Christians")
        assert isinstance(result, str)

    def test_handles_female_prefix(self) -> None:
        """Should handle female prefix."""
        result = resolve_nats_jobs("female christians")
        assert isinstance(result, str)

    def test_handles_womens_prefix(self) -> None:
        """Should handle women's prefix."""
        result = resolve_nats_jobs("women's christians")
        assert isinstance(result, str)

    def test_handles_nationality_with_religion(self) -> None:
        """Should handle nationality + religion pattern."""
        result = resolve_nats_jobs("yemeni christians")
        assert isinstance(result, str)

    def test_handles_painters(self) -> None:
        """Should handle painters input."""
        result = resolve_nats_jobs("painters")
        assert isinstance(result, str)

    def test_handles_artists(self) -> None:
        """Should handle artists input."""
        result = resolve_nats_jobs("artists")
        assert isinstance(result, str)

    def test_strips_whitespace(self) -> None:
        """Should strip leading/trailing whitespace."""
        result1 = resolve_nats_jobs("  christians  ")
        result2 = resolve_nats_jobs("christians")
        # Both should produce same result after normalization
        assert result1 == result2

    def test_returns_empty_for_unknown(self) -> None:
        """Should return empty string for unknown patterns."""
        result = resolve_nats_jobs("unknown_pattern_xyz_123")
        assert result == ""
