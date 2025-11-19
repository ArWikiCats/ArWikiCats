#!/usr/bin/python3
""" """
import pytest
from src.translations.sports_formats_teams.sport_lab import Get_New_team_xo
from src.translations.sports_formats_nats.new import create_label


@pytest.mark.fast
def test_create_label() -> None:
    label = create_label("Yemeni football championships")
    assert label == "بطولة اليمن لكرة القدم"


@pytest.mark.fast
def test_Get_New_team_xo() -> None:
    label = Get_New_team_xo("Yemeni football championships")
    assert label == "بطولة اليمن لكرة القدم"


@pytest.mark.fast
def test_compare() -> None:
    label = create_label("Yemeni football championships")
    label2 = Get_New_team_xo("Yemeni football championships")
    assert label == label2
