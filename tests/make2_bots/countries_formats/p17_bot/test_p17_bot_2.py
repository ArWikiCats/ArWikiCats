"""
Tests
"""

import pytest

from src.make2_bots.countries_formats.p17_bot_2 import (
    Get_P17_2,
    add_definite_article,
)


get_p17_2_data = {
    "united states navy": "البحرية الأمريكية",
    "china navy": "البحرية الصينية",
    "united states air force": "القوات الجوية الأمريكية",
    "united states government officials": "مسؤولون حكوميون أمريكيون",
    "north yemen civil war": "الحرب الأهلية الشمالية اليمنية",
    "pakistan navy": "البحرية الباكستانية",
    "new zealand royal air force": "القوات الجوية الملكية النيوزيلندية",
    "korea navy": "البحرية الكورية",
    "yemen navy": "البحرية اليمنية",
    "new zealand royal navy": "البحرية الملكية النيوزيلندية",
    "vietnam navy": "البحرية الفيتنامية",
    "china air force": "القوات الجوية الصينية",
    "myanmar civil war": "الحرب الأهلية الميانمارية",
    "netherlands royal navy": "البحرية الملكية الهولندية",
    "iran navy": "البحرية الإيرانية",
    "sri lanka navy": "البحرية السريلانكية",
    "sri lanka air force": "القوات الجوية السريلانكية",
    "bahamas royal defence force": "قوات الدفاع الملكية البهامية",
    "south yemen navy": "البحرية الجنوبية اليمنية",
    "sierra leone civil war": "الحرب الأهلية السيراليونية",
    "japan navy": "البحرية اليابانية",
    "united arab emirates navy": "البحرية الإماراتية",
    "netherlands royal air force": "القوات الجوية الملكية الهولندية",
    "benin navy": "البحرية البنينية",
    "cyprus navy": "البحرية القبرصية",
    "morocco government officials": "مسؤولون حكوميون مغاربة",
    "brunei royal navy": "البحرية الملكية البرونية",
    "korea air force": "القوات الجوية الكورية",
}


@pytest.mark.parametrize("category, expected", get_p17_2_data.items(), ids=list(get_p17_2_data.keys()))
@pytest.mark.fast
def test_get_p17_2(category, expected) -> None:
    label = Get_P17_2(category)
    assert label == expected


definite_article_data = {
    "أمريكية": "الأمريكية",
    "صينية": "الصينية",
    "شمالية يمنية": "الشمالية اليمنية",
    "باكستانية": "الباكستانية",
    "نيوزيلندية": "النيوزيلندية",
    "كورية": "الكورية",
    "يمنية": "اليمنية",
    "فيتنامية": "الفيتنامية",
    "ميانمارية": "الميانمارية",
    "هولندية": "الهولندية",
    "إيرانية": "الإيرانية",
    "سريلانكية": "السريلانكية",
    "بهامية": "البهامية",
    "جنوبية يمنية": "الجنوبية اليمنية",
    "سيراليونية": "السيراليونية",
    "يابانية": "اليابانية",
    "إماراتية": "الإماراتية",
    "بنينية": "البنينية",
    "قبرصية": "القبرصية",
    "برونية": "البرونية",
}


@pytest.mark.parametrize("category, expected", definite_article_data.items(), ids=list(definite_article_data.keys()))
@pytest.mark.fast
def test_add_definite_article(category, expected) -> None:
    label = add_definite_article(category)
    assert label == expected
