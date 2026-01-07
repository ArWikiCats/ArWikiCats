#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data_1 = {
    "Category:20th-century American Buddhist nuns": "تصنيف:راهبات بوذيات أمريكيات في القرن 20",
    "Category:21st-century American Buddhist nuns": "تصنيف:راهبات بوذيات أمريكيات في القرن 21",
    "Category:Chilean men shot putters": "تصنيف:لاعبو دفع ثقل تشيليون",
    "Category:Somalian men sprinters": "تصنيف:عداؤون سريعون صوماليون",
    "Category:Sculptures of men in England": "تصنيف:منحوتات في رجال في إنجلترا",
    "Category:Sculptures of men in London": "تصنيف:منحوتات في رجال في لندن"
}

data_2 = {
    "10th-century Buddhist nuns": "تصنيف:بوذيون في القرن 10",
    "10th-century Christian nuns": "تصنيف:مسيحيون في القرن 10",
    "11th-century Buddhist nuns": "تصنيف:بوذيون في القرن 11",
    "11th-century Christian nuns": "تصنيف:مسيحيون في القرن 11",
    "12th-century Buddhist nuns": "تصنيف:بوذيون في القرن 12",
    "12th-century Christian nuns": "تصنيف:مسيحيون في القرن 12",
    "13th-century Buddhist nuns": "تصنيف:بوذيون في القرن 13",
    "13th-century Christian nuns": "تصنيف:مسيحيون في القرن 13",
    "14th-century Buddhist nuns": "تصنيف:بوذيون في القرن 14",
    "14th-century Christian nuns": "تصنيف:مسيحيون في القرن 14",
    "15th-century Buddhist nuns": "تصنيف:بوذيون في القرن 15",
    "15th-century Christian nuns": "تصنيف:مسيحيون في القرن 15",
    "16th-century Buddhist nuns": "تصنيف:بوذيون في القرن 16",
    "16th-century Christian nuns": "تصنيف:مسيحيون في القرن 16",
    "17th-century Buddhist nuns": "تصنيف:بوذيون في القرن 17",
    "17th-century Christian nuns": "تصنيف:مسيحيون في القرن 17",
    "18th-century Buddhist nuns": "تصنيف:بوذيون في القرن 18",
    "18th-century Christian nuns": "تصنيف:مسيحيون في القرن 18",
    "19th-century Anglican nuns": "تصنيف:أنجليكيون في القرن 19",
    "19th-century Australian Christian nuns": "تصنيف:مسيحيون أستراليون في القرن 19",
    "19th-century British Anglican nuns": "تصنيف:أنجليكيون بريطانيون في القرن 19",
    "19th-century Buddhist nuns": "تصنيف:بوذيون في القرن 19",
    "19th-century Christian nuns": "تصنيف:مسيحيون في القرن 19",
    "1st-century Buddhist nuns": "تصنيف:بوذيون في القرن 1",
    "20th-century Anglican nuns": "تصنيف:أنجليكيون في القرن 20",
    "20th-century Australian Christian nuns": "تصنيف:مسيحيون أستراليون في القرن 20",
    "20th-century British Anglican nuns": "تصنيف:أنجليكيون بريطانيون في القرن 20",
    "20th-century Buddhist nuns": "تصنيف:بوذيون في القرن 20",
    "20th-century Christian nuns": "تصنيف:مسيحيون في القرن 20",
    "21st-century Anglican nuns": "تصنيف:أنجليكيون في القرن 21",
    "21st-century Australian Christian nuns": "تصنيف:مسيحيون أستراليون في القرن 21",
    "21st-century British Anglican nuns": "تصنيف:أنجليكيون بريطانيون في القرن 21",
    "21st-century Buddhist nuns": "تصنيف:بوذيون في القرن 21",
    "21st-century Christian nuns": "تصنيف:مسيحيون في القرن 21",
    "3rd-century BC Buddhist nuns": "تصنيف:بوذيون في القرن 3 ق م",
    "4th-century Buddhist nuns": "تصنيف:بوذيون في القرن 4",
    "4th-century Christian nuns": "تصنيف:مسيحيون في القرن 4",
    "5th-century Buddhist nuns": "تصنيف:بوذيون في القرن 5",
    "5th-century Christian nuns": "تصنيف:مسيحيون في القرن 5",
    "6th-century Buddhist nuns": "تصنيف:بوذيون في القرن 6",
    "6th-century Christian nuns": "تصنيف:مسيحيون في القرن 6",
    "7th-century Buddhist nuns": "تصنيف:بوذيون في القرن 7",
    "7th-century Christian nuns": "تصنيف:مسيحيون في القرن 7",
    "8th-century Buddhist nuns": "تصنيف:بوذيون في القرن 8",
    "8th-century Christian nuns": "تصنيف:مسيحيون في القرن 8",
    "9th-century Buddhist nuns": "تصنيف:بوذيون في القرن 9",
    "9th-century Christian nuns": "تصنيف:مسيحيون في القرن 9",
    "American Buddhist nuns": "تصنيف:بوذيون أمريكيون",
    "American Christian nuns": "تصنيف:مسيحيون أمريكيون",
    "American Hindu nuns": "تصنيف:هندوس أمريكيون",
    "Australian Christian nuns": "تصنيف:مسيحيون أستراليون",
    "Belgian Buddhist nuns": "تصنيف:بوذيون بلجيكيون",
    "British Anglican nuns": "تصنيف:أنجليكيون بريطانيون",
    "British Buddhist nuns": "تصنيف:بوذيون بريطانيون",
    "Buddhist nuns by century": "تصنيف:بوذيون حسب القرن",
    "Buddhist nuns by nationality": "تصنيف:بوذيون حسب الجنسية",
    "Buddhist nuns of Nara period": "تصنيف:بوذيون من فترة نارا",
    "Chinese Buddhist nuns": "تصنيف:بوذيون صينيون",
    "Christian nuns by century": "تصنيف:مسيحيون حسب القرن",
    "Fictional Buddhist nuns": "تصنيف:بوذيون خياليون",
    "Fictional Christian nuns": "تصنيف:مسيحيون خياليون",
    "French Buddhist nuns": "تصنيف:بوذيون فرنسيون",
    "German Buddhist nuns": "تصنيف:بوذيون ألمان",
    "Indian Buddhist nuns": "تصنيف:بوذيون هنود",
    "Indian Hindu nuns": "تصنيف:هندوس هنود",
    "Indonesian Buddhist nuns": "تصنيف:بوذيون إندونيسيون",
    "Irish Buddhist nuns": "تصنيف:بوذيون أيرلنديون",
    "Italian Buddhist nuns": "تصنيف:بوذيون إيطاليون",
    "Japanese Buddhist nuns by period": "تصنيف:بوذيون يابانيون حسب الحقبة",
    "Japanese Buddhist nuns": "تصنيف:بوذيون يابانيون",
    "Korean Buddhist nuns": "تصنيف:بوذيون كوريون",
    "Nepalese Buddhist nuns": "تصنيف:بوذيون نيباليون",
    "Scottish Buddhist nuns": "تصنيف:بوذيون إسكتلنديون",
    "Singaporean Buddhist nuns": "تصنيف:بوذيون سنغافوريون",
    "South Korean Buddhist nuns": "تصنيف:بوذيون كوريون جنوبيون",
    "Taiwanese Buddhist nuns": "تصنيف:بوذيون تايوانيون",
    "Thai Buddhist nuns": "تصنيف:بوذيون تايلنديون",
    "Vietnamese Buddhist nuns": "تصنيف:بوذيون فيتناميون",
}

data_3 = {

}

to_test = [
    ("test_nuns_1", data_1),
    ("test_nuns_2", data_2),
    ("test_nuns_3", data_3),
]


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_nuns_1(category: str, expected: str) -> None:
    """
    pytest tests/event_lists/test_2.py::test_nuns_1
    """
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_nuns_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
@pytest.mark.fast
def test_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
