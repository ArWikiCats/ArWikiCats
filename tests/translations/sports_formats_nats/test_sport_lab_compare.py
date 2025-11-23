#!/usr/bin/python3
""" """

import pytest

from src.translations.sports_formats_nats.new import create_label
from src.translations.sports_formats_teams.sport_lab2 import wrap_team_xo_normal_2025


data = {
    "british softball championshipszz": "بطولة المملكة المتحدة للكرة اللينة",
    "ladies british softball tour": "بطولة المملكة المتحدة للكرة اللينة للسيدات",
    "british football tour": "بطولة المملكة المتحدة لكرة القدم",
    "Yemeni football championships": "بطولة اليمن لكرة القدم",
    "german figure skating championships": "بطولة ألمانيا للتزلج الفني",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
@pytest.mark.skip2
def test_compare_x(key, expected) -> None:
    label1 = wrap_team_xo_normal_2025(key)
    label2 = create_label(key)
    assert label1 != ""
    assert label1 == expected == label2
