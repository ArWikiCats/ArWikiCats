#!/usr/bin/python3
"""Integration tests"""


import pytest

from ArWikiCats.translations_formats import FormatData


@pytest.fixture
def yc_bot() -> FormatData:
    formatted_data = {
        "{nat_en} actors": "ممثلون {nat_ar}",
        "{nat_en} people actors": "أعلام ممثلون {nat_ar}",
    }
    return FormatData(
        formatted_data=formatted_data,
        data_list={"yemeni": "يمنيون"},
        key_placeholder="{nat_en}",
        value_placeholder="{nat_ar}",
        text_before="the ",
        text_after=" people",
    )


def test_with_text_after(yc_bot: FormatData) -> None:
    """Test FormatData with text_after parameter."""
    category = "yemeni people actors"
    result = yc_bot.create_label(category)

    assert result == "أعلام ممثلون يمنيون"


def test_with_text_before(yc_bot: FormatData) -> None:
    """Test FormatData with text_before parameter."""
    category = "the yemeni actors"
    result = yc_bot.create_label(category)

    assert result == "ممثلون يمنيون"


def test_new_after_key() -> None:
    """Test FormatData with text_after parameter."""
    formatted_data = {
        "{nat_en} actors": "ممثلون {nat_ar}",
    }

    bot = FormatData(
        formatted_data=formatted_data,
        data_list={"yemeni": "يمنيون"},
        key_placeholder="{nat_en}",
        value_placeholder="{nat_ar}",
        text_before="the ",
        text_after=" people",
    )

    category = "yemeni people actors"
    result = bot.create_label(category)

    assert result == "ممثلون يمنيون"


def test_new_before_key() -> None:
    """Test FormatData with text_after parameter."""
    formatted_data = {
        "the {nat_en} actors": "ممثلون {nat_ar}",
    }

    bot = FormatData(
        formatted_data=formatted_data,
        data_list={"yemeni": "يمنيون"},
        key_placeholder="{nat_en}",
        value_placeholder="{nat_ar}",
        text_before="the ",  # dosn't matter here because "the {nat_en} actors" is in formatted_data
        text_after=" people",
    )

    category = "the yemeni actors"
    result = bot.create_label(category)

    assert result == "ممثلون يمنيون"
