#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

data = {
    "Gymnastics organizations": "منظمات جمباز",
    "Publications by format": "منشورات حسب التنسيق",
    "Publications disestablished in 1946": "منشورات انحلت في 1946",
    "Subfields by academic discipline": "حقول فرعية حسب التخصص الأكاديمي",
    "Women's organizations based in Cuba": "منظمات نسائية مقرها في كوبا",
}


data_2 = {
    "Indonesian women singers by century": "مغنيات إندونيسيات حسب القرن",
    "Iranian women singers by century": "مغنيات إيرانيات حسب القرن",
    "20th-century Italian women singers": "مغنيات إيطاليات في القرن 20",
    "Bulgarian women singers by century": "مغنيات بلغاريات حسب القرن",
    "20th-century Panamanian women singers": "مغنيات بنميات في القرن 20",
    "Puerto Rican women singers by century": "مغنيات بورتوريكيات حسب القرن",
    "Women singers by former country": "مغنيات حسب البلد السابق",
    "Women singers by ethnicity": "مغنيات حسب المجموعة العرقية",
    "Women singers by genre": "مغنيات حسب النوع الفني",
    "19th-century Sudanese women singers": "مغنيات سودانيات في القرن 19",
    "Ghanaian women singers by century": "مغنيات غانيات حسب القرن",
    "Finnish women singers by century": "مغنيات فنلنديات حسب القرن",
    "17th-century women singers by nationality": "مغنيات في القرن 17 حسب الجنسية",
    "18th-century women singers by nationality": "مغنيات في القرن 18 حسب الجنسية",
    "Cuban women singers by century": "مغنيات كوبيات حسب القرن",
    "20th-century Lithuanian women singers": "مغنيات ليتوانيات في القرن 20",
    "19th-century Mexican women singers": "مغنيات مكسيكيات في القرن 19",
    "Women singers from the Russian Empire": "مغنيات من الإمبراطورية الروسية",
    "Women singers from the Holy Roman Empire": "مغنيات من الإمبراطورية الرومانية المقدسة",
    "18th-century women singers from the Holy Roman Empire": "مغنيات من الإمبراطورية الرومانية المقدسة في القرن 18",
    "Women singers from Georgia (country) by century": "مغنيات من جورجيا حسب القرن",
    "Women singers from the Kingdom of Prussia": "مغنيات من مملكة بروسيا",
    "Norwegian women singers by century": "مغنيات نرويجيات حسب القرن",
    "Austrian women singers by century": "مغنيات نمساويات حسب القرن",
    "Jewish women singers": "مغنيات يهوديات",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_institutions(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_women_singers(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_institutions", data),
    ("test_women_singers", data_2),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
