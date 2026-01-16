#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data = {
    "Category:Gymnastics organizations": "تصنيف:منظمات جمباز",
    "Category:Publications by format": "تصنيف:منشورات حسب التنسيق",
    "Category:Publications disestablished in 1946": "تصنيف:منشورات انحلت في 1946",
    "Category:Subfields by academic discipline": "تصنيف:حقول فرعية حسب التخصص الأكاديمي",
    "Category:Women's organizations based in Cuba": "تصنيف:منظمات نسائية مقرها في كوبا",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_institutions(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


data_2 = {
    "Category:Indonesian women singers by century": "تصنيف:مغنيات إندونيسيات حسب القرن",
    "Category:Iranian women singers by century": "تصنيف:مغنيات إيرانيات حسب القرن",
    "Category:20th-century Italian women singers": "تصنيف:مغنيات إيطاليات في القرن 20",
    "Category:Bulgarian women singers by century": "تصنيف:مغنيات بلغاريات حسب القرن",
    "Category:20th-century Panamanian women singers": "تصنيف:مغنيات بنميات في القرن 20",
    "Category:Puerto Rican women singers by century": "تصنيف:مغنيات بورتوريكيات حسب القرن",
    "Category:Women singers by former country": "تصنيف:مغنيات حسب البلد السابق",
    "Category:Women singers by ethnicity": "تصنيف:مغنيات حسب المجموعة العرقية",
    "Category:Women singers by genre": "تصنيف:مغنيات حسب النوع الفني",
    "Category:19th-century Sudanese women singers": "تصنيف:مغنيات سودانيات في القرن 19",
    "Category:Ghanaian women singers by century": "تصنيف:مغنيات غانيات حسب القرن",
    "Category:Finnish women singers by century": "تصنيف:مغنيات فنلنديات حسب القرن",
    "Category:17th-century women singers by nationality": "تصنيف:مغنيات في القرن 17 حسب الجنسية",
    "Category:18th-century women singers by nationality": "تصنيف:مغنيات في القرن 18 حسب الجنسية",
    "Category:Cuban women singers by century": "تصنيف:مغنيات كوبيات حسب القرن",
    "Category:20th-century Lithuanian women singers": "تصنيف:مغنيات ليتوانيات في القرن 20",
    "Category:19th-century Mexican women singers": "تصنيف:مغنيات مكسيكيات في القرن 19",
    "Category:Women singers from the Russian Empire": "تصنيف:مغنيات من الإمبراطورية الروسية",
    "Category:Women singers from the Holy Roman Empire": "تصنيف:مغنيات من الإمبراطورية الرومانية المقدسة",
    "Category:18th-century women singers from the Holy Roman Empire": "تصنيف:مغنيات من الإمبراطورية الرومانية المقدسة في القرن 18",
    "Category:Women singers from Georgia (country) by century": "تصنيف:مغنيات من جورجيا حسب القرن",
    "Category:Women singers from the Kingdom of Prussia": "تصنيف:مغنيات من مملكة بروسيا",
    "Category:Norwegian women singers by century": "تصنيف:مغنيات نرويجيات حسب القرن",
    "Category:Austrian women singers by century": "تصنيف:مغنيات نمساويات حسب القرن",
    "Category:Jewish women singers": "تصنيف:مغنيات يهوديات",
}


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.skip2
def test_women_singers(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_institutions", data),
    ("test_women_singers", data_2),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    # dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
