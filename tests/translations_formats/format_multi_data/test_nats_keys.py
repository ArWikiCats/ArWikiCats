#!/usr/bin/python3
"""Integration tests for format_multi_data  """

import pytest

from ArWikiCats.translations_formats import FormatData
from ArWikiCats.translations_formats.DataModel.model_multi_data import MultiDataFormatterBase

nationality_data = {
    "Afghan": {"man": "أفغاني", "men": "أفغان"},
    "yemeni": {"man": "يمني", "men": "يمنيون"},
    "british": {"man": "بريطاني", "men": "بريطانيون"},
    "american": {"man": "أمريكي", "men": "أمريكيون"},
    "egyptian": {"man": "مصري", "men": "مصريون"},
    "Algerian": {"man": "جزائري", "men": "جزائريون"},
    "Moroccan": {"man": "مغربي", "men": "مغاربة"},
}

formatted_data = {
    "{nat1_en} {nat2_en}": "{nat1_ar_men} {nat2_ar_mens}",
    "{nat1_en} people of {nat2_en} descent": "{nat1_ar_men} من أصل {nat2_ar_man}",
    "{nat1_en} people of {nat2_en} jewish descent": "{nat1_ar_men} من أصل يهودي {nat2_ar_man}",
}

nationality_data_men = {x: v["men"] for x, v in nationality_data.items()}
nationality_data_man = {x: v["man"] for x, v in nationality_data.items()}


@pytest.fixture
def multi_bot() -> MultiDataFormatterBase:
    # Country bot (FormatData)
    country_bot = FormatData(
        formatted_data=formatted_data,
        data_list=nationality_data_men,
        key_placeholder="{nat1_en}",
        value_placeholder="{nat1_ar_men}",
    )

    other_bot = FormatData(
        {},  # to use from search_all
        nationality_data_man,
        key_placeholder="{nat2_en}",
        value_placeholder="{nat2_ar_man}",
    )

    return MultiDataFormatterBase(
        country_bot=country_bot,
        other_bot=other_bot,
    )


test_match_key_data = {
    "Afghan American": "أمريكيون أفغان",
    "Afghan people of American descent": "أفغان من أصل أمريكي",
    "American people of Afghan descent": "أمريكيون من أصل أفغاني",
    "Algerian people of Moroccan Jewish descent": "جزائريون من أصل يهودي مغربي",
}


@pytest.mark.parametrize("category, expected", test_match_key_data.items(), ids=list(test_match_key_data.keys()))
@pytest.mark.fast
def test_standers(multi_bot: MultiDataFormatterBase, category: str, expected: str) -> None:
    result = multi_bot.search_all(category)
    assert result == expected
