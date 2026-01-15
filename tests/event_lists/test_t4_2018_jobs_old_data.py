"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

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
    "english-language fantasy adventure films": "أفلام فانتازيا مغامرات باللغة الإنجليزية",
    "english-language radio stations": "محطات إذاعية باللغة الإنجليزية",
    "fijian language": "لغة فيجية",
    "francisco goya": "فرانثيسكو غويا",
    "french-language albums": "ألبومات باللغة الفرنسية",
    "french-language television": "تلفاز باللغة الفرنسية",
    "german people by occupation": "ألمان حسب المهنة",
    "german-language films": "أفلام باللغة الألمانية",
    "idina menzel": "إيدينا مينزيل",
    "igor stravinsky": "إيغور سترافينسكي",
    "japanese language": "لغة يابانية",
    "johann wolfgang von goethe": "يوهان فولفغانغ فون غوته",
    "lithuanian men's footballers": "لاعبو كرة قدم ليتوانيون",
    "marathi films": "أفلام باللغة الماراثية",
    "michael porter": "مايكل بورتر",
    "polish-language films": "أفلام باللغة البولندية",
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


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)

    # dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
