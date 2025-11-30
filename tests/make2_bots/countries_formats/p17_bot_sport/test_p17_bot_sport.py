"""
Tests
"""

import pytest

from load_one_data import dump_diff, one_dump_test
from ArWikiCats.make_bots.countries_formats.p17_bot_sport import (
    get_p17_with_sport,
    Get_Sport_Format_xo_en_ar_is_P17,
)

# =========================================================
#                   get_p17_with_sport
# =========================================================

data_1 = {
    "armenia national football team managers": "مدربو منتخب أرمينيا لكرة القدم",
    "kosovo national football team managers": "مدربو منتخب كوسوفو لكرة القدم",
    "trinidad and tobago national football team managers": "مدربو منتخب ترينيداد وتوباغو لكرة القدم",
    "tunisia national team": "منتخبات تونس الوطنية",
    "tunisia national teams": "منتخبات تونس الوطنية",
    "tunisia rally championship": "بطولة تونس للراليات",
    "venezuela international footballers": "لاعبو منتخب فنزويلا لكرة القدم ",
    "venezuela rally championship": "بطولة فنزويلا للراليات",
    "yemen rally championship": "بطولة اليمن للراليات",
    "yemen sports templates": "قوالب اليمن الرياضية",
    "zambia international footballers": "لاعبو منتخب زامبيا لكرة القدم ",
    "zambia rally championship": "بطولة زامبيا للراليات",
    "zimbabwe international footballers": "لاعبو منتخب زيمبابوي لكرة القدم ",
    "zimbabwe rally championship": "بطولة زيمبابوي للراليات",
}
data_2 = {
    "africa football league": "دوري إفريقيا لكرة القدم",
    "angola basketball cup": "كأس أنغولا لكرة السلة",
    "angola national football team lists": "قوائم منتخب أنغولا لكرة القدم",
    "argentina national field hockey team navigational boxes": "صناديق تصفح منتخب الأرجنتين لهوكي الميدان",
    "argentina national football team navigational boxes": "صناديق تصفح منتخب الأرجنتين لكرة القدم",
    "aruba national football team navigational boxes": "صناديق تصفح منتخب أروبا لكرة القدم",
    "australia national men's under-23 soccer team": "منتخب أستراليا لكرة القدم تحت 23 سنة للرجال",
    "australia national netball team": "منتخب أستراليا لكرة الشبكة",
    "australia national water polo team": "منتخب أستراليا لكرة الماء",
    "austria national basketball team": "منتخب النمسا لكرة السلة",
    "belgium national basketball team": "منتخب بلجيكا لكرة السلة",
    "brazil national rugby league team": "منتخب البرازيل لدوري الرجبي",
    "brazil national under-23 football team results": "نتائج منتخب البرازيل لكرة القدم تحت 23 سنة",
    "brazil national women's football team managers": "مدربو منتخب البرازيل لكرة القدم للسيدات",
    "cameroon national women's football team navigational boxes": "صناديق تصفح منتخب الكاميرون لكرة القدم للسيدات",
    "canada national basketball team players": "لاعبو منتخب كندا لكرة السلة",
    "canada national men's soccer team matches": "مباريات منتخب كندا لكرة القدم للرجال",
    "canada national women's soccer team navigational boxes": "صناديق تصفح منتخب كندا لكرة القدم للسيدات",
    "china national baseball team navigational boxes": "صناديق تصفح منتخب الصين لكرة القاعدة",
    "china national football team results": "نتائج منتخب الصين لكرة القدم",
    "colombia national under-20 football team managers": "مدربو منتخب كولومبيا لكرة القدم تحت 20 سنة",
    "croatia national football team": "منتخب كرواتيا لكرة القدم",
    "cuba national football team navigational boxes": "صناديق تصفح منتخب كوبا لكرة القدم",
    "czech republic national futsal team navigational boxes": "صناديق تصفح منتخب التشيك لكرة الصالات",
    "czech republic national women's football team managers": "مدربو منتخب التشيك لكرة القدم للسيدات",
    "democratic-republic-of-the-congo national football team matches": "مباريات منتخب جمهورية الكونغو الديمقراطية لكرة القدم",
    "denmark national field hockey team navigational boxes": "صناديق تصفح منتخب الدنمارك لهوكي الميدان",
    "denmark national men's ice hockey team": "منتخب الدنمارك لهوكي الجليد للرجال",
    "ecuador national football team results": "نتائج منتخب الإكوادور لكرة القدم",
    "england football league": "دوري إنجلترا لكرة القدم",
    "england national women's cricket team": "منتخب إنجلترا للكريكت للسيدات",
    "england national women's rugby union team matches": "مباريات منتخب إنجلترا لاتحاد الرجبي للسيدات",
    "fiji national rugby union team": "منتخب فيجي لاتحاد الرجبي",
    "fiji women's international rugby union players": "لاعبات اتحاد رجبي دوليات من فيجي",
    "finland national football team navigational boxes": "صناديق تصفح منتخب فنلندا لكرة القدم",
    "france international women's rugby sevens players": "لاعبات سباعيات رجبي دوليات من فرنسا",
    "france national football team": "منتخب فرنسا لكرة القدم",
    "france national under-21 football team": "منتخب فرنسا لكرة القدم تحت 21 سنة",
    "germany national football team": "منتخب ألمانيا لكرة القدم",
    "germany national under-21 football team managers": "مدربو منتخب ألمانيا لكرة القدم تحت 21 سنة",
    "ghana national football team": "منتخب غانا لكرة القدم",
    "guinea national football team": "منتخب غينيا لكرة القدم",
    "hong kong national football team matches": "مباريات منتخب هونغ كونغ لكرة القدم",
    "hungary national men's ice hockey team": "منتخب المجر لهوكي الجليد للرجال",
    "iceland national women's football team": "منتخب آيسلندا لكرة القدم للسيدات",
    "india national women's football team": "منتخب الهند لكرة القدم للسيدات",
    "israel national football team matches": "مباريات منتخب إسرائيل لكرة القدم",
    "italy national women's football team": "منتخب إيطاليا لكرة القدم للسيدات",
    "italy national women's water polo team coaches": "مدربو منتخب إيطاليا لكرة الماء للسيدات",
    "ivory coast national football team navigational boxes": "صناديق تصفح منتخب ساحل العاج لكرة القدم",
    "jamaica national women's football team navigational boxes": "صناديق تصفح منتخب جامايكا لكرة القدم للسيدات",
    "kazakhstan national handball team templates": "قوالب منتخب كازاخستان لكرة اليد",
    "liberia national football team": "منتخب ليبيريا لكرة القدم",
    "malaysia national football team results": "نتائج منتخب ماليزيا لكرة القدم",
    "maldives national women's football team": "منتخب جزر المالديف لكرة القدم للسيدات",
    "mali summer olympics football": "كرة قدم مالي في الألعاب الأولمبية الصيفية",
    "mauritania national basketball team": "منتخب موريتانيا لكرة السلة",
    "mauritius national women's football team": "منتخب موريشيوس لكرة القدم للسيدات",
    "mexico national women's football team navigational boxes": "صناديق تصفح منتخب المكسيك لكرة القدم للسيدات",
    "moldova football manager history": "تاريخ مدربو كرة قدم مولدافيا",
    "netherlands national rugby union team coaches": "مدربو منتخب هولندا لاتحاد الرجبي",
    "new zealand national women's cricket team": "منتخب نيوزيلندا للكريكت للسيدات",
    "new zealand national women's football team managers": "مدربو منتخب نيوزيلندا لكرة القدم للسيدات",
    "new zealand national women's rugby league team": "منتخب نيوزيلندا لدوري الرجبي للسيدات",
    "nigeria professional football league": "دوري نيجيريا لكرة القدم للمحترفين",
    "norway football league": "دوري النرويج لكرة القدم",
    "palestine national football team": "منتخب فلسطين لكرة القدم",
    "paraguay national handball team templates": "قوالب منتخب باراغواي لكرة اليد",
    "paraguay national women's football team navigational boxes": "صناديق تصفح منتخب باراغواي لكرة القدم للسيدات",
    "peru national football team navigational boxes": "صناديق تصفح منتخب بيرو لكرة القدم",
    "philippines national football team records and statistics": "سجلات وإحصائيات منتخب الفلبين لكرة القدم",
    "philippines national football team records": "سجلات منتخب الفلبين لكرة القدم",
    "philippines national women's football team navigational boxes": "صناديق تصفح منتخب الفلبين لكرة القدم للسيدات",
    "poland summer olympics football": "كرة قدم بولندا في الألعاب الأولمبية الصيفية",
    "portugal national football team records and statistics": "سجلات وإحصائيات منتخب البرتغال لكرة القدم",
    "portugal national football team records": "سجلات منتخب البرتغال لكرة القدم",
    "qatar national football team navigational boxes": "صناديق تصفح منتخب قطر لكرة القدم",
    "romania national rugby union team": "منتخب رومانيا لاتحاد الرجبي",
    "russia national futsal team navigational boxes": "صناديق تصفح منتخب روسيا لكرة الصالات",
    "russia national handball team templates": "قوالب منتخب روسيا لكرة اليد",
    "russia national volleyball team": "منتخب روسيا لكرة الطائرة",
    "russia national women's basketball team": "منتخب روسيا لكرة السلة للسيدات",
    "scotland football league": "دوري إسكتلندا لكرة القدم",
    "scotland national field hockey team navigational boxes": "صناديق تصفح منتخب إسكتلندا لهوكي الميدان",
    "scotland national rugby union team": "منتخب إسكتلندا لاتحاد الرجبي",
    "senegal national football team matches": "مباريات منتخب السنغال لكرة القدم",
    "senegal national football team navigational boxes": "صناديق تصفح منتخب السنغال لكرة القدم",
    "serbia national men's basketball team": "منتخب صربيا لكرة السلة للرجال",
    "slovakia national handball team templates": "قوالب منتخب سلوفاكيا لكرة اليد",
    "slovenia football league": "دوري سلوفينيا لكرة القدم",
    "south africa national soccer team results": "نتائج منتخب جنوب إفريقيا لكرة القدم",
    "south africa national water polo team navigational boxes": "صناديق تصفح منتخب جنوب إفريقيا لكرة الماء",
    "south africa national women's cricket team templates": "قوالب منتخب جنوب إفريقيا للكريكت للسيدات",
    "south korea national rugby sevens team coaches": "مدربو منتخب كوريا الجنوبية لسباعيات الرجبي",
    "south korea national volleyball team navigational boxes": "صناديق تصفح منتخب كوريا الجنوبية لكرة الطائرة",
    "south korea national women's football team managers": "مدربو منتخب كوريا الجنوبية لكرة القدم للسيدات",
    "soviet union national basketball team": "منتخب الاتحاد السوفيتي لكرة السلة",
    "soviet union national water polo team navigational boxes": "صناديق تصفح منتخب الاتحاد السوفيتي لكرة الماء",
    "soviet union national water polo team": "منتخب الاتحاد السوفيتي لكرة الماء",
    "spain national rugby union team navigational boxes": "صناديق تصفح منتخب إسبانيا لاتحاد الرجبي",
    "spain national water polo team navigational boxes": "صناديق تصفح منتخب إسبانيا لكرة الماء",
    "spain national women's water polo team coaches": "مدربو منتخب إسبانيا لكرة الماء للسيدات",
    "sweden national under-21 football team managers": "مدربو منتخب السويد لكرة القدم تحت 21 سنة",
    "switzerland national men's ice hockey team": "منتخب سويسرا لهوكي الجليد للرجال",
    "switzerland national women's basketball team": "منتخب سويسرا لكرة السلة للسيدات",
    "togo national women's basketball team": "منتخب توغو لكرة السلة للسيدات",
    "turkey national women's volleyball team coaches": "مدربو منتخب تركيا لكرة الطائرة للسيدات",
    "united states national field hockey team": "منتخب الولايات المتحدة لهوكي الميدان",
    "united states national men's soccer team records and statistics": "سجلات وإحصائيات منتخب الولايات المتحدة لكرة القدم للرجال",
    "united states national men's soccer team records": "سجلات منتخب الولايات المتحدة لكرة القدم للرجال",
    "united states national rugby league team coaches": "مدربو منتخب الولايات المتحدة لدوري الرجبي",
    "wales national football team results": "نتائج منتخب ويلز لكرة القدم",
    "wales national women's rugby league team players": "لاعبات منتخب ويلز لدوري الرجبي للسيدات",
}

data_3 = {
    # "yemen international footballers": "لاعبو كرة قدم دوليون من اليمن",
    "yemen international footballers": "لاعبو منتخب اليمن لكرة القدم",
    "yemen international soccer players": "لاعبو منتخب اليمن لكرة القدم",

    "democratic-republic-of-the-congo amateur international soccer players": "لاعبو منتخب جمهورية الكونغو الديمقراطية لكرة القدم للهواة",

    "yemen under-13 international footballers": "لاعبو منتخب اليمن تحت 13 سنة لكرة القدم ",
    "yemen under-14 international footballers": "لاعبو منتخب اليمن تحت 14 سنة لكرة القدم ",

    "tunisia sports templates": "قوالب تونس الرياضية",
    "angola men's international footballers": "لاعبو منتخب أنغولا لكرة القدم للرجال",
    "aruba men's under-20 international footballers": "لاعبو منتخب أروبا تحت 20 سنة لكرة القدم للرجال",
    "bolivia men's international footballers": "لاعبو منتخب بوليفيا لكرة القدم للرجال",
    "bulgaria women's international footballers": "لاعبات منتخب بلغاريا لكرة القدم للسيدات",
    "chad sports templates": "قوالب تشاد الرياضية",
    "costa rica sports templates": "قوالب كوستاريكا الرياضية",
    "croatia men's international footballers": "لاعبو منتخب كرواتيا لكرة القدم للرجال",
    "cyprus women's international footballers": "لاعبات منتخب قبرص لكرة القدم للسيدات",
    "czech republic men's youth international footballers": "لاعبو منتخب التشيك لكرة القدم للشباب",
    "democratic-republic-of-the-congo men's a' international footballers": "لاعبو منتخب جمهورية الكونغو الديمقراطية لكرة القدم للرجال للمحليين",
    "guam men's international footballers": "لاعبو منتخب غوام لكرة القدم للرجال",
    "guam women's international footballers": "لاعبات منتخب غوام لكرة القدم للسيدات",
    "guinea-bissau women's international footballers": "لاعبات منتخب غينيا بيساو لكرة القدم للسيدات",
    "iceland women's youth international footballers": "لاعبات منتخب آيسلندا لكرة القدم للشابات",
    "latvia men's youth international footballers": "لاعبو منتخب لاتفيا لكرة القدم للشباب",
    "lithuania men's under-21 international footballers": "لاعبو منتخب ليتوانيا تحت 21 سنة لكرة القدم للرجال",
    "malawi men's international footballers": "لاعبو منتخب مالاوي لكرة القدم للرجال",
    "malaysia women's international footballers": "لاعبات منتخب ماليزيا لكرة القدم للسيدات",
    "mauritania men's under-20 international footballers": "لاعبو منتخب موريتانيا تحت 20 سنة لكرة القدم للرجال",
    "mauritania sports templates": "قوالب موريتانيا الرياضية",
    "mexico women's international footballers": "لاعبات منتخب المكسيك لكرة القدم للسيدات",
    "north korea men's international footballers": "لاعبو منتخب كوريا الشمالية لكرة القدم للرجال",
    "peru men's youth international footballers": "لاعبو منتخب بيرو لكرة القدم للشباب",
    "poland men's international footballers": "لاعبو منتخب بولندا لكرة القدم للرجال",
    "san marino men's international footballers": "لاعبو منتخب سان مارينو لكرة القدم للرجال",
    "slovakia sports templates": "قوالب سلوفاكيا الرياضية",
    "switzerland men's youth international footballers": "لاعبو منتخب سويسرا لكرة القدم للشباب",
    "tanzania sports templates": "قوالب تنزانيا الرياضية",
    "tunisia men's a' international footballers": "لاعبو منتخب تونس لكرة القدم للرجال للمحليين",
    "ukraine women's international footballers": "لاعبات منتخب أوكرانيا لكرة القدم للسيدات",
    "zambia men's youth international footballers": "لاعبو منتخب زامبيا لكرة القدم للشباب",
    "zambia women's international footballers": "لاعبات منتخب زامبيا لكرة القدم للسيدات"
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=list(data_1.keys()))
@pytest.mark.fast
def test_get_p17_with_sport_1(category, expected) -> None:
    label = get_p17_with_sport(category)
    assert label.strip() == expected.strip()


@pytest.mark.parametrize("category, expected", data_2.items(), ids=list(data_2.keys()))
@pytest.mark.fast
def test_get_p17_with_sport_data_2(category, expected) -> None:
    label = get_p17_with_sport(category)
    assert label.strip() == expected.strip()


@pytest.mark.parametrize("category, expected", data_3.items(), ids=list(data_3.keys()))
@pytest.mark.fast
def test_get_p17_with_sport_data_3(category, expected) -> None:
    label = get_p17_with_sport(category)
    assert label.strip() == expected.strip()


# =========================================================
#                   Get_Sport_Format_xo_en_ar_is_P17
# =========================================================

data2 = {
    "national women's soccer team": "منتخب {} لكرة القدم للسيدات",
    "winter olympics softball": "كرة لينة {} في الألعاب الأولمبية الشتوية",
}


@pytest.mark.parametrize("category, expected_key", data2.items(), ids=list(data2.keys()))
@pytest.mark.fast
def test_Get_Sport_Format_xo_en_ar_is_P17(category, expected_key) -> None:
    label = Get_Sport_Format_xo_en_ar_is_P17(category)
    assert label.strip() == expected_key


# =========================================================
#                   DUMP
# =========================================================

TEMPORAL_CASES = [
    ("test_get_p17_with_sport_1", data_1, get_p17_with_sport),
    ("test_get_p17_with_sport_2", data_2, get_p17_with_sport),
    ("test_get_p17_with_sport_3", data_3, get_p17_with_sport),
    ("test_Get_Sport_Format_xo_en_ar_is_P17", data2, Get_Sport_Format_xo_en_ar_is_P17),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name, data, callback):
    expected, diff_result = one_dump_test(data, callback, do_strip=True)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
