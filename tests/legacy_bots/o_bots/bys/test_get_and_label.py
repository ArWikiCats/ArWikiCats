"""Tests for :mod:`make_bots.o_bots.bys`."""

from __future__ import annotations

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.legacy_bots.o_bots.bys import get_and_label

# TODO: need to fix results by_and_data_true_result, by_and_data

by_and_data_true_result = {
    "angus and dundee": "أنغوس ودندي",
    "architecture and construction": "هندسة معمارية وبناء",
    "architecture and planning": "هندسة معمارية وتخطيط",
    "architecture and technology": "الهندسة المعمارية والتقانة",
    "art and design": "الفن والتصميم",
    "arts and architecture": "الفنون والهندسة المعمارية",
    "arts and design": "الفنون والتصميم",
    "arts and sciences": "الفنون والعلوم",
    "british columbia and vancouver island": "كولومبيا البريطانية وجزيرة فانكوفر",
    "british columbia and yukon": "كولومبيا البريطانية ويوكون",
    "business and economics": "الأعمال والاقتصاد",
    "egypt and syria": "مصر وسوريا",
    "people and nations": "أشخاص وبلدان",
    "pesaro and urbino": "بيزارو وأوربينو",
    "philosophy and religion": "الفلسفة والدين",
    "pisa and sardinia": "بيزا وسردينيا",
    "poland and ukraine": "بولندا وأوكرانيا",
    "road transport and bridges": "نقل بري وجسور",
    "russia and soviet union": "روسيا والاتحاد السوفيتي",
    "schools and colleges": "مدارس وكليات",
    "science and engineering": "العلم والهندسة",
    "science and mathematics": "العلم والرياضيات",
    "theatre and film": "المسرح والأفلام",
}

by_and_data = {
    "angus and dundee": "أنغوس ودندي",
    "architecture and construction": "هندسة معمارية وبناء",
    "architecture and planning": "هندسة معمارية وتخطيط",
    "architecture and technology": "هندسة معمارية والتقانة",
    "art and design": "الفن وتصميم",
    "arts and architecture": "الفنون وهندسة معمارية",
    "arts and design": "الفنون وتصميم",
    "arts and sciences": "الفنون وعلوم",
    "british columbia and vancouver island": "كولومبيا البريطانية وجزيرة فانكوفر",
    "british columbia and yukon": "كولومبيا البريطانية ويوكون",
    "business and economics": "أعمال والاقتصاد",
    "egypt and syria": "مصر وسوريا",
    "people and nations": "أشخاص وبلدان",
    "pesaro and urbino": "بيزارو وأوربينو",
    "philosophy and religion": "الفلسفة والدين",
    "pisa and sardinia": "بيزا وسردينيا",
    "poland and ukraine": "بولندا وأوكرانيا",
    "road transport and bridges": "نقل بري وجسور",
    "russia and soviet union": "روسيا والاتحاد السوفيتي",
    "schools and colleges": "مدارس وكليات",
    "science and engineering": "العلم وهندسة",
    "science and mathematics": "العلم والرياضيات",
    "theatre and film": "المسرح وأفلام",
}


to_test = [
    ("test_get_and_label", by_and_data, get_and_label),
]


@pytest.mark.parametrize("category, expected", by_and_data.items(), ids=by_and_data.keys())
@pytest.mark.fast
def test_get_and_label(category: str, expected: str) -> None:
    label = get_and_label(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("name,data, callback", to_test)
@pytest.mark.skip2
def test_dump_all(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
