#!/usr/bin/python3
""" """

import pytest

from ArWikiCats.translations.sports import games_labs


@pytest.mark.unit
def test_seasonal_labels_include_variants() -> None:
    labels = games_labs.SEASONAL_GAME_LABELS

    assert labels["olympic games"] == "الألعاب الأولمبية"
    assert labels["winter olympic games"] == "الألعاب الأولمبية الشتوية"
    assert labels["summer olympic games"] == "الألعاب الأولمبية الصيفية"
    assert labels["west olympic games"] == "الألعاب الأولمبية الغربية"
