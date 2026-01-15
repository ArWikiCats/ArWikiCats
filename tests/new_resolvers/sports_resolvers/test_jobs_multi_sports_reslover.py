"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.sports_resolvers.jobs_multi_sports_reslover import jobs_in_multi_sports

multi_sports_data_competitors = {
    "summer olympics coaches": "مدربون في الألعاب الأولمبية الصيفية",
    "paralympic coaches": "مدربون في الألعاب البارالمبية",
    "afc asian cup managers": "مدربون في كأس آسيا",
    "olympic gold medalists": "فائزون بميداليات ذهبية أولمبية",
    "paralympic competitors": "منافسون بارالمبيون",
    "african games competitors": "منافسون في الألعاب الإفريقية",
    "asian games competitors": "منافسون في الألعاب الآسيوية",
    "parapan american games competitors": "منافسون في ألعاب بارابان الأمريكية",
    "sea games competitors": "منافسون في ألعاب البحر",
    "south american games competitors": "منافسون في ألعاب أمريكا الجنوبية",
    "summer olympics competitors": "منافسون أولمبيون صيفيون",
    "summer world university games competitors": "منافسون في ألعاب الجامعات العالمية الصيفية",
    "winter olympics competitors": "منافسون أولمبيون شتويون",
    "pan american games competitors": "منافسون في دورة الألعاب الأمريكية",
    "maccabiah games competitors": "منافسون في الألعاب المكابيه",
    "mediterranean games competitors": "منافسون في الألعاب المتوسطية",
    "islamic solidarity games competitors": "منافسون في ألعاب التضامن الإسلامي",
    "european games competitors": "منافسون في الألعاب الأوروبية",
    "asian para games competitors": "منافسون في الألعاب البارالمبية الآسيوية",
    "central american and caribbean games competitors": "منافسون في ألعاب أمريكا الوسطى والكاريبي",
    "commonwealth games competitors": "منافسون في ألعاب الكومنولث",
}

multi_sports_data = {
    "paralympic sailors": "بحارة في الألعاب البارالمبية",
    "pan american games sailors": "بحارة في دورة الألعاب الأمريكية",
    "islamic solidarity games cyclists": "دراجون في ألعاب التضامن الإسلامي",
    "paralympic cyclists": "دراجون في الألعاب البارالمبية",
    "pan american games cyclists": "دراجون في دورة الألعاب الأمريكية",
    "islamic solidarity games weightlifters": "رباعون في ألعاب التضامن الإسلامي",
    "commonwealth games weightlifters": "رباعون في ألعاب الكومنولث",
    "asian games weightlifters": "رباعون في الألعاب الآسيوية",
    "paralympic weightlifters": "رباعون في الألعاب البارالمبية",
    "pan american games weightlifters": "رباعون في دورة الألعاب الأمريكية",
    "islamic solidarity games shooters": "رماة في ألعاب التضامن الإسلامي",
    "asian games shooters": "رماة في الألعاب الآسيوية",
    "paralympic shooters": "رماة في الألعاب البارالمبية",
    "islamic solidarity games track and field athletes": "رياضيو المسار والميدان في ألعاب التضامن الإسلامي",
    "paralympic track and field athletes": "رياضيو المسار والميدان في الألعاب البارالمبية",
    "pan american games track and field athletes": "رياضيو المسار والميدان في دورة الألعاب الأمريكية",
    "islamic solidarity games swimmers": "سباحون في ألعاب التضامن الإسلامي",
    "commonwealth games swimmers": "سباحون في ألعاب الكومنولث",
    "asian games swimmers": "سباحون في الألعاب الآسيوية",
    "paralympic swimmers": "سباحون في الألعاب البارالمبية",
    "pan american games swimmers": "سباحون في دورة الألعاب الأمريكية",
    "paralympic marathon runners": "عداؤو ماراثون في الألعاب البارالمبية",
    "commonwealth games divers": "غواصون في ألعاب الكومنولث",
    "asian games divers": "غواصون في الألعاب الآسيوية",
    "paralympic equestrians": "فرسان خيول في الألعاب البارالمبية",
    "pan american games equestrians": "فرسان خيول في دورة الألعاب الأمريكية",
    "maccabiah games rugby union players": "لاعبو اتحاد رجبي في الألعاب المكابيه",
    "commonwealth games squash players": "لاعبو اسكواش في ألعاب الكومنولث",
    "paralympic boccia players": "لاعبو بوتشيا في الألعاب البارالمبية",
    "commonwealth games bowls players": "لاعبو بولينج في ألعاب الكومنولث",
    "asian games bowlers": "لاعبو بولينج في الألعاب الآسيوية",
    "pan american games bowlers": "لاعبو بولينج في دورة الألعاب الأمريكية",
    "youth olympics biathletes": "لاعبو بياثلون في الألعاب الأولمبية الشبابية",
    "paralympic biathletes": "لاعبو بياثلون في الألعاب البارالمبية",
    "islamic solidarity games taekwondo practitioners": "لاعبو تايكوندو في ألعاب التضامن الإسلامي",
    "asian games taekwondo practitioners": "لاعبو تايكوندو في الألعاب الآسيوية",
    "african games taekwondo practitioners": "لاعبو تايكوندو في الألعاب الإفريقية",
    "paralympic taekwondo practitioners": "لاعبو تايكوندو في الألعاب البارالمبية",
    "commonwealth games triathletes": "لاعبو ترياثلون في ألعاب الكومنولث",
    "commonwealth games badminton players": "لاعبو تنس ريشة في ألعاب الكومنولث",
    "parapan american games badminton players": "لاعبو تنس ريشة في ألعاب بارابان الأمريكية",
    "asian games badminton players": "لاعبو تنس ريشة في الألعاب الآسيوية",
    "paralympic badminton players": "لاعبو تنس ريشة في الألعاب البارالمبية",
    "islamic solidarity games gymnasts": "لاعبو جمباز في ألعاب التضامن الإسلامي",
    "commonwealth games gymnasts": "لاعبو جمباز في ألعاب الكومنولث",
    "european games gymnasts": "لاعبو جمباز في الألعاب الأوروبية",
    "maccabiah games gymnasts": "لاعبو جمباز في الألعاب المكابيه",
    "pan american games gymnasts": "لاعبو جمباز في دورة الألعاب الأمريكية",
    "islamic solidarity games judoka": "لاعبو جودو في ألعاب التضامن الإسلامي",
    "parapan american games judoka": "لاعبو جودو في ألعاب بارابان الأمريكية",
    "asian games judoka": "لاعبو جودو في الألعاب الآسيوية",
    "african games judoka": "لاعبو جودو في الألعاب الإفريقية",
    "paralympic judoka": "لاعبو جودو في الألعاب البارالمبية",
    "parapan american games wheelchair rugby players": "لاعبو رجبي على كراسي متحركة في ألعاب بارابان الأمريكية",
    "paralympic wheelchair rugby players": "لاعبو رجبي على كراسي متحركة في الألعاب البارالمبية",
    "commonwealth games rugby sevens players": "لاعبو سباعيات رجبي في ألعاب الكومنولث",
    "pan american games rugby sevens players": "لاعبو سباعيات رجبي في دورة الألعاب الأمريكية",
    "paralympic snooker players": "لاعبو سنوكر في الألعاب البارالمبية",
    "asian games xiangqi players": "لاعبو شطرنج صيني في الألعاب الآسيوية",
    "asian games chess players": "لاعبو شطرنج في الألعاب الآسيوية",
    "asian games golfers": "لاعبو غولف في الألعاب الآسيوية",
    "paralympic long jumpers": "لاعبو قفز طويل في الألعاب البارالمبية",
    "commonwealth games athletes": "لاعبو قوى في ألعاب الكومنولث",
    "asian games athletes": "لاعبو قوى في الألعاب الآسيوية",
    "paralympic athletes": "لاعبو قوى في الألعاب البارالمبية",
    "pan american games athletes": "لاعبو قوى في دورة الألعاب الأمريكية",
    "parapan american games wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة في ألعاب بارابان الأمريكية",
    "paralympic wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية",
    "islamic solidarity games basketball players": "لاعبو كرة سلة في ألعاب التضامن الإسلامي",
    "pan american games basketball players": "لاعبو كرة سلة في دورة الألعاب الأمريكية",
    "islamic solidarity games volleyball players": "لاعبو كرة طائرة في ألعاب التضامن الإسلامي",
    "asian games volleyball players": "لاعبو كرة طائرة في الألعاب الآسيوية",
    "european games volleyball players": "لاعبو كرة طائرة في الألعاب الأوروبية",
    "paralympic volleyball players": "لاعبو كرة طائرة في الألعاب البارالمبية",
    "pan american games volleyball players": "لاعبو كرة طائرة في دورة الألعاب الأمريكية",
    "islamic solidarity games table tennis players": "لاعبو كرة طاولة في ألعاب التضامن الإسلامي",
    "asian games table tennis players": "لاعبو كرة طاولة في الألعاب الآسيوية",
    "paralympic table tennis players": "لاعبو كرة طاولة في الألعاب البارالمبية",
    "pan american games baseball players": "لاعبو كرة قاعدة في دورة الألعاب الأمريكية",
    "islamic solidarity games footballers": "لاعبو كرة قدم في ألعاب التضامن الإسلامي",
    "asian games footballers": "لاعبو كرة قدم في الألعاب الآسيوية",
    "paralympic footballers": "لاعبو كرة قدم في الألعاب البارالمبية",
    "pan american games footballers": "لاعبو كرة قدم في دورة الألعاب الأمريكية",
    "pan american games softball players": "لاعبو كرة لينة في دورة الألعاب الأمريكية",
    "asian games water polo players": "لاعبو كرة ماء في الألعاب الآسيوية",
    "pan american games water polo players": "لاعبو كرة ماء في دورة الألعاب الأمريكية",
    "parapan american games wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة في ألعاب بارابان الأمريكية",
    "paralympic wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية",
    "islamic solidarity games tennis players": "لاعبو كرة مضرب في ألعاب التضامن الإسلامي",
    "asian games tennis players": "لاعبو كرة مضرب في الألعاب الآسيوية",
    "pan american games tennis players": "لاعبو كرة مضرب في دورة الألعاب الأمريكية",
    "asian games soft tennis players": "لاعبو كرة مضرب لينة في الألعاب الآسيوية",
    "paralympic goalball players": "لاعبو كرة هدف في الألعاب البارالمبية",
    "islamic solidarity games handball players": "لاعبو كرة يد في ألعاب التضامن الإسلامي",
    "asian games handball players": "لاعبو كرة يد في الألعاب الآسيوية",
    "pan american games handball players": "لاعبو كرة يد في دورة الألعاب الأمريكية",
    "asian games cricketers": "لاعبو كريكت في الألعاب الآسيوية",
    "paralympic wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية",
    "youth olympics ice hockey players": "لاعبو هوكي جليد في الألعاب الأولمبية الشبابية",
    "paralympic sledge hockey players": "لاعبو هوكي مزلجة في الألعاب البارالمبية",
    "commonwealth games field hockey players": "لاعبو هوكي ميدان في ألعاب الكومنولث",
    "youth olympics field hockey players": "لاعبو هوكي ميدان في الألعاب الأولمبية الشبابية",
    "pan american games field hockey players": "لاعبو هوكي ميدان في دورة الألعاب الأمريكية",
    "paralympic triple jumpers": "لاعبو وثب ثلاثي في الألعاب البارالمبية",
    "afc asian cup players": "لاعبون في كأس آسيا",
    "paralympic wheelchair fencers": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية",
    "islamic solidarity games fencers": "مبارزون في ألعاب التضامن الإسلامي",
    "commonwealth games fencers": "مبارزون في ألعاب الكومنولث",
    "youth olympics nordic combined skiers": "متزحلقو تزلج نوردي مزدوج في الألعاب الأولمبية الشبابية",
    "asian games alpine skiers": "متزحلقو منحدرات ثلجية في الألعاب الآسيوية",
    "paralympic alpine skiers": "متزحلقو منحدرات ثلجية في الألعاب البارالمبية",
    "paralympic cross-country skiers": "متزحلقون ريفيون في الألعاب البارالمبية",
    "paralympic snowboarders": "متزلجون على الثلج في الألعاب البارالمبية",
    "asian games ski-orienteers": "متسابقو تزلج موجه في الألعاب الآسيوية",
    "asian games modern pentathletes": "متسابقو خماسي حديث في الألعاب الآسيوية",
    "asian games canoeists": "متسابقو قوارب الكانوي في الألعاب الآسيوية",
    "paralympic wheelchair racers": "متسابقو كراسي متحركة في الألعاب البارالمبية",
    "asian games sport climbers": "متسلقون في الألعاب الآسيوية",
    "paralympic rowers": "مجدفون في الألعاب البارالمبية",
    "pan american games rowers": "مجدفون في دورة الألعاب الأمريكية",
    "paralympic wheelchair rugby coaches": "مدربو رجبي على كراسي متحركة في الألعاب البارالمبية",
    "paralympic wheelchair basketball coaches": "مدربو كرة سلة على كراسي متحركة في الألعاب البارالمبية",
    "islamic solidarity games wrestlers": "مصارعون في ألعاب التضامن الإسلامي",
    "asian games wrestlers": "مصارعون في الألعاب الآسيوية",
    "paralympic wrestlers": "مصارعون في الألعاب البارالمبية",
    "pan american games wrestlers": "مصارعون في دورة الألعاب الأمريكية",
    "islamic solidarity games kickboxers": "مقاتلو كيك بوكسنغ في ألعاب التضامن الإسلامي",
    "islamic solidarity games boxers": "ملاكمون في ألعاب التضامن الإسلامي",
    "commonwealth games boxers": "ملاكمون في ألعاب الكومنولث",
    "asian games boxers": "ملاكمون في الألعاب الآسيوية",
    "european games boxers": "ملاكمون في الألعاب الأوروبية",
    "pan american games boxers": "ملاكمون في دورة الألعاب الأمريكية",
    "paralympic powerlifters": "ممارسو رياضة القوة في الألعاب البارالمبية",
    "asian games sambo practitioners": "ممارسو سامبو في الألعاب الآسيوية",
    "european games sambo practitioners": "ممارسو سامبو في الألعاب الأوروبية",
    "islamic solidarity games karateka": "ممارسو كاراتيه في ألعاب التضامن الإسلامي",
    "asian games karateka": "ممارسو كاراتيه في الألعاب الآسيوية",
    "islamic solidarity games archers": "نبالون في ألعاب التضامن الإسلامي",
    "asian games archers": "نبالون في الألعاب الآسيوية",
    "paralympic archers": "نبالون في الألعاب البارالمبية",
    "pan american games archers": "نبالون في دورة الألعاب الأمريكية",
}


@pytest.mark.parametrize("category, expected", multi_sports_data.items(), ids=multi_sports_data.keys())
@pytest.mark.fast
def test_jobs_in_multi_sports(category: str, expected: str) -> None:
    label = jobs_in_multi_sports(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", multi_sports_data.items(), ids=multi_sports_data.keys())
# @pytest.mark.parametrize("category, expected", multi_sports_data_competitors.items(), ids=multi_sports_data_competitors.keys())
@pytest.mark.fast
def test_jobs_in_multi_sports_new(category: str, expected: str) -> None:
    label = jobs_in_multi_sports(category)
    assert label == expected


ENTERTAINMENT_CASES = [
    ("test_jobs_in_multi_sports", multi_sports_data, jobs_in_multi_sports),
]


@pytest.mark.parametrize("name,data,callback", ENTERTAINMENT_CASES)
@pytest.mark.dump
def test_entertainment(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
