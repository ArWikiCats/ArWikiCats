"""
Tests for COUNTRY_YEAR_DATA
"""

import pytest

from ArWikiCats import resolve_label_ar

test_data = {
    "14th-century lords of Monaco": "لوردات موناكو في القرن 14",
    "15th-century lords of Monaco": "لوردات موناكو في القرن 15",
    "16th-century lords of Monaco": "لوردات موناكو في القرن 16",
    "17th-century lords of Monaco": "لوردات موناكو في القرن 17",
    "1830s alabama": "ألاباما في عقد 1830",
    "1830s arkansas": "أركنساس في عقد 1830",
    "1830s connecticut": "كونيتيكت في عقد 1830",
    "1830s delaware": "ديلاوير في عقد 1830",
    "1830s georgia (u.s. state)": "ولاية جورجيا في عقد 1830",
    "1830s indiana": "إنديانا في عقد 1830",
    "1830s iowa": "آيوا في عقد 1830",
    "1830s kentucky": "كنتاكي في عقد 1830",
    "1830s louisiana": "لويزيانا في عقد 1830",
    "1830s maine": "مين في عقد 1830",
    "1830s maryland": "ماريلند في عقد 1830",
    "1830s massachusetts": "ماساتشوستس في عقد 1830",
    "1830s michigan": "ميشيغان في عقد 1830",
    "1830s mississippi": "مسيسيبي في عقد 1830",
    "1830s missouri": "ميزوري في عقد 1830",
    "1830s new hampshire": "نيوهامشير في عقد 1830",
    "1830s new jersey": "نيوجيرسي في عقد 1830",
    "1830s new york (state)": "ولاية نيويورك في عقد 1830",
    "1830s north carolina": "كارولاينا الشمالية في عقد 1830",
    "1830s ohio": "أوهايو في عقد 1830",
    "1830s pennsylvania": "بنسلفانيا في عقد 1830",
    "1830s rhode island": "رود آيلاند في عقد 1830",
    "1830s south carolina": "كارولاينا الجنوبية في عقد 1830",
    "1830s tennessee": "تينيسي في عقد 1830",
    "1830s vermont": "فيرمونت في عقد 1830",
    "1830s virginia": "فرجينيا في عقد 1830",
    "1830s wisconsin": "ويسكونسن في عقد 1830",
}


@pytest.mark.parametrize("category,expected", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_country_time_pattern(category: str, expected: str) -> None:
    """Test all year-country translation patterns."""
    result = resolve_label_ar(category)
    assert result == expected
