"""
Tests
"""

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar
data_list_1 = {}

data_list_2 = {
    "1450s disasters in kazakhstan": "كوارث عقد 1450 في كازاخستان",
    "1450s disasters in kyrgyzstan": "كوارث عقد 1450 في قيرغيزستان",
    "1450s disasters in north america": "كوارث عقد 1450 في أمريكا الشمالية",
    "1450s disasters in norway": "كوارث عقد 1450 في النرويج",
    "1450s disasters in the united arab emirates": "كوارث عقد 1450 في الإمارات العربية المتحدة",
    "1450s mass shootings in oceania": "إطلاق نار عشوائي عقد 1450 في أوقيانوسيا",
    "1450s murders in honduras": "جرائم قتل عقد 1450 في هندوراس",
    "1450s murders in ireland": "جرائم قتل عقد 1450 في أيرلندا",
    "1450s murders in peru": "جرائم قتل عقد 1450 في بيرو",
    "1450s murders in singapore": "جرائم قتل عقد 1450 في سنغافورة",
    "1450s murders in sri lanka": "جرائم قتل عقد 1450 في سريلانكا",
    "1450s murders in switzerland": "جرائم قتل عقد 1450 في سويسرا",
    "6th century kings of italy": "ملوك القرن 6 إيطاليا",
    "15th century mosques in iran": "مساجد القرن 15 في إيران",
    "15th century synagogues in portugal": "كنس القرن 15 في البرتغال",
    "16th century astronomers from the holy roman empire": "فلكيون في القرن 16 من الإمبراطورية الرومانية المقدسة",
    "16th century monarchs in the middle east": "ملكيون في القرن 16 في الشرق الأوسط",
    "16th century roman catholic bishops in hungary": "أساقفة كاثوليك رومان في القرن 16 في المجر",
    "17th century roman catholic archbishops in serbia": "رؤساء أساقفة رومان كاثوليك القرن 17 في صربيا",
    "18th century actors from the holy roman empire": "ممثلون في القرن 18 من الإمبراطورية الرومانية المقدسة",
    "18th century historians from the russian empire": "مؤرخون في القرن 18 من الإمبراطورية الروسية",
    "18th century roman catholic bishops in china": "أساقفة كاثوليك رومان في القرن 18 في الصين",
    "18th century roman catholic bishops in paraguay": "أساقفة كاثوليك رومان في القرن 18 في باراغواي",
    "18th century roman catholic church buildings in austria": "مبان كنائس رومانية كاثوليكية القرن 18 في النمسا",
    "19th century british dramatists and playwrights": "دراميون بريطانيون في القرن 19 وكتاب مسرحيون",
    "19th century mosques in the ottoman empire": "مساجد القرن 19 في الدولة العثمانية",
    "19th century roman catholic bishops in argentina": "أساقفة كاثوليك رومان في القرن 19 في الأرجنتين",
    "20th century mosques in asia": "مساجد القرن 20 في آسيا",
    "20th century people from south dakota": "أشخاص في القرن 20 من داكوتا الجنوبية",
    "20th century photographers from northern ireland": "مصورون في القرن 20 من أيرلندا الشمالية",
    "21st century disasters in namibia": "كوارث القرن 21 في ناميبيا",
    "21st century executions in kentucky": "إعدامات في القرن 21 في كنتاكي",
    "21st century fires in south america": "حرائق القرن 21 في أمريكا الجنوبية",
    "21st century singer-songwriters from northern ireland": "مغنون وكتاب أغاني في القرن 21 من أيرلندا الشمالية",
    "21st century welsh dramatists and playwrights": "دراميون ويلزيون في القرن 21 وكتاب مسرحيون"
}

to_test = [
    ("data_list_1", data_list_1),
    ("data_list_2", data_list_2),
]


@pytest.mark.parametrize("category, expected", data_list_1.items(), ids=data_list_1.keys())
@pytest.mark.fast
def test_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
