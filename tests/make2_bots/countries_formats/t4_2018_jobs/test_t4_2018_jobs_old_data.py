"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

data_fast = {

    "african people by nationality": "أفارقة حسب الجنسية",
    "andy warhol": "آندي وارهول",
    "brazilian women's rights activists": "برازيليون ناشطون في حقوق المرأة",
    "breton language activists": "ناشطون بلغة بريتانية",
    "burmese men marathon runners": "عداؤو ماراثون رجال بورميون",
    "caymanian expatriates": "كايمانيون مغتربون",
    "cuban christians": "كوبيون مسيحيون",
    "eddie murphy": "إيدي ميرفي",
    "english-language culture": "ثقافة اللغة الإنجليزية",
    "english-language fantasy adventure films": "أفلام فانتازيا مغامرات باللغة الإنجليزية",
    "english-language radio stations": "محطات إذاعية باللغة الإنجليزية",
    "fijian language": "لغة فيجية",
    "francisco goya": "فرانثيسكو غويا",
    "french-language albums": "ألبومات باللغة الفرنسية",
    "french-language singers": "مغنون باللغة الفرنسية",
    "french-language television": "تلفاز باللغة الفرنسية",
    "german people by occupation": "ألمان حسب المهنة",
    "german-language films": "أفلام باللغة الألمانية",
    "idina menzel": "إيدينا مينزيل",
    "igor stravinsky": "إيغور سترافينسكي",
    "japanese language": "لغة يابانية",
    "johann wolfgang von goethe": "يوهان فولفغانغ فون غوته",
    "lithuanian men's footballers": "لاعبو كرة قدم ليتوانيون",
    "manx sailors (sport)": "بحارة رياضيون مانكسيون",
    "marathi films": "أفلام باللغة الماراثية",
    "michael porter": "مايكل بورتر",
    "native american aviators": "طيارون أمريكيون أصليون",
    "new caledonian women runners": "عداءات كاليدونيات",
    "polish-language films": "أفلام باللغة البولندية",
    "puerto rican men high jumpers": "متسابقو قفز عالي رجال بورتوريكيون",
    "sara bareilles": "سارة باريلز",
    "shi'a muslims expatriates": "مسلمون شيعة مغتربون",
    "spanish-language mass media": "إعلام اللغة الإسبانية",
    "surinamese women children's writers": "كاتبات أطفال سوريناميات",
    "swedish-language albums": "ألبومات باللغة السويدية",
    "turkish women's rights activists": "أتراك ناشطون في حقوق المرأة",
    "urdu-language musical comedy films": "أفلام كوميدية موسيقية باللغة الأردية",
    "yemeni shi'a muslims": "يمنيون مسلمون شيعة",

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
