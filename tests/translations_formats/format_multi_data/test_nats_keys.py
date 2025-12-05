#!/usr/bin/python3
"""Integration tests for format_multi_data  """

import pytest

from ArWikiCats.translations_formats import FormatData
from ArWikiCats.translations_formats.DataModel.model_multi_data import MultiDataFormatterBase

nationality_data = {
    "Afghan": {"man": "أفغاني", "mens": "أفغان"},
    "yemeni": {"man": "يمني", "mens": "يمنيون"},
    "british": {"man": "بريطاني", "mens": "بريطانيون"},
    "american": {"man": "أمريكي", "mens": "أمريكيون"},
    "egyptian": {"man": "مصري", "mens": "مصريون"},
    "Algerian": {"man": "جزائري", "mens": "جزائريون"},
    "Moroccan": {"man": "مغربي", "mens": "مغاربة"},
}

formatted_data = {
    "{nat1_en} {nat2_en}": "{nat1_men} {nat2_man}",
    "{nat1_en} people": "{nat1_men}",
    "{nat1_en} people of {nat2_en} descent": "{nat1_men} من أصل {nat2_man}",
    "{nat1_en} people of {nat2_en} jewish descent": "{nat1_men} من أصل يهودي {nat2_man}",
}

nationality_data_men = {x: v["mens"] for x, v in nationality_data.items()}
nationality_data_man = {x: v["man"] for x, v in nationality_data.items()}


@pytest.fixture
def multi_bot() -> MultiDataFormatterBase:
    # Country bot (FormatData)
    country_bot = FormatData(
        formatted_data=formatted_data,
        data_list=nationality_data_men,
        key_placeholder="{nat1_en}",
        value_placeholder="{nat1_men}",
    )

    other_bot = FormatData(
        {},  # to use from search_all
        nationality_data_man,
        key_placeholder="{nat2_en}",
        value_placeholder="{nat2_man}",
    )

    return MultiDataFormatterBase(
        country_bot=country_bot,
        other_bot=other_bot,
    )


test_match_key_data = {
    "Afghan people": "أفغان",
    "Afghan people of American descent": "أفغان من أصل أمريكي",
    "American people of Afghan descent": "أمريكيون من أصل أفغاني",
    "Algerian people of Moroccan Jewish descent": "جزائريون من أصل يهودي مغربي",
}


@pytest.mark.parametrize("category, expected", test_match_key_data.items(), ids=list(test_match_key_data.keys()))
@pytest.mark.fast
def test_standers(multi_bot: MultiDataFormatterBase, category: str, expected: str) -> None:
    result = multi_bot.search_all(category)
    assert result == expected
