"""Tests for the player and singer job datasets."""

from __future__ import annotations

from src.ma_lists.jobs.jobs_players_list import (
    FEMALE_JOBS_TO,
    FOOTBALL_KEYS_PLAYERS,
    PLAYERS_TO_MEN_WOMENS_JOBS,
)
from src.ma_lists.jobs.jobs_singers import Men_Womens_Singers


def test_players_dataset_includes_core_sports_roles() -> None:
    """Key sports roles should provide both masculine and feminine labels."""

    football_labels = PLAYERS_TO_MEN_WOMENS_JOBS["footballers"]
    assert football_labels["mens"] == "لاعبو كرة قدم"
    assert football_labels["womens"] == "لاعبات كرة قدم"

    assert "women's football players" in FEMALE_JOBS_TO
    assert FEMALE_JOBS_TO["women's football players"].startswith("لاعبات كرة قدم")


def test_football_key_players_are_registered() -> None:
    """The football helper dictionary should include standard team keys."""

    assert "wide receivers" in FOOTBALL_KEYS_PLAYERS
    assert FOOTBALL_KEYS_PLAYERS["wide receivers"]["mens"]


def test_singer_dataset_contains_common_genres() -> None:
    """Singer datasets should expose popular genre categories."""

    assert "pop singers" in Men_Womens_Singers
    labels = Men_Womens_Singers["pop singers"]
    assert labels["mens"].startswith("مغنو")
    assert labels["womens"].startswith("مغنيات")
