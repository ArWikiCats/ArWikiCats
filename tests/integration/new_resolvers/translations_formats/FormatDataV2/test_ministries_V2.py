#!/usr/bin/python3
"""Integration tests for format_multi_data"""

import pytest

from ArWikiCats.translations_formats import MultiDataFormatterBaseV2, format_multi_data_v2


@pytest.fixture
def multi_bot() -> MultiDataFormatterBaseV2:
    countries_data = {
        "Guam": {"ar": "غوام"},
        "yemen": {"ar": "اليمن"},
    }

    formatted_data = {
        # category:ministries of education
        "ministries of {ministry}": "وزارات {no_al}",
        "Secretaries of {en}": "وزراء {ar}",
    }

    _keys = {
        "education": {"no_al": "تعليم", "with_al": "التعليم"},
        "finance": {"no_al": "مالية", "with_al": "المالية"},
        "health": {"no_al": "صحة", "with_al": "الصحة"},
    }

    return format_multi_data_v2(
        formatted_data=formatted_data,
        data_list=countries_data,
        key_placeholder="{en}",
        data_list2=_keys,
        key2_placeholder="{ministry}",
        text_after="",
        text_before="the ",
        search_first_part=True,
        use_other_formatted_data=True,
    )


test_data_1 = {
    "Category:Ministries of education": "تصنيف:وزارات تعليم",
    "Category:Ministries of finance": "تصنيف:وزارات مالية",
    "Category:Ministries of health": "تصنيف:وزارات صحة",
    "Category:Secretaries of Guam": "تصنيف:وزراء غوام",
}


@pytest.mark.parametrize("category, expected", test_data_1.items(), ids=test_data_1.keys())
@pytest.mark.fast
def test_multi_bot(multi_bot: MultiDataFormatterBaseV2, category: str, expected: str) -> None:
    result = multi_bot.search_all_category(category)
    assert result == expected
