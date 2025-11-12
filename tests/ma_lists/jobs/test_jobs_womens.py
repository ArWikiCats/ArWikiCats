"""Tests for the player and singer job datasets."""

from __future__ import annotations

from src.ma_lists.jobs.jobs_womens import (
    Jobs_key_womens,
    FEMALE_JOBS_TO,
    Female_Jobs,
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


def test_jobs_key_womens_mirrors_female_jobs() -> None:
    """Female job lookups should align with the lower-case key mapping."""

    assert Jobs_key_womens
    for key, label in Jobs_key_womens.items():
        assert key in Female_Jobs
        assert Female_Jobs[key] == label
