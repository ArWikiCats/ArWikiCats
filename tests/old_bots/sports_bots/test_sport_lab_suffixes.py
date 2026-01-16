"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.legacy_bots.sport_lab_suffixes import get_teams_new

get_teams_new_data = {
    "international cricket records and statistics": "سجلات وإحصائيات كريكت دولية",
    "sports cup competitions": "منافسات كؤوس رياضية",
    "international men's football competitions": "منافسات كرة قدم دولية للرجال",
    "international women's basketball competitions": "منافسات كرة سلة دولية للسيدات",
    "international women's cricket competitions": "منافسات كريكت دولية للسيدات",
    "international women's field hockey competitions": "منافسات هوكي ميدان دولية للسيدات",
    "international women's football competitions": "منافسات كرة قدم دولية للسيدات",
    "under-13 equestrian manager history": "تاريخ مدربو فروسية تحت 13 سنة",
    "under-14 equestrian manager history": "تاريخ مدربو فروسية تحت 14 سنة",
    "soccer cup competitions": "منافسات كؤوس كرة قدم",
    "national youth baseball teams": "منتخبات كرة قاعدة وطنية شبابية",
    "national youth basketball teams": "منتخبات كرة سلة وطنية شبابية",
    "australian rules football awards": "جوائز كرة قدم أسترالية",
    "badminton world cup": "كأس العالم لتنس الريشة",
    "baseball commissioners": "مفوضو كرة قاعدة",
    "baseball music": "موسيقى كرة قاعدة",
    "baseball video games": "ألعاب فيديو كرة قاعدة",
    "basketball awards": "جوائز كرة سلة",
    "basketball comics": "قصص مصورة كرة سلة",
    "basketball cup competitions": "منافسات كؤوس كرة سلة",
    "basketball league": "دوري كرة السلة",
    "basketball terminology": "مصطلحات كرة سلة",
    "biathlon world cup": "كأس العالم للبياثلون",
    "bowling broadcasters": "مذيعو بولينج",
    "bowling television series": "مسلسلات تلفزيونية بولينج",
    "boxing world cup": "كأس العالم للبوكسينغ",
    "canoeing logos": "شعارات ركوب الكنو",
    "current football seasons": "مواسم كرة قدم حالية",
    "cycling races": "سباقات سباق دراجات هوائية",
    "cycling television series": "مسلسلات تلفزيونية سباق دراجات هوائية",
    "defunct american football teams": "فرق كرة قدم أمريكية سابقة",
    "defunct baseball leagues": "دوريات كرة قاعدة سابقة",
    "defunct baseball teams": "فرق كرة قاعدة سابقة",
    "defunct basketball competitions": "منافسات كرة سلة سابقة",
    "defunct basketball teams": "فرق كرة سلة سابقة",
    "defunct cycling teams": "فرق سباق دراجات هوائية سابقة",
    "defunct esports competitions": "منافسات رياضة إلكترونية سابقة",
    "defunct football clubs": "أندية كرة قدم سابقة",
    "defunct football competitions": "منافسات كرة قدم سابقة",
    "defunct football cup competitions": "منافسات كؤوس كرة قدم سابقة",
    "defunct football cups": "كؤوس كرة قدم سابقة",
    "defunct football leagues": "دوريات كرة قدم سابقة",
    "defunct gaelic football competitions": "منافسات كرة قدم غالية سابقة",
    "defunct hockey competitions": "منافسات هوكي سابقة",
    "defunct ice hockey leagues": "دوريات هوكي جليد سابقة",
    "defunct ice hockey teams": "فرق هوكي جليد سابقة",
    "defunct indoor soccer leagues": "دوريات كرة قدم داخل الصالات سابقة",
    "defunct netball leagues": "دوريات كرة شبكة سابقة",
    "defunct rugby league teams": "فرق دوري رجبي سابقة",
    "defunct rugby union cup competitions": "منافسات كؤوس اتحاد رجبي سابقة",
    "defunct rugby union leagues": "دوريات اتحاد رجبي سابقة",
    "defunct rugby union teams": "فرق اتحاد رجبي سابقة",
    "defunct soccer clubs": "أندية كرة قدم سابقة",
    "defunct sports clubs": "أندية رياضية سابقة",
    "defunct sports competitions": "منافسات رياضية سابقة",
    "defunct sports leagues": "دوريات رياضية سابقة",
    "defunct water polo clubs": "أندية كرة ماء سابقة",
    "defunct water polo competitions": "منافسات كرة ماء سابقة",
    "domestic cricket competitions": "منافسات كريكت محلية",
    "domestic football cup": "كؤوس كرة قدم محلية",
    "domestic football cups": "كؤوس كرة قدم محلية",
    "domestic football leagues": "دوريات كرة قدم محلية",
    "domestic football": "كرة قدم محلية",
    "domestic handball leagues": "دوريات كرة يد محلية",
    "domestic women's football leagues": "دوريات كرة قدم محلية للسيدات",
    "fencing logos": "شعارات مبارزة سيف شيش",
    "first-class cricket": "كريكت من الدرجة الأولى",
    "football chairmen and investors": "رؤساء ومسيرو كرة قدم",
    "football cup competitions": "منافسات كؤوس كرة قدم",
    "football cups": "كؤوس كرة قدم",
    "football governing bodies": "هيئات تنظيم كرة قدم",
    "football league": "دوري كرة القدم",
    "go comics": "قصص مصورة غو",
    "indoor football": "كرة قدم داخل الصالات",
    "indoor hockey": "هوكي داخل الصالات",
    "indoor track and field": "سباقات مضمار وميدان داخل الصالات",
    "international aquatics competitions": "منافسات رياضات مائية دولية",
    "international archery competitions": "منافسات نبالة دولية",
    "international athletics competitions": "منافسات ألعاب قوى دولية",
    "international bandy competitions": "منافسات باندي دولية",
    "international baseball competitions": "منافسات كرة قاعدة دولية",
    "international basketball competitions": "منافسات كرة سلة دولية",
    "international boxing competitions": "منافسات بوكسينغ دولية",
    "international cricket competitions": "منافسات كريكت دولية",
    "international cycle races": "سباقات دراجات دولية",
    "international fencing competitions": "منافسات مبارزة سيف شيش دولية",
    "international field hockey competitions": "منافسات هوكي ميدان دولية",
    "international figure skating competitions": "منافسات تزلج فني دولية",
    "international football competitions": "منافسات كرة قدم دولية",
    "international futsal competitions": "منافسات كرة صالات دولية",
    "international gymnastics competitions": "منافسات جمباز دولية",
    "international handball competitions": "منافسات كرة يد دولية",
    "international ice hockey competitions": "منافسات هوكي جليد دولية",
    "international karate competitions": "منافسات كاراتيه دولية",
    "international kickboxing competitions": "منافسات كيك بوكسينغ دولية",
    "international netball players": "لاعبو كرة شبكة دوليون",
    "international roller hockey competitions": "منافسات هوكي دحرجة دولية",
    "international rugby league competitions": "منافسات دوري رجبي دولية",
    "international rugby union competitions": "منافسات اتحاد رجبي دولية",
    "international shooting competitions": "منافسات رماية دولية",
    "international softball competitions": "منافسات كرة لينة دولية",
    "international speed skating competitions": "منافسات تزلج سريع دولية",
    "international volleyball competitions": "منافسات كرة طائرة دولية",
    "international water polo competitions": "منافسات كرة ماء دولية",
    "international weightlifting competitions": "منافسات رفع أثقال دولية",
    "international wrestling competitions": "منافسات مصارعة دولية",
    "international youth basketball competitions": "منافسات كرة سلة شبابية دولية",
    "international youth football competitions": "منافسات كرة قدم شبابية دولية",
    "ju-jitsu world championships": "بطولة العالم للجوجوتسو",
    "men's hockey world cup": "كأس العالم للهوكي للرجال",
    "men's international basketball": "كرة سلة دولية للرجال",
    "men's international football": "كرة قدم دولية للرجال",
    "muay thai video games": "ألعاب فيديو موياي تاي",
    "multi-national basketball leagues": "دوريات كرة سلة متعددة الجنسيات",
    "national basketball team results": "نتائج منتخبات كرة سلة وطنية",
    "national cycling champions": "أبطال بطولات سباق دراجات هوائية وطنية",
    "national equestrian manager history": "تاريخ مدربو منتخبات فروسية وطنية",
    "national football team results": "نتائج منتخبات كرة قدم وطنية",
    "national ice hockey teams": "منتخبات هوكي جليد وطنية",
    "national junior football teams": "منتخبات كرة قدم وطنية للناشئين",
    "national junior men's handball teams": "منتخبات كرة يد وطنية للناشئين",
    "national lacrosse league": "دوريات لاكروس وطنية",
    "national men's equestrian manager history": "تاريخ مدربو منتخبات فروسية وطنية للرجال",
    "national rugby union premier leagues": "دوريات اتحاد رجبي وطنية من الدرجة الممتازة",
    "national rugby union teams": "منتخبات اتحاد رجبي وطنية",
    "national shooting championships": "بطولات رماية وطنية",
    "national squash teams": "منتخبات اسكواش وطنية",
    "national under-13 equestrian manager history": "تاريخ مدربو منتخبات فروسية تحت 13 سنة",
    "national under-14 equestrian manager history": "تاريخ مدربو منتخبات فروسية تحت 14 سنة",
    "national water polo teams": "منتخبات كرة ماء وطنية",
    "national women's equestrian manager history": "تاريخ مدربو منتخبات فروسية وطنية للسيدات",
    "netball world cup": "كأس العالم لكرة الشبكة",
    "outdoor equestrian": "فروسية في الهواء الطلق",
    "outdoor ice hockey": "هوكي جليد في الهواء الطلق",
    "premier lacrosse league": "دوريات لاكروس من الدرجة الممتازة",
    "professional football cups": "كؤوس كرة قدم للمحترفين",
    "professional ice hockey leagues": "دوريات هوكي جليد للمحترفين",
    "professional sports leagues": "دوريات رياضية للمحترفين",
    "roller hockey logos": "شعارات هوكي دحرجة",
    "rowing equipment": "معدات تجديف",
    "rugby league chairmen and investors": "رؤساء ومسيرو دوري رجبي",
    "rugby league world cup": "كأس العالم لدوري الرجبي",
    "shooting sports equipment": "معدات رماية",
    "snooker terminology": "مصطلحات سنوكر",
    "summer olympics football": "كرة القدم في الألعاب الأولمبية الصيفية",
    "summer olympics volleyball": "كرة الطائرة في الألعاب الأولمبية الصيفية",
    "summer olympics water polo": "كرة الماء في الألعاب الأولمبية الصيفية",
    "tennis logos": "شعارات كرة مضرب",
    "under-13 equestrian": "فروسية تحت 13 سنة",
    "under-14 equestrian": "فروسية تحت 14 سنة",
    "under-16 basketball": "كرة سلة تحت 16 سنة",
    "under-19 basketball": "كرة سلة تحت 19 سنة",
    "under-23 cycle racing": "سباق دراجات تحت 23 سنة",
    "water polo comics": "قصص مصورة كرة ماء",
    "water polo competition": "منافسات كرة ماء",
    "women's cricket world cup": "كأس العالم للكريكت للسيدات",
    "women's hockey world cup": "كأس العالم للهوكي للسيدات",
    "women's international football": "كرة قدم دولية للسيدات",
    "women's international futsal": "كرة صالات دولية للسيدات",
    "women's softball world cup": "كأس العالم للكرة اللينة للسيدات",
    "world athletics championships": "بطولة العالم لألعاب القوى",
    "world netball championship": "بطولة العالم لكرة الشبكة",
    "world netball championships": "بطولة العالم لكرة الشبكة",
    "world rowing championships medalists": "فائزون بميداليات بطولة العالم للتجديف",
    "world taekwondo championships": "بطولة العالم للتايكوندو",
    "wrestling world cup": "كأس العالم للمصارعة",
}


@pytest.mark.parametrize("category, expected_key", get_teams_new_data.items(), ids=get_teams_new_data.keys())
@pytest.mark.fast
def test_get_teams_new_data(category: str, expected_key: str) -> None:
    label = get_teams_new(category)
    assert label == expected_key


to_test = [
    ("test_get_teams_new_data", get_teams_new_data),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, get_teams_new)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


def test_get_teams_new() -> None:
    # Test with a basic input
    result = get_teams_new("football team")
    assert isinstance(result, str)

    result_empty = get_teams_new("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = get_teams_new("basketball team")
    assert isinstance(result_various, str)
