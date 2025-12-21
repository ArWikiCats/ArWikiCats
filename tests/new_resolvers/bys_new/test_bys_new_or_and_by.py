"""
Tests for bys_new bot
"""

from __future__ import annotations

import pytest
from load_one_data import dump_diff, one_dump_test
from ArWikiCats.new_resolvers.bys_new import resolve_by_labels

test_data = {
    "by university or college": "حسب الجامعة أو الكلية",
    "by territory or dependency": "حسب الإقليم أو التبعية",
    "by state or division": " حسب الولاية أو المقاطعة",
    "by state or union territory": "حسب الولاية أو الإقليم الاتحادي",
    "by province or territory": "حسب المقاطعة أو الإقليم",
    "by faith or belief": "حسب الإيمان أو العقيدة",
    "by division or state": " حسب المقاطعة أو الولاية",
    "by ethnic or national origin": "حسب الأصل العرقي أو الوطني",
    "by country or language": "حسب البلد أو اللغة",
    "by city or town": "حسب المدينة أو البلدة",

    "by ethnic or national origin and occupation": "حسب الأصل العرقي أو الوطني والمهنة",
    "by state and year": "حسب الولاية والسنة",
    "by nation and year": "حسب الموطن والسنة",
    "by nationality and instrument ": "حسب الجنسية والآلة الموسيقية",
    "by nationality, genre and instrument": "حسب الجنسية والنوع والآلة",
    "by occupation and continent": "حسب المهنة والقارة",

    "by populated place and occupation": "حسب المكان المأهول والمهنة",
    "by instrument and genre": "حسب الآلة والنوع الفني",
    "by instrument and nationality": "حسب الآلة والجنسية",
    "by instrument, genre and nationality": "حسب الآلة والنوع الفني والجنسية",
    "by genre and instrument": "حسب النوع الفني والآلة",
    "by genre, nationality and instrument": "حسب النوع الفني والجنسية والآلة",
    "by country and city": "حسب البلد والمدينة",
    "by country and occupation": "حسب البلد والمهنة",
    "by country and war": "حسب البلد والحرب",
    "by continent and occupation": "حسب القارة والمهنة",
    "by century and instrument": "حسب القرن والآلة",

    "by year of closing": "حسب سنة الاغلاق",
    "by year of completion": "حسب سنة الانتهاء",
    "by year of conclusion": "حسب سنة الإبرام",
    "by year of entry into force": "حسب سنة دخولها حيز التنفيذ",
    "by year of introduction": "حسب سنة الاستحداث",
    "by year of photographing": "حسب سنة التصوير",
    "by decade of closing": "حسب عقد الاغلاق",
    "by decade of introduction": "حسب عقد الاستحداث",
    "by country of arrest": "حسب بلد الاعتقال",
    "by country of location": "حسب بلد الموقع",
    "by country of origin": "حسب البلد الأصل",
    "by country of production": "حسب بلد الإنتاج",
    "by country of residence": "حسب بلد الإقامة",
    "by country of setting": "حسب بلد الأحداث",
    "by country of setting location": "حسب بلد موقع الأحداث",
    "by country of shooting location": "حسب بلد موقع التصوير",
    "by continent of production": "حسب قارة الإنتاج",
    "by continent of setting": "حسب قارة الأحداث",
    "by continent of shooting location": "حسب قارة موقع التصوير",
    "by century of closing": "حسب قرن الاغلاق",
    "by city of location": "حسب مدينة الموقع",
    "by city of setting": "حسب مدينة الأحداث",
    "by city of shooting location": "حسب مدينة موقع التصوير",

    "by club or team": "حسب النادي أو الفريق"
}


@pytest.mark.parametrize("category,expected", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_bys_new_or_and_by(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = resolve_by_labels(category)
    assert result == expected


to_test = [
    ("test_bys_new_or_and_by", test_data),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_by_labels)
    dump_diff(diff_result, name)

    expected2 = {x: v for x, v in expected.items() if v and x in diff_result}
    dump_diff(expected2, f"{name}_expected")

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
