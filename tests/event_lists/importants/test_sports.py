#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data0 = {
    "Category:Sports sidebar templates": "تصنيف:قوالب أشرطة جانبية رياضية",
    "Category:Sports at multi-sport events sidebar templates": "تصنيف:قوالب أشرطة جانبية رياضية في الأحداث الرياضية المتعددة",
    "Category:Sports at the Summer Universiade": "تصنيف:ألعاب رياضية في الألعاب الجامعية الصيفية",
    "Category:sports by country": "تصنيف:ألعاب رياضية حسب البلد",
    "Category:sports by month": "تصنيف:ألعاب رياضية حسب الشهر",
    "Category:Sports in Westchester County, New York": "تصنيف:ألعاب رياضية في مقاطعة ويستتشستر (نيويورك)",
    "Category:Summer Olympics sports sidebar templates": "تصنيف:قوالب أشرطة جانبية ألعاب رياضية في الألعاب الأولمبية الصيفية",
    "Category:wheelchair sports": "تصنيف:ألعاب رياضية على الكراسي المتحركة",
    "Category:Winter Olympics sports sidebar templates": "تصنيف:قوالب أشرطة جانبية ألعاب رياضية في الألعاب الأولمبية الشتوية",
}

data1 = {
    "Category:1964 in American women's sports": "تصنيف:رياضات نسائية أمريكية في 1964",
    "Category:1972 in American women's sports": "تصنيف:رياضات نسائية أمريكية في 1972",
    "Category:2003 in Canadian women's sports": "تصنيف:رياضات نسائية كندية في 2003",
    "Category:2026 in American women's sports": "تصنيف:رياضات نسائية أمريكية في 2026",
    "Category:american women's sports": "تصنيف:رياضات نسائية أمريكية",
    "Category:canadian women's sports": "تصنيف:رياضات نسائية كندية",
    "Category:mexican women's sports": "تصنيف:رياضات نسائية مكسيكية",

    "Category:1550 in sports": "تصنيف:ألعاب رياضية في 1550",
    "Category:december 1550 in sports": "تصنيف:ألعاب رياضية في ديسمبر 1550",
    "Category:june 1550 in sports": "تصنيف:ألعاب رياضية في يونيو 1550",
    "Category:Sports leagues in Papua New Guinea": "تصنيف:دوريات رياضية في بابوا غينيا الجديدة",
    "Category:honduran people in sports": "تصنيف:هندوراسيون في ألعاب رياضية",
    "Category:Jewish sports": "تصنيف:ألعاب رياضية يهودية",
    "Category:surinamese sports federation": "تصنيف:الاتحاد السورينامي للرياضة",
    "Category:Women's basketball players in the United States by league": "تصنيف:لاعبات كرة سلة نسائية في الولايات المتحدة حسب الدوري",
    "Category:Women's soccer players in Australia by competition": "تصنيف:لاعبات كرة قدم نسائية في أستراليا حسب المنافسة",
    "Category:zaïrean wheelchair sports federation": "تصنيف:الاتحاد الزائيري للرياضة على الكراسي المتحركة",
}
data2 = {
    "Category:Women's sport by country and year": "تصنيف:رياضة نسوية حسب البلد حسب السنة",
    "Category:American women's sports by year": "تصنيف:رياضية أمريكية نسائية حسب السنة",
    "Category:American women's sports by decade": "تصنيف:رياضية أمريكية نسائية حسب العقد",
    "Category:1887 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1887",
    "Category:1889 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1889",
    "Category:1930 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1930",
    "Category:1931 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1931",
    "Category:1934 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1934",
    "Category:1938 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1938",
    "Category:1945 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1945",
    "Category:1946 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1946",
    "Category:1947 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1947",
    "Category:1948 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1948",
    "Category:1950 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1950",
    "Category:1951 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1951",
    "Category:1953 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1953",
    "Category:1954 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1954",
    "Category:1955 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1955",
    "Category:1956 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1956",
    "Category:1959 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1959",
    "Category:1961 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1961",
    "Category:1963 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1963",
    "Category:1964 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1964",
    "Category:1966 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1966",
    "Category:1967 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1967",
    "Category:1968 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1968",
    "Category:1970 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1970",
    "Category:1971 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1971",
    "Category:1973 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1973",
    "Category:1974 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1974",
    "Category:1975 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1975",
    "Category:1978 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1978",
    "Category:1979 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1979",
    "Category:1980 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1980",
    "Category:1982 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1982",
    "Category:1983 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1983",
    "Category:1984 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1984",
    "Category:1985 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1985",
    "Category:1986 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1986",
    "Category:1987 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1987",
    "Category:1989 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1989",
    "Category:1990 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1990",
    "Category:1991 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1991",
    "Category:1992 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1992",
    "Category:1993 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1993",
    "Category:1995 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1995",
    "Category:1996 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1996",
    "Category:1998 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 1998",
    "Category:2000 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2000",
    "Category:2001 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2001",
    "Category:2004 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2004",
    "Category:2005 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2005",
    "Category:2006 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2006",
    "Category:2007 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2007",
    "Category:2009 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2009",
    "Category:2010 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2010",
    "Category:2011 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2011",
    "Category:2012 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2012",
    "Category:2013 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2013",
    "Category:2014 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2014",
    "Category:2015 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2015",
    "Category:2016 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2016",
    "Category:2017 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2017",
    "Category:2018 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2018",
    "Category:2021 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2021",
    "Category:2022 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2022",
    "Category:2023 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2023",
    "Category:2024 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2024",
    "Category:2025 in American women's sports": "تصنيف:رياضية أمريكية نسائية في 2025",
    "Category:1880s in American women's sports": "تصنيف:رياضية أمريكية نسائية في عقد 1880",
    "Category:1930s in American women's sports": "تصنيف:رياضية أمريكية نسائية في عقد 1930",
    "Category:1940s in American women's sports": "تصنيف:رياضية أمريكية نسائية في عقد 1940",
    "Category:1950s in American women's sports": "تصنيف:رياضية أمريكية نسائية في عقد 1950",
    "Category:1960s in American women's sports": "تصنيف:رياضية أمريكية نسائية في عقد 1960",
    "Category:1970s in American women's sports": "تصنيف:رياضية أمريكية نسائية في عقد 1970",
    "Category:1980s in American women's sports": "تصنيف:رياضية أمريكية نسائية في عقد 1980",
    "Category:1990s in American women's sports": "تصنيف:رياضية أمريكية نسائية في عقد 1990",
    "Category:2010s in American women's sports": "تصنيف:رياضية أمريكية نسائية في عقد 2010",
    "Category:2020s in American women's sports": "تصنيف:رياضية أمريكية نسائية في عقد 2020",
    "Category:Canadian women's sports by year": "تصنيف:رياضية كندية نسائية حسب السنة",
    "Category:Canadian women's sports by decade": "تصنيف:رياضية كندية نسائية حسب العقد",
    "Category:1983 in Canadian women's sports": "تصنيف:رياضية كندية نسائية في 1983",
    "Category:2004 in Canadian women's sports": "تصنيف:رياضية كندية نسائية في 2004",
    "Category:2007 in Canadian women's sports": "تصنيف:رياضية كندية نسائية في 2007",
    "Category:2011 in Canadian women's sports": "تصنيف:رياضية كندية نسائية في 2011",
    "Category:2012 in Canadian women's sports": "تصنيف:رياضية كندية نسائية في 2012",
    "Category:2023 in Canadian women's sports": "تصنيف:رياضية كندية نسائية في 2023",
    "Category:1980s in Canadian women's sports": "تصنيف:رياضية كندية نسائية في عقد 1980",
    "Category:1990s in Canadian women's sports": "تصنيف:رياضية كندية نسائية في عقد 1990",
    "Category:2000s in Canadian women's sports": "تصنيف:رياضية كندية نسائية في عقد 2000",
    "Category:2010s in Canadian women's sports": "تصنيف:رياضية كندية نسائية في عقد 2010",
    "Category:2020s in Canadian women's sports": "تصنيف:رياضية كندية نسائية في عقد 2020",
    "Category:Mexican women's sports by year": "تصنيف:رياضية مكسيكية نسائية حسب السنة",
    "Category:Mexican women's sports by decade": "تصنيف:رياضية مكسيكية نسائية حسب العقد",
    "Category:1971 in Mexican women's sports": "تصنيف:رياضية مكسيكية نسائية في 1971",
    "Category:1974 in Mexican women's sports": "تصنيف:رياضية مكسيكية نسائية في 1974",
    "Category:2010 in Mexican women's sports": "تصنيف:رياضية مكسيكية نسائية في 2010",
    "Category:1970s in Mexican women's sports": "تصنيف:رياضية مكسيكية نسائية في عقد 1970",
    "Category:2010s in Mexican women's sports": "تصنيف:رياضية مكسيكية نسائية في عقد 2010",
}

to_test = [
    ("test_sports_data_0", data0),
    ("test_sports_data_1", data1),
    ("test_sports_data_2", data2),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
def test_sports_data_0(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
def test_sports_data_1(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
