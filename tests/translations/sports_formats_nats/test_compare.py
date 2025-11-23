#!/usr/bin/python3
""" """

import pytest

from src.translations.sports_formats_nats.sport_lab_with_nat import (
    match_sports_labels_with_nat,
    match_sports_labels_with_nat_new,
)

data = {
    "british xoxo championships" : "بطولة المملكة المتحدة xoxo",
    "dominican republic national xoxo teams": "منتخبات xoxo وطنية جمهورية الدومينيكان",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
def test_2(key, expected) -> None:
    template_label1 = match_sports_labels_with_nat(key)
    template_label2 = match_sports_labels_with_nat_new(key)

    assert template_label1 != ""
    assert template_label1 == expected
    assert template_label1 == template_label2
