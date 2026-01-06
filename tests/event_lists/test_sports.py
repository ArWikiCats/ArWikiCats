import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data1 = {
    "Category:Irish association football managers": "تصنيف:مدربو كرة قدم أيرلنديون",
    "Category:Lists of association football players by national team": "تصنيف:قوائم لاعبو كرة قدم حسب المنتخب الوطني",
    "Category:Male long-distance runners": "تصنيف:عداؤو مسافات طويلة ذكور",
    "Category:Male runners by nationality": "تصنيف:عداؤون ذكور حسب الجنسية",
    "Category:Male steeplechase runners": "تصنيف:عداؤو موانع ذكور",
    "Category:Moroccan competitors by sports event": "تصنيف:منافسون مغاربة حسب الحدث الرياضي",
    "Category:Moroccan male middle-distance runners": "تصنيف:عداؤو مسافات متوسطة ذكور مغاربة",
    "Category:Norwegian figure skaters": "تصنيف:متزلجون فنيون نرويجيون",
    "Category:Norwegian male pair skaters": "تصنيف:متزلجون فنيون على الجليد ذكور نرويجيون",
    "Category:Norwegian male single skaters": "تصنيف:متزلجون فرديون ذكور نرويجيون",
    "Category:Water polo at the Summer Universiade": "تصنيف:كرة الماء في الألعاب الجامعية الصيفية",
    "Category:World Judo Championships": "تصنيف:بطولة العالم للجودو",
    "Category:Youth athletics competitions": "تصنيف:منافسات ألعاب قوى شبابية",
    "Category:Youth athletics": "تصنيف:ألعاب القوى للشباب",
    "Category:Youth sports competitions": "تصنيف:منافسات رياضية شبابية",
    "Category:football in 2050–51": "تصنيف:كرة القدم في 2050–51",
    "Category:nations at the universiade": "تصنيف:بلدان في الألعاب الجامعية",
    "Category:ugandan football": "تصنيف:كرة القدم الأوغندية",
    "Category:Spanish sports broadcasters": "تصنيف:مذيعون رياضيون إسبان",
    "Category:Sports broadcasters by nationality": "تصنيف:مذيعون رياضيون حسب الجنسية",
    "Category:Afghanistan national football team managers": "تصنيف:مدربو منتخب أفغانستان لكرة القدم",
    "Category:African women's national association football teams": "تصنيف:منتخبات كرة قدم وطنية إفريقية للسيدات",
    "Category:Argentina women's international footballers": "تصنيف:لاعبات منتخب الأرجنتين لكرة القدم للسيدات",
    "Category:Belgian athletics coaches": "تصنيف:مدربو ألعاب قوى بلجيكيون",
    "Category:Coaches of national cricket teams": "تصنيف:مدربو منتخبات كريكت وطنية",
    "Category:International women's basketball competitions hosted by Cuba": "تصنيف:منافسات كرة سلة دولية للسيدات استضافتها كوبا",
    "Category:Sports coaches by nationality": "تصنيف:مدربو رياضة حسب الجنسية",
    "Category:Transport companies established in 1909": "تصنيف:شركات نقل أسست في 1909",
}

data2 = {
    "Category:Female association football managers": "تصنيف:مدربات كرة قدم",
    # "Category:Coaches of the West Indies national cricket team": "",
    # "Category:Nauru international soccer players": "",
    "Category:Australia international soccer players": "تصنيف:لاعبو منتخب أستراليا لكرة القدم",
    "Category:Canada men's international soccer players": "تصنيف:لاعبو كرة قدم دوليون من كندا",
    "Category:Afghanistan women's national football team coaches": "تصنيف:مدربو منتخب أفغانستان لكرة القدم للسيدات",
    "Category:Coaches of Yemen national cricket team": "تصنيف:مدربو منتخب اليمن للكريكت",
    "Category:Cuba women's national basketball team": "تصنيف:منتخب كوبا لكرة السلة للسيدات",
    "Category:Equatorial Guinea women's national football team": "تصنيف:منتخب غينيا الاستوائية لكرة القدم للسيدات",
    "Category:Norwegian pair skaters": "تصنيف:متزلجون فنيون على الجليد نرويجيون",
    "Category:Norwegian short track speed skaters": "تصنيف:متزلجون على مسار قصير نرويجيون",
    "Category:Olympic competitors for Cape Verde": "تصنيف:منافسون أولمبيون من الرأس الأخضر",
    "Category:Olympic figure skating": "تصنيف:تزلج فني أولمبي",
    "Category:Olympic medalists in alpine skiing": "تصنيف:فائزون بميداليات أولمبية في التزلج على المنحدرات الثلجية",
    "Category:Rail transport in the United Kingdom": "تصنيف:السكك الحديدية في المملكة المتحدة",
    "Category:Republic of Ireland football managers": "تصنيف:مدربو كرة قدم أيرلنديون",
    "Category:Seasons in Omani football": "تصنيف:مواسم في كرة القدم العمانية",
    "Category:Ski jumping at the Winter Universiade": "تصنيف:القفز التزلجي في الألعاب الجامعية الشتوية",
    "Category:Skiing coaches": "تصنيف:مدربو تزلج",
    "Category:Sports competitors by nationality and competition": "تصنيف:منافسون رياضيون حسب الجنسية والمنافسة",
    "Category:Sports organisations of Andorra": "تصنيف:منظمات رياضية في أندورا",
    "Category:sports-people from Boston": "تصنيف:رياضيون من بوسطن",
    "Category:Table tennis clubs": "تصنيف:أندية كرة طاولة",
    "Category:Transport disasters in 2017": "تصنيف:كوارث نقل في 2017",
    "Category:Turkish expatriate sports-people": "تصنيف:رياضيون أتراك مغتربون",
    "Category:Universiade medalists by sport": "تصنيف:فائزون بميداليات الألعاب الجامعية حسب الرياضة",
    "Category:Universiade medalists in water polo": "تصنيف:فائزون بميداليات الألعاب الجامعية في كرة الماء",
    "Category:Association football players by under-20 national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني تحت 20 سنة",
    "Category:Association football players by under-21 national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني تحت 21 سنة",
    "Category:Association football players by under-23 national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني تحت 23 سنة",
    "Category:Association football players by youth national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني للشباب",
    "Category:Association football": "تصنيف:كرة القدم",
}
data3 = {
    "Category:Female short track speed skaters": "تصنيف:متزلجات على مسار قصير",
    "Category:Female speed skaters": "تصنيف:متزلجات سرعة",
    "Category:Figure skaters by competition": "تصنيف:متزلجون فنيون حسب المنافسة",
    "Category:Figure skating coaches": "تصنيف:مدربو تزلج فني",
    "Category:Figure skating people": "تصنيف:أعلام تزلج فني",
    "Category:Icelandic male athletes": "تصنيف:لاعبو قوى ذكور آيسلنديون",
    "Category:Icelandic male runners": "تصنيف:عداؤون ذكور آيسلنديون",
    "Category:Icelandic male steeplechase runners": "تصنيف:عداؤو موانع ذكور آيسلنديون",
    "Category:IndyCar": "تصنيف:أندي كار",
    "Category:International sports competitions hosted by Mexico": "تصنيف:منافسات رياضية دولية استضافتها المكسيك",
    "Category:Egyptian male sport shooters": "تصنيف:لاعبو رماية ذكور مصريون",
    "Category:Egyptian sport shooters": "تصنيف:لاعبو رماية مصريون",
    "Category:Emirati football in 2017": "تصنيف:كرة القدم الإماراتية في 2017",
    "Category:Emirati football in 2017–18": "تصنيف:كرة القدم الإماراتية في 2017–18",
    "Category:England amateur international footballers": "تصنيف:لاعبو منتخب إنجلترا لكرة القدم للهواة",
    "Category:Equatoguinean women's footballers": "تصنيف:لاعبات كرة قدم غينيات استوائيات",
    "Category:European national under-21 association football teams": "تصنيف:منتخبات كرة قدم وطنية أوروبية تحت 21 سنة",
    "Category:Expatriate women's association football players": "تصنيف:لاعبات كرة قدم مغتربات",
    "Category:Expatriate women's footballers by location": "تصنيف:لاعبات كرة قدم مغتربات حسب الموقع",
    "Category:Australia at the Summer Universiade": "تصنيف:أستراليا في الألعاب الجامعية الصيفية",
    "Category:Australian male sprinters": "تصنيف:عداؤون سريعون ذكور أستراليون",
    "Category:Canadian sports businesspeople": "تصنيف:شخصيات أعمال رياضيون كنديون",
    "Category:Cape Verde at the Paralympics": "تصنيف:الرأس الأخضر في الألعاب البارالمبية",
    "Category:Cape Verdean football managers": "تصنيف:مدربو كرة قدم أخضريون",
    "Category:Egyptian female sport shooters": "تصنيف:لاعبات رماية مصريات",
    "Category:Afghan competitors by sports event": "تصنيف:منافسون أفغان حسب الحدث الرياضي",
    "Category:American basketball players by ethnic or national origin": "تصنيف:لاعبو كرة سلة أمريكيون حسب الأصل العرقي أو الوطني",
    "Category:Argentina at the Universiade": "تصنيف:الأرجنتين في الألعاب الجامعية",
    "Category:Argentina at the Winter Olympics": "تصنيف:الأرجنتين في الألعاب الأولمبية الشتوية",
    "Category:Association football players by amateur national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني للهواة",
}

to_test = [
    ("test_sports_1", data1),
    ("test_sports_2", data2),
    ("test_sports_3", data3),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_sports_1(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_sports_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data3.items(), ids=data3.keys())
@pytest.mark.fast
def test_sports_3(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_sports(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
