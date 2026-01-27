"""Tests for the player and singer job datasets."""

from __future__ import annotations

from ArWikiCats.translations.jobs.jobs_players_list import (
    FOOTBALL_KEYS_PLAYERS,
    PLAYERS_TO_MEN_WOMENS_JOBS,
)


def test_players_dataset_includes_core_sports_roles() -> None:
    """Key sports roles should provide both masculine and feminine labels."""

    football_labels = PLAYERS_TO_MEN_WOMENS_JOBS["footballers"]
    assert football_labels["males"] == "لاعبو كرة قدم"
    assert football_labels["females"] == "لاعبات كرة قدم"


def test_football_key_players_are_registered() -> None:
    """The football helper dictionary should include standard team keys."""

    assert "wide receivers" in FOOTBALL_KEYS_PLAYERS
    assert FOOTBALL_KEYS_PLAYERS["wide receivers"]["males"]
