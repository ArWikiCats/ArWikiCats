import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data1 = {
    "Category:People in arts occupations by nationality": "تصنيف:أشخاص في مهن فنية حسب الجنسية",
    "Category:People of Ivorian descent": "تصنيف:أشخاص من أصل إيفواري",
    "Category:Polish women by occupation": "تصنيف:بولنديات حسب المهنة",
    "Category:Portuguese healthcare managers": "تصنيف:مدراء رعاية صحية برتغاليون",
    "Category:Prisoners and detainees of Afghanistan": "تصنيف:سجناء ومعتقلون في أفغانستان",
    "Category:Prisons in Afghanistan": "تصنيف:سجون في أفغانستان",
    "Category:Scholars by subfield": "تصنيف:دارسون حسب الحقل الفرعي",
    "Category:Women in business by nationality": "تصنيف:سيدات أعمال حسب الجنسية",
    "Category:women in business": "تصنيف:سيدات أعمال",
}

data2 = {
    "Category:Iranian nuclear medicine physicians": "تصنيف:أطباء طب نووي إيرانيون",
    "Category:Israeli people of Northern Ireland descent": "تصنيف:إسرائيليون من أصل أيرلندي شمالي",
    "Category:Ivorian diaspora in Asia": "تصنيف:شتات إيفواري في آسيا",
    "Category:Medical doctors by specialty and nationality": "تصنيف:أطباء حسب التخصص والجنسية",
    "Category:Multi-instrumentalists": "تصنيف:عازفون على عدة آلات",
    "Category:People by nationality and status": "تصنيف:أشخاص حسب الجنسية والحالة",
}

data3 = {
    "Category:Canadian nuclear medicine physicians": "تصنيف:أطباء طب نووي كنديون",
    "Category:Croatian nuclear medicine physicians": "تصنيف:أطباء طب نووي كروات",
    "Category:Expatriate male actors in New Zealand": "تصنيف:ممثلون ذكور مغتربون في نيوزيلندا",
    "Category:Expatriate male actors": "تصنيف:ممثلون ذكور مغتربون",
    "Category:German nuclear medicine physicians": "تصنيف:أطباء طب نووي ألمان",
    "Category:Immigrants to New Zealand": "تصنيف:مهاجرون إلى نيوزيلندا",
    "Category:Immigration to New Zealand": "تصنيف:الهجرة إلى نيوزيلندا",
    "Category:Internees at the Sheberghan Prison": "تصنيف:معتقلون في سجن شيبرغان",
}


data4 = {
    "Category:Afghan diplomats": "تصنيف:دبلوماسيون أفغان",
    "Category:Ambassadors of Afghanistan": "تصنيف:سفراء أفغانستان",
    "Category:Ambassadors of the Ottoman Empire": "تصنيف:سفراء الدولة العثمانية",
    "Category:Ambassadors to the Ottoman Empire": "تصنيف:سفراء لدى الدولة العثمانية",
    "Category:American nuclear medicine physicians": "تصنيف:أطباء طب نووي أمريكيون",
    "Category:Argentine multi-instrumentalists": "تصنيف:عازفون على عدة آلات أرجنتينيون",
    "Category:Attacks on diplomatic missions": "تصنيف:هجمات على بعثات دبلوماسية",
    "Category:Australian Internet celebrities": "تصنيف:مشاهير إنترنت أستراليون",
}

to_test = [
    ("test_people_1", data1),
    ("test_people_2", data2),
    ("test_people_3", data3),
    ("test_people_4", data4),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_people_1(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_people_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data3.items(), ids=data3.keys())
@pytest.mark.fast
def test_people_3(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data4.items(), ids=data4.keys())
@pytest.mark.fast
def test_people_4(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
