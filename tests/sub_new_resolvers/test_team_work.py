"""
Tests
"""

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar
from ArWikiCats.sub_new_resolvers.team_work import resolve_clubs_teams_leagues
from utils.dump_runner import make_dump_test_name_data_callback

test_data_0 = {
    "Category:waba champions cup": "تصنيف:كأس دوري غرب آسيا لكرة السلة",
    "west bank premier league": "الدوري الفلسطيني الممتاز للضفة الغربية",
    "Category:African Nations Championship": "تصنيف:كأس الأمم الإفريقية للمحليين",
}
fast_data = {
    "major league baseball owners and executives": "رؤساء تنفيذيون وملاك دوري كرة القاعدة الرئيسي",
    "wta tour seasons": "مواسم رابطة محترفات التنس",
    "ad alcorcón seasons": "مواسم نادي ألكوركون",
    "aj auxerre seasons": "مواسم نادي أوكسير",
    "aldershot f.c. managers": "مدربو نادي ألدرشوت",
    "algerian ligue professionnelle 1 seasons": "مواسم الرابطة الجزائرية المحترفة الأولى",
    "associação chapecoense de futebol seasons": "مواسم نادي شابيكوينسي",
    "bc brno players": "لاعبو نادي برنو لكرة السلة",
    "bc juventus players": "لاعبو أوتينوس يوفنتوس",
    "bc lietkabelis coaches": "مدربو نادي ليتكابليس لكرة السلة",
    "birmingham city f.c. seasons": "مواسم برمنغهام سيتي",
    "blackburn rovers f.c. seasons": "مواسم بلاكبيرن روفرز",
    "blackpool f.c. seasons": "مواسم نادي بلاكبول",
    "boston redskins coaches": "مدربو بوسطن ريدسكينس",
    "buffalo sabres coaches": "مدربو بافالو سيبرز",
    "canton charge players": "لاعبو كانتون شارج",
    "charlotte hornets owners": "ملاك شارلوت هورنتس",
    "copa américa managers": "مدربو كوبا أمريكا",
    "cs sfaxien players": "لاعبو النادي الرياضي الصفاقسي",
    "fc barcelona managers": "مدربو نادي برشلونة",
    "fc bunyodkor players": "لاعبو نادي بونيودكور لكرة القدم",
    "fc dinamo batumi players": "لاعبو نادي دينامو باتومي",
    "fc gueugnon players": "لاعبو نادي غويونيون",
    "fc haka players": "لاعبو هكا",
    "fc nantes seasons": "مواسم نادي نانت",
    "fc petrolul ploiești seasons": "مواسم نادي بترولول بلويشتي لكرة القدم",
    "fc wacker innsbruck seasons": "مواسم واكر انسبروك",
    "fifa women's world cup managers": "مدربو كأس العالم لكرة القدم للسيدات",
    "fk borac banja luka managers": "مدربو نادي بوراتس بانيا لوكا",
    "fk horizont turnovo seasons": "مواسم نادي هوريزونت تورنوفو",
    "fk spartaks jūrmala players": "لاعبو نادي سبارتاكس يورمالا",
    "gfa league first division players": "لاعبو دوري الدرجة الأولى الغامبي",
    "gimnasia y esgrima de jujuy managers": "مدربو خميناسيا خوخوي",
    "harlem globetrotters coaches": "مدربو هارلم غلوبتروترز",
    "houston rockets seasons": "مواسم هيوستن روكتس",
    "if elfsborg managers": "مدربو نادي إلفسبورغ",
    "ifk mariehamn seasons": "مواسم نادي ماريهامن",
    "kashiwa reysol players": "لاعبو كاشيوا ريسول",
    "kazma sc players": "لاعبو نادي كاظمة",
    "knattspyrnufélag reykjavíkur managers": "مدربو ناتدبيرنوفيلاغ ريكيافيكور",
    "liga mx seasons": "مواسم الدوري المكسيكي الممتاز",
    "ljungskile sk players": "لاعبو نادي ليونغسكايل",
    "los angeles angels coaches": "مدربو لوس أنجلوس آنجلز لأنهايم",
    "mc oran players": "لاعبو مولودية وهران",
    "mighty jets f.c. players": "لاعبو مايتي جيتس",
    "oakland raiders owners": "ملاك أوكلاند ريدرز",
    "orlando pride players": "لاعبو أورلاندو برايد",
    "pfc beroe stara zagora players": "لاعبو نادي بيروي ستارا زاغورا",
    "portsmouth f.c. players": "لاعبو نادي بورتسموث",
    "rampla juniors managers": "مدربو رامبلا جونيورز",
    "san antonio spurs owners": "ملاك سان أنطونيو سبرز",
    "silkeborg if players": "لاعبو نادي سيلكيبورج",
    "smouha sc players": "لاعبو نادي سموحة",
    "stade lavallois players": "لاعبو نادي لافال",
    "tunisian ligue professionnelle 2 managers": "مدربو الرابطة التونسية المحترفة الثانية لكرة القدم",
    "u.d. leiria players": "لاعبو يو دي ليريا",
    "udinese calcio players": "لاعبو نادي أودينيزي",
    "utah jazz players": "لاعبو يوتا جاز",
    "vegas golden knights coaches": "مدربو فيجاس جولدن نايتس",
    "washington state cougars football players": "لاعبو واشنطن ستايت كوجرز فوتبول",
    "western sydney wanderers fc players": "لاعبو نادي وسترن سيدني واندررز",
}

fast_data_not_same = {
    # "baseball world cup players": "لاعبو كأس العالم لكرة القاعدة",
    # "egyptian second division seasons": "مواسم الدوري المصري الدرجة الثانية",
    # "rugby world cup referees": "حكام كأس العالم للرجبي",
    # "taekwondo competitions": "منافسات تايكوندو",
    "aj auxerre matches": "مباريات نادي أوكسير",
    "al ansar fc matches": "مباريات نادي الأنصار",
    "atlante f.c. footballers": "لاعبو أتلانتي إف سي",
    "bayer 04 leverkusen non-playing staff": "طاقم باير 04 ليفركوزن غير اللاعبين",
    "borussia dortmund non-playing staff": "طاقم بوروسيا دورتموند غير اللاعبين",
    "c.d. tondela matches": "مباريات نادي تونديلا",
    "copa américa matches": "مباريات كوبا أمريكا",
    "dallas cowboys personnel": "أفراد دالاس كاوبويز",
    "deportivo toluca f.c. matches": "مباريات نادي تولوكا",
    "derry city f.c. matches": "مباريات ديري سيتي",
    "go ahead eagles matches": "مباريات غو أهد إيغلز",
    "ipswich town f.c. non-playing staff": "طاقم إيبسويتش تاون غير اللاعبين",
    "kayserispor footballers": "لاعبو كايسري سبور",
    "nac breda non-playing staff": "طاقم إن أي سي بريدا غير اللاعبين",
    "philadelphia 76ers lists": "قوائم فيلادلفيا سفنتي سيكسرز",
    "queensland lions fc matches": "مباريات كوينزلاند ليونز",
    "racing club de avellaneda non-playing staff": "طاقم نادي راسينغ غير اللاعبين",
    "rosario central matches": "مباريات روزاريو سنترال",
    "toronto argonauts lists": "قوائم تورونتو أرغونتس",
    "uae president's cup matches": "مباريات كأس رئيس دولة الإمارات",
    "vegalta sendai matches": "مباريات فيغالتا سنداي",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_fast_data_1(category: str, expected: str) -> None:
    label = resolve_clubs_teams_leagues(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_fast_data_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


to_test = [
    # ("test_fast_data_1", fast_data, resolve_clubs_teams_leagues),
    ("test_fast_data_2", fast_data, resolve_label_ar),
]

test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
