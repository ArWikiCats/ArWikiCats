"""
Tests
"""

import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data_callback

test_data_0 = {
    "waba champions cup": "كأس دوري غرب آسيا لكرة السلة",
    "west bank premier league": "الدوري الفلسطيني الممتاز للضفة الغربية",
    "African Nations Championship": "كأس الأمم الإفريقية للمحليين",
}

fast_data = {
    "major league baseball owners and executives": "رؤساء تنفيذيون وملاك دوري كرة القاعدة الرئيسي",
    "wta tour seasons": "مواسم رابطة محترفات التنس",
    "ad alcorcón seasons": "مواسم نادي ألكوركون",
    "aj auxerre seasons": "مواسم نادي أوكسير",
    "cs sfaxien players": "لاعبو النادي الرياضي الصفاقسي",
    "fc barcelona managers": "مدربو نادي برشلونة",
    "fc bunyodkor players": "لاعبو نادي بونيودكور لكرة القدم",
    "fc dinamo batumi players": "لاعبو نادي دينامو باتومي",
    "kashiwa reysol players": "لاعبو كاشيوا ريسول",
    "kazma sc players": "لاعبو نادي كاظمة",
    "knattspyrnufélag reykjavíkur managers": "مدربو ناتدبيرنوفيلاغ ريكيافيكور",
    "liga mx seasons": "مواسم الدوري المكسيكي الممتاز",
    "ljungskile sk players": "لاعبو نادي ليونغسكايل",
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
def test_fast_data_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


to_test = [
    ("test_fast_data_2", fast_data, resolve_label_ar),
]

test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
