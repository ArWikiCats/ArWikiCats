#!/usr/bin/python3
""" """

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats.new_resolvers.sports_resolvers.countries_names_and_sports import (
    resolve_countries_names_sport_with_ends,
)
from ArWikiCats.new_resolvers.sports_resolvers.nationalities_and_sports import resolve_nats_sport_multi_v2
from ArWikiCats.new_resolvers.sports_resolvers.raw_sports import (
    resolve_sport_label_unified,
)
from ArWikiCats.new_resolvers.sports_resolvers.raw_sports_with_suffixes import wrap_team_xo_normal_2025_with_ends
from ArWikiCats.new_resolvers.sports_resolvers.sport_lab_nat import sport_lab_nat_load_new

data_0 = {
    "Association football cup competitions": "منافسات كأس كرة القدم",
    "Football cup competitions in United Arab Emirates": "منافسات كأس كرة القدم في الإمارات العربية المتحدة",
    "Managers of baseball teams in Japan": "مدربو فرق كرة قاعدة في اليابان",
    "Men's football cup competitions in France": "منافسات كأس كرة القدم رجالية في فرنسا",
    "Men's football cup competitions in Scotland": "منافسات كأس كرة القدم رجالية في إسكتلندا",
    "beach volleyball racing teams": "فرق سباق كرة الطائرة الشاطئية",
    "football teams": "فرق كرة القدم",
    "canadian-football teams": "فرق كرة القدم الكندية",
    "trampolining teams": "فرق جمباز القفز",
    "tennis racing teams": "فرق سباق كرة المضرب",
    "javelin throw racing teams": "فرق سباق رمي الرمح",
    "freestyle wrestling teams": "فرق المصارعة الحرة",
    "beach soccer racing teams": "فرق سباق كرة القدم الشاطئية",
    "ice sledge hockey teams": "فرق هوكي المزلجة على الجليد",
    "motorboat teams": "فرق الزوارق النارية",
    "long jump teams": "فرق القفز الطويل",
    "beach handball racing teams": "فرق سباق كرة اليد الشاطئية",
}

resolve_team_suffix_test_data = {
    "short track speed skating cup": "كأس التزلج على مسار قصير",
    "wheelchair basketball cup": "كأس كرة السلة على الكراسي المتحركة",
    "luge cup": "كأس الزحف الثلجي",
    "motorsports racing cup": "كأس سباق رياضة المحركات",
    "speed skating cup": "كأس التزلج السريع",
    "roller hockey (quad) cup": "كأس هوكي الدحرجة",
    "association football cup": "كأس كرة القدم",
    "kick boxing racing cup": "كأس سباق الكيك بوكسينغ",
    "shot put racing cup": "كأس سباق دفع الثقل",
    "luge racing cup": "كأس سباق الزحف الثلجي",
    "water skiing cup": "كأس التزلج على الماء",
    "motocross cup": "كأس موتو كروس",
    "pencak silat cup": "كأس بنكات سيلات",
    "pesäpallo cup": "كأس بيسبالو",
    "fifa world cup racing records and statistics": "سجلات وإحصائيات سباق كأس العالم لكرة القدم",
    "davis cup racing music": "موسيقى سباق كأس ديفيز",
    "davis cup racing songs": "أغاني سباق كأس ديفيز",
    "polo cup playoffs": "تصفيات كأس بولو",
    "fifa world cup films": "أفلام كأس العالم لكرة القدم",
    "fifa futsal world cup racing manager history": "تاريخ مدربو سباق كأس العالم لكرة الصالات",
    "dragon boat cup playoffs": "تصفيات كأس سباق قوارب التنين",
    "fifa world cup racing chairmen and investors": "رؤساء ومسيرو سباق كأس العالم لكرة القدم",
    "road bicycle racing cup playoffs": "تصفيات كأس سباق دراجات على الطريق",
    "fifa world cup umpires": "حكام كأس العالم لكرة القدم",
    "fifa futsal world cup racing leagues seasons": "مواسم دوريات سباق كأس العالم لكرة الصالات",
    "davis cup tactics and skills": "مهارات كأس ديفيز",
    "formula racing cup playoffs": "تصفيات كأس سباقات فورمولا",
    "fifa world cup racing non-profit organizations": "منظمات غير ربحية سباق كأس العالم لكرة القدم",
    "long jump cup playoffs": "تصفيات كأس قفز طويل",
    "freestyle wrestling cup playoffs": "تصفيات كأس مصارعة حرة",
    "pair skating cup playoffs": "تصفيات كأس تزلج فني على الجليد",
    "beach handball cup playoffs": "تصفيات كأس كرة يد شاطئية",
    "darts cup playoffs": "تصفيات كأس سهام مريشة",
    "fifa futsal world cup racing terminology": "مصطلحات سباق كأس العالم لكرة الصالات",
    "rifle shooting cup playoffs": "تصفيات كأس رماية بندقية",
    "bullfighting cup playoffs": "تصفيات كأس مصارعة ثيران",
    "water polo cup playoffs": "تصفيات كأس كرة ماء",
    "roller skating racing cups": "كؤوس سباق تزلج بالعجلات",
    "dragon boat racing cups": "كؤوس سباق قوارب التنين",
    "racingxx cups": "كؤوس سباق سيارات",
    "silat cups": "كؤوس سيلات",
    "rugby league racing cups": "كؤوس سباق دوري رجبي",
    "speed skating racing cups": "كؤوس سباق تزلج سريع",
    "goalball racing cups": "كؤوس سباق كرة هدف",
    "boxing cups": "كؤوس بوكسينغ",
    "roller hockey cups": "كؤوس هوكي دحرجة",
    "bandy cups": "كؤوس باندي",
    "high jump racing cups": "كؤوس سباق قفز عالي",
    "powerlifting cups": "كؤوس رياضة قوة",
    "bowling cups": "كؤوس بولينج",
    "table tennis cups": "كؤوس كرة طاولة",
    "racquets racing cups": "كؤوس سباق لعبة الراح",
    "yacht racing cups": "كؤوس سباقات يخوت",
}

test_2025 = {
    # "sports cup competitions": "منافسات كؤوس رياضية",
    "defunct football cups": "كؤوس كرة قدم سابقة",
    "domestic football cups": "كؤوس كرة قدم محلية",
    "football cups": "كؤوس كرة قدم",
    "professional football cups": "كؤوس كرة قدم للمحترفين",
    "motorcycle racing cups": "كؤوس سباق دراجات نارية",
    "domestic football cup": "",  # "كؤوس كرة قدم محلية",
    "defunct football cup competitions": "",  # "منافسات كؤوس كرة قدم سابقة",
    "defunct rugby union cup competitions": "",  # "منافسات كؤوس اتحاد رجبي سابقة",
    "basketball cup competitions": "منافسات كأس كرة السلة",
    "football cup competitions": "منافسات كأس كرة القدم",
    "soccer cup competitions": "منافسات كأس كرة القدم",
    "motorcycle racing cup": "كأس سباق الدراجات النارية",
}

sport_lab2_test_data = {
    "defunct indoor boxing": "بوكسينغ داخل الصالات سابقة",
    "defunct indoor boxing clubs": "أندية بوكسينغ داخل الصالات سابقة",
    "defunct indoor boxing cups": "كؤوس بوكسينغ داخل الصالات سابقة",
    "defunct football cup competitions": "منافسات كؤوس كرة قدم سابقة",
    "defunct football cups": "كؤوس كرة قدم سابقة",
    "professional football cups": "كؤوس كرة قدم للمحترفين",
    "domestic football cup": "كؤوس كرة قدم محلية",
    "domestic football cups": "كؤوس كرة قدم محلية",
    "football cup competitions": "منافسات كؤوس كرة قدم",
    "football cups": "كؤوس كرة قدم",
    "basketball cup competitions": "منافسات كؤوس كرة سلة",
    "field hockey cup competitions": "منافسات كؤوس هوكي ميدان",
    "baseball world cup": "كأس العالم لكرة القاعدة",
    "biathlon world cup": "كأس العالم للبياثلون",
    "cricket world cup": "كأس العالم للكريكت",
    "curling world cup": "كأس العالم للكيرلنغ",
    "esports world cup": "كأس العالم للرياضة الإلكترونية",
    "hockey world cup": "كأس العالم للهوكي",
    "men's hockey world cup": "كأس العالم للهوكي للرجال",
    "men's rugby world cup": "كأس العالم للرجبي للرجال",
    "men's softball world cup": "كأس العالم للكرة اللينة للرجال",
    "netball world cup": "كأس العالم لكرة الشبكة",
    "rugby league world cup": "كأس العالم لدوري الرجبي",
    "rugby world cup": "كأس العالم للرجبي",
    "wheelchair rugby league world cup": "كأس العالم لدوري الرجبي على الكراسي المتحركة",
    "wheelchair rugby world cup": "كأس العالم للرجبي على الكراسي المتحركة",
    "women's cricket world cup ": "كأس العالم للكريكت للسيدات",
    "women's cricket world cup tournaments": "بطولات كأس العالم للكريكت للسيدات",
    "women's cricket world cup": "كأس العالم للكريكت للسيدات",
    "women's field hockey world cup": "كأس العالم لهوكي الميدان للسيدات",
    "women's hockey world cup": "كأس العالم للهوكي للسيدات",
    "women's rugby league world cup": "كأس العالم لدوري الرجبي للسيدات",
    "women's rugby world cup": "كأس العالم للرجبي للسيدات",
    "women's softball world cup": "كأس العالم للكرة اللينة للسيدات",
    "wrestling world cup": "كأس العالم للمصارعة",
}

nats_sport_multi_v2_data = {
    "yemeni mens basketball cup": "كأس اليمن لكرة السلة للرجال",
    "yemeni womens basketball cup": "كأس اليمن لكرة السلة للسيدات",
    "yemeni basketball cup": "كأس اليمن لكرة السلة",
    "yemeni defunct basketball cup": "كؤوس كرة سلة يمنية سابقة",
    "chinese domestic boxing cup": "كؤوس بوكسينغ صينية محلية",
    "chinese boxing cup": "كأس الصين للبوكسينغ",
    "chinese boxing cup competitions": "منافسات كأس الصين للبوكسينغ",
    "chinese defunct boxing cup competitions": "منافسات كؤوس بوكسينغ صينية سابقة",
    "chinese defunct indoor boxing cups": "كؤوس بوكسينغ صينية داخل الصالات سابقة",
    "chinese defunct boxing cups": "كؤوس بوكسينغ صينية سابقة",
    "chinese defunct outdoor boxing cups": "كؤوس بوكسينغ صينية في الهواء الطلق سابقة",
    "chinese professional boxing cups": "كؤوس بوكسينغ صينية للمحترفين",
    "chinese indoor boxing cups": "كؤوس بوكسينغ صينية داخل الصالات",
    "chinese outdoor boxing cups": "كؤوس بوكسينغ صينية في الهواء الطلق",
    "chinese domestic boxing cups": "كؤوس بوكسينغ صينية محلية",
    "chinese domestic women's boxing cups": "كؤوس بوكسينغ صينية محلية للسيدات",
    "chinese boxing cups": "كؤوس بوكسينغ صينية",
}

sport_lab_nat_load_new_data = {
    "asian domestic football cups": "كؤوس كرة قدم آسيوية محلية",
    "austrian football cups": "كؤوس كرة قدم نمساوية",
    "belgian football cups": "كؤوس كرة قدم بلجيكية",
    "dutch football cups": "كؤوس كرة قدم هولندية",
    "english football cups": "كؤوس كرة قدم إنجليزية",
    "european domestic football cups": "كؤوس كرة قدم أوروبية محلية",
    "german football cups": "كؤوس كرة قدم ألمانية",
    "irish football cups": "كؤوس كرة قدم أيرلندية",
    "italian football cups": "كؤوس كرة قدم إيطالية",
    "north american domestic football cups": "كؤوس كرة قدم أمريكية شمالية محلية",
    "oceanian domestic football cups": "كؤوس كرة قدم أوقيانوسية محلية",
    "republic-of ireland football cups": "كؤوس كرة قدم أيرلندية",
    "scottish football cups": "كؤوس كرة قدم إسكتلندية",
    "spanish basketball cups": "كؤوس كرة سلة إسبانية",
    "spanish football cups": "كؤوس كرة قدم إسبانية",
    "thai football cups": "كؤوس كرة قدم تايلندية",
    "welsh football cups": "كؤوس كرة قدم ويلزية",
}

rcn_sport_with_ends_data = {
    "new zealand amateur kick boxing cup": "كأس نيوزيلندا للكيك بوكسينغ للهواة",
    "new zealand youth kick boxing cup": "كأس نيوزيلندا للكيك بوكسينغ للشباب",
    "new zealand men's kick boxing cup": "كأس نيوزيلندا للكيك بوكسينغ للرجال",
    "new zealand women's kick boxing cup": "كأس نيوزيلندا للكيك بوكسينغ للسيدات",
    "new zealand kick boxing cup": "كأس نيوزيلندا للكيك بوكسينغ",
    "yemen amateur kick boxing cup": "كأس اليمن للكيك بوكسينغ للهواة",
    "yemen youth kick boxing cup": "كأس اليمن للكيك بوكسينغ للشباب",
    "yemen men's kick boxing cup": "كأس اليمن للكيك بوكسينغ للرجال",
    "yemen women's kick boxing cup": "كأس اليمن للكيك بوكسينغ للسيدات",
    "yemen kick boxing cup": "كأس اليمن للكيك بوكسينغ",
}

to_test = [
    ("test_sport_lab2_data", sport_lab2_test_data, wrap_team_xo_normal_2025_with_ends),
    ("test_resolve_nats_sport_multi_v2", nats_sport_multi_v2_data, resolve_nats_sport_multi_v2),
    ("test_sport_lab_nat_load_new", sport_lab_nat_load_new_data, sport_lab_nat_load_new),
    ("test_rcn_sport_with_ends", rcn_sport_with_ends_data, resolve_countries_names_sport_with_ends),
    # ---
    ("test_test_sport_cup_1", sport_lab2_test_data, resolve_nats_sport_multi_v2),
    ("test_test_sport_cup_2", sport_lab2_test_data, sport_lab_nat_load_new),
    ("test_test_sport_cup_3", sport_lab2_test_data, resolve_countries_names_sport_with_ends),
    ("test_resolve_sport_label_unified", resolve_team_suffix_test_data, resolve_sport_label_unified),
    # ---
]


@pytest.mark.parametrize(
    "category, expected", resolve_team_suffix_test_data.items(), ids=resolve_team_suffix_test_data.keys()
)
@pytest.mark.fast
def test_resolve_team_suffix(category: str, expected: str) -> None:
    label1 = resolve_sport_label_unified(category)
    assert label1 == expected


@pytest.mark.parametrize("category, expected", test_2025.items(), ids=test_2025.keys())
@pytest.mark.fast
def test_wrap_team_xo_normal_2025(category: str, expected: str) -> None:
    label1 = wrap_team_xo_normal_2025_with_ends(category)
    assert label1 == expected


@pytest.mark.parametrize("category, expected", nats_sport_multi_v2_data.items(), ids=nats_sport_multi_v2_data.keys())
@pytest.mark.skip2
def test_resolve_nats_sport_multi_v2(category: str, expected: str) -> None:
    label1 = resolve_nats_sport_multi_v2(category)
    assert isinstance(label1, str)
    assert label1 == expected


@pytest.mark.parametrize("category, expected", sport_lab2_test_data.items(), ids=sport_lab2_test_data.keys())
@pytest.mark.skip2
def test_sport_lab2_data(category: str, expected: str) -> None:
    label1 = wrap_team_xo_normal_2025_with_ends(category)
    assert isinstance(label1, str)
    assert label1 == expected


@pytest.mark.parametrize(
    "category, expected", sport_lab_nat_load_new_data.items(), ids=sport_lab_nat_load_new_data.keys()
)
@pytest.mark.skip2
def test_sport_lab_nat_load_new(category: str, expected: str) -> None:
    label1 = sport_lab_nat_load_new(category)
    assert isinstance(label1, str)
    assert label1 == expected


@pytest.mark.parametrize("category, expected", rcn_sport_with_ends_data.items(), ids=rcn_sport_with_ends_data.keys())
@pytest.mark.skip2
def test_rcn_sport_with_ends(category: str, expected: str) -> None:
    label1 = resolve_countries_names_sport_with_ends(category)
    assert isinstance(label1, str)
    assert label1 == expected


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.skip2
def test_dump_it(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)

    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
