"""Tests for the player and singer job datasets."""

from __future__ import annotations

from ArWikiCats.translations.jobs.jobs_womens import (
    short_womens_jobs,
)


def test_female_jobs_include_film_and_sport_variants() -> None:
    """Female-specific roles should include derived movie and sport categories."""

    assert "sportswomen" in short_womens_jobs
    assert "film actresses" in short_womens_jobs
    assert short_womens_jobs["sportswomen"] == "رياضيات"
    assert short_womens_jobs["film actresses"].startswith("ممثلات")
