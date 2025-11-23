#!/usr/bin/python3
""" """

import pytest

from src.translations.sports_formats_nats.new import create_label
from src.translations.sports_formats_nats.sport_lab_with_nat import (
    Get_New_team_xo_with_nat,
)
from src.translations.utils.match_sport_keys import match_sport_key

data = {
    "german figure skating championships": "بطولة ألمانيا للتزلج الفني",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
def test_compare_create_label(key, expected) -> None:
    sport_key = match_sport_key(key)
    template_label1 = Get_New_team_xo_with_nat(key, sport_key)
    template_label2 = create_label(key)

    assert template_label1 != ""
    assert template_label1 == expected
    assert template_label1 == template_label2
