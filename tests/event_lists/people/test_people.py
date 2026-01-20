import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data1 = {
    "People in arts occupations by nationality": "أشخاص في مهن فنية حسب الجنسية",
    "People of Ivorian descent": "أشخاص من أصل إيفواري",
    "Polish women by occupation": "بولنديات حسب المهنة",
    "Portuguese healthcare managers": "مدراء رعاية صحية برتغاليون",
    "Prisoners and detainees of Afghanistan": "سجناء ومعتقلون في أفغانستان",
    "Prisons in Afghanistan": "سجون في أفغانستان",
    "Scholars by subfield": "دارسون حسب الحقل الفرعي",
    "Women in business by nationality": "سيدات أعمال حسب الجنسية",
    "women in business": "سيدات أعمال",
}

data2 = {
    "Iranian nuclear medicine physicians": "أطباء طب نووي إيرانيون",
    "Israeli people of Northern Ireland descent": "إسرائيليون من أصل أيرلندي شمالي",
    "Ivorian diaspora in Asia": "شتات إيفواري في آسيا",
    "Medical doctors by specialty and nationality": "أطباء حسب التخصص والجنسية",
    "Multi-instrumentalists": "عازفون على عدة آلات",
    "People by nationality and status": "أشخاص حسب الجنسية والحالة",
}

data3 = {
    "Canadian nuclear medicine physicians": "أطباء طب نووي كنديون",
    "Croatian nuclear medicine physicians": "أطباء طب نووي كروات",
    "Expatriate male actors in New Zealand": "ممثلون ذكور مغتربون في نيوزيلندا",
    "Expatriate male actors": "ممثلون ذكور مغتربون",
    "German nuclear medicine physicians": "أطباء طب نووي ألمان",
    "Immigrants to New Zealand": "مهاجرون إلى نيوزيلندا",
    "Immigration to New Zealand": "الهجرة إلى نيوزيلندا",
    "Internees at the Sheberghan Prison": "معتقلون في سجن شيبرغان",
}


data4 = {
    "Afghan diplomats": "دبلوماسيون أفغان",
    "Ambassadors of Afghanistan": "سفراء أفغانستان",
    "Ambassadors of the Ottoman Empire": "سفراء الدولة العثمانية",
    "Ambassadors to the Ottoman Empire": "سفراء لدى الدولة العثمانية",
    "American nuclear medicine physicians": "أطباء طب نووي أمريكيون",
    "Argentine multi-instrumentalists": "عازفون على عدة آلات أرجنتينيون",
    "Attacks on diplomatic missions": "هجمات على بعثات دبلوماسية",
    "Australian Internet celebrities": "مشاهير إنترنت أستراليون",
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
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_people_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data3.items(), ids=data3.keys())
@pytest.mark.fast
def test_people_3(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data4.items(), ids=data4.keys())
@pytest.mark.fast
def test_people_4(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
