#
import pytest
from load_one_data import dump_diff, one_dump_test, dump_same_and_not_same, dump_diff_text

from ArWikiCats import resolve_label_ar

test_jesuits_1 = {
    "16th-century Austrian Jesuits": "مبتكرون نمساويون في القرن 16",
    "16th-century Dutch Jesuits": "مبتكرون هولنديون في القرن 16",
    "16th-century English Jesuits": "مبتكرون إنجليز في القرن 16",
    "16th-century German Jesuits": "مبتكرون ألمان في القرن 16",
    "16th-century Hungarian Jesuits": "مبتكرون مجريون في القرن 16",
    "16th-century Indian Jesuits": "مبتكرون هنود في القرن 16",
    "17th-century Austrian Jesuits": "مبتكرون نمساويون في القرن 17",
    "17th-century Canadian Jesuits": "مبتكرون كنديون في القرن 17",
    "17th-century Dutch Jesuits": "مبتكرون هولنديون في القرن 17",
    "17th-century German Jesuits": "مبتكرون ألمان في القرن 17",
    "17th-century Hungarian Jesuits": "مبتكرون مجريون في القرن 17",
    "17th-century Indian Jesuits": "مبتكرون هنود في القرن 17",
    "18th-century Austrian Jesuits": "مبتكرون نمساويون في القرن 18",
    "18th-century Chilean Jesuits": "مبتكرون تشيليون في القرن 18",
    "17th-century Peruvian Jesuits": "مبتكرون بيرويون في القرن 17",
    "17th-century Welsh Jesuits": "مبتكرون ويلزيون في القرن 17",
    "18th-century Croatian Jesuits": "مبتكرون كروات في القرن 18",
    "18th-century German Jesuits": "مبتكرون ألمان في القرن 18",
    "18th-century Peruvian Jesuits": "مبتكرون بيرويون في القرن 18",
    "18th-century Portuguese Jesuits": "مبتكرون برتغاليون في القرن 18",
    "18th-century Spanish Jesuits": "مبتكرون إسبان في القرن 18",
    "19th-century Austrian Jesuits": "مبتكرون نمساويون في القرن 19",
    "19th-century Belgian Jesuits": "مبتكرون بلجيكيون في القرن 19",
    "19th-century Canadian Jesuits": "مبتكرون كنديون في القرن 19",
    "19th-century Dutch Jesuits": "مبتكرون هولنديون في القرن 19",
    "19th-century German Jesuits": "مبتكرون ألمان في القرن 19",
    "19th-century Irish Jesuits": "مبتكرون أيرلنديون في القرن 19",
    "19th-century Italian Jesuits": "مبتكرون إيطاليون في القرن 19",
    "19th-century Polish Jesuits": "مبتكرون بولنديون في القرن 19",
    "19th-century Spanish Jesuits": "مبتكرون إسبان في القرن 19",
    "20th-century Belgian Jesuits": "مبتكرون بلجيكيون في القرن 20",
    "20th-century Brazilian Jesuits": "مبتكرون برازيليون في القرن 20",
    "20th-century Canadian Jesuits": "مبتكرون كنديون في القرن 20",
    "20th-century Dutch Jesuits": "مبتكرون هولنديون في القرن 20",
    "20th-century Filipino Jesuits": "مبتكرون فلبينيون في القرن 20",
    "20th-century German Jesuits": "مبتكرون ألمان في القرن 20",
    "20th-century Indian Jesuits": "مبتكرون هنود في القرن 20",
    "20th-century Irish Jesuits": "مبتكرون أيرلنديون في القرن 20",
    "20th-century Italian Jesuits": "مبتكرون إيطاليون في القرن 20",
    "20th-century Peruvian Jesuits": "مبتكرون بيرويون في القرن 20",
    "20th-century Polish Jesuits": "مبتكرون بولنديون في القرن 20",
    "20th-century Portuguese Jesuits": "مبتكرون برتغاليون في القرن 20",
    "20th-century Spanish Jesuits": "مبتكرون إسبان في القرن 20",
    "21st-century Belgian Jesuits": "مبتكرون بلجيكيون في القرن 21",
    "21st-century Chilean Jesuits": "مبتكرون تشيليون في القرن 21",
    "21st-century Dutch Jesuits": "مبتكرون هولنديون في القرن 21",
    "21st-century German Jesuits": "مبتكرون ألمان في القرن 21",
    "21st-century Indian Jesuits": "مبتكرون هنود في القرن 21",
    "21st-century Italian Jesuits": "مبتكرون إيطاليون في القرن 21",
    "21st-century Spanish Jesuits": "مبتكرون إسبان في القرن 21",
    "Australian Jesuits": "مبتكرون أستراليون",
    "Basque Jesuits": "مبتكرون باسكيون",
    "Belizean Jesuits": "مبتكرون في بليز",
    "Colombian Jesuits": "مبتكرون كولومبيون",
    "Cuban Jesuits": "مبتكرون كوبيون",
    "Dutch Jesuits": "مبتكرون هولنديون",
    "Ecuadorian Jesuits": "مبتكرون إكوادوريون",
    "Filipino Jesuits": "مبتكرون فلبينيون",
    "Guyanese Jesuits": "مبتكرون غيانيون",
    "Hong Kong Jesuits": "مبتكرون هونغ كونغيون",
    "Hungarian Jesuits": "مبتكرون مجريون",
    "Indian Jesuits": "مبتكرون هنود",
    "Indonesian Jesuits": "مبتكرون إندونيسيون",
    "Irish Jesuits": "مبتكرون أيرلنديون",
    "Israeli Jesuits": "مبتكرون إسرائيليون",
    "Jamaican Jesuits": "مبتكرون جامايكيون",
    "Jesuits by century": "مبتكرون حسب القرن",
    "Jesuits from the Austrian Netherlands": "مبتكرون من الأراضي المنخفضة النمساوية",
    "Jesuits from the Canary Islands": "مبتكرون من جزر الكناري",
    "Jesuits from the Spanish Netherlands": "مبتكرون من هولندا الإسبانية",
    "Lebanese Jesuits": "مبتكرون لبنانيون",
    "Luxembourgian Jesuits": "مبتكرون لوكسمبورغيون",
    "Malaysian Jesuits": "مبتكرون ماليزيون",
    "Maltese Jesuits": "مبتكرون مالطيون",
    "Mexican Jesuits": "مبتكرون مكسيكيون",
    "Nepalese Jesuits": "مبتكرون نيباليون",
    "New Zealand Jesuits": "مبتكرون نيوزيلنديون",
    "Nicaraguan Jesuits": "مبتكرون نيكاراغويون",
    "Salvadoran Jesuits": "مبتكرون سلفادوريون",
    "Slovenian Jesuits": "مبتكرون سلوفينيون",
    "Sri Lankan Jesuits": "مبتكرون سريلانكيون",
    "Swiss Jesuits": "مبتكرون سويسريون",
    "Venezuelan Jesuits": "مبتكرون فنزويليون",
    "Welsh Jesuits": "مبتكرون ويلزيون",

}

test_jesuits_2 = {
    "16th-century French Jesuits": "يسوعيون فرنسيون في القرن 16",
    "16th-century Italian Jesuits": "يسوعيون إيطاليون في القرن 16",
    "16th-century Jesuits": "يسوعيون في القرن 16",
    "16th-century Portuguese Jesuits": "يسوعيون برتغاليون في القرن 16",
    "16th-century Spanish Jesuits": "يسوعيون إسبان في القرن 16",
    "17th-century Belgian Jesuits": "يسوعيون بلجيكيون في القرن 17",
    "17th-century Chilean Jesuits": "يسوعيون تشيليون في القرن 17",
    "17th-century English Jesuits": "يسوعيون إنجليز في القرن 17",
    "17th-century French Jesuits": "يسوعيون فرنسيون في القرن 17",
    "17th-century Italian Jesuits": "يسوعيون إيطاليون في القرن 17",
    "17th-century Jesuits": "يسوعيون في القرن 17",
    "17th-century Portuguese Jesuits": "يسوعيون برتغاليون في القرن 17",
    "17th-century Spanish Jesuits": "يسوعيون إسبان في القرن 17",
    "18th-century American Jesuits": "يسوعيون أمريكيون في القرن 18",
    "18th-century Italian Jesuits": "يسوعيون إيطاليون في القرن 18",
    "18th-century Jesuits": "يسوعيون في القرن 18",
    "19th-century American Jesuits": "يسوعيون أمريكيون في القرن 19",
    "19th-century Chilean Jesuits": "يسوعيون تشيليون في القرن 19",
    "19th-century English Jesuits": "يسوعيون إنجليز في القرن 19",
    "19th-century French Jesuits": "يسوعيون فرنسيون في القرن 19",
    "19th-century Jesuits": "يسوعيون في القرن 19",
    "20th-century American Jesuits": "يسوعيون أمريكيون في القرن 20",
    "20th-century Chilean Jesuits": "يسوعيون تشيليون في القرن 20",
    "20th-century English Jesuits": "يسوعيون إنجليز في القرن 20",
    "20th-century French Jesuits": "يسوعيون فرنسيون في القرن 20",
    "20th-century Jesuits": "يسوعيون في القرن 20",
    "21st-century American Jesuits": "يسوعيون أمريكيون في القرن 21",
    "21st-century French Jesuits": "يسوعيون فرنسيون في القرن 21",
    "21st-century Jesuits": "يسوعيون في القرن 21",
    "American Jesuits": "يسوعيون أمريكيون",
    "Argentine Jesuits": "يسوعيون أرجنتينيون",
    "Austrian Jesuits": "يسوعيون نمساويون",
    "Belgian Jesuits": "يسوعيون بلجيكيون",
    "Brazilian Jesuits": "يسوعيون برازيليون",
    "British Jesuits": "يسوعيون بريطانيون",
    "Canadian Jesuits": "يسوعيون كنديون",
    "Chilean Jesuits": "يسوعيون تشيليون",
    "Chinese Jesuits": "يسوعيون صينيون",
    "Croatian Jesuits": "يسوعيون كروات",
    "Czech Jesuits": "يسوعيون تشيكيون",
    "Egyptian Jesuits": "يسوعيون مصريون",
    "English Jesuits": "يسوعيون إنجليز",
    "French Jesuits": "يسوعيون فرنسيون",
    "German Jesuits": "يسوعيون ألمان",
    "Italian Jesuits": "يسوعيون إيطاليون",
    "Japanese Jesuits": "يسوعيون يابانيون",
    "Jesuits by nationality": "يسوعيون حسب الجنسية",
    "Peruvian Jesuits": "يسوعيون بيرويون",
    "Polish Jesuits": "يسوعيون بولنديون",
    "Portuguese Jesuits": "يسوعيون برتغاليون",
    "Spanish Jesuits": "يسوعيون إسبان",

}

to_test = [
    ("test_jesuits_1", test_jesuits_1),
    ("test_jesuits_2", test_jesuits_2),
]


@pytest.mark.parametrize("category, expected", test_jesuits_2.items(), ids=test_jesuits_2.keys())
@pytest.mark.fast
def test_data_jesuits_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    dump_diff_text(expected, diff_result, name)
    # dump_same_and_not_same(data, diff_result, name, True)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
