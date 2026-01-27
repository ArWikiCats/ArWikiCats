#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_empty = {
    "lists of 20th millennium women's olympic table tennis players films by city": "قوائم أفلام لاعبات كرة طاولة أولمبيات الألفية 20 حسب المدينة",
    "2020 women's wheelchair tennis players by city": "لاعبات كرة مضرب على كراسي متحركة نسائية في 2020 حسب المدينة",
    "2020 wheelchair tennis by city": "كرة المضرب على الكراسي المتحركة في 2020 حسب المدينة",
    "Political positions of the 2000 United States presidential candidates": "مواقف سياسية لمرشحي الرئاسة الأمريكية 2000",
    "Political positions of the 2008 United States presidential candidates": "مواقف سياسية لمرشحي الرئاسة الأمريكية 2008",
    "Political positions of the 2016 United States presidential candidates": "مواقف سياسية لمرشحي الرئاسة الأمريكية 2016",
    "Political positions of the 2020 United States presidential candidates": "مواقف سياسية لمرشحي الرئاسة الأمريكية 2020",
    "Political positions of the 2024 United States presidential candidates": "مواقف سياسية لمرشحي الرئاسة الأمريكية 2024",
    "17th-century dukes of Limburg": "دوقات ليمبورغ في القرن 17",
    "Politics and technology": "السياسة والتقانة",
    "National association football second-tier league champions": "x",
    "Association football third-tier league seasons": "x",
    "Association football second-tier league seasons": "x",
    "Association football fourth-tier league seasons": "x",
    "National association football third-tier leagues": "x",
    "National association football fifth-tier leagues": "x",
    "National association football fourth-tier leagues": "x",
    "National association football second-tier leagues": "x",
    "National association football seventh-tier leagues": "x",
    "National association football sixth-tier leagues": "x",
    "Seasons in European third-tier association football leagues": "x",
    "Academic staff of Incheon National University": "أعضاء هيئة تدريس جامعة إنتشون الوطنية",
    "Lists of 1900s films": "قوائم أفلام إنتاج عقد 1900",
    "Academic staff of University of Galați": "أعضاء هيئة تدريس جامعة غالاتس",
    "Women members of Senate of Spain": "عضوات مجلس شيوخ إسبانيا",
    "Defunct shopping malls in Malaysia": "مراكز تسوق سابقة في ماليزيا",
    "Defunct communist parties in Nepal": "أحزاب شيوعية سابقة في نيبال",
    "Defunct European restaurants in London": "مطاعم أوروبية سابقة في لندن",
    "Burial sites of Aragonese royal houses": "",
    "Burial sites of Castilian royal houses": "",
    "Burial sites of Frankish noble families": "",
    "Burial sites of Georgian royal dynasties": "",
    "Burial sites of Hawaiian royal houses": "",
    "Burial sites of Hessian noble families": "",
    "Burial sites of Kotromanić dynasty": "",
    "Burial sites of Leonese royal houses": "",
    "Burial sites of Lorraine noble families": "",
    "Burial sites of Lower Saxon noble families": "",
    "Burial sites of Muslim dynasties": "",
    "Burial sites of Navarrese royal houses": "",
    "Burial sites of Neapolitan royal houses": "",
    "Burial sites of noble families": "",
    "Burial sites of Norman families": "",
}

data0 = {
    "chess composers": "مؤلفو مسائل شطرنج",
    "cultural depictions of Canadian activists": "تصوير ثقافي عن ناشطون كنديون",
    "Assassinated Canadian activists": "ناشطون كنديون مغتالون",
    "Assassinated Guatemalan diplomats": "دبلوماسيون غواتيماليون مغتالون",
    "Assassinated Swedish diplomats": "دبلوماسيون سويديون مغتالون",
    "Ancient Indian people by occupation": "هنود قدماء حسب المهنة",
    "Fictional Australian criminals": "مجرمون أستراليون خياليون",
    "Assassinated Peruvian politicians": "سياسيون بيرويون مغتالون",
    # "Native American women leaders": "قائدات أمريكيات أصليون",
    "yemeni national junior women's under-16 football teams players": "لاعبات منتخبات كرة قدم وطنية يمنية تحت 16 سنة للناشئات",
    "yemeni national junior women's football teams players": "لاعبات منتخبات كرة قدم وطنية يمنية للناشئات",
    "yemeni national women's under-16 football teams players": "لاعبات منتخبات كرة قدم وطنية يمنية تحت 16 سنة للسيدات",
    "yemeni national youth women's under-16 football teams players": "لاعبات منتخبات كرة قدم وطنية يمنية تحت 16 سنة للشابات",
    "yemeni national youth women's football teams players": "لاعبات منتخبات كرة قدم وطنية يمنية للشابات",
    "zaïrean wheelchair sports federation": "الاتحاد الزائيري للرياضة على الكراسي المتحركة",
    "surinamese sports federation": "الاتحاد السورينامي للرياضة",
    "Romania football manager history navigational boxes": "صناديق تصفح تاريخ مدربو كرة قدم رومانيا",
    "Jewish football clubs": "أندية كرة القدم اليهودية",
    "Jewish sports": "ألعاب رياضية يهودية",
    "European League of Football coaches": "مدربو الدوري الأوروبي لكرة القدم",
    "Australian soccer by year": "كرة القدم الأسترالية حسب السنة",
    "Political positions of United States presidential candidates": "مواقف سياسية لمرشحي الرئاسة الأمريكية",
}

data1 = {
    "Lists of American reality television series episodes": "قوائم حلقات مسلسلات تلفزيونية واقعية أمريكية",
    "Academic staff of University of Nigeria": "أعضاء هيئة تدريس جامعة نيجيريا",
    "Early modern history of Portugal": "تاريخ البرتغال الحديث المبكر",
    "south american second tier football leagues": "دوريات كرة قدم أمريكية جنوبية من الدرجة الثانية",
    "european second tier basketball leagues": "دوريات كرة سلة أوروبية من الدرجة الثانية",
    "european second tier ice hockey leagues": "دوريات هوكي جليد أوروبية من الدرجة الثانية",
    "israeli basketball premier league": "الدوري الإسرائيلي الممتاز لكرة السلة",
    "Burial sites of ancient Irish dynasties": "مواقع دفن أسر أيرلندية قديمة",
    "Burial sites of Arab dynasties": "مواقع دفن أسر عربية",
    "Burial sites of Asian royal families": "مواقع دفن عائلات ملكية آسيوية",
    "Burial sites of Austrian noble families": "مواقع دفن عائلات نبيلة نمساوية",
    "Burial sites of Belgian noble families": "مواقع دفن عائلات نبيلة بلجيكية",
    "Burial sites of Bohemian royal houses": "مواقع دفن بيوت ملكية بوهيمية",
    "Burial sites of Bosnian noble families": "مواقع دفن عائلات نبيلة بوسنية",
    "Burial sites of British royal houses": "مواقع دفن بيوت ملكية بريطانية",
    "Burial sites of Bulgarian royal houses": "مواقع دفن بيوت ملكية بلغارية",
    "Burial sites of Byzantine imperial dynasties": "مواقع دفن أسر إمبراطورية بيزنطية",
    "Burial sites of Cornish families": "مواقع دفن عائلات كورنية",
    "Burial sites of Danish noble families": "مواقع دفن عائلات نبيلة دنماركية",
    "Burial sites of Dutch noble families": "مواقع دفن عائلات نبيلة هولندية",
    "Burial sites of English families": "مواقع دفن عائلات إنجليزية",
    "Burial sites of English royal houses": "مواقع دفن بيوت ملكية إنجليزية",
    "Burial sites of European noble families": "مواقع دفن عائلات نبيلة أوروبية",
    "Burial sites of European royal families": "مواقع دفن عائلات ملكية أوروبية",
    "Burial sites of French noble families": "مواقع دفن عائلات نبيلة فرنسية",
    "Burial sites of French royal families": "مواقع دفن عائلات ملكية فرنسية",
    "Burial sites of German noble families": "مواقع دفن عائلات نبيلة ألمانية",
    "Burial sites of German royal houses": "مواقع دفن بيوت ملكية ألمانية",
    "Burial sites of Hungarian noble families": "مواقع دفن عائلات نبيلة مجرية",
    "Burial sites of Hungarian royal houses": "مواقع دفن بيوت ملكية مجرية",
    "Burial sites of Iranian dynasties": "مواقع دفن أسر إيرانية",
    "Burial sites of Irish noble families": "مواقع دفن عائلات نبيلة أيرلندية",
    "Burial sites of Irish royal families": "مواقع دفن عائلات ملكية أيرلندية",
    "Burial sites of Italian noble families": "مواقع دفن عائلات نبيلة إيطالية",
    "Burial sites of Italian royal houses": "مواقع دفن بيوت ملكية إيطالية",
    "Burial sites of Lithuanian noble families": "مواقع دفن عائلات نبيلة ليتوانية",
    "Burial sites of Luxembourgian noble families": "مواقع دفن عائلات نبيلة لوكسمبورغية",
    "Burial sites of Mexican noble families": "مواقع دفن عائلات نبيلة مكسيكية",
    "Burial sites of Middle Eastern royal families": "مواقع دفن عائلات ملكية شرقية أوسطية",
    "Burial sites of Polish noble families": "مواقع دفن عائلات نبيلة بولندية",
    "Burial sites of Polish royal houses": "مواقع دفن بيوت ملكية بولندية",
    "Burial sites of Romanian noble families": "مواقع دفن عائلات نبيلة رومانية",
    "Burial sites of Romanian royal houses": "مواقع دفن بيوت ملكية رومانية",
    "Burial sites of imperial Chinese families": "مواقع دفن أسر إمبراطورية صينية",
}

data_2 = {}

data_3 = {
    "1550 in asian women's football": "كرة قدم آسيوية للسيدات في 1550",
    "1520 in south american women's football": "كرة قدم أمريكية جنوبية للسيدات في 1520",
    "canadian women's ice hockey by league": "هوكي جليد كندية للسيدات حسب الدوري",
    "european women's football by country": "كرة قدم أوروبية للسيدات حسب البلد",
    "south american women's football": "كرة قدم أمريكية جنوبية للسيدات",
    "1789 in south american women's football": "كرة قدم أمريكية جنوبية للسيدات في 1789",
    "european national men's field hockey teams": "منتخبات هوكي ميدان وطنية أوروبية للرجال",
    "northern ireland national men's football teams": "منتخبات كرة قدم وطنية أيرلندية شمالية للرجال",
}

to_test = [
    ("test_5_data_0", data0),
    # ("test_5_data_1", data1),
    # ("test_5_data_3", data_3),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
def test_5_data_0(category: str, expected: str) -> None:
    """
    pytest tests/event_lists/importants/test_5_important.py::test_5_data_0
    """
    assert resolve_label_ar(category) == expected


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
def test_5_data_1(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
def test_5_data_3(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
