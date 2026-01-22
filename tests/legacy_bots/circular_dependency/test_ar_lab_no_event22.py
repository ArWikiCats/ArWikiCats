"""
Tests
"""

import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_list_2 = {
    "1450s disasters in kazakhstan": "كوارث في كازاخستان في عقد 1450",
    "1450s disasters in kyrgyzstan": "كوارث في قيرغيزستان في عقد 1450",
    "1450s disasters in north america": "كوارث في أمريكا الشمالية في عقد 1450",
    "1450s disasters in norway": "كوارث في النرويج في عقد 1450",
    "1450s disasters in the united arab emirates": "كوارث في الإمارات العربية المتحدة في عقد 1450",
    "1450s mass shootings in oceania": "إطلاق نار عشوائي في أوقيانوسيا في عقد 1450",
    "1450s murders in honduras": "جرائم قتل في هندوراس في عقد 1450",
    "1450s murders in peru": "جرائم قتل في بيرو في عقد 1450",
    "1450s murders in singapore": "جرائم قتل في سنغافورة في عقد 1450",
    "1450s murders in sri lanka": "جرائم قتل في سريلانكا في عقد 1450",
    "1450s murders in switzerland": "جرائم قتل في سويسرا في عقد 1450",
    "15th century mosques in iran": "مساجد في إيران في القرن 15",
    "15th century synagogues in portugal": "كنس في البرتغال في القرن 15",
    "16th century astronomers from the holy roman empire": "فلكيون من الإمبراطورية الرومانية المقدسة في القرن 16",
    "16th century monarchs in the middle east": "ملكيون في الشرق الأوسط في القرن 16",
    "16th century roman catholic bishops in hungary": "أساقفة كاثوليك رومان في المجر في القرن 16",
    "17th century roman catholic archbishops in serbia": "رؤساء أساقفة رومان كاثوليك في صربيا في القرن 17",
    "18th century actors from the holy roman empire": "ممثلون من الإمبراطورية الرومانية المقدسة في القرن 18",
    "18th century historians from the russian empire": "مؤرخون من الإمبراطورية الروسية في القرن 18",
    "18th century roman catholic bishops in china": "أساقفة كاثوليك رومان في الصين في القرن 18",
    "18th century roman catholic bishops in paraguay": "أساقفة كاثوليك رومان في باراغواي في القرن 18",
    "18th century roman catholic church buildings in austria": "مبان كنائس رومانية كاثوليكية في النمسا في القرن 18",
    "19th century british dramatists and playwrights": "كتاب دراما ومسرح بريطانيون في القرن 19",
    "19th century mosques in the ottoman empire": "مساجد في الدولة العثمانية في القرن 19",
    "19th century roman catholic bishops in argentina": "أساقفة كاثوليك رومان في الأرجنتين في القرن 19",
    "20th century mosques in asia": "مساجد في آسيا في القرن 20",
    "20th century people from south dakota": "أشخاص من داكوتا الجنوبية في القرن 20",
    "20th century photographers from northern ireland": "مصورون من أيرلندا الشمالية في القرن 20",
    "21st century disasters in namibia": "كوارث في ناميبيا في القرن 21",
    "21st century fires in south america": "حرائق في أمريكا الجنوبية في القرن 21",
    "21st century singer-songwriters from northern ireland": "مغنون وكتاب أغاني من أيرلندا الشمالية في القرن 21",
    "21st century welsh dramatists and playwrights": "كتاب دراما ومسرح ويلزيون في القرن 21",
}

to_test = [
    ("data_list_2", data_list_2),
]


@pytest.mark.parametrize("category, expected", data_list_2.items(), ids=data_list_2.keys())
@pytest.mark.fast
def test_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
