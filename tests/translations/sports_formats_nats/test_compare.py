#!/usr/bin/python3
""" """

from _collections_abc import dict_items
import pytest

from src.translations.sports_formats_nats.sport_lab_with_nat import (
    match_sports_labels_with_nat,
)

from src.translations.sports_formats_nats.new import create_label

data = {
    "british xoxo championships" : "بطولة المملكة المتحدة xoxo",
    "dominican republic national xoxo teams": "منتخبات xoxo وطنية جمهورية الدومينيكان",
    "Yemeni national xoxo teams": "منتخبات xoxo وطنية اليمن",
}


@pytest.mark.parametrize("key,expected", data.items(), ids=data.keys())
def test_2(key: dict_items[str, str], expected) -> None:
    template_label1 = match_sports_labels_with_nat(key)
    template_label2 = create_label(key)

    assert template_label1 != ""
    assert template_label1 == expected
    assert template_label1 == template_label2
