#!/usr/bin/python3
""" """

import pytest

from src.translations.sports_formats_nats.sport_lab_with_nat import (
    compare_to_create_label,
)

from src.translations.sports_formats_nats.new import create_label

data = {
    "british football championships" : "بطولة المملكة المتحدة لكرة القدم",
    "dominican republic national football teams": "منتخبات كرة قدم وطنية جمهورية الدومينيكان",
    "Yemeni national football teams": "منتخبات كرة قدم وطنية اليمن",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
@pytest.mark.skip2
def test_2(key, expected) -> None:
    template_label1 = compare_to_create_label(key)
    template_label2 = create_label(key)

    assert template_label1 != ""
    assert template_label2 != ""

    assert template_label1 == expected == template_label2
