"""
Tests
"""

import pytest

from ArWikiCats.patterns_resolvers.country_time_pattern import resolve_country_time_pattern

test_data = {
    # "Category:19th-century West Virginia politicians": "تصنيف:سياسيو فرجينيا الغربية في القرن 19",
    # standard
    # "Category:18th-century people of the Dutch Empire": "تصنيف:أشخاص من الإمبراطورية الهولندية القرن 18",
    # "Category:years of the 1990s in egypt": "تصنيف:سنوات عقد 1990 في مصر",
    "Category:July 2003 in Russia": "تصنيف:يوليو 2003 في روسيا",
    "Category:May 1939 in Canada": "تصنيف:مايو 1939 في كندا",
    "Category:2010s establishments in egypt": "تصنيف:تأسيسات عقد 2010 في مصر",
    "Category:1999 establishments in egypt": "تصنيف:تأسيسات سنة 1999 في مصر",
    "Category:2010 events in iraq": "تصنيف:أحداث 2010 في العراق",
    "Category:2020 disasters in france": "تصنيف:كوارث في فرنسا في 2020",
    "Category:2022 sports events in egypt": "تصنيف:أحداث 2022 الرياضية في مصر",
    "Category:2021 crimes in iraq": "تصنيف:جرائم 2021 في العراق",
    "Category:2022 murders in yemen": "تصنيف:جرائم قتل في اليمن في 2022",
    "Category:2015 in united states by month": "تصنيف:2015 في الولايات المتحدة حسب الشهر",
    "Category:2010 events in yemen by month": "تصنيف:أحداث 2010 في اليمن حسب الشهر",
    "Category:2023 in sports in iraq": "تصنيف:الرياضة في العراق في 2023",
    "Category:2020 in yemen by city": "تصنيف:اليمن في 2020 حسب المدينة",
    "Category:2021 in egypt (state)": "تصنيف:ولاية مصر في 2021",
    "Category:2022 establishments in france territory": "تصنيف:تأسيسات سنة 2022 في إقليم فرنسا",
    "Category:1999 establishments in iraq (state)": "تصنيف:تأسيسات سنة 1999 في ولاية العراق",
    "Category:terrorist incidents in yemen in 2018": "تصنيف:حوادث إرهابية في اليمن في 2018",
    "Category:railway stations in france opened in 2012": "تصنيف:محطات السكك الحديدية في فرنسا افتتحت في 2012",
    "Category:2020 in iraq territory": "تصنيف:إقليم العراق في 2020",
    "Category:2005 architecture in egypt": "تصنيف:عمارة 2005 في مصر",
    "Category:2020 in iraq by state": "تصنيف:2020 في العراق حسب الولاية",
    "Category:2020 in iraq by state or territory": "تصنيف:العراق في 2020 حسب الولاية",
    "Category:2021 mass shootings in united states": "تصنيف:إطلاق نار عشوائي في الولايات المتحدة في 2021",
    "Category:attacks in france in 2015": "تصنيف:هجمات في فرنسا في 2015",
    "Category:2022 roman catholic bishops in france": "تصنيف:أساقفة كاثوليك رومان في فرنسا في 2022",
    "Category:2019 establishments in egypt": "تصنيف:تأسيسات سنة 2019 في مصر",
    "Category:2010 in egypt city": "تصنيف:مدينة مصر في 2010",
    "Category:2011 religious buildings and structures in iraq": "تصنيف:مبان ومنشآت دينية في العراق في 2011",
    "Category:2011 churches in iraq": "تصنيف:كنائس في العراق في 2011",
    "Category:2022 mosques in egypt": "تصنيف:مساجد في مصر في 2022",
}


@pytest.mark.parametrize("category,expected", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_country_time_pattern(category: str, expected: str) -> None:
    """Test all year-country translation patterns."""
    result = resolve_country_time_pattern(category)
    assert result == expected
