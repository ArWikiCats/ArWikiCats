"""
Tests
"""

import pytest

from src.make2_bots.sports_bots.team_work import Get_Club, Get_team_work_Club

fast_data = {
    "ad alcorcón seasons": "مواسم نادي ألكوركون",
    "aj auxerre matches": "مباريات نادي أوكسير",
    "aj auxerre seasons": "مواسم نادي أوكسير",
    "al ansar fc matches": "مباريات نادي الأنصار",
    "albanian cup seasons": "مواسم كأس ألبانيا",
    "aldershot f.c. managers": "مدربو نادي ألدرشوت",
    "algerian ligue professionnelle 1 seasons": "مواسم الرابطة الجزائرية المحترفة الأولى",
    "american football films": "أفلام كرة القدم الأمريكية",
    "american football league seasons": "مواسم دوري كرة القدم الأمريكية",
    "american indoor soccer league seasons": "مواسم الدوري الأمريكي لكرة القدم داخل الصالات",
    "associação chapecoense de futebol seasons": "مواسم نادي شابيكوينسي",
    "atlante f.c. footballers": "لاعبو أتلانتي إف سي",
    "baseball world cup players": "لاعبو كأس العالم لكرة القاعدة",
    "bayer 04 leverkusen non-playing staff": "طاقم باير 04 ليفركوزن غير اللاعبين",
    "bc brno players": "لاعبو نادي برنو لكرة السلة",
    "bc juventus players": "لاعبو أوتينوس يوفنتوس",
    "bc lietkabelis coaches": "مدربو نادي ليتكابليس لكرة السلة",
    "birmingham city f.c. seasons": "مواسم برمنغهام سيتي",
    "blackburn rovers f.c. seasons": "مواسم بلاكبيرن روفرز",
    "blackpool f.c. seasons": "مواسم نادي بلاكبول",
    "borussia dortmund non-playing staff": "طاقم بوروسيا دورتموند غير اللاعبين",
    "boston redskins coaches": "مدربو بوسطن ريدسكينس",
    "buffalo sabres coaches": "مدربو بافالو سيبرز",
    "c.d. tondela matches": "مباريات نادي تونديلا",
    "canton charge players": "لاعبو كانتون شارج",
    "charlotte hornets owners": "ملاك شارلوت هورنتس",
    "chinese professional baseball league awards": "جوائز دوري كرة القاعدة الصيني للمحترفين",
    "copa américa managers": "مدربو كوبا أمريكا",
    "copa américa matches": "مباريات كوبا أمريكا",
    "cs sfaxien players": "لاعبو النادي الرياضي الصفاقسي",
    "cuban football logos": "شعارات كرة القدم الكوبية",
    "czech deaf people": "أعلام تشيكيون صم",
    "dallas cowboys personnel": "أفراد دالاس كاوبويز",
    "danish dance songs": "أغاني رقص دنماركي",
    "deaf culture": "ثقافة صم",
    "deportivo toluca f.c. matches": "مباريات نادي تولوكا",
    "derry city f.c. matches": "مباريات ديري سيتي",
    "egyptian second division seasons": "مواسم الدوري المصري الدرجة الثانية",
    "fc barcelona managers": "مدربو نادي برشلونة",
    "fc bunyodkor players": "لاعبو نادي بونيودكور لكرة القدم",
    "fc dinamo batumi players": "لاعبو نادي دينامو باتومي",
    "fc gueugnon players": "لاعبو نادي غويونيون",
    "fc haka players": "لاعبو هكا",
    "fc nantes seasons": "مواسم نادي نانت",
    "fc petrolul ploiești seasons": "مواسم نادي بترولول بلويشتي لكرة القدم",
    "fc wacker innsbruck seasons": "مواسم واكر انسبروك",
    "fictional executed people": "أعلام معدومون خياليون",
    "fifa women's world cup managers": "مدربو كأس العالم لكرة القدم للسيدات",
    "fk borac banja luka managers": "مدربو نادي بوراتس بانيا لوكا",
    "fk horizont turnovo seasons": "مواسم نادي هوريزونت تورنوفو",
    "fk spartaks jūrmala players": "لاعبو نادي سبارتاكس يورمالا",
    "gfa league first division players": "لاعبو دوري الدرجة الأولى الغامبي",
    "gimnasia y esgrima de jujuy managers": "مدربو خميناسيا خوخوي",
    "go ahead eagles matches": "مباريات غو أهد إيغلز",
    "harlem globetrotters coaches": "مدربو هارلم غلوبتروترز",
    "hong kong rock songs": "أغاني روك هونغ كونغي",
    "houston rockets seasons": "مواسم هيوستن روكتس",
    "if elfsborg managers": "مدربو نادي إلفسبورغ",
    "ifk mariehamn seasons": "مواسم نادي ماريهامن",
    "ipswich town f.c. non-playing staff": "طاقم إيبسويتش تاون غير اللاعبين",
    "irish pop songs": "أغاني بوب أيرلندي",
    "kashiwa reysol players": "لاعبو كاشيوا ريسول",
    "kayserispor footballers": "لاعبو كايسري سبور",
    "kazma sc players": "لاعبو نادي كاظمة",
    "knattspyrnufélag reykjavíkur managers": "مدربو ناتدبيرنوفيلاغ ريكيافيكور",
    "korean traditional music": "موسيقى تقليدية كوري",
    "lao premier league seasons": "مواسم الدوري اللاوسي الممتاز",
    "liga mx seasons": "مواسم الدوري المكسيكي الممتاز",
    "ljungskile sk players": "لاعبو نادي ليونغسكايل",
    "los angeles angels coaches": "مدربو لوس أنجلوس آنجلز لأنهايم",
    "luxembourgian european commissioners": "مفوضو أوروبيون لوكسمبورغيون",
    "major league baseball owners and executives": "رؤساء تنفيذيون وملاك دوري كرة القاعدة الرئيسي",
    "mc oran players": "لاعبو مولودية وهران",
    "mexican revolution films": "أفلام الثورة المكسيكية",
    "middle eastern traditional music": "موسيقى تقليدية شرق أوسطي",
    "mighty jets f.c. players": "لاعبو مايتي جيتس",
    "music managers": "مدربو موسيقى",
    "nac breda non-playing staff": "طاقم إن أي سي بريدا غير اللاعبين",
    "north american television awards": "جوائز التلفزة الأمريكية الشمالية",
    "northern-ireland football cups": "كؤوس كرة القدم الأيرلندية الشمالية",
    "oakland raiders owners": "ملاك أوكلاند ريدرز",
    "orlando pride players": "لاعبو أورلاندو برايد",
    "people people": "أعلام أعلام",
    "pfc beroe stara zagora players": "لاعبو نادي بيروي ستارا زاغورا",
    "philadelphia 76ers lists": "قوائم فيلادلفيا سفنتي سيكسرز",
    "portsmouth f.c. players": "لاعبو نادي بورتسموث",
    "queensland lions fc matches": "مباريات كوينزلاند ليونز",
    "racing club de avellaneda non-playing staff": "طاقم نادي راسينغ غير اللاعبين",
    "rampla juniors managers": "مدربو رامبلا جونيورز",
    "romanian motorsport people": "أعلام رياضة محركات رومانية",
    "rosario central matches": "مباريات روزاريو سنترال",
    "rugby world cup referees": "حكام كأس العالم للرجبي",
    "russian blind people": "أعلام روس مكفوفون",
    "san antonio spurs owners": "ملاك سان أنطونيو سبرز",
    "silkeborg if players": "لاعبو نادي سيلكيبورج",
    "singaporean blind people": "أعلام سنغافوريون مكفوفون",
    "slovenian deaf people": "أعلام سلوفينيون صم",
    "smouha sc players": "لاعبو نادي سموحة",
    "stade lavallois players": "لاعبو نادي لافال",
    "taekwondo competitions": "منافسات تايكوندو",
    "thai league cup": "كأس الدوري التايلندي",
    "toronto argonauts lists": "قوائم تورونتو أرغونتس",
    "tunisian ligue professionnelle 2 managers": "مدربو الرابطة التونسية المحترفة الثانية لكرة القدم",
    "u.d. leiria players": "لاعبو يو دي ليريا",
    "uae president's cup matches": "مباريات كأس رئيس دولة الإمارات",
    "udinese calcio players": "لاعبو نادي أودينيزي",
    "ukrainian deaf people": "أعلام أوكرانيون صم",
    "utah jazz players": "لاعبو يوتا جاز",
    "vegalta sendai matches": "مباريات فيغالتا سنداي",
    "vegas golden knights coaches": "مدربو فيجاس جولدن نايتس",
    "washington state cougars football players": "لاعبو واشنطن ستايت كوجرز فوتبول",
    "webcomic logos": "شعارات ويب كومكس",
    "western sydney wanderers fc players": "لاعبو نادي وسترن سيدني واندررز",
    "wta tour seasons": "مواسم رابطة محترفات التنس",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data(category, expected) -> None:

    label = Get_team_work_Club(category)
    assert label.strip() == expected


def test_get_club():
    # Test with a basic category that might have a club
    result = Get_Club("football players")
    assert isinstance(result, str) or isinstance(result, dict)

    # Test with return_tab option
    result_with_tab = Get_Club("football players", return_tab=True)
    assert isinstance(result_with_tab, dict)

    result_empty = Get_Club("")
    assert isinstance(result_empty, str) or isinstance(result_with_tab, dict)


def test_get_team_work_club():
    # Test basic functionality
    result = Get_team_work_Club("football players")
    assert isinstance(result, str)

    result_empty = Get_team_work_Club("")
    assert isinstance(result_empty, str)

    # Test with different categories
    result_various = Get_team_work_Club("basketball teams")
    assert isinstance(result_various, str)
