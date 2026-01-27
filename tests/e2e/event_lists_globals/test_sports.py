import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data1 = {
    "Irish association football managers": "مدربو كرة قدم أيرلنديون",
    "Lists of association football players by national team": "قوائم لاعبو كرة قدم حسب المنتخب الوطني",
    "Male long-distance runners": "عداؤو مسافات طويلة ذكور",
    "Male runners by nationality": "عداؤون ذكور حسب الجنسية",
    "Male steeplechase runners": "عداؤو موانع ذكور",
    "Moroccan competitors by sports event": "منافسون مغاربة حسب الحدث الرياضي",
    "Moroccan male middle-distance runners": "عداؤو مسافات متوسطة ذكور مغاربة",
    "Norwegian figure skaters": "متزلجون فنيون نرويجيون",
    "Norwegian male pair skaters": "متزلجون فنيون على الجليد ذكور نرويجيون",
    "Norwegian male single skaters": "متزلجون فرديون ذكور نرويجيون",
    "Water polo at the Summer Universiade": "كرة الماء في الألعاب الجامعية الصيفية",
    "World Judo Championships": "بطولة العالم للجودو",
    "Youth athletics competitions": "منافسات ألعاب قوى شبابية",
    "Youth sports competitions": "منافسات رياضية شبابية",
    "football in 2050–51": "كرة القدم في 2050–51",
    "nations at the universiade": "بلدان في الألعاب الجامعية",
    "ugandan football": "كرة القدم الأوغندية",
    "Spanish sports broadcasters": "مذيعون رياضيون إسبان",
    "Sports broadcasters by nationality": "مذيعون رياضيون حسب الجنسية",
    "Afghanistan national football team managers": "مدربو منتخب أفغانستان لكرة القدم",
    "African women's national association football teams": "منتخبات كرة قدم وطنية إفريقية للسيدات",
    "Argentina women's international footballers": "لاعبات منتخب الأرجنتين لكرة القدم للسيدات",
    "Belgian athletics coaches": "مدربو ألعاب قوى بلجيكيون",
    "Coaches of national cricket teams": "مدربو منتخبات كريكت وطنية",
    "International women's basketball competitions hosted by Cuba": "منافسات كرة سلة دولية للسيدات استضافتها كوبا",
    "Sports coaches by nationality": "مدربو رياضة حسب الجنسية",
    "Transport companies established in 1909": "شركات نقل أسست في 1909",
}

data2 = {
    "Female association football managers": "مدربات كرة قدم",
    # "Coaches of the West Indies national cricket team": "",
    # "Nauru international soccer players": "",
    "Australia international soccer players": "لاعبو منتخب أستراليا لكرة القدم",
    "Canada men's international soccer players": "لاعبو كرة قدم دوليون من كندا",
    "Afghanistan women's national football team coaches": "مدربو منتخب أفغانستان لكرة القدم للسيدات",
    "Coaches of Yemen national cricket team": "مدربو منتخب اليمن للكريكت",
    "Cuba women's national basketball team": "منتخب كوبا لكرة السلة للسيدات",
    "Equatorial Guinea women's national football team": "منتخب غينيا الاستوائية لكرة القدم للسيدات",
    "Norwegian pair skaters": "متزلجون فنيون على الجليد نرويجيون",
    "Norwegian short track speed skaters": "متزلجون على مسار قصير نرويجيون",
    "Olympic competitors for Cape Verde": "منافسون أولمبيون من الرأس الأخضر",
    "Olympic figure skating": "تزلج فني أولمبي",
    "Olympic medalists in alpine skiing": "فائزون بميداليات أولمبية في التزلج على المنحدرات الثلجية",
    "Rail transport in the United Kingdom": "السكك الحديدية في المملكة المتحدة",
    "Republic of Ireland football managers": "مدربو كرة قدم أيرلنديون",
    "Seasons in Omani football": "مواسم في كرة القدم العمانية",
    "Ski jumping at the Winter Universiade": "القفز التزلجي في الألعاب الجامعية الشتوية",
    "Skiing coaches": "مدربو تزلج",
    "Sports competitors by nationality and competition": "منافسون رياضيون حسب الجنسية والمنافسة",
    "Sports organisations of Andorra": "منظمات رياضية في أندورا",
    "sports-people from Boston": "رياضيون من بوسطن",
    "Transport disasters in 2017": "كوارث نقل في 2017",
    "Turkish expatriate sports-people": "رياضيون أتراك مغتربون",
    "Universiade medalists by sport": "فائزون بميداليات الألعاب الجامعية حسب الرياضة",
    "Universiade medalists in water polo": "فائزون بميداليات الألعاب الجامعية في كرة الماء",
    "Association football players by under-20 national team": "لاعبو كرة قدم حسب المنتخب الوطني تحت 20 سنة",
    "Association football players by under-21 national team": "لاعبو كرة قدم حسب المنتخب الوطني تحت 21 سنة",
    "Association football players by under-23 national team": "لاعبو كرة قدم حسب المنتخب الوطني تحت 23 سنة",
    "Association football players by youth national team": "لاعبو كرة قدم حسب المنتخب الوطني للشباب",
    "Association football": "كرة القدم",
}
data3 = {
    "Female short track speed skaters": "متزلجات على مسار قصير",
    "Female speed skaters": "متزلجات سرعة",
    "Figure skaters by competition": "متزلجون فنيون حسب المنافسة",
    "Figure skating coaches": "مدربو تزلج فني",
    "Figure skating people": "أعلام تزلج فني",
    "Icelandic male athletes": "لاعبو قوى ذكور آيسلنديون",
    "Icelandic male runners": "عداؤون ذكور آيسلنديون",
    "Icelandic male steeplechase runners": "عداؤو موانع ذكور آيسلنديون",
    "IndyCar": "أندي كار",
    "International sports competitions hosted by Mexico": "منافسات رياضية دولية استضافتها المكسيك",
    "Egyptian male sport shooters": "لاعبو رماية ذكور مصريون",
    "Egyptian sport shooters": "لاعبو رماية مصريون",
    "Emirati football in 2017": "كرة القدم الإماراتية في 2017",
    "Emirati football in 2017–18": "كرة القدم الإماراتية في 2017–18",
    "England amateur international footballers": "لاعبو منتخب إنجلترا لكرة القدم للهواة",
    "Equatoguinean women's footballers": "لاعبات كرة قدم غينيات استوائيات",
    "European national under-21 association football teams": "منتخبات كرة قدم وطنية أوروبية تحت 21 سنة",
    "Expatriate women's association football players": "لاعبات كرة قدم مغتربات",
    "Expatriate women's footballers by location": "لاعبات كرة قدم مغتربات حسب الموقع",
    "Australia at the Summer Universiade": "أستراليا في الألعاب الجامعية الصيفية",
    "Australian male sprinters": "عداؤون سريعون ذكور أستراليون",
    "Canadian sports businesspeople": "شخصيات أعمال رياضيون كنديون",
    "Cape Verde at the Paralympics": "الرأس الأخضر في الألعاب البارالمبية",
    "Cape Verdean football managers": "مدربو كرة قدم أخضريون",
    "Egyptian female sport shooters": "لاعبات رماية مصريات",
    "Afghan competitors by sports event": "منافسون أفغان حسب الحدث الرياضي",
    "American basketball players by ethnic or national origin": "لاعبو كرة سلة أمريكيون حسب الأصل العرقي أو الوطني",
    "Argentina at the Universiade": "الأرجنتين في الألعاب الجامعية",
    "Argentina at the Winter Olympics": "الأرجنتين في الألعاب الأولمبية الشتوية",
    "Association football players by amateur national team": "لاعبو كرة قدم حسب المنتخب الوطني للهواة",
}

to_test = [
    ("test_sports_1", data1),
    ("test_sports_2", data2),
    ("test_sports_3", data3),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_sports_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_sports_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data3.items(), ids=data3.keys())
@pytest.mark.fast
def test_sports_3(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)
