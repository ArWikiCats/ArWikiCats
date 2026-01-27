#!/usr/bin/python3
"""Integration tests for format_year_country_data and"""

import pytest

from ArWikiCats.translations import all_country_ar
from ArWikiCats.translations_formats import MultiDataFormatterBaseYear, format_year_country_data

# Template data with both nationality and sport placeholders
formatted_data = {
    "{year1} in new {country1}": "{country1} الجديدة في {year1}",
    "{year1} establishments in new {country1}": "تأسيسات سنة {year1} في {country1} الجديدة",
    "{year1} in {country1}": "{country1} في {year1}",
    "{year1} establishments in {country1}": "تأسيسات سنة {year1} في {country1}",
    "{year1} events in {country1}": "أحداث {year1} في {country1}",
    "{year1} disestablishments in {country1}": "انحلالات سنة {year1} في {country1}",
    "{year1} sports events in {country1}": "أحداث {year1} الرياضية في {country1}",
    "{year1} crimes in {country1}": "جرائم {year1} في {country1}",
    "{year1} murders in {country1}": "جرائم قتل في {country1} في {year1}",
    "{year1} disasters in {country1}": "كوارث في {country1} في {year1}",
    "{year1} in {country1} by month": "أحداث {year1} في {country1} حسب الشهر",
    "{year1} elections in {country1}": "انتخابات {country1} في {year1}",
    "{year1} events in {country1} by month": "أحداث {year1} في {country1} حسب الشهر",
    "years of the {year1} in {country1}": "سنوات {year1} في {country1}",
    "{year1} in sports in {country1}": "الرياضة في {country1} في {year1}",
    "{year1} in {country1} by city": "{country1} في {year1} حسب المدينة",
    "{country1} at the {year1} fifa world cup": "{country1} في كأس العالم {year1}",
    "{year1} in {country1} (state)": "ولاية {country1} في {year1}",
    "{year1} establishments in {country1} territory": "تأسيسات سنة {year1} في إقليم {country1}",
    "{year1} establishments in {country1} (state)": "تأسيسات سنة {year1} في ولاية {country1}",
    "terrorist incidents in {country1} in {year1}": "حوادث إرهابية في {country1} في {year1}",
    "railway stations in {country1} opened in {year1}": "محطات السكك الحديدية في {country1} افتتحت في {year1}",
    "{year1} in {country1} territory": "إقليم {country1} في {year1}",
    "{year1} architecture in {country1}": "عمارة {year1} في {country1}",
    "{year1} in {country1} by state": "{year1} في {country1} حسب الولاية",
    "{year1} in {country1} by state or territory": "{country1} في {year1} حسب الولاية",
    "{year1} mass shootings in {country1}": "إطلاق نار عشوائي في {country1} في {year1}",
    "attacks in {country1} in {year1}": "هجمات في {country1} في {year1}",
    "{year1} roman catholic bishops in {country1}": "أساقفة كاثوليك رومان في {country1} في {year1}",
    "{year1} in {country1} city": "مدينة {country1} في {year1}",
    "{year1} religious buildings and structures in {country1}": "مبان ومنشآت دينية في {country1} في {year1}",
    "{year1} churches in {country1}": "كنائس في {country1} في {year1}",
    "{year1} in {country1} (u.s. state)": "ولاية {country1} في {year1}",
    "{country1} at uefa euro {year1}": "{country1} في بطولة أمم أوروبا {year1}",
    "{year1} mosques in {country1}": "مساجد في {country1} في {year1}",
}


@pytest.fixture
def yc_bot() -> MultiDataFormatterBaseYear:
    return format_year_country_data(
        formatted_data=formatted_data,
        data_list=all_country_ar,
        key_placeholder="{country1}",
        value_placeholder="{country1}",
        key2_placeholder="{year1}",
        value2_placeholder="{year1}",
        text_after=" !",
        text_before="the ",
    )


test_data = [
    # standard
    ("2010s in united states", "الولايات المتحدة في عقد 2010"),
    # with text_before
    ("2010s in the united states", "الولايات المتحدة في عقد 2010"),
    # with text_after
    ("2010s in the united states !", "الولايات المتحدة في عقد 2010"),
    ("2025 in Yemen", "اليمن في 2025"),
    ("2020s in Yemen", "اليمن في عقد 2020"),
    ("2010s establishments in egypt", "تأسيسات عقد 2010 في مصر"),
    ("1999 establishments in egypt", "تأسيسات سنة 1999 في مصر"),
    ("2025 in yemen", "اليمن في 2025"),
    ("1999 establishments in egypt", "تأسيسات سنة 1999 في مصر"),
    ("2010 events in iraq", "أحداث 2010 في العراق"),
    ("2020 disasters in france", "كوارث في فرنسا في 2020"),
    ("2022 sports events in egypt", "أحداث 2022 الرياضية في مصر"),
    ("2021 crimes in iraq", "جرائم 2021 في العراق"),
    ("2022 murders in yemen", "جرائم قتل في اليمن في 2022"),
    ("2015 in united states by month", "أحداث 2015 في الولايات المتحدة حسب الشهر"),
    ("2020 elections in france", "انتخابات فرنسا في 2020"),
    ("2010 events in yemen by month", "أحداث 2010 في اليمن حسب الشهر"),
    ("years of the 1990s in egypt", "سنوات عقد 1990 في مصر"),
    ("2023 in sports in iraq", "الرياضة في العراق في 2023"),
    ("2020 in yemen by city", "اليمن في 2020 حسب المدينة"),
    ("yemen at the 2022 fifa world cup", "اليمن في كأس العالم 2022"),
    ("2021 in egypt (state)", "ولاية مصر في 2021"),
    ("2022 establishments in france territory", "تأسيسات سنة 2022 في إقليم فرنسا"),
    ("1999 establishments in iraq (state)", "تأسيسات سنة 1999 في ولاية العراق"),
    ("terrorist incidents in yemen in 2018", "حوادث إرهابية في اليمن في 2018"),
    ("railway stations in france opened in 2012", "محطات السكك الحديدية في فرنسا افتتحت في 2012"),
    ("2020 in iraq territory", "إقليم العراق في 2020"),
    ("2005 architecture in egypt", "عمارة 2005 في مصر"),
    ("2010 in new yemen", "اليمن الجديدة في 2010"),
    ("2020 in iraq by state", "2020 في العراق حسب الولاية"),
    ("2020 in iraq by state or territory", "العراق في 2020 حسب الولاية"),
    ("2021 mass shootings in united states", "إطلاق نار عشوائي في الولايات المتحدة في 2021"),
    ("attacks in france in 2015", "هجمات في فرنسا في 2015"),
    ("2022 roman catholic bishops in france", "أساقفة كاثوليك رومان في فرنسا في 2022"),
    ("2019 establishments in new egypt", "تأسيسات سنة 2019 في مصر الجديدة"),
    ("2010 in egypt city", "مدينة مصر في 2010"),
    ("2011 religious buildings and structures in iraq", "مبان ومنشآت دينية في العراق في 2011"),
    ("2011 churches in iraq", "كنائس في العراق في 2011"),
    ("2010 in iraq (u.s. state)", "ولاية العراق في 2010"),
    ("france at uefa euro 2020", "فرنسا في بطولة أمم أوروبا 2020"),
    ("2022 mosques in egypt", "مساجد في مصر في 2022"),
]


@pytest.mark.parametrize("category,expected", test_data, ids=[x[0] for x in test_data])
def test_year_country_combinations(yc_bot: MultiDataFormatterBaseYear, category: str, expected: str) -> None:
    """Test all year-country translation patterns."""
    result = yc_bot.create_label(category)
    assert result == expected
