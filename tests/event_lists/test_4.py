#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data0 = {

}

data1 = {
    "2002 commonwealth games": "تصنيف:ألعاب الكومنولث 2002",
    "2006 commonwealth games": "تصنيف:ألعاب الكومنولث 2006",
    "2014 commonwealth games": "تصنيف:ألعاب الكومنولث 2014",
    "afghan premier league": "تصنيف:الدوري الأفغاني الممتاز",
    "africa cup of nations": "تصنيف:كأس إفريقيا في بلدان",
    "african judo championships": "تصنيف:بطولات جودو إفريقية",
    "african swimming championships": "تصنيف:بطولات سباحة إفريقية",
    "albanian second division": "تصنيف:الدوري الألباني الدرجة الثانية",
    "algerian basketball championship": "تصنيف:بطولة الجزائر لكرة السلة",
    "algerian league cup": "تصنيف:كأس الدوري الجزائري",
    "algerian women's volleyball league": "تصنيف:الدوري الجزائري لكرة الطائرة للسيدات",
    "all-africa games": "تصنيف:ألعاب عموم إفريقيا",
    "american hockey league": "تصنيف:الدوري الأمريكي للهوكي",
    "anguillan league": "تصنيف:الدوري الأنغويلاني",
    "armenian independence cup": "تصنيف:كأس استقلال أرمينيا",
    "armenian premier league": "تصنيف:الدوري الأرميني الممتاز",
    "asian athletics championships": "تصنيف:بطولات ألعاب قوى آسيوية",
    "asian games": "تصنيف:الألعاب الآسيوية",
    "asian swimming championships": "تصنيف:بطولات سباحة آسيوية",
    "asian wrestling championships": "تصنيف:بطولات مصارعة آسيوية",
    "australian baseball league": "تصنيف:الدوري الأسترالي لكرة القاعدة",
    "australian football league": "تصنيف:الدوري الأسترالي لكرة القدم",
    "azerbaijan first division": "تصنيف:أذربيجان",
    "bandy world cup": "تصنيف:كأس العالم للباندي",
    "bangladesh football premier league": "تصنيف:دوريات كرة قدم بنغلاديشية من الدرجة الممتازة",
    "barbados fa cup": "تصنيف:كأس الاتحاد البربادوسي",
    "barbados premier division": "تصنيف:الدوري البربادوسي الممتاز",
    "bermudian premier division": "تصنيف:الدوري البرمودي الممتاز",
    "bosnia and herzegovina football cup": "تصنيف:كأس البوسنة والهرسك لكرة القدم",
    "botswana premier league": "تصنيف:الدوري البوتسواني الممتاز",
    "british empire and commonwealth games": "تصنيف:الإمبراطورية البريطانية وألعاب الكومنولث",
    "burkinabé premier league": "تصنيف:الدوري البوركينابي الممتاز",
    "cambodian league": "تصنيف:الدوري الكمبودي",
    "costa rican cup": "تصنيف:كأس كوستاريكا",
    "cricket world cup": "تصنيف:كأس العالم للكريكت",
    "croatian premier handball league": "تصنيف:دوريات كرة يد كرواتية من الدرجة الممتازة",
    "cyprus cup": "تصنيف:كأس قبرص",
    "east asian games": "تصنيف:الألعاب الآسيوية الشرقية",
    "european amateur boxing championships": "تصنيف:بطولة أوروبا للبوكسينغ للهواة",
    "european beach volleyball championships": "تصنيف:بطولات كرة طائرة شاطئية أوروبية",
    "european fencing championships": "تصنيف:بطولات مبارزة سيف شيش أوروبية",
    "european judo championships": "تصنيف:بطولات جودو أوروبية",
    "european karate championships": "تصنيف:بطولات كاراتيه أوروبية",
    "european speed skating championships": "تصنيف:بطولات تزلج سريع أوروبية",
    "first league of serbia and montenegro": "تصنيف:دوري كرة القدم الدرجة الأولى في صربيا والجبل الأسود",
    "french women's handball championship": "تصنيف:بطولة فرنسا لكرة اليد للسيدات",
    "gerry weber open": "تصنيف:بطولة هالي المفتوحة",
    "grand prix": "تصنيف:سباق الجائزة الكبرى",
    "greek men's handball championship": "تصنيف:بطولة اليونان لكرة اليد للرجال",
    "greek women's handball championship": "تصنيف:بطولة اليونان لكرة اليد للسيدات",
    "gulf cup of nations": "تصنيف:كأس الخليج العربي",
    "handball league of serbia": "تصنيف:دوري كرة اليد في صربيا",
    "hockey world cup": "تصنيف:كأس العالم للهوكي",
    "hong kong first division league": "تصنيف:الدوري الهونغ الكونغي الدرجة الأولى",
    "hong kong premier league": "تصنيف:الدوري الهونغ الكونغي الممتاز",
    "iraqi super cup": "تصنيف:كأس السوبر العراقي",
    "japan football league": "تصنيف:دوري اليابان لكرة القدم",
    "japan professional basketball league": "تصنيف:دوري اليابان لكرة السلة للمحترفين",
    "kenyan premier league": "تصنيف:الدوري الكيني الممتاز",
    "kuwaiti premier league": "تصنيف:الدوري الكويتي الممتاز",
    "lao league": "تصنيف:الدوري اللاوسي",
    "latvian football cup": "تصنيف:كأس لاتفيا لكرة القدم",
    "lebanese football league": "تصنيف:الدوري اللبناني لكرة القدم",
    "lega basket serie a": "تصنيف:ليغا باسكيت الدرجة الأولى",
    "lesotho premier league": "تصنيف:الدوري الليسوتي الممتاز",
    "libyan premier league": "تصنيف:الدوري الليبي الممتاز",
    "lithuanian football cup": "تصنيف:كأس ليتوانيا لكرة القدم",
    "maccabiah games": "تصنيف:الألعاب المكابيه",
    "macedonian cup": "تصنيف:كأس مقدونيا",
    "macedonian handball super league": "تصنيف:دوري السوبر كرة اليد المقدوني",
    "malawi premier division": "تصنيف:الدوري الملاوي الممتاز",
    "maldives fa cup": "تصنيف:كأس الاتحاد المالديفي",
    "maltese second division": "تصنيف:الدوري المالطي الدرجة الثانية",
    "mauritian league": "تصنيف:الدوري الموريشيوسي",
    "men's african volleyball championship": "تصنيف:بطولة إفريقيا لكرة الطائرة رجالية",
    "moldovan cup": "تصنيف:كأس مولدافيا",
    "national basketball league of canada": "تصنيف:دوريات كرة سلة وطنية في كندا",
    "national basketball league": "تصنيف:دوريات كرة سلة وطنية",
    "national football league": "تصنيف:دوري كرة القدم الوطني الأيرلندي",
    "national hockey league": "تصنيف:دوريات هوكي وطنية",
    "national soccer league": "تصنيف:دوريات كرة قدم وطنية",
    "nigerian professional football league": "تصنيف:دوري كرة القدم النيجيري للمحترفين",
    "north african super cup": "تصنيف:كأس السوبر الشمال الإفريقي",
    "norwegian football cup": "تصنيف:كأس النرويج لكرة القدم",
    "omani league": "تصنيف:الدوري العماني",
    "palestine cup": "تصنيف:كأس فلسطين",
    "premier soccer league": "تصنيف:دوريات كرة قدم من الدرجة الممتازة",
    "russian basketball super league": "تصنيف:دوري السوبر كرة السلة الروسي",
    "russian handball super league": "تصنيف:دوري السوبر كرة اليد الروسي",
    "samoa cup": "تصنيف:كأس ساموا",
    "saudi second division": "تصنيف:الدوري السعودي الدرجة الثانية",
    "scottish cup": "تصنيف:كأس إسكتلندا",
    "scottish football league second division": "تصنيف:الدوري الإسكتلندي لكرة القدم",
    "scottish football league": "تصنيف:الدوري الإسكتلندي لكرة القدم",
    "seychelles first division": "تصنيف:سيشل",
    "slovenian football cup": "تصنيف:كأس سلوفينيا لكرة القدم",
    "south african premier division": "تصنيف:الدوري الجنوب الإفريقي الممتاز",
    "south american games": "تصنيف:الألعاب الأمريكية الجنوبية",
    "south american swimming championships": "تصنيف:بطولات سباحة أمريكية جنوبية",
    "south american volleyball championship": "تصنيف:بطولة أمريكا الجنوبية لكرة الطائرة",
    "south american women's football championship": "تصنيف:بطولة أمريكا الجنوبية لكرة القدم للسيدات",
    "soviet cup": "تصنيف:كأس الاتحاد السوفيتي",
    "sumo": "تصنيف:السومو",
    "syrian premier league": "تصنيف:الدوري السوري الممتاز",
    "table tennis world cup": "تصنيف:كأس العالم لكرة الطاولة",
    "taekwondo": "تصنيف:التايكوندو",
    "thai fa cup": "تصنيف:كأس الاتحاد التايلندي",
    "thai premier league": "تصنيف:الدوري التايلندي الممتاز",
    "tour de france": "تصنيف:طواف فرنسا",
    "turkish basketball super league": "تصنيف:دوري السوبر كرة السلة التركي",
    "irish super league": "تصنيف:دوري السوبر الأيرلندي",
    "turkish handball super league": "تصنيف:دوري السوبر كرة اليد التركي",
    "vietnamese second division": "تصنيف:الدوري الفيتنامي الدرجة الثانية",
    "waba champions cup": "تصنيف:كأس دوري غرب آسيا لكرة السلة",
    "women's chinese basketball association": "تصنيف:الرابطة الصينية لكرة السلة نسائية",
    "women's korean basketball league": "تصنيف:الدوري الكوري لكرة السلة نسائية",
    "world games": "تصنيف:دورة الألعاب العالمية",
    "world karate championships": "تصنيف:بطولة العالم للكاراتيه",
    "yemeni unity cup": "تصنيف:كأس الوحدة اليمنية",
    "College sports coaches in the United States by sport by state": "تصنيف:مدربو رياضات الكليات في الولايات المتحدة حسب الرياضة حسب الولاية",
    "national university of singapore": "تصنيف:جامعة سنغافورة الوطنية",
    "sri lankan civil war by decade": "تصنيف:الحرب الأهلية السريلانكية حسب العقد",
    "church of jesus christ of latter-day saints": "تصنيف:كنيسة يسوع المسيح لقديسي الأيام الأخيرة",
    "senate of pakistan": "تصنيف:مجلس شيوخ باكستان",
    "parliament of india": "تصنيف:برلمان الهند",
    "political people": "تصنيف:ساسة",
}


data_2 ={
    "puerto princesa international airport": "مطار بويرتو برينسيسا الدولي",
    "united states military academy": "الأكاديمية العسكرية الأمريكية",
    "west end theatre": "مسارح وست اند",
    "xin dynasty": "سلالة شين الحاكمة",
    "tokyo metropolitan police department": "قسم شرطة العاصمة طوكيو",
    "supreme court of israel": "المحكمة العليا (إسرائيل)",
    "sydney opera house": "دار أوبرا سيدني",
    "sovereign military order of malta": "فرسان مالطة",
    "second congo war": "حرب الكونغو الثانية",
    "san quentin state prison": "سجن سان كوينتن",
    "royal canadian mounted police": "شرطة الخيالة الكندية الملكية",
    "royal danish army": "القوات البرية الدانماركية",
    "russian academy of arts": "الأكاديمية الروسية للفنون",
    "lgbtq people": "أعلام إل جي بي تي كيو",
    "black people": "أعلام سوداء",
}

data_3 = {
    # "Category:second italo-ethiopian war": "تصنيف:الحرب الإيطالية الإثيوبية الثانية",
    "Category:Afghanistan Football Federation": "تصنيف:الاتحاد الأفغاني لكرة القدم",
    "Category:Aruba Football Federation": "تصنيف:الاتحاد الأروبي لكرة القدم",
    "Category:Bhutan Football Federation": "تصنيف:الاتحاد البوتاني لكرة القدم",

    "Category:Bodies of water of Germany by state": "تصنيف:مسطحات مائية في ألمانيا حسب الولاية",
    "Category:Bodies of water of Carmarthenshire": "تصنيف:مسطحات مائية في كرمرثنشير",

    "Category:2023 in dependent territories of United Kingdom": "تصنيف:أقاليم ما وراء البحار البريطانية في 2023",
    "Category:Battles involving al-Qaeda in Arabian Peninsula": "تصنيف:معارك تشمل تنظيم القاعدة في جزيرة العرب",
    "Category:Film set at Metropolitan Museum of Art": "تصنيف:أفلام تقع أحداثها في متحف المتروبوليتان للفنون",
    "Category:Halo (franchise) players": "تصنيف:لاعبو هيلو (سلسلة)",
    "Category:Lists of members of Parliament of Syria": "تصنيف:قوائم أعضاء برلمان سوريا",
    "Category:National Library of Israel": "تصنيف:مكتبة إسرائيل الوطنية",
    "Category:Paintings of Judas Iscariot": "تصنيف:لوحات عن يهوذا الإسخريوطي",
    "Category:People of Third Punic War": "تصنيف:أشخاص في الحرب البونيقية الثالثة",
    "Category:Rectors of Stellenbosch University": "تصنيف:عمدات جامعة ستيلينبوش",
    "Category:Violence against LGBTQ people in Oceania": "تصنيف:عنف ضد أعلام إل جي بي تي كيو في أوقيانوسيا",
}

to_test = [
    ("test_1", data1),
    # ("test_2", data_2),
    ("test_3", data_3),
]


@pytest.mark.parametrize("category, expected", data_3.items(), ids=[k for k in data_3])
def test_3(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    add_result = {x: v for x, v in data.items() if x in diff_result and "" == diff_result.get(x)}
    dump_diff(add_result, f"{name}_add")
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
