
import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test
from ArWikiCats import resolve_label_ar

test_data_0 = {
    "2020s Taiwanese television series debuts": "مسلسلات تلفزيونية تايوانية بدأ عرضها في عقد 2020",
    "2000s Singaporean television series debuts": "مسلسلات تلفزيونية سنغافورية بدأ عرضها في عقد 2000",
    "1950s Scottish television series debuts": "مسلسلات تلفزيونية إسكتلندية بدأ عرضها في عقد 1950",

    "14th-century lords of Monaco": "لوردات موناكو في القرن 14",
    "15th-century lords of Monaco": "لوردات موناكو القرن 15",
    "16th-century lords of Monaco": "لوردات موناكو القرن 16",
    "17th-century lords of Monaco": "لوردات موناكو القرن 17",

    "1st-century BC Kings of Bithynia": "ملوك بيثينيا القرن 1 ق م",
    "20th-century House of Habsburg": "آل هابسبورغ القرن 20",
    "5th-century BC kings of Tyre": "ملوك صور القرن 5 ق م",

}

test_data_1 ={
    "20th-century Islamic terrorist incidents": "حوادث إرهابية منسوبة للمسلمين القرن 20",
    "21st-century terrorist incidents in Denmark": "حوادث إرهابية في الدنمارك القرن 21",
    "21st-century Islamic terrorist incidents": "حوادث إرهابية منسوبة للمسلمين القرن 21",
    "13th-century Roman Catholic archbishops in Ireland": "رؤساء أساقفة رومان كاثوليك في أيرلندا في القرن 13",
    "16th century music": "الموسيقى في القرن 16",
    "16th century theatre": "المسرح في القرن 16",
    "17th century music": "الموسيقى في القرن 17",
    "17th century theatre": "المسرح في القرن 17",
    "1980s Christmas albums": "ألبومات عيد الميلاد عقد 1980",
    "20th century religious buildings": "مبان دينية القرن 20",
    "20th century roman catholic church buildings": "مبان كنائس رومانية كاثوليكية القرن 20",
    "20th-century railway accidents": "حوادث سكك حديد في القرن 20",
    "21st-century military alliances": "تحالفات عسكرية في القرن 21",
    "Deaths by drone strikes": "وفيات بواسطة هجمات الطائرات بدون طيار",
    "20th-century executions by Gambia": "إعدامات في غامبيا في القرن 20",
    "21st-century executions by Alabama": "إعدامات في ألاباما في القرن 21",
    "21st-century executions by Somalia": "إعدامات في الصومال في القرن 21",
    "8th-century executions by Umayyad Caliphate": "إعدامات في الدولة الأموية في القرن 8",
    "19th-century executions by Spain": "إعدامات في إسبانيا في القرن 19",
    "Qualification for 1968 Summer Olympics": "تصفيات مؤهلة إلى الألعاب الأولمبية الصيفية 1968",
    "Qualification for the 2026 Winter Olympics": "تصفيات مؤهلة إلى الألعاب الأولمبية الشتوية 2026",
    "Works by musicians from Northern Ireland": "أعمال موسيقيون من أيرلندا الشمالية",
    "21st-century men from Northern Ireland": "رجال من أيرلندا الشمالية في القرن 21",
    "20th-century men from Northern Ireland": "رجال من أيرلندا الشمالية في القرن 20"
}


@pytest.mark.parametrize("category, expected", test_data_0.items(), ids=test_data_0.keys())
@pytest.mark.fast
def test_mk3_skips_test_data_0(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_1.items(), ids=test_data_1.keys())
@pytest.mark.fast
def test_mk3_skips_test_data_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


to_test = [
    ("test_mk3_skips_test_data_0", test_data_0),
    ("test_mk3_skips_test_data_1", test_data_1),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, expected, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
