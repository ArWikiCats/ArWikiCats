#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data0 = {
    "Category:Sports at the Summer Universiade": "تصنيف:ألعاب رياضية في الألعاب الجامعية الصيفية",
    "Category:sports by country": "تصنيف:ألعاب رياضية حسب البلد",
    "Category:sports by month": "تصنيف:ألعاب رياضية حسب الشهر",
    "Category:Sports in Westchester County, New York": "تصنيف:ألعاب رياضية في مقاطعة ويستتشستر (نيويورك)",
    "Category:Summer Olympics sports sidebar templates": "تصنيف:قوالب أشرطة جانبية ألعاب رياضية في الألعاب الأولمبية الصيفية",
    "Category:wheelchair sports": "تصنيف:ألعاب رياضية على الكراسي المتحركة",
    "Category:Winter Olympics sports sidebar templates": "تصنيف:قوالب أشرطة جانبية ألعاب رياضية في الألعاب الأولمبية الشتوية",
}

data1 = {
    "Category:1550 in sports": "تصنيف:ألعاب رياضية في 1550",
    "Category:december 1550 in sports": "تصنيف:ألعاب رياضية في ديسمبر 1550",
    "Category:june 1550 in sports": "تصنيف:ألعاب رياضية في يونيو 1550",
    "Category:Sports at multi-sport events sidebar templates": "تصنيف:قوالب أشرطة جانبية رياضية في الأحداث الرياضية المتعددة",
    "Category:Sports leagues in Papua New Guinea": "تصنيف:دوريات رياضية في بابوا غينيا الجديدة",
    "Category:Sports sidebar templates": "تصنيف:قوالب أشرطة جانبية رياضية",
    "Category:1964 in American women's sports": "تصنيف:رياضات نسائية أمريكية في 1964",
    "Category:1972 in American women's sports": "تصنيف:رياضات نسائية أمريكية في 1972",
    "Category:2003 in Canadian women's sports": "تصنيف:رياضات نسائية كندية في 2003",
    "Category:2026 in American women's sports": "تصنيف:رياضات نسائية أمريكية في 2026",
    "Category:american women's sports": "تصنيف:رياضات نسائية أمريكية",
    "Category:canadian women's sports": "تصنيف:رياضات نسائية كندية",
    "Category:honduran people in sports": "تصنيف:هندوراسيون في ألعاب رياضية",
    "Category:Jewish sports": "تصنيف:ألعاب رياضية يهودية",
    "Category:mexican women's sports": "تصنيف:رياضات نسائية مكسيكية",
    "Category:surinamese sports federation": "تصنيف:الاتحاد السورينامي للرياضة",
    "Category:Women's basketball players in the United States by league": "تصنيف:لاعبات كرة سلة نسائية في الولايات المتحدة حسب الدوري",
    "Category:Women's soccer players in Australia by competition": "تصنيف:لاعبات كرة قدم نسائية في أستراليا حسب المنافسة",
    "Category:zaïrean wheelchair sports federation": "تصنيف:الاتحاد الزائيري للرياضة على الكراسي المتحركة",
}

to_test = [
    ("test_sports_data_0", data0),
    ("test_sports_data_1", data1),
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

    # dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
