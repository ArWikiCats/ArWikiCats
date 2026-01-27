#!/usr/bin/python3
"""Integration tests for format_multi_data"""

import pytest

from ArWikiCats.translations_formats import FormatDataV2


@pytest.fixture
def bot() -> FormatDataV2:
    nationality_data = {
        "egyptian": {
            "male": "مصري",
            "female": "مصرية",
            "males": "مصريون",
            "females": "مصريات",
        },
        "yemeni": {
            "male": "يمني",
            "female": "يمنية",
            "males": "يمنيون",
            "females": "يمنيات",
        },
        "Algerian": {
            "male": "جزائري",
            "female": "جزائرية",
            "males": "جزائريون",
            "females": "جزائريات",
        },
        "Moroccan": {
            "male": "مغربي",
            "female": "مغربية",
            "males": "مغاربة",
            "females": "مغربيات",
        },
    }

    formatted_data = {
        "{nat_en} writers": "كتاب {males}",  # كتاب يمنيون
        "{nat_en} descent": "أصل {male}",  # أصل يمني
        "{nat_en} women activists": "ناشطات {females}",  # ناشطات يمنيات
        "{nat_en} gods": "آلهة {female}",  # أصل يمني
    }

    # nationality_data_men = {x: v["males"] for x, v in nationality_data.items()}

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=nationality_data,
        key_placeholder="{nat_en}",
    )


test_match_key_data = {
    "Algerian writers": "كتاب جزائريون",
    "Moroccan descent": "أصل مغربي",
    "Algerian women activists": "ناشطات جزائريات",
    "egyptian gods": "آلهة مصرية",
}


@pytest.mark.parametrize("category, expected", test_match_key_data.items(), ids=test_match_key_data.keys())
@pytest.mark.fast
def test_standers(bot: FormatDataV2, category: str, expected: str) -> None:
    result = bot.search(category)
    assert result == expected


# Test for no matches
test_no_match_data = {
    "Unknown writers": "",
    "Random category": "",
    "French descent": "",
}


@pytest.mark.parametrize("category, expected", test_no_match_data.items(), ids=test_no_match_data.keys())
@pytest.mark.fast
def test_no_matches(bot: FormatDataV2, category: str, expected: str) -> None:
    result = bot.search(category)
    assert result == expected


# Test for text_before and text_after


@pytest.fixture
def bot_with_text_affixes() -> FormatDataV2:
    nationality_data = {
        "egyptian": {
            "male": "مصري",
            "males": "مصريون",
        },
    }

    formatted_data = {
        "{nat_en} writers": "كتاب {males}",
    }

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=nationality_data,
        key_placeholder="{nat_en}",
        text_before="of ",
        text_after=" origin",
    )


@pytest.mark.fast
def test_text_before_after(bot_with_text_affixes: FormatDataV2) -> None:
    # Test that text_before and text_after are properly handled during normalization
    key, normalized = bot_with_text_affixes.normalize_category_with_key("of egyptian origin writers")
    assert key == "egyptian"
    assert normalized == "{nat_en} writers"


# Test for overlapping keys
@pytest.fixture
def bot_with_overlapping_keys() -> FormatDataV2:
    nationality_data = {
        "South African": {
            "males": "جنوب إفريقيون",
        },
        "African": {
            "males": "إفريقيون",
        },
    }

    formatted_data = {
        "{nat_en} writers": "كتاب {males}",
    }

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=nationality_data,
        key_placeholder="{nat_en}",
    )


test_overlapping_keys_data = {
    "South African writers": "كتاب جنوب إفريقيون",
    "African writers": "كتاب إفريقيون",
}


@pytest.mark.parametrize(
    "category, expected", test_overlapping_keys_data.items(), ids=test_overlapping_keys_data.keys()
)
@pytest.mark.fast
def test_overlapping_keys(bot_with_overlapping_keys: FormatDataV2, category: str, expected: str) -> None:
    result = bot_with_overlapping_keys.search(category)
    assert result == expected


# Test for missing template
@pytest.fixture
def bot_with_missing_template() -> FormatDataV2:
    nationality_data = {
        "egyptian": {
            "males": "مصريون",
        },
    }

    formatted_data = {
        "{nat_en} writers": "كتاب {males}",
        # Missing template for "descent"
    }

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=nationality_data,
        key_placeholder="{nat_en}",
    )


@pytest.mark.fast
def test_missing_template(bot_with_missing_template: FormatDataV2) -> None:
    result = bot_with_missing_template.search("egyptian descent")
    assert result == ""
