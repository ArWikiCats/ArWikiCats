#!/usr/bin/python3
"""Integration tests for format_multi_data"""

import pytest

from ArWikiCats.translations_formats import FormatDataV2, MultiDataFormatterBaseV2


@pytest.fixture
def multi_bot() -> MultiDataFormatterBaseV2:
    nationality_data = {
        "Afghan": {"male": "أفغاني", "males": "أفغان"},
        "yemeni": {"male": "يمني", "males": "يمنيون"},
        "british": {"male": "بريطاني", "males": "بريطانيون"},
        "american": {"male": "أمريكي", "males": "أمريكيون"},
        "egyptian": {"male": "مصري", "males": "مصريون"},
        "Algerian": {"male": "جزائري", "males": "جزائريون"},
        "Moroccan": {"male": "مغربي", "males": "مغاربة"},
    }

    formatted_data = {
        "{nat1_en} people": "{nat1_men}",  # أمريكيون أفغان
        "{nat1_en} people of jewish descent": "{nat1_men} من أصل يهودي",  # أمريكيون من أصل يهودي
        "{nat1_en} {nat2_en}": "{nat1_men} {nat2_men}",  # أمريكيون أفغان
        "{nat2_en} {nat1_en}": "{nat2_men} {nat1_men}",  # أفغان أمريكيون
        "{nat1_en} people of {nat2_en} descent": "{nat1_men} من أصل {nat2_man}",  # أفغان من أصل أمريكي
        "{nat1_en} people of {nat2_en} jewish descent": "{nat1_men} من أصل يهودي {nat2_man}",
        "{nat1_en} people of {nat2_en}-jewish descent": "{nat1_men} من أصل يهودي {nat2_man}",
    }

    nationality_data_1 = {x: {"nat1_man": v["male"], "nat1_men": v["males"]} for x, v in nationality_data.items()}
    nationality_data_2 = {x: {"nat2_man": v["male"], "nat2_men": v["males"]} for x, v in nationality_data.items()}

    country_bot = FormatDataV2(
        formatted_data=formatted_data,
        data_list=nationality_data_1,
        key_placeholder="{nat1_en}",
    )

    other_bot = FormatDataV2(
        {},
        nationality_data_2,
        key_placeholder="{nat2_en}",
    )

    return MultiDataFormatterBaseV2(
        country_bot=country_bot,
        other_bot=other_bot,
    )


test_first_data = {
    "Afghan people": "أفغان",
    "Algerian people of Jewish descent": "جزائريون من أصل يهودي",
}


@pytest.mark.parametrize("category, expected", test_first_data.items(), ids=test_first_data.keys())
@pytest.mark.fast
def test_first_bot(multi_bot: MultiDataFormatterBaseV2, category: str, expected: str) -> None:
    result = multi_bot.country_bot.search(category)
    assert result == expected


test_match_key_data = {
    "Afghan American": "أفغان أمريكيون",
    "Afghan people of American descent": "أفغان من أصل أمريكي",
    "American people of Afghan descent": "أمريكيون من أصل أفغاني",
    "Algerian people of Moroccan Jewish descent": "جزائريون من أصل يهودي مغربي",
    "Algerian people of Moroccan-Jewish descent": "جزائريون من أصل يهودي مغربي",
}


@pytest.mark.parametrize("category, expected", test_match_key_data.items(), ids=test_match_key_data.keys())
@pytest.mark.fast
def test_standers(multi_bot: MultiDataFormatterBaseV2, category: str, expected: str) -> None:
    result = multi_bot.search_all(category)
    assert result == expected
