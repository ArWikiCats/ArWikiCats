"""
Tests
"""

import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_fast = {
    "bulgarian cup": "كأس بلغاريا",
    "swiss grand prix": "جائزة سويسرا الكبرى",
    "Anglican archbishops of Papua New Guinea": "رؤساء أساقفة أنجليكيون في بابوا غينيا الجديدة",
    "shi'a muslims expatriates": "مسلمون شيعة مغتربون",
    "african people by nationality": "أفارقة حسب الجنسية",
    "andy warhol": "آندي وارهول",
    "caymanian expatriates": "كايمانيون مغتربون",
    "eddie murphy": "إيدي ميرفي",
    "english-language culture": "ثقافة اللغة الإنجليزية",
    "english-language radio stations": "محطات إذاعية باللغة الإنجليزية",
    "francisco goya": "فرانثيسكو غويا",
    "french-language albums": "ألبومات باللغة الفرنسية",
    "french-language television": "تلفاز باللغة الفرنسية",
    "german people by occupation": "ألمان حسب المهنة",
    "idina menzel": "إيدينا مينزيل",
    "igor stravinsky": "إيغور سترافينسكي",
    "johann wolfgang von goethe": "يوهان فولفغانغ فون غوته",
    "lithuanian men's footballers": "لاعبو كرة قدم ليتوانيون",
    "marathi films": "أفلام باللغة الماراثية",
    "michael porter": "مايكل بورتر",
    "sara bareilles": "سارة باريلز",
    "spanish-language mass media": "إعلام اللغة الإسبانية",
    "surinamese women children's writers": "كاتبات أطفال سوريناميات",
    "swedish-language albums": "ألبومات باللغة السويدية",
}


@pytest.mark.parametrize("category, expected_key", data_fast.items(), ids=data_fast.keys())
@pytest.mark.fast
def test_data_fast(category: str, expected_key: str) -> None:
    label1 = resolve_label_ar(category)
    assert label1 == expected_key


to_test = [
    ("te4_2018_data_fast", data_fast),
]

test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
