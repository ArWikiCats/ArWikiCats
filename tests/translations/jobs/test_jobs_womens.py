"""Tests for the player and singer job datasets."""

from __future__ import annotations

from src.translations.jobs.jobs_womens import (
    FEMALE_JOBS_TO,
    Female_Jobs,
    short_womens_jobs,
)


def test_players_dataset_includes_core_sports_roles() -> None:
    """Key sports roles should provide both masculine and feminine labels."""

    assert "women's football players" in FEMALE_JOBS_TO
    assert FEMALE_JOBS_TO["women's football players"].startswith("لاعبات كرة قدم")


def test_female_jobs_include_film_and_sport_variants() -> None:
    """Female-specific roles should include derived movie and sport categories."""

    assert "sportswomen" in Female_Jobs
    assert "film actresses" in Female_Jobs
    assert Female_Jobs["sportswomen"] == "رياضيات"
    assert Female_Jobs["film actresses"].startswith("ممثلات")


def test_short_womens_jobs_mirrors_female_jobs() -> None:
    """Female job lookups should align with the lower-case key mapping."""

    assert short_womens_jobs
    for key, label in short_womens_jobs.items():
        assert key in Female_Jobs
        assert Female_Jobs[key] == label
