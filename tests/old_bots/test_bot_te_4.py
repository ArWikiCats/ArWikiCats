"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.old_bots.bot_te_4 import (
    Jobs_in_Multi_Sports,
    nat_match,
)

fast_data = {
    "anti-haitian sentiment": "مشاعر معادية للهايتيون",
    "anti-palestinian sentiment": "مشاعر معادية للفلسطينيون",
    "anti-turkish sentiment": "مشاعر معادية للأتراك",
    "anti-american sentiment": "مشاعر معادية للأمريكيون",
    "anti-czech sentiment": "مشاعر معادية للتشيكيون",
    "anti-japanese sentiment": "مشاعر معادية لليابانيون",
    "anti-asian sentiment": "مشاعر معادية للآسيويون",
    "anti-slovene sentiment": "مشاعر معادية للسلوفينيون",
    "anti-ukrainian sentiment": "مشاعر معادية للأوكرانيون",
    "anti-chechen sentiment": "مشاعر معادية للشيشانيون",
    "anti-mexican sentiment": "مشاعر معادية للمكسيكيون",
    "anti-chinese sentiment": "مشاعر معادية للصينيون",
    "anti-christian sentiment": "مشاعر معادية للمسيحيون",
    "anti-serbian sentiment": "مشاعر معادية للصرب",
    "anti-armenian sentiment": "مشاعر معادية للأرمن",
    "anti-scottish sentiment": "مشاعر معادية للإسكتلنديون",
    "anti-iranian sentiment": "مشاعر معادية للإيرانيون",
    "anti-english sentiment": "مشاعر معادية للإنجليز",
    "anti-hungarian sentiment": "مشاعر معادية للمجريون",
    "anti-greek sentiment": "مشاعر معادية لليونانيون",
}

Multi_Sports_data = {
    "afc asian cup managers": "مدربون في كأس آسيا",
    "afc asian cup players": "لاعبون في كأس آسيا",
    "african games competitors": "منافسون في الألعاب الإفريقية",
    "african games judoka": "لاعبو جودو في الألعاب الإفريقية",
    "african games taekwondo practitioners": "لاعبو تايكوندو في الألعاب الإفريقية",
    "asian games alpine skiers": "متزحلقو منحدرات ثلجية في الألعاب الآسيوية",
    "asian games archers": "نبالون في الألعاب الآسيوية",
    "asian games athletes": "لاعبو قوى في الألعاب الآسيوية",
    "asian games badminton players": "لاعبو تنس ريشة في الألعاب الآسيوية",
    "asian games bowlers": "لاعبو بولينج في الألعاب الآسيوية",
    "asian games boxers": "ملاكمون في الألعاب الآسيوية",
    "asian games canoeists": "متسابقو قوارب الكانوي في الألعاب الآسيوية",
    "asian games chess players": "لاعبو شطرنج في الألعاب الآسيوية",
    "asian games competitors": "منافسون في الألعاب الآسيوية",
    "asian games cricketers": "لاعبو كريكت في الألعاب الآسيوية",
    "asian games divers": "غواصون في الألعاب الآسيوية",
    "asian games footballers": "لاعبو كرة قدم في الألعاب الآسيوية",
    "asian games golfers": "لاعبو غولف في الألعاب الآسيوية",
    "asian games handball players": "لاعبو كرة يد في الألعاب الآسيوية",
    "asian games judoka": "لاعبو جودو في الألعاب الآسيوية",
    "asian games karateka": "ممارسو كاراتيه في الألعاب الآسيوية",
    "asian games modern pentathletes": "متسابقو خماسي حديث في الألعاب الآسيوية",
    "asian games sambo practitioners": "ممارسو سامبو في الألعاب الآسيوية",
    "asian games shooters": "رماة في الألعاب الآسيوية",
    "asian games ski-orienteers": "متسابقو تزلج موجه في الألعاب الآسيوية",
    "asian games soft tennis players": "لاعبو كرة مضرب لينة في الألعاب الآسيوية",
    "asian games sport climbers": "متسلقون في الألعاب الآسيوية",
    "asian games swimmers": "سباحون في الألعاب الآسيوية",
    "asian games table tennis players": "لاعبو كرة طاولة في الألعاب الآسيوية",
    "asian games taekwondo practitioners": "لاعبو تايكوندو في الألعاب الآسيوية",
    "asian games tennis players": "لاعبو كرة مضرب في الألعاب الآسيوية",
    "asian games volleyball players": "لاعبو كرة طائرة في الألعاب الآسيوية",
    "asian games water polo players": "لاعبو كرة ماء في الألعاب الآسيوية",
    "asian games weightlifters": "رباعون في الألعاب الآسيوية",
    "asian games wrestlers": "مصارعون في الألعاب الآسيوية",
    "asian games xiangqi players": "لاعبو شطرنج صيني في الألعاب الآسيوية",
    "asian para games competitors": "منافسون في الألعاب البارالمبية الآسيوية",
    "central american and caribbean games competitors": "منافسون في ألعاب أمريكا الوسطى والكاريبي",
    "commonwealth games athletes": "لاعبو قوى في ألعاب الكومنولث",
    "commonwealth games badminton players": "لاعبو تنس ريشة في ألعاب الكومنولث",
    "commonwealth games bowls players": "لاعبو بولينج في ألعاب الكومنولث",
    "commonwealth games boxers": "ملاكمون في ألعاب الكومنولث",
    "commonwealth games competitors": "منافسون في ألعاب الكومنولث",
    "commonwealth games divers": "غواصون في ألعاب الكومنولث",
    "commonwealth games fencers": "مبارزون في ألعاب الكومنولث",
    "commonwealth games field hockey players": "لاعبو هوكي ميدان في ألعاب الكومنولث",
    "commonwealth games gymnasts": "لاعبو جمباز في ألعاب الكومنولث",
    "commonwealth games rugby sevens players": "لاعبو سباعيات رجبي في ألعاب الكومنولث",
    "commonwealth games squash players": "لاعبو اسكواش في ألعاب الكومنولث",
    "commonwealth games swimmers": "سباحون في ألعاب الكومنولث",
    "commonwealth games triathletes": "لاعبو ترياثلون في ألعاب الكومنولث",
    "european games boxers": "ملاكمون في الألعاب الأوروبية",
    "european games competitors": "منافسون في الألعاب الأوروبية",
    "european games gymnasts": "لاعبو جمباز في الألعاب الأوروبية",
    "european games sambo practitioners": "ممارسو سامبو في الألعاب الأوروبية",
    "european games volleyball players": "لاعبو كرة طائرة في الألعاب الأوروبية",
    "islamic solidarity games competitors": "منافسون في ألعاب التضامن الإسلامي",
    "islamic solidarity games judoka": "لاعبو جودو في ألعاب التضامن الإسلامي",
    "islamic solidarity games swimmers": "سباحون في ألعاب التضامن الإسلامي",
    "islamic solidarity games taekwondo practitioners": "لاعبو تايكوندو في ألعاب التضامن الإسلامي",
    "maccabiah games competitors": "منافسون في الألعاب المكابيه",
    "maccabiah games gymnasts": "لاعبو جمباز في الألعاب المكابيه",
    "maccabiah games rugby union players": "لاعبو اتحاد رجبي في الألعاب المكابيه",
    "mediterranean games competitors": "منافسون في الألعاب المتوسطية",
    "pan american games archers": "نبالون في دورة الألعاب الأمريكية",
    "pan american games athletes": "لاعبو قوى في دورة الألعاب الأمريكية",
    "pan american games baseball players": "لاعبو كرة قاعدة في دورة الألعاب الأمريكية",
    "pan american games basketball players": "لاعبو كرة سلة في دورة الألعاب الأمريكية",
    "pan american games bowlers": "لاعبو بولينج في دورة الألعاب الأمريكية",
    "pan american games boxers": "ملاكمون في دورة الألعاب الأمريكية",
    "pan american games competitors": "منافسون في دورة الألعاب الأمريكية",
    "pan american games cyclists": "دراجون في دورة الألعاب الأمريكية",
    "pan american games equestrians": "فرسان خيول في دورة الألعاب الأمريكية",
    "pan american games field hockey players": "لاعبو هوكي ميدان في دورة الألعاب الأمريكية",
    "pan american games footballers": "لاعبو كرة قدم في دورة الألعاب الأمريكية",
    "pan american games gymnasts": "لاعبو جمباز في دورة الألعاب الأمريكية",
    "pan american games handball players": "لاعبو كرة يد في دورة الألعاب الأمريكية",
    "pan american games rugby sevens players": "لاعبو سباعيات رجبي في دورة الألعاب الأمريكية",
    "pan american games sailors": "بحارة في دورة الألعاب الأمريكية",
    "pan american games softball players": "لاعبو كرة لينة في دورة الألعاب الأمريكية",
    "pan american games swimmers": "سباحون في دورة الألعاب الأمريكية",
    "pan american games tennis players": "لاعبو كرة مضرب في دورة الألعاب الأمريكية",
    "pan american games track and field athletes": "رياضيو المسار والميدان في دورة الألعاب الأمريكية",
    "pan american games volleyball players": "لاعبو كرة طائرة في دورة الألعاب الأمريكية",
    "pan american games water polo players": "لاعبو كرة ماء في دورة الألعاب الأمريكية",
    "pan american games weightlifters": "رباعون في دورة الألعاب الأمريكية",
    "pan american games wrestlers": "مصارعون في دورة الألعاب الأمريكية",
    "paralympic alpine skiers": "متزحلقو منحدرات ثلجية في الألعاب البارالمبية",
    "paralympic archers": "نبالون في الألعاب البارالمبية",
    "paralympic athletes": "لاعبو قوى في الألعاب البارالمبية",
    "paralympic badminton players": "لاعبو تنس ريشة في الألعاب البارالمبية",
    "paralympic biathletes": "لاعبو بياثلون في الألعاب البارالمبية",
    "paralympic boccia players": "لاعبو بوتشيا في الألعاب البارالمبية",
    "paralympic coaches": "مدربون في الألعاب البارالمبية",
    "paralympic competitors": "منافسون في الألعاب البارالمبية",
    "paralympic cross-country skiers": "متزحلقون ريفيون في الألعاب البارالمبية",
    "paralympic cyclists": "دراجون في الألعاب البارالمبية",
    "paralympic equestrians": "فرسان خيول في الألعاب البارالمبية",
    "paralympic footballers": "لاعبو كرة قدم في الألعاب البارالمبية",
    "paralympic goalball players": "لاعبو كرة هدف في الألعاب البارالمبية",
    "paralympic judoka": "لاعبو جودو في الألعاب البارالمبية",
    "paralympic long jumpers": "لاعبو قفز طويل في الألعاب البارالمبية",
    "paralympic marathon runners": "عداؤو ماراثون في الألعاب البارالمبية",
    "paralympic powerlifters": "ممارسو رياضة القوة في الألعاب البارالمبية",
    "paralympic rowers": "مجدفون في الألعاب البارالمبية",
    "paralympic sailors": "بحارة في الألعاب البارالمبية",
    "paralympic shooters": "رماة في الألعاب البارالمبية",
    "paralympic sledge hockey players": "لاعبو هوكي مزلجة في الألعاب البارالمبية",
    "paralympic snooker players": "لاعبو سنوكر في الألعاب البارالمبية",
    "paralympic snowboarders": "متزلجون على الثلج في الألعاب البارالمبية",
    "paralympic swimmers": "سباحون في الألعاب البارالمبية",
    "paralympic table tennis players": "لاعبو كرة طاولة في الألعاب البارالمبية",
    "paralympic taekwondo practitioners": "لاعبو تايكوندو في الألعاب البارالمبية",
    "paralympic track and field athletes": "رياضيو المسار والميدان في الألعاب البارالمبية",
    "paralympic triple jumpers": "لاعبو وثب ثلاثي في الألعاب البارالمبية",
    "paralympic volleyball players": "لاعبو كرة طائرة في الألعاب البارالمبية",
    "paralympic weightlifters": "رباعون في الألعاب البارالمبية",
    "paralympic wheelchair basketball coaches": "مدربو كرة سلة على كراسي متحركة في الألعاب البارالمبية",
    "paralympic wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة في الألعاب البارالمبية",
    "paralympic wheelchair curlers": "لاعبو كيرلنغ على الكراسي المتحركة في الألعاب البارالمبية",
    "paralympic wheelchair fencers": "مبارزون على الكراسي المتحركة في الألعاب البارالمبية",
    "paralympic wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة في الألعاب البارالمبية",
    "paralympic wrestlers": "مصارعون في الألعاب البارالمبية",
    "paralympics people": "أشخاص في الألعاب البارالمبية",
    "parapan american games badminton players": "لاعبو تنس ريشة في ألعاب بارابان الأمريكية",
    "parapan american games competitors": "منافسون في ألعاب بارابان الأمريكية",
    "parapan american games judoka": "لاعبو جودو في ألعاب بارابان الأمريكية",
    "parapan american games wheelchair tennis players": "لاعبو كرة مضرب على كراسي متحركة في ألعاب بارابان الأمريكية",
    "sea games competitors": "منافسون في ألعاب البحر",
    "south american games competitors": "منافسون في ألعاب أمريكا الجنوبية",
    "summer olympics coaches": "مدربون في الألعاب الأولمبية الصيفية",
    "summer olympics competitors": "منافسون أولمبيون صيفيون",
    "summer world university games competitors": "منافسون في ألعاب الجامعات العالمية الصيفية",
    "winter olympics competitors": "منافسون أولمبيون شتويون",
    "youth olympics biathletes": "لاعبو بياثلون في الألعاب الأولمبية الشبابية",
    "youth olympics ice hockey players": "لاعبو هوكي جليد في الألعاب الأولمبية الشبابية",
    "youth olympics nordic combined skiers": "متزحلقو تزلج نوردي مزدوج في الألعاب الأولمبية الشبابية",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_nat_match(category: str, expected: str) -> None:
    label = nat_match(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", Multi_Sports_data.items(), ids=Multi_Sports_data.keys())
@pytest.mark.fast
def test_Jobs_in_Multi_Sports(category: str, expected: str) -> None:
    label = Jobs_in_Multi_Sports(category)
    assert label == expected


ENTERTAINMENT_CASES = [
    ("test_nat_match", fast_data, nat_match),
    ("test_Jobs_in_Multi_Sports", Multi_Sports_data, Jobs_in_Multi_Sports),
]


@pytest.mark.parametrize("name,data,callback", ENTERTAINMENT_CASES)
@pytest.mark.dump
def test_entertainment(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
