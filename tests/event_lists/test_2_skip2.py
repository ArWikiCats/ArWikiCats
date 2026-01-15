#
import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar

data0_no_label = {
    "north american television awards": "جوائز التلفزة الأمريكية الشمالية",
    "mexican revolution films": "أفلام الثورة المكسيكية",
    "northern-ireland football cups": "كؤوس كرة القدم الأيرلندية الشمالية",
    "chinese professional baseball league awards": "جوائز دوري كرة القاعدة الصيني للمحترفين",
    "paralympics people": "أشخاص في الألعاب البارالمبية",
    "Fictional people executed for murder": "أشخاص خياليون أعدموا بتهمة قتل",
    "Fictional people executed for treason": "أشخاص خياليون أعدموا بتهمة خيانة",
    "Buddhist comics": "قصص مصورة بوذيون",
    "Buddhist media in Taiwan": "إعلام بوذيون في تايوان",
    "Buddhist media": "إعلام بوذيون",
    "Buddhist music": "موسيقى بوذيون",
    "Mexican television awards": "جوائز التلفزة المكسيكية",
    "2025–26 in Northern Ireland association football": "كرة القدم الأيرلندية الشمالية في 2025–26",
    "1971–72 in Northern Ireland association football": "كرة القدم الأيرلندية الشمالية في 1971–72",
    "Buddhist video games": "ألعاب فيديو بوذيون",
    "Hindu music": "موسيقى هندوس",
    "Islamic media in India": "إعلام إسلاميون في الهند",
    "Islamic media": "إعلام إسلاميون",
    "Islamic music": "موسيقى إسلاميون",
    "Nazi culture": "ثقافة نازيون",
    "Nazi songs": "أغاني نازيون",
    "Saints and Soldiers films": "قديسون وأفلام مجندون",
    "muslim people templates": "قوالب أعلام مسلمون",
    "deaf culture": "ثقافة صم",
    "singaporean blind people": "أعلام سنغافوريون مكفوفون",
    "ukrainian deaf people": "أعلام أوكرانيون صم",
    "slovenian deaf people": "أعلام سلوفينيون صم",
    "russian blind people": "أعلام روس مكفوفون",
    "czech deaf people": "أعلام تشيكيون صم",
    "by benjamin britten": "بواسطة بنجامين بريتن",
    "by james cameron": "بواسطة جيمس كاميرون",
    "by raphael": "بواسطة رافاييل",
    "by vaikom muhammad basheer": "بواسطة محمد بشير",
    "expatriate men's footballers": "لاعبو كرة قدم مغتربون",
    "expatriate men's soccer players": "لاعبو كرة قدم مغتربون",
    "Icelandic deaf people": "أعلام آيسلنديون صم",
    "Romantic composers": "ملحنون رومانسيون",
    "Expatriate men's footballers in Papua New Guinea": "لاعبو كرة قدم مغتربون في بابوا غينيا الجديدة",
    "American expatriate men's soccer players": "لاعبو كرة قدم أمريكيون مغتربون",
    "Byzantine female saints": "قديسات بيزنطيات",
    "Ancient Christians": "مسيحيون قدماء",
    "Ancient Christian female saints": "قديسات مسيحيات قدماء",
    "Ancient Jewish physicians": "أطباء يهود قدماء",
    "Ancient Jewish scholars": "دارسون يهود قدماء",
    "Ancient Jewish women": "يهوديات قدماء",
    "Ancient Jewish writers": "كتاب يهود قدماء",
    "Murdered American Jews": "أمريكيون يهود قتلوا",
}

data0 = {
    "20th-century Anglican archbishops in Ireland": "رؤساء أساقفة أنجليكيون في أيرلندا في القرن 20",
    "20th-century Anglican archbishops in New Zealand": "رؤساء أساقفة أنجليكيون في نيوزيلندا في القرن 20",
    "21st-century Anglican archbishops in New Zealand": "رؤساء أساقفة أنجليكيون في نيوزيلندا في القرن 21",
    "17th-century Dutch books": "كتب هولندية في القرن 17",
}

data1 = {}

to_test = [
    # ("test_2_skip2_0", data0),
    ("test_2_skip2_2", data1),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
@pytest.mark.skip2
def test_2_skip2_0(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data0_no_label.items(), ids=data0_no_label.keys())
@pytest.mark.skip2
def test_2_skip2_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, expected, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
