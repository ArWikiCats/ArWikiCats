#
import pytest
from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset, dump_diff

data = {
    "Category:Afghan competitors by sports event": "تصنيف:منافسون أفغان حسب الحدث الرياضي",
    "Category:American basketball players by ethnic or national origin": "تصنيف:لاعبو كرة سلة أمريكيون حسب الأصل العرقي أو الوطني",
    "Category:Argentina at the Universiade": "تصنيف:الأرجنتين في الألعاب الجامعية",
    "Category:Argentina at the Winter Olympics": "تصنيف:الأرجنتين في الألعاب الأولمبية الشتوية",
    "Category:Association football players by amateur national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني للهواة",
    "Category:Association football players by under-20 national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني تحت 20 سنة",
    "Category:Association football players by under-21 national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني تحت 21 سنة",
    "Category:Association football players by under-23 national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني تحت 23 سنة",
    "Category:Association football players by youth national team": "تصنيف:لاعبو كرة قدم حسب المنتخب الوطني للشباب",
    "Category:Association football": "تصنيف:كرة القدم",
    "Category:Athletics at the Summer Universiade navigational boxes": "تصنيف:صناديق تصفح ألعاب القوى في الألعاب الجامعية الصيفية",
    "Category:Athletics at the Universiade navigational boxes": "تصنيف:صناديق تصفح ألعاب القوى في الألعاب الجامعية",
    "Category:Australia at the Summer Universiade": "تصنيف:أستراليا في الألعاب الجامعية الصيفية",
    "Category:Australia international soccer players": "تصنيف:لاعبو منتخب أستراليا لكرة القدم",
    "Category:Australian male sprinters": "تصنيف:عداؤون سريعون ذكور أستراليون",
    "Category:Canada men's international soccer players": "تصنيف:لاعبو منتخب كندا لكرة القدم للرجال",
    "Category:Canadian sports businesspeople": "تصنيف:شخصيات أعمال رياضيون كنديون",
    "Category:Cape Verde at the Paralympics": "تصنيف:الرأس الأخضر في الألعاب البارالمبية",
    "Category:Cape Verdean football managers": "تصنيف:مدربو كرة قدم أخضريون",
    "Category:Egyptian female sport shooters": "تصنيف:لاعبات رماية مصريات",
    "Category:Egyptian male sport shooters": "تصنيف:لاعبو رماية ذكور مصريون",
    "Category:Egyptian sport shooters": "تصنيف:لاعبو رماية مصريون",
    "Category:Emirati football in 2017": "تصنيف:كرة القدم الإماراتية في 2017",
    "Category:Emirati football in 2017–18": "تصنيف:كرة القدم الإماراتية في 2017–18",
    "Category:England amateur international footballers": "تصنيف:لاعبو منتخب إنجلترا لكرة القدم للهواة",
    "Category:Equatoguinean women's footballers": "تصنيف:لاعبات كرة قدم غينيات استوائيات",
    "Category:European national under-21 association football teams": "تصنيف:منتخبات كرة قدم وطنية أوروبية تحت 21 سنة",
    "Category:Expatriate women's association football players": "تصنيف:لاعبات كرة قدم مغتربات",
    "Category:Expatriate women's footballers by location": "تصنيف:لاعبات كرة قدم مغتربات حسب الموقع",
    "Category:Female association football managers": "تصنيف:مديرات كرة قدم",
    "Category:Female short track speed skaters": "تصنيف:متزلجات على مسار قصير",
    "Category:Female speed skaters": "تصنيف:متزلجات سرعة",
    "Category:Figure skaters at the 2002 Winter Olympics": "تصنيف:متزلجون فنيون في الألعاب الأولمبية الشتوية 2002",
    "Category:Figure skaters at the 2003 Asian Winter Games": "تصنيف:متزلجون فنيون في الألعاب الآسيوية الشتوية 2003",
    "Category:Figure skaters at the 2007 Winter Universiade": "تصنيف:متزلجون فنيون في الألعاب الجامعية الشتوية 2007",
    "Category:Figure skaters by competition": "تصنيف:متزلجون فنيون حسب المنافسة",
    "Category:Figure skating coaches": "تصنيف:مدربو تزلج فني",
    "Category:Figure skating people": "تصنيف:أعلام تزلج فني",
    "Category:Icelandic male athletes": "تصنيف:لاعبو قوى ذكور آيسلنديون",
    "Category:Icelandic male runners": "تصنيف:عداؤون ذكور آيسلنديون",
    "Category:Icelandic male steeplechase runners": "تصنيف:عداؤو موانع ذكور آيسلنديون",
    "Category:IndyCar": "تصنيف:أندي كار",
    "Category:International sports competitions hosted by Mexico": "تصنيف:منافسات رياضية دولية استضافتها المكسيك",
    "Category:Irish association football managers": "تصنيف:مدربو كرة قدم أيرلنديون",
    "Category:Lists of association football players by national team": "تصنيف:قوائم لاعبو كرة قدم حسب المنتخب الوطني",
    "Category:Male long-distance runners": "تصنيف:عداؤو مسافات طويلة ذكور",
    "Category:Male runners by nationality": "تصنيف:عداؤون ذكور حسب الجنسية",
    "Category:Male steeplechase runners": "تصنيف:عداؤو موانع ذكور",
    "Category:Moroccan competitors by sports event": "تصنيف:منافسون مغاربة حسب الحدث الرياضي",
    "Category:Moroccan male middle-distance runners": "تصنيف:عداؤو مسافات متوسطة ذكور مغاربة",
    "Category:Nations at the 2010 Summer Youth Olympics": "تصنيف:بلدان في الألعاب الأولمبية الشبابية الصيفية 2010",
    "Category:Norwegian figure skaters": "تصنيف:متزلجون فنيون نرويجيون",
    "Category:Norwegian male pair skaters": "تصنيف:متزلجون فنيون على الجليد ذكور نرويجيون",
    "Category:Norwegian male single skaters": "تصنيف:متزلجون فرديون ذكور نرويجيون",
    "Category:Norwegian pair skaters": "تصنيف:متزلجون فنيون على الجليد نرويجيون",
    "Category:Norwegian short track speed skaters": "تصنيف:متزلجون على مسار قصير نرويجيون",
    "Category:Olympic competitors for Cape Verde": "تصنيف:منافسون أولمبيون من الرأس الأخضر",
    "Category:Olympic figure skaters of Argentina": "تصنيف:متزلجون فنيون أولمبيون من الأرجنتين",
    "Category:Olympic figure skaters of Armenia": "تصنيف:متزلجون فنيون أولمبيون من أرمينيا",
    "Category:Olympic figure skaters of Australia": "تصنيف:متزلجون فنيون أولمبيون من أستراليا",
    "Category:Olympic figure skating": "تصنيف:تزلج فني أولمبي",
    "Category:Olympic medalists in alpine skiing": "تصنيف:فائزون بميداليات أولمبية في التزلج على المنحدرات الثلجية",
    "Category:Olympic shooters of Egypt": "تصنيف:رماة أولمبيون من مصر",
    "Category:Olympic short track speed skaters of Japan": "تصنيف:متزلجون على مسار قصير أولمبيون من اليابان",
    "Category:Rail transport in the United Kingdom": "تصنيف:السكك الحديدية في المملكة المتحدة",
    "Category:Republic of Ireland football managers": "تصنيف:مدربو كرة قدم أيرلنديون",
    "Category:Roller skaters at the 2003 Pan American Games": "تصنيف:متزلجون بالعجلات في دورة الألعاب الأمريكية 2003",
    "Category:Seasons in Omani football": "تصنيف:مواسم في كرة القدم العمانية",
    "Category:Ski jumpers at the 2007 Winter Universiade": "تصنيف:متزلجو قفز في الألعاب الجامعية الشتوية 2007",
    "Category:Ski jumping at the Winter Universiade": "تصنيف:القفز التزلجي في الألعاب الجامعية الشتوية",
    "Category:Skiing coaches": "تصنيف:مدربو تزلج",
    "Category:South Africa international soccer players": "تصنيف:لاعبو منتخب جنوب إفريقيا لكرة القدم",
    "Category:Sports at the Summer Universiade": "تصنيف:ألعاب رياضية في الألعاب الجامعية الصيفية",
    "Category:Sports competitors by nationality and competition": "تصنيف:منافسون رياضيون حسب الجنسية والمنافسة",
    "Category:Sports organisations of Andorra": "تصنيف:منظمات رياضية في أندورا",
    "Category:Sportspeople from Boston": "تصنيف:رياضيون من بوسطن",
    "Category:Table tennis clubs": "تصنيف:أندية كرة طاولة",
    "Category:Transport disasters in 2017": "تصنيف:كوارث نقل في 2017",
    "Category:Turkish expatriate sportspeople": "تصنيف:رياضيون أتراك مغتربون",
    "Category:Universiade medalists by sport": "تصنيف:فائزون بميداليات الألعاب الجامعية حسب الرياضة",
    "Category:Universiade medalists in water polo": "تصنيف:فائزون بميداليات الألعاب الجامعية في كرة الماء",
    "Category:Water polo at the Summer Universiade": "تصنيف:كرة الماء في الألعاب الجامعية الصيفية",
    "Category:Women's national sports teams of Cuba": "تصنيف:منتخبات رياضية وطنية نسائية في كوبا",
    "Category:Women's national youth association football teams": "تصنيف:منتخبات كرة قدم وطنية للشابات",
    "Category:World Judo Championships": "تصنيف:بطولة العالم للجودو",
    "Category:Youth athletics competitions": "تصنيف:منافسات ألعاب قوى شبابية",
    "Category:Youth athletics": "تصنيف:ألعاب القوى للشباب",
    "Category:Youth sports competitions": "تصنيف:منافسات رياضية شبابية",
    "Category:football in 2050–51": "تصنيف:كرة القدم في 2050–51",
    "Category:nations at the universiade": "تصنيف:بلدان في الألعاب الجامعية",
    "Category:ugandan football": "تصنيف:كرة القدم الأوغندية"
}


def test_sports():
    print(f"len of data: {len(data)}")
    org, diff = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff, "test_sports")
    assert diff == org, f"Differences found: {len(diff)}"


def test_sports_2():
    data = {
        "Category:Afghanistan national football team managers": "تصنيف:مدربو منتخب أفغانستان لكرة القدم",
        "Category:African women's national association football teams": "تصنيف:منتخبات كرة قدم وطنية إفريقية للسيدات",
        "Category:Argentina women's international footballers": "تصنيف:لاعبات منتخب الأرجنتين لكرة القدم للسيدات",
        "Category:Association football players by women's national team": "تصنيف:لاعبو كرة قدم حسب منتخب السيدات الوطني",
        "Category:Belgian athletics coaches": "تصنيف:مدربو ألعاب قوى بلجيكيون",
        "Category:Coaches of national cricket teams": "تصنيف:مدربو من منتخبات كريكت وطنية",
        "Category:International women's basketball competitions hosted by Cuba": "تصنيف:منافسات كرة سلة نسائية دولية استضافتها كوبا",
        "Category:Paralympic competitors for Cape Verde": "تصنيف:منافسون في الألعاب البارالمبية من الرأس الأخضر",
        "Category:Spanish sports broadcasters": "تصنيف:مذيعو رياضية إسبانية",
        "Category:Sports broadcasters by nationality": "تصنيف:مذيعو رياضية حسب الجنسية",
        "Category:Sports coaches by nationality": "تصنيف:مدربو رياضة حسب الجنسية",
        "Category:Transport companies established in 1909": "تصنيف:شركات النقل أسست في 1909",
        "Category:Women's sports teams in Cuba": "تصنيف:فرق الرياضات النسوية في كوبا",
    }
    print(f"len of data: {len(data)}")
    org, diff = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff, "test_sports")
    assert diff == org, f"Differences found: {len(diff)}"


@pytest.mark.skip(reason="Test data incomplete")
def test_sports_3():
    data = {
        "Category:Afghanistan women's national football team coaches": "",
        "Category:Coaches of Yemen national cricket team": "",
        "Category:Coaches of the West Indies national cricket team": "",
        "Category:Cuba women's national basketball team": "",
        "Category:Equatorial Guinea women's national football team": "",
        "Category:National under-18 ice hockey teams": "",
        "Category:Nauru international soccer players": "",
        "Category:Women's national ice hockey teams": "",
        "Category:Women's national under-18 ice hockey teams": "",
    }
    print(f"len of data: {len(data)}")
    org, diff = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff, "test_sports")
    assert diff == org, f"Differences found: {len(diff)}"
