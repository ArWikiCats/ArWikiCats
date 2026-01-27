"""
Tests
"""

import pytest

from ArWikiCats.patterns_resolvers.time_patterns_resolvers import resolve_lab_from_years_patterns

test_data = {
    "16th century music": "الموسيقى في القرن 16",
    "16th century theatre": "المسرح في القرن 16",
    "17th century music": "الموسيقى في القرن 17",
    "17th century theatre": "المسرح في القرن 17",
    "1520s censuses": "تعداد السكان في عقد 1520",
    "1630s science fiction works": "أعمال خيال علمي عقد 1630",
    "1650s controversies": "خلافات عقد 1650",
    "1650s floods": "فيضانات عقد 1650",
    "1650s mass shootings": "إطلاق نار عشوائي عقد 1650",
    "1650s murders": "جرائم قتل في عقد 1650",
    "1650s science fiction works": "أعمال خيال علمي عقد 1650",
    "17th-century cookbooks": "كتب طبخ القرن 17",
    "1910s musicals": "مسرحيات غنائية عقد 1910",
    "1910s racehorse deaths": "خيول سباق نفقت في عقد 1910",
    "1914 mining disasters": "كوارث التعدين 1914",
    "1970s albums": "ألبومات عقد 1970",
    "1990s landslides": "انهيارات أرضية عقد 1990",
    "19th-century publications": "منشورات القرن 19",
    "2020s revolutions": "ثورات عقد 2020",
    "2020s transport disasters": "كوارث نقل في عقد 2020",
    "21st-century mosques": "مساجد القرن 21",
    "2nd-millennium texts": "نصوص الألفية 2",
    "15th-century executions": "إعدامات في القرن 15",
    "February 2020 sports-events": "أحداث فبراير 2020 الرياضية",
}

@pytest.mark.parametrize("category, expected", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_test_data_1(category: str, expected: str) -> None:
    label = resolve_lab_from_years_patterns(category)
    assert label == expected
