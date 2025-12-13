#
import pytest

from ArWikiCats import resolve_arabic_category_label

data = {
    "Category:Gymnastics organizations": "تصنيف:منظمات جمباز",
    "Category:Publications by format": "تصنيف:منشورات حسب التنسيق",
    "Category:Publications disestablished in 1946": "تصنيف:منشورات انحلت في 1946",
    "Category:Subfields by academic discipline": "تصنيف:حقول فرعية حسب التخصص الأكاديمي",
    "Category:Women's organizations based in Cuba": "تصنيف:منظمات نسائية مقرها في كوبا",
    "Category:Women's universities and colleges in India": "تصنيف:جامعات نسائية وكليات في الهند",

}


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_institutions(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


data_2 = {
    "Category:Indonesian women singers by century": "تصنيف:مغنبات إندونيسيات حسب القرن",
    "Category:Iranian women singers by century": "تصنيف:مغنبات إيرانيات حسب القرن",
    "Category:20th-century Italian women singers": "تصنيف:مغنبات إيطاليات في القرن 20",
    "Category:Bulgarian women singers by century": "تصنيف:مغنبات بلغاريات حسب القرن",
    "Category:20th-century Panamanian women singers": "تصنيف:مغنبات بنميات في القرن 20",
    "Category:Puerto Rican women singers by century": "تصنيف:مغنبات بورتوريكيات حسب القرن",
    "Category:Women singers by former country": "تصنيف:مغنبات حسب البلد السابق",
    "Category:Women singers by ethnicity": "تصنيف:مغنبات حسب المجموعة العرقية",
    "Category:Women singers by genre": "تصنيف:مغنبات حسب النوع الفني",
    "Category:19th-century Sudanese women singers": "تصنيف:مغنبات سودانيات في القرن 19",
    "Category:Ghanaian women singers by century": "تصنيف:مغنبات غانيات حسب القرن",
    "Category:Finnish women singers by century": "تصنيف:مغنبات فنلنديات حسب القرن",
    "Category:17th-century women singers by nationality": "تصنيف:مغنبات في القرن 17 حسب الجنسية",
    "Category:18th-century women singers by nationality": "تصنيف:مغنبات في القرن 18 حسب الجنسية",
    "Category:Cuban women singers by century": "تصنيف:مغنبات كوبيات حسب القرن",
    "Category:20th-century Lithuanian women singers": "تصنيف:مغنبات ليتوانيات في القرن 20",
    "Category:19th-century Mexican women singers": "تصنيف:مغنبات مكسيكيات في القرن 19",
    "Category:Women singers from the Russian Empire": "تصنيف:مغنبات من الإمبراطورية الروسية",
    "Category:Women singers from the Holy Roman Empire": "تصنيف:مغنبات من الإمبراطورية الرومانية المقدسة",
    "Category:18th-century women singers from the Holy Roman Empire": "تصنيف:مغنبات من الإمبراطورية الرومانية المقدسة القرن 18",
    "Category:Women singers from Georgia (country) by century": "تصنيف:مغنبات من جورجيا حسب القرن",
    "Category:Women singers from the Kingdom of Prussia": "تصنيف:مغنبات من مملكة بروسيا",
    "Category:Norwegian women singers by century": "تصنيف:مغنبات نرويجيات حسب القرن",
    "Category:Austrian women singers by century": "تصنيف:مغنبات نمساويات حسب القرن",
    "Category:Jewish women singers": "تصنيف:مغنبات يهوديات",
}


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_women_singers(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected
