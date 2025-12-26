#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test, dump_same_and_not_same

from ArWikiCats import resolve_arabic_category_label

data0 = {
    "Category:American women's sports": "تصنيف:رياضات نسائية أمريكية",
    "Category:women's sports leagues in uzbekistan": "تصنيف:دوريات رياضات نسائية في أوزبكستان",
    "Category:Women's sports organizations in the United States": "تصنيف:منظمات رياضات نسائية في الولايات المتحدة",
    "Category:Women's sports teams in Cuba": "تصنيف:فرق رياضات نسائية في كوبا",
    "Category:Women's sports in United States by state": "تصنيف:رياضات نسائية في الولايات المتحدة حسب الولاية",
    "Category:Women's sports by dependent territory": "تصنيف:رياضات نسائية حسب الأقاليم التابعة",
    "Category:Women's sports seasons by continent": "تصنيف:مواسم رياضات نسائية حسب القارة",
    "Category:Women's sports seasons": "تصنيف:مواسم رياضات نسائية",
    "Category:women's sports clubs": "تصنيف:أندية رياضية نسائية",
    "Category:women's sports competitions": "تصنيف:منافسات رياضية نسائية",
    "Category:women's sports leagues": "تصنيف:دوريات رياضية نسائية",
    "Category:women's sports organizations": "تصنيف:منظمات رياضية نسائية",
    "Category:women's sports teams": "تصنيف:فرق رياضية نسائية",
    "Category:national women's sports teams": "تصنيف:منتخبات رياضية وطنية نسائية",
    "Category:college women's sports teams in united states": "تصنيف:فرق رياضات الكليات للسيدات في الولايات المتحدة",

    "Category:mexican women's sports": "تصنيف:رياضات نسائية مكسيكية",
    "Category:canadian women's sports": "تصنيف:رياضات نسائية كندية",
    "Category:american women's sports": "تصنيف:رياضات نسائية أمريكية",
    "Category:2026 in American women's sports": "تصنيف:رياضات نسائية أمريكية في 2026",
    "Category:1964 in American women's sports": "تصنيف:رياضات نسائية أمريكية في 1964",
    "Category:1972 in American women's sports": "تصنيف:رياضات نسائية أمريكية في 1972",
    "Category:2003 in Canadian women's sports": "تصنيف:رياضات نسائية كندية في 2003",
    "Category:Defunct women's sports clubs and teams": "",
    "Category:Women's sport by continent and period": "تصنيف:رياضة نسائية حسب القارة والحقبة",
    "Category:Women's sport by period": "تصنيف:رياضة نسائية حسب الحقبة",
    "Category:Women's sport in Mexico City": "تصنيف:رياضة نسائية في مدينة مكسيكو",
    "Category:Women's sport in Oceania by period": "تصنيف:رياضة نسائية في أوقيانوسيا حسب الحقبة",
}

data1 = {
    "Category:Summer Olympics sports navigational boxes": "تصنيف:صناديق تصفح الرياضة في الألعاب الأولمبية الصيفية",
    "Category:Olympic sports navigational boxes": "تصنيف:صناديق تصفح الرياضة في الألعاب الأولمبية",
    "Category:Winter Olympics sports sidebar templates": "تصنيف:قوالب أشرطة جانبية ألعاب رياضية في الألعاب الأولمبية الشتوية",
    "Category:Summer Olympics sports sidebar templates": "تصنيف:قوالب أشرطة جانبية ألعاب رياضية في الألعاب الأولمبية الصيفية",
    "Category:Winter Olympics sports templates": "تصنيف:قوالب ألعاب رياضية في الألعاب الأولمبية الشتوية",
    "Category:Summer Olympics sports templates": "تصنيف:قوالب الألعاب الأولمبية الصيفية الرياضية",
    "Category:Former Olympic sports": "تصنيف:ألعاب أولمبية سابقة",
    "Category:Ancient Olympic sports": "تصنيف:رياضات أولمبية قديمة",
    "Category:Summer Olympic sports": "تصنيف:رياضات الألعاب الأولمبية الصيفية",
    "Category:Olympic sports": "تصنيف:ألعاب رياضية أولمبية",
}

data2 = {
    "Category:Summer Olympics sidebar templates": "تصنيف:قوالب أشرطة جانبية الألعاب الأولمبية الصيفية",
    "Category:Azerbaijan sports navigational boxes": "تصنيف:صناديق تصفح الرياضة في أذربيجان",
    "Category:Austria sports navigational boxes": "تصنيف:صناديق تصفح الرياضة في النمسا",
    "Category:Winter Olympics sports navigational boxes": "تصنيف:صناديق تصفح الرياضة في الألعاب الأولمبية الشتوية",
    "Category:wheelchair sports": "تصنيف:ألعاب رياضية على الكراسي المتحركة",
    "Category:Sports sidebar templates": "تصنيف:قوالب أشرطة جانبية ألعاب رياضية",
    "Category:Sports at multi-sport events sidebar templates": "تصنيف:قوالب أشرطة جانبية ألعاب رياضية في الأحداث الرياضية المتعددة",
    "Category:Sports at the Summer Universiade": "تصنيف:ألعاب رياضية في الألعاب الجامعية الصيفية",
    "Category:sports by country": "تصنيف:ألعاب رياضية حسب البلد",
    "Category:sports by month": "تصنيف:ألعاب رياضية حسب الشهر",
    "Category:Sports in Westchester County, New York": "تصنيف:ألعاب رياضية في مقاطعة ويستتشستر (نيويورك)",
}

to_test = [
    ("test_sports2_data_0", data0),
    ("test_sports2_data_1", data1),
    ("test_sports2_data_2", data2),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
def test_sports2_data_0(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
def test_sports2_data_1(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
def test_sports2_data_2(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)
    # dump_same_and_not_same(data, diff_result, name, True)
    dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
