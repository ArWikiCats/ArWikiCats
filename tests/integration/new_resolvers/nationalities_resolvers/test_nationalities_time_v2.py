"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.nationalities_resolvers.nationalities_time_v2 import resolve_nats_time_v2

test_data = {
    "10th-century Christian texts": "نصوص مسيحية في القرن 10",
    "11th-century Christian texts": "نصوص مسيحية في القرن 11",
    "12th-century Christian texts": "نصوص مسيحية في القرن 12",
    "13th-century Christian texts": "نصوص مسيحية في القرن 13",
    "13th-century Jewish texts": "نصوص يهودية في القرن 13",
    "14th-century Christian texts": "نصوص مسيحية في القرن 14",
    "15th-century Christian texts": "نصوص مسيحية في القرن 15",
    "16th-century Christian texts": "نصوص مسيحية في القرن 16",
    "17th-century Christian texts": "نصوص مسيحية في القرن 17",
    "18th-century Christian texts": "نصوص مسيحية في القرن 18",
    "19th-century Christian texts": "نصوص مسيحية في القرن 19",
    "1st-century Christian texts": "نصوص مسيحية في القرن 1",
    "1st-millennium Christian texts": "نصوص مسيحية في الألفية 1",
    "20th-century Christian texts": "نصوص مسيحية في القرن 20",
    "21st-century Christian texts": "نصوص مسيحية في القرن 21",
    "2nd-century Christian texts": "نصوص مسيحية في القرن 2",
    "2nd-millennium Christian texts": "نصوص مسيحية في الألفية 2",
    "3rd-century Christian texts": "نصوص مسيحية في القرن 3",
    "3rd-millennium Christian texts": "نصوص مسيحية في الألفية 3",
    "4th-century Christian texts": "نصوص مسيحية في القرن 4",
    "5th-century Christian texts": "نصوص مسيحية في القرن 5",
    "6th-century Christian texts": "نصوص مسيحية في القرن 6",
    "7th-century Christian texts": "نصوص مسيحية في القرن 7",
    "8th-century Christian texts": "نصوص مسيحية في القرن 8",
    "9th-century Christian texts": "نصوص مسيحية في القرن 9",
    # standard
    "2060 American coming-of-age story television programmes endings": "برامج تلفزيونية قصة تقدم في العمر انتهت في 2060",
    "Category:2000 American films": "تصنيف:أفلام أمريكية في 2000",
    "Category:2020s American films": "تصنيف:أفلام أمريكية في عقد 2020",
    "Category:2020s the American films": "تصنيف:أفلام أمريكية في عقد 2020",
    "Category:turkish general election june 2015": "تصنيف:الانتخابات التشريعية التركية يونيو 2015",
    "Category:turkish general election november 2015": "تصنيف:الانتخابات التشريعية التركية نوفمبر 2015",
}


@pytest.mark.parametrize("category,expected", test_data.items(), ids=test_data.keys())
def test_resolve_nats_time_v2(category: str, expected: str) -> None:
    """Test all year-country translation patterns."""
    result = resolve_nats_time_v2(category)
    assert result == expected
