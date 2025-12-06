#!/usr/bin/python3
"""Integration tests for format_multi_data  """

import pytest

from ArWikiCats.translations_formats import FormatDataV2, MultiDataFormatterBaseV2


@pytest.fixture
def multi_bot() -> MultiDataFormatterBaseV2:
    nationality_data = {
        "United States": {
            "country_ar": "الولايات المتحدة"
        },
        "yemen": {
            "country_ar": "اليمن"
        },
    }

    formatted_data = {
        "{country_en}": "{country_ar}",
        "Olympic gold medalists for {country_en}": "فائزون بميداليات ذهبية أولمبية من {country_ar}",
        "Olympic gold medalists for {country_en} in alpine skiing":
        "فائزون بميداليات ذهبية أولمبية من {country_ar} في التزلج على المنحدرات الثلجية",
        "Olympic gold medalists for {country_en} in {sport_en}": "فائزون بميداليات ذهبية أولمبية من {country_ar} في {sport_ar}",
    }

    sport_data = {
        "alpine skiing": {
            "sport_ar": "التزلج على المنحدرات الثلجية",
        },
        "football": {
            "sport_ar": "كرة القدم",
        },
    }

    country_bot = FormatDataV2(
        formatted_data=formatted_data,
        data_list=nationality_data,
        key_placeholder="{country_en}",
    )

    other_bot = FormatDataV2(
        {},
        sport_data,
        key_placeholder="{sport_en}",
    )

    return MultiDataFormatterBaseV2(
        country_bot=country_bot,
        other_bot=other_bot,
        search_first_part=True,
    )


test_data_1 = {
    "United States": "الولايات المتحدة",
    "Olympic gold medalists for United States": "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة",
    "Olympic gold medalists for United States in alpine skiing": "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة في التزلج على المنحدرات الثلجية",
    "Olympic gold medalists for the United States in football": "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة في كرة القدم",
}


@pytest.mark.parametrize("category, expected", test_data_1.items(), ids=list(test_data_1.keys()))
@pytest.mark.fast
def test_multi_bot(multi_bot: MultiDataFormatterBaseV2, category: str, expected: str) -> None:
    result = multi_bot.search_all(category)
    assert result == expected
