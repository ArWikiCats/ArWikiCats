"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.legacy_bots.films_and_others_bot import te_films

fast_data_drama = {
}

fast_data = {
    "croatian biographical films": "أفلام سير ذاتية كرواتية",
    "albanian film directors": "مخرجو أفلام ألبان",
    "american film directors": "مخرجو أفلام أمريكيون",
    "argentine film actors": "ممثلو أفلام أرجنتينيون",
    "australian films": "أفلام أسترالية",
    "austrian films": "أفلام نمساوية",
    "british films": "أفلام بريطانية",
    "bruneian film producers": "منتجو أفلام برونيون",
    "czech silent film actors": "ممثلو أفلام صامتة تشيكيون",
    "dutch films": "أفلام هولندية",
    "film directors": "مخرجو أفلام",
    "french films": "أفلام فرنسية",
    "ghanaian films": "أفلام غانية",
    "indonesian film actresses": "ممثلات أفلام إندونيسيات",
    "iranian film actors": "ممثلو أفلام إيرانيون",
    "iranian film producers": "منتجو أفلام إيرانيون",
    "japanese films": "أفلام يابانية",
    "japanese male film actors": "ممثلو أفلام ذكور يابانيون",
    "kosovan filmmakers": "صانعو أفلام كوسوفيون",
    "latvian films": "أفلام لاتفية",
    "maldivian women film directors": "مخرجات أفلام مالديفيات",
    "moldovan film actors": "ممثلو أفلام مولدوفيون",
    "moroccan musical films": "أفلام موسيقية مغربية",
    "nepalese male film actors": "ممثلو أفلام ذكور نيباليون",
    "nigerien film actors": "ممثلو أفلام نيجريون",
    "romanian films": "أفلام رومانية",
    "russian silent film actresses": "ممثلات أفلام صامتة روسيات",
    "saudiarabian films": "أفلام سعودية",
    "somalian film producers": "منتجو أفلام صوماليون",
    "soviet films": "أفلام سوفيتية",
    "telugu film directors": "مخرجو أفلام تيلوغويون",
    "thai film actors": "ممثلو أفلام تايلنديون",
    "ukrainian filmmakers": "صانعو أفلام أوكرانيون",
    "welsh film producers": "منتجو أفلام ويلزيون",
}


@pytest.mark.parametrize("category, expected", fast_data_drama.items(), ids=fast_data_drama.keys())
@pytest.mark.fast
def test_fast_data_drama(category: str, expected: str) -> None:
    label = te_films(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_fast_data_films(category: str, expected: str) -> None:
    label = te_films(category)
    assert label == expected


to_test = [
    ("test_fast_data_drama", fast_data_drama, te_films),
    ("test_fast_data_films", fast_data, te_films),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


def test_test_films() -> None:
    # Test with a basic input
    result = te_films("action films")
    assert isinstance(result, str)

    result_empty = te_films("")
    assert isinstance(result_empty, str)

    # Test with reference category
    result_with_ref = te_films("drama movies")
    assert isinstance(result_with_ref, str)
