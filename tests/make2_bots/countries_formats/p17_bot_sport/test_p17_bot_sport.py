"""
Tests
"""

import pytest
from typing import Callable

from load_one_data import dump_diff, one_dump_test
from ArWikiCats.make_bots.countries_formats.p17_bot_sport import get_p17_with_sport

# =========================================================
#                   get_p17_with_sport
# =========================================================

data_1 = {
    "africa football league": "دوري إفريقيا لكرة القدم",
    "angola basketball cup": "كأس أنغولا لكرة السلة",
    "angola national football team lists": "قوائم منتخب أنغولا لكرة القدم",
    "argentina national field hockey team navigational boxes": "صناديق تصفح منتخب الأرجنتين لهوكي الميدان",
    "argentina national football team navigational boxes": "صناديق تصفح منتخب الأرجنتين لكرة القدم",
    "armenia national football team managers": "مدربو منتخب أرمينيا لكرة القدم",
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
    "democratic-republic-of-congo national football team matches": "مباريات منتخب جمهورية الكونغو الديمقراطية لكرة القدم",
    "denmark national field hockey team navigational boxes": "صناديق تصفح منتخب الدنمارك لهوكي الميدان",
    "denmark national men's ice hockey team": "منتخب الدنمارك لهوكي الجليد للرجال",
    "ecuador national football team results": "نتائج منتخب الإكوادور لكرة القدم",
    "england football league": "دوري إنجلترا لكرة القدم",
    "england national women's cricket team": "منتخب إنجلترا للكريكت للسيدات",
    "england national women's rugby union team matches": "مباريات منتخب إنجلترا لاتحاد الرجبي للسيدات",
    "fiji national rugby union team": "منتخب فيجي لاتحاد الرجبي",
    "finland national football team navigational boxes": "صناديق تصفح منتخب فنلندا لكرة القدم",
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
    "kosovo national football team managers": "مدربو منتخب كوسوفو لكرة القدم",
    "liberia national football team": "منتخب ليبيريا لكرة القدم",
    "malaysia national football team results": "نتائج منتخب ماليزيا لكرة القدم",
    "maldives national women's football team": "منتخب جزر المالديف لكرة القدم للسيدات",
    "mauritania national basketball team": "منتخب موريتانيا لكرة السلة",
    "mauritius national women's football team": "منتخب موريشيوس لكرة القدم للسيدات",
    "mexico national women's football team navigational boxes": "صناديق تصفح منتخب المكسيك لكرة القدم للسيدات",
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
    "trinidad and tobago national football team managers": "مدربو منتخب ترينيداد وتوباغو لكرة القدم",
    "turkey national women's volleyball team coaches": "مدربو منتخب تركيا لكرة الطائرة للسيدات",
    "united states national field hockey team": "منتخب الولايات المتحدة لهوكي الميدان",
    "united states national men's soccer team records and statistics": "سجلات وإحصائيات منتخب الولايات المتحدة لكرة القدم للرجال",
    "united states national men's soccer team records": "سجلات منتخب الولايات المتحدة لكرة القدم للرجال",
    "united states national rugby league team coaches": "مدربو منتخب الولايات المتحدة لدوري الرجبي",
    "wales national football team results": "نتائج منتخب ويلز لكرة القدم",
    "wales national women's rugby league team players": "لاعبات منتخب ويلز لدوري الرجبي للسيدات",
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_get_p17_with_sport_1(category: str, expected: str) -> None:
    label = get_p17_with_sport(category)
    assert label == expected


# =========================================================
#                   DUMP
# =========================================================

TEMPORAL_CASES = [
    ("test_get_p17_with_sport_1", data_1, get_p17_with_sport),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback, do_strip=False)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
