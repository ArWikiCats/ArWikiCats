#!/usr/bin/python3
"""Integration tests for v3i translations resolvers validating country, year, and combined formatters."""

import pytest

from ArWikiCats import resolve_label_ar
from ArWikiCats.new_resolvers.time_and_jobs_resolvers.year_job_origin_resolver import resolve_year_job_from_countries
from utils.dump_runner import make_dump_test_name_data_callback

test_deaths_data = {
    "16th-century deaths from tuberculosis": "وفيات بسبب السل في القرن 16",
    "20th-century deaths from infectious disease": "وفيات بسبب أمراض معدية في القرن 20",
    "17th-century deaths from tuberculosis": "وفيات بسبب السل في القرن 17",
    "18th-century deaths from tuberculosis": "وفيات بسبب السل في القرن 18",
    "19th-century deaths from tuberculosis": "وفيات بسبب السل في القرن 19",
    "20th-century deaths from tuberculosis": "وفيات بسبب السل في القرن 20",
    "7th-century deaths from tuberculosis": "وفيات بسبب السل في القرن 7",
    "21st-century deaths from tuberculosis": "وفيات بسبب السل في القرن 21",
    "14th-century deaths from tuberculosis": "وفيات بسبب السل في القرن 14",
}

test_females_data = {
    "18th-century businesswomen from the Russian Empire": "سيدات أعمال من الإمبراطورية الروسية في القرن 18",
    "18th-century actresses from Bohemia": "ممثلات من بوهيميا في القرن 18",
    "18th-century actresses from the Holy Roman Empire": "ممثلات من الإمبراطورية الرومانية المقدسة في القرن 18",
    "19th-century actresses from the Ottoman Empire": "ممثلات من الدولة العثمانية في القرن 19",
    "19th-century actresses from the Russian Empire": "ممثلات من الإمبراطورية الروسية في القرن 19",
    "19th-century businesswomen from the Russian Empire": "سيدات أعمال من الإمبراطورية الروسية في القرن 19",
    "20th-century actresses from Georgia (country)": "ممثلات من جورجيا في القرن 20",
    "20th-century actresses from Northern Ireland": "ممثلات من أيرلندا الشمالية في القرن 20",
    "20th-century actresses from the Ottoman Empire": "ممثلات من الدولة العثمانية في القرن 20",
    "21st-century actresses from Georgia (country)": "ممثلات من جورجيا في القرن 21",
    "21st-century actresses from Northern Ireland": "ممثلات من أيرلندا الشمالية في القرن 21",
}

test_data_standard = {
    "19th-century LGBTQ people from the Russian Empire": "أعلام إل جي بي تي كيو من الإمبراطورية الروسية في القرن 19",
    "19th-century journalists from the Ottoman Empire": "صحفيون من الدولة العثمانية في القرن 19",
    "20th-century journalists from the Ottoman Empire": "صحفيون من الدولة العثمانية في القرن 20",
    "9th-century Jews from al-Andalus": "يهود من الأندلس في القرن 9",
    "9th-century people from al-Andalus": "أشخاص من الأندلس في القرن 9",
    "17th-century writers from Bohemia": "كتاب من بوهيميا في القرن 17",
    "16th-century writers from the Ottoman Empire": "كتاب من الدولة العثمانية في القرن 16",
    "12th-century princes from Kievan Rus'": "أمراء من كييف روس في القرن 12",
    "13th-century princes from Kievan Rus'": "أمراء من كييف روس في القرن 13",
    "15th-century rabbis from the Ottoman Empire": "حاخامات من الدولة العثمانية في القرن 15",
    "16th-century rabbis from the Ottoman Empire": "حاخامات من الدولة العثمانية في القرن 16",
    "17th-century writers from the Ottoman Empire": "كتاب من الدولة العثمانية في القرن 17",
    "10th-century historians from al-Andalus": "مؤرخون من الأندلس في القرن 10",
    "10th-century historians from the Abbasid Caliphate": "مؤرخون من الدولة العباسية في القرن 10",
    "11th-century historians from al-Andalus": "مؤرخون من الأندلس في القرن 11",
    "11th-century people from the Kingdom of Aragon": "أشخاص من مملكة أرغون في القرن 11",
    "12th-century historians from al-Andalus": "مؤرخون من الأندلس في القرن 12",
    "13th-century clergy from the Holy Roman Empire": "رجال دين من الإمبراطورية الرومانية المقدسة في القرن 13",
    "13th-century historians from al-Andalus": "مؤرخون من الأندلس في القرن 13",
    "13th-century people from the crown of aragon": "أشخاص من تاج أرغون في القرن 13",
    "14th-century historians from al-Andalus": "مؤرخون من الأندلس في القرن 14",
    "15th-century artists from the Ottoman Empire": "فنانون من الدولة العثمانية في القرن 15",
    "15th-century astronomers from the Holy Roman Empire": "فلكيون من الإمبراطورية الرومانية المقدسة في القرن 15",
    "15th-century people from the Crown of Aragon": "أشخاص من تاج أرغون في القرن 15",
    "16th-century artists from the Ottoman Empire": "فنانون من الدولة العثمانية في القرن 16",
    "16th-century astronomers from the Holy Roman Empire": "فلكيون من الإمبراطورية الرومانية المقدسة في القرن 16",
    "16th-century astronomers from the Ottoman Empire": "فلكيون من الدولة العثمانية في القرن 16",
    "16th-century botanists from the Holy Roman Empire": "علماء نباتات من الإمبراطورية الرومانية المقدسة في القرن 16",
    "16th-century businesspeople from the Ottoman Empire": "شخصيات أعمال من الدولة العثمانية في القرن 16",
    "16th-century clergy from the Holy Roman Empire": "رجال دين من الإمبراطورية الرومانية المقدسة في القرن 16",
    "16th-century composers from the Holy Roman Empire": "ملحنون من الإمبراطورية الرومانية المقدسة في القرن 16",
    "16th-century historians from Bohemia": "مؤرخون من بوهيميا في القرن 16",
    "17th-century architects from the Holy Roman Empire": "معماريون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "17th-century artists from the Ottoman Empire": "فنانون من الدولة العثمانية في القرن 17",
    "17th-century astronomers from the Holy Roman Empire": "فلكيون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "17th-century astronomers from the Ottoman Empire": "فلكيون من الدولة العثمانية في القرن 17",
    "17th-century botanists from the Holy Roman Empire": "علماء نباتات من الإمبراطورية الرومانية المقدسة في القرن 17",
    "17th-century businesspeople from the Holy Roman Empire": "شخصيات أعمال من الإمبراطورية الرومانية المقدسة في القرن 17",
    "17th-century businesspeople from the Ottoman Empire": "شخصيات أعمال من الدولة العثمانية في القرن 17",
    "17th-century civil servants from the Ottoman Empire": "موظفو خدمة مدنية من الدولة العثمانية في القرن 17",
    "17th-century clergy from the Holy Roman Empire": "رجال دين من الإمبراطورية الرومانية المقدسة في القرن 17",
    "17th-century composers from the Holy Roman Empire": "ملحنون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "17th-century engineers from the Holy Roman Empire": "مهندسون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "17th-century engravers from the Holy Roman Empire": "نقاشون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "17th-century historians from Bohemia": "مؤرخون من بوهيميا في القرن 17",
    "17th-century sculptors from the Holy Roman Empire": "نحاتون من الإمبراطورية الرومانية المقدسة في القرن 17",
    "18th-century actors from Bohemia": "ممثلون من بوهيميا في القرن 18",
    "18th-century architects from the Holy Roman Empire": "معماريون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century architects from the Russian Empire": "معماريون من الإمبراطورية الروسية في القرن 18",
    "18th-century artists from the Holy Roman Empire": "فنانون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century artists from the Ottoman Empire": "فنانون من الدولة العثمانية في القرن 18",
    "18th-century artists from the Republic of Geneva": "فنانون من جمهورية جنيف في القرن 18",
    "18th-century artists from the Russian Empire": "فنانون من الإمبراطورية الروسية في القرن 18",
    "18th-century astronomers from the Holy Roman Empire": "فلكيون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century ballet dancers from Bohemia": "راقصو باليه من بوهيميا في القرن 18",
    "18th-century botanists from the Holy Roman Empire": "علماء نباتات من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century botanists from the Russian Empire": "علماء نباتات من الإمبراطورية الروسية في القرن 18",
    "18th-century businesspeople from the Holy Roman Empire": "شخصيات أعمال من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century businesspeople from the Russian Empire": "شخصيات أعمال من الإمبراطورية الروسية في القرن 18",
    "18th-century chemists from the Holy Roman Empire": "كيميائيون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century classical composers from Bohemia": "ملحنون كلاسيكيون من بوهيميا في القرن 18",
    "18th-century classical composers from the Holy Roman Empire": "ملحنون كلاسيكيون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century clergy from the Holy Roman Empire": "رجال دين من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century composers from the Holy Roman Empire": "ملحنون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century engineers from the Holy Roman Empire": "مهندسون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century engravers from the Holy Roman Empire": "نقاشون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th-century women from the Russian Empire": "نساء من الإمبراطورية الروسية في القرن 18",
    "19th-century architects from the Russian Empire": "معماريون من الإمبراطورية الروسية في القرن 19",
    "19th-century artists from the Ottoman Empire": "فنانون من الدولة العثمانية في القرن 19",
    "19th-century artists from the Russian Empire": "فنانون من الإمبراطورية الروسية في القرن 19",
    "19th-century astronomers from the Russian Empire": "فلكيون من الإمبراطورية الروسية في القرن 19",
    "19th-century ballet dancers from the Russian Empire": "راقصو باليه من الإمبراطورية الروسية في القرن 19",
    "19th-century biologists from the Russian Empire": "علماء أحياء من الإمبراطورية الروسية في القرن 19",
    "19th-century botanists from the Russian Empire": "علماء نباتات من الإمبراطورية الروسية في القرن 19",
    "19th-century businesspeople from the Ottoman Empire": "شخصيات أعمال من الدولة العثمانية في القرن 19",
    "19th-century businesspeople from the Russian Empire": "شخصيات أعمال من الإمبراطورية الروسية في القرن 19",
    "19th-century classical composers from the Russian Empire": "ملحنون كلاسيكيون من الإمبراطورية الروسية في القرن 19",
    "19th-century women from Georgia (country)": "نساء من جورجيا في القرن 19",
    "19th-century women from Ottoman Arabia": "نساء من الدولة العثمانية في شبه الجزيرة العربية في القرن 19",
    "19th-century women from the Ottoman Empire": "نساء من الدولة العثمانية في القرن 19",
    "19th-century women from the Russian Empire": "نساء من الإمبراطورية الروسية في القرن 19",
    "20th-century actors from Georgia (country)": "ممثلون من جورجيا في القرن 20",
    "20th-century artists from Georgia (country)": "فنانون من جورجيا في القرن 20",
    "20th-century artists from the Ottoman Empire": "فنانون من الدولة العثمانية في القرن 20",
    "20th-century civil servants from the Ottoman Empire": "موظفو خدمة مدنية من الدولة العثمانية في القرن 20",
    "20th-century classical composers from Northern Ireland": "ملحنون كلاسيكيون من أيرلندا الشمالية في القرن 20",
    "20th-century dramatists and playwrights from Georgia (country)": "كتاب دراما ومسرح من جورجيا في القرن 20",
    "20th-century people from insular areas of the United States": "أشخاص من المناطق المعزولة في الولايات المتحدة في القرن 20",
    "20th-century politicians from insular areas of the United States": "سياسيون من المناطق المعزولة في الولايات المتحدة في القرن 20",
    "20th-century women from Georgia (country)": "نساء من جورجيا في القرن 20",
    "20th-century women from Northern Ireland": "نساء من أيرلندا الشمالية في القرن 20",
    "20th-century women from the Ottoman Empire": "نساء من الدولة العثمانية في القرن 20",
    "20th-century women politicians from insular areas of the United States": "سياسيات من المناطق المعزولة في الولايات المتحدة في القرن 20",
    "21st-century artists from Georgia (country)": "فنانون من جورجيا في القرن 21",
    "21st-century classical composers from Northern Ireland": "ملحنون كلاسيكيون من أيرلندا الشمالية في القرن 21",
    "21st-century dramatists and playwrights from Georgia (country)": "كتاب دراما ومسرح من جورجيا في القرن 21",
    "21st-century people from insular areas of the United States": "أشخاص من المناطق المعزولة في الولايات المتحدة في القرن 21",
    "21st-century politicians from insular areas of the United States": "سياسيون من المناطق المعزولة في الولايات المتحدة في القرن 21",
    "21st-century women from Georgia (country)": "نساء من جورجيا في القرن 21",
    "21st-century women from Northern Ireland": "نساء من أيرلندا الشمالية في القرن 21",
    "21st-century women politicians from insular areas of the United States": "سياسيات من المناطق المعزولة في الولايات المتحدة في القرن 21",
    "8th-century women from the Abbasid Caliphate": "نساء من الدولة العباسية في القرن 8",
    "9th-century women from the Abbasid Caliphate": "نساء من الدولة العباسية في القرن 9",
}


@pytest.mark.parametrize("category,expected", test_data_standard.items(), ids=test_data_standard.keys())
@pytest.mark.fast
def test_year_job_origin_resolver_more_1(category: str, expected: str) -> None:
    """Test resolve year job from countries function for test_data_standard."""
    result1 = resolve_year_job_from_countries(category)
    assert result1 == expected

    result2 = resolve_label_ar(category)
    assert result2 == expected


@pytest.mark.parametrize("category,expected", test_females_data.items(), ids=test_females_data.keys())
@pytest.mark.fast
def test_females_data_1(category: str, expected: str) -> None:
    """Test resolve year job from countries function for test_females_data."""
    result2 = resolve_label_ar(category)
    assert result2 == expected

    result1 = resolve_year_job_from_countries(category)
    assert result1 == expected


to_test = [
    ("test_year_job_origin_resolver_more_2", test_data_standard, resolve_year_job_from_countries),
    ("test_females_data_1", test_females_data, resolve_year_job_from_countries),
]

test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
