#
import pytest
from load_one_data import dump_diff, one_dump_test, dump_same_and_not_same

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
    "expatriate men's footballers": "لاعبو كرة قدم رجالية مغتربون",
    "expatriate men's soccer players": "لاعبو كرة قدم رجالية مغتربون",
    "Icelandic deaf people": "أعلام آيسلنديون صم",
    "Romantic composers": "ملحنون رومانسيون",
    "Expatriate men's footballers in Papua New Guinea": "لاعبو كرة قدم رجالية مغتربون في بابوا غينيا الجديدة",
    "American expatriate men's soccer players": "لاعبو كرة قدم أمريكيون مغتربون",
    "Byzantine female saints": "قديسات بيزنطيات",
    "Ancient Christians": "مسيحيون قدماء",
    "Ancient Christian female saints": "قديسات مسيحيات قدماء",
    "Ancient Jewish physicians": "أطباء يهود قدماء",
    "Ancient Jewish scholars": "دارسون يهود قدماء",
    "Ancient Jewish women": "يهوديات قدماء",
    "Ancient Jewish writers": "كتاب يهود قدماء",
    "Murdered American Jews": "أمريكيون يهود قتلوا"
}

data0 = {
    "20th-century Anglican archbishops in Ireland": "رؤساء أساقفة أنجليكيون في أيرلندا في القرن 20",
    "20th-century Anglican archbishops in New Zealand": "رؤساء أساقفة أنجليكيون في نيوزيلندا في القرن 20",
    "21st-century Anglican archbishops in New Zealand": "رؤساء أساقفة أنجليكيون في نيوزيلندا في القرن 21",
    "17th-century Dutch books": "كتب هولندية في القرن 17",
    "1888 in American sports": "رياضة أمريكية في 1888",
    "1919 in American motorsport": "رياضة محركات أمريكية في 1919",
    "1919 in American tennis": "كرة مضرب أمريكية في 1919",
    "1930 in Australian tennis": "كرة مضرب أسترالية في 1930",
    "1931 in American motorsport": "رياضة محركات أمريكية في 1931",
    "1937 in Belgian motorsport": "رياضة محركات بلجيكية في 1937",
    "1970s in Australian tennis": "كرة مضرب أسترالية في عقد 1970",
    "1971 in American tennis": "كرة مضرب أمريكية في 1971",
    "1974 in West German motorsport": "رياضة محركات ألمانية غربية في 1974",
    "1984 in American motorsport": "رياضة محركات أمريكية في 1984",
    "1987 in American sports by state": "رياضة أمريكية في 1987 حسب الولاية",
    "1990s in Colombian tennis": "كرة مضرب كولومبية في عقد 1990",
    "1991 in Australian tennis": "كرة مضرب أسترالية في 1991",
    "1997 in British motorsport": "رياضة محركات بريطانية في 1997",
    "1998 in Indian tennis": "كرة مضرب هندية في 1998",
    "2000 in Canadian sports by province or territory": "رياضة كندية في 2000 حسب المقاطعة أو الإقليم",
    "2004 in Chilean tennis": "كرة مضرب تشيلية في 2004",
    "2004 in French motorsport": "رياضة محركات فرنسية في 2004",
    "2005 in Australian tennis": "كرة مضرب أسترالية في 2005",
    "2010s in Taiwanese tennis": "كرة مضرب تايوانية في عقد 2010",
    "Ancient Egyptian Jews": "مصريون يهود قدماء",
    "2017 sports events": "أحداث 2017 الرياضية",
    "Canarian Jews": "يهود كناريون",
    "Ancient Christian saints": "مسيحيون قديسون قدماء",
    "works by gotthold ephraim lessing": "أعمال بواسطة إفرايم ليسينغ",
    "works by leo tolstoy": "أعمال بواسطة ليو تولستوي",
    "works by osamu tezuka": "أعمال بواسطة أوسامو تزوكا",
    "bengali-language romantic comedy films": "أفلام كوميدية رومانسية باللغة البنغالية",
    "2012 in Luxembourgian tennis": "كرة مضرب لوكسمبورغية في 2012",
    "2013 in Hungarian motorsport": "رياضة محركات مجرية في 2013",
    "2020 in French tennis": "كرة مضرب فرنسية في 2020",
    "2020s in Thai motorsport": "رياضة محركات تايلندية في عقد 2020",
    "2023 in Malaysian motorsport": "رياضة محركات ماليزية في 2023",
    "Lists of office-holders in 2014": "قوائم أصحاب المناصب في 2014",
    "Lists of office-holders in Armenia": "قوائم أصحاب المناصب في أرمينيا",
    "Lists of office-holders in Syria": "قوائم أصحاب المناصب في سوريا",
    "Men's footballers in Azerbaijan by competition": "لاعبو كرة قدم رجالية في أذربيجان حسب المنافسة",
    "Men's footballers in Guinea-Bissau by club": "لاعبو كرة قدم رجالية في غينيا بيساو حسب النادي",
    "Men's footballers in Portugal by competition": "لاعبو كرة قدم رجالية في البرتغال حسب المنافسة",
    "Men's footballers in Slovenia by club": "لاعبو كرة قدم رجالية في سلوفينيا حسب النادي",
    "Men's footballers in Solomon Islands by club": "لاعبو كرة قدم رجالية في جزر سليمان حسب النادي",
    "Men's footballers in Tajikistan by club": "لاعبو كرة قدم رجالية في طاجيكستان حسب النادي",
    "Women's soccer players in United States by competition": "لاعبات كرة قدم نسائية في الولايات المتحدة حسب المنافسة",
    "1999–2000 in European rugby union leagues": "اتحاد دوري الرجبي الأوروبي في 1999–2000",
    "2016–17 in European women's rugby union": "اتحاد الرجبي الأوروبي للنساء في 2016–17",
    "Canadian Premier League players": "لاعبو الدوري الكندي الممتاز",
    "Hong Kong motorsport people": "أعلام رياضة محركات هونغ كونغية",
    "American football culture": "ثقافة كرة القدم الأمريكية",
    "2012–13 in Spanish rugby union leagues": "اتحاد دوري الرجبي الإسباني في 2012–13",
    "american football films": "أفلام كرة القدم الأمريكية",
    "Jewish music genres": "أنواع موسيقى يهود",

}

data1 = {
}

to_test = [
    ("test_2_skip2_0", data0),
    ("test_2_skip2_2", data1),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
@pytest.mark.skip2
def test_2_skip2_0(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
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
