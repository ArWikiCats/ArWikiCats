"""
Tests
"""

import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data_callback

fast_data_drama = {}

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
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_fast_data_films(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


to_test = [
    ("test_fast_data_drama", fast_data_drama, resolve_label_ar),
    ("test_fast_data_films", fast_data, resolve_label_ar),
]
test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
