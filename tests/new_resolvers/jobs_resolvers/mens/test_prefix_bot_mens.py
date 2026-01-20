"""
TODO: use mens_resolver_labels
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.jobs_resolvers.mens import mens_resolver_labels

test_mens_data = {
    "ancient romans killed in action": "رومان قدماء قتلوا في عمليات قتالية",
    "bulgarian deaf": "بلغاريون صم",
    "czech deaf": "تشيكيون صم",
    "expatriate academics": "أكاديميون مغتربون",
    "expatriate actors": "ممثلون مغتربون",
    "expatriate artists": "فنانون مغتربون",
    "expatriate baseball players": "لاعبو كرة قاعدة مغتربون",
    "expatriate bishops": "أساقفة مغتربون",
    "expatriate cricketers": "لاعبو كريكت مغتربون",
    "expatriate dancers": "راقصون مغتربون",
    "expatriate field hockey players": "لاعبو هوكي ميدان مغتربون",
    "expatriate football managers": "مدربو كرة قدم مغتربون",
    "expatriate footballers": "لاعبو كرة قدم مغتربون",
    "expatriate futsal players": "لاعبو كرة صالات مغتربون",
    "expatriate golfers": "لاعبو غولف مغتربون",
    "expatriate handball players": "لاعبو كرة يد مغتربون",
    "expatriate ice hockey players": "لاعبو هوكي جليد مغتربون",
    "expatriate rugby league players": "لاعبو دوري رجبي مغتربون",
    "expatriate rugby union players": "لاعبو اتحاد رجبي مغتربون",
    "expatriate soccer players": "لاعبو كرة قدم مغتربون",
    "expatriate swimmers": "سباحون مغتربون",
    "expatriate tennis players": "لاعبو كرة مضرب مغتربون",
    "expatriate volleyball players": "لاعبو كرة طائرة مغتربون",
    "hungarian blind": "مجريون مكفوفون",
    "liberian blind": "ليبيريون مكفوفون",
    "malagasy people murdered abroad": "مدغشقريون قتلوا في الخارج",
    "mercenaries killed in action": "مرتزقة قتلوا في عمليات قتالية",
    "military personnel killed-in-action": "أفراد عسكريون قتلوا في عمليات قتالية",
    "russian blind": "روس مكفوفون",
    "singaporean blind": "سنغافوريون مكفوفون",
    "slovenian deaf": "سلوفينيون صم",
    "sri lankan deaf": "سريلانكيون صم",
    "taiwanese blind": "تايوانيون مكفوفون",
    "ukrainian deaf": "أوكرانيون صم",
    "uruguayan deaf": "أوروغويانيون صم",
}

test_mens_data2 = {
    "men athletes": "لاعبو قوى",
    "men centenarians": "مئويون",
    "men competitors": "منافسون",
    "men discus throwers": "رماة قرص",
    "men hammer throwers": "رماة مطرقة",
    "men high jumpers": "متسابقو قفز عالي",
    "men hurdlers": "لاعبو قفز الحواجز",
    "men long jumpers": "لاعبو قفز طويل",
    "men long-distance runners": "عداؤو مسافات طويلة",
    "men marathon runners": "عداؤو ماراثون",
    "men middle-distance runners": "عداؤو مسافات متوسطة",
    "men pole vaulters": "قافزون بالزانة",
    "men runners": "عداؤون",
    "men shot putters": "لاعبو دفع ثقل",
    "men sprinters": "عداؤون سريعون",
    "men steeplechase runners": "عداؤو موانع",
    "men triple jumpers": "لاعبو وثب ثلاثي",
    "men wheelchair racers": "متسابقو كراسي متحركة",
    "fictional firefighters": "رجال إطفاء خياليون",
    "fictional australian rules footballers": "لاعبو كرة قدم أسترالية خياليون",
    "assassinated civil rights activists": "ناشطو حقوق مدنية مغتالون",
    "assassinated ecuadorian people": "إكوادوريون مغتالون",
    "assassinated educators": "معلمون مغتالون",
    "assassinated english people": "إنجليز مغتالون",
    "assassinated journalists": "صحفيون مغتالون",
    "assassinated kenyan people": "كينيون مغتالون",
    "assassinated latvian people": "لاتفيون مغتالون",
    "assassinated liberian people": "ليبيريون مغتالون",
    "assassinated monarchs": "ملكيون مغتالون",
    "assassinated monegasque people": "موناكيون مغتالون",
    "assassinated newspaper editors": "محررو صحف مغتالون",
    "assassinated politicians": "سياسيون مغتالون",
    "assassinated radio people": "أعلام راديو مغتالون",
    "assassinated spanish people": "إسبان مغتالون",
    "blind blues musicians": "موسيقيو بلوز مكفوفون",
    "blind harmonica players": "لاعبو هارمونيكا مكفوفون",
    "blind musicians": "موسيقيون مكفوفون",
    "blind writers": "كتاب مكفوفون",
    "child actors": "ممثلون أطفال",
    "child jazz musicians": "موسيقيو جاز أطفال",
    "child singers": "مغنون أطفال",
    "child writers": "كتاب أطفال",
    "contemporary artists": "فنانون معاصرون",
    "contemporary painters": "رسامون معاصرون",
    "contemporary philosophers": "فلاسفة معاصرون",
    "contemporary sculptors": "نحاتون معاصرون",
    "deaf baseball players": "لاعبو كرة قاعدة صم",
    "deaf poets": "شعراء صم",
    "deaf sports-people": "رياضيون صم",
    "deaf television presenters": "مذيعو تلفزيون صم",
    "deaf triathletes": "لاعبو ترياثلون صم",
    "disabled sports-people": "رياضيون معاقون",
    "fictional american people": "أمريكيون خياليون",
    "fictional armenian people": "أرمن خياليون",
    "fictional barons": "بارونات خياليون",
    "fictional british people": "بريطانيون خياليون",
    "fictional burmese people": "بورميون خياليون",
    "fictional businesspeople": "شخصيات أعمال خياليون",
    "fictional catholics": "كاثوليك خياليون",
    "fictional civil servants": "موظفو خدمة مدنية خياليون",
    "fictional diarists": "كتاب يوميات خياليون",
    "fictional engineers": "مهندسون خياليون",
    "fictional entertainers": "فنانون ترفيهيون خياليون",
    "fictional herpetologists": "علماء زواحف وبرمائيات خياليون",
    "fictional indian people": "هنود خياليون",
    "fictional murderers": "قتلة خياليون",
    "fictional pakistani people": "باكستانيون خياليون",
    "fictional politicians": "سياسيون خياليون",
    "fictional psychics": "وسطاء خياليون",
    "fictional salvadoran people": "سلفادوريون خياليون",
    "fictional scientists": "علماء خياليون",
    "fictional sheriffs": "مأمورون خياليون",
    "fictional southeast asian people": "آسيويون جنوبيون شرقيون خياليون",
    "fictional tajikistani people": "طاجيك خياليون",
    "kidnapped american people": "أمريكيون مختطفون",
    "kidnapped chinese people": "صينيون مختطفون",
    "kidnapped politicians": "سياسيون مختطفون",
    "kidnapped sri lankan people": "سريلانكيون مختطفون",
    "latin american people": "أمريكيون لاتينيون",
    "latin dance singers": "مغنو رقص لاتينيون",
    "latin jazz pianists": "عازفو بيانو جاز لاتينيون",
    "military aviators": "طيارون عسكريون",
    "military doctors": "أطباء عسكريون",
    "military governors": "حكام عسكريون",
    "military snipers": "قناصون عسكريون",
    "political artists": "فنانون سياسيون",
    "political consultants": "استشاريون سياسيون",
    "political prisoners": "مسجونون سياسيون",
    "political sociologists": "علماء اجتماع سياسيون",
    "religious philosophers": "فلاسفة دينيون",
    "religious workers": "عمال دينيون",
    "religious writers": "كتاب دينيون",
}

test_mens_data_male = {
    "expatriate male actors": "ممثلون ذكور مغتربون",
    "male actors": "ممثلون ذكور",
    "male alpine skiers": "متزحلقو منحدرات ثلجية ذكور",
    "male archers": "نبالون ذكور",
    "male artistic gymnasts": "لاعبو جمباز فني ذكور",
    "male artists": "فنانون ذكور",
    "male athletes": "لاعبو قوى ذكور",
    "male badminton players": "لاعبو تنس ريشة ذكور",
    "male ballet dancers": "راقصو باليه ذكور",
    "male biathletes": "لاعبو بياثلون ذكور",
    "male bloggers": "مدونون ذكور",
    "male bobsledders": "متزلجون جماعيون ذكور",
    "male boxers": "ملاكمون ذكور",
    "male canoeists": "متسابقو قوارب الكانوي ذكور",
    "male classical composers": "ملحنون كلاسيكيون ذكور",
    "male classical pianists": "عازفو بيانو كلاسيكيون ذكور",
    "male comedians": "كوميديون ذكور",
    "male composers": "ملحنون ذكور",
    "male conductors (music)": "قادة فرق موسيقية ذكور",
    "male critics": "نقاد ذكور",
    "male cross-country skiers": "متزحلقون ريفيون ذكور",
    "male cyclists": "دراجون ذكور",
    "male dancers": "راقصون ذكور",
    "male divers": "غواصون ذكور",
    "male dramatists and playwrights": "كتاب دراما ومسرح ذكور",
    "male dramatists": "دراميون ذكور",
    "male entertainers": "فنانون ترفيهيون ذكور",
    "male equestrians": "فرسان خيول ذكور",
    "male essayists": "كتاب مقالات ذكور",
    "male fencers": "مبارزون ذكور",
    "male field hockey defenders": "مدافعو هوكي ميدان ذكور",
    "male field hockey players": "لاعبو هوكي ميدان ذكور",
    "male figure skaters": "متزلجون فنيون ذكور",
    "male film actors": "ممثلو أفلام ذكور",
    "male folk singers": "مغنو فولك ذكور",
    "male freestyle skiers": "ممارسو تزلج حر ذكور",
    "male freestyle swimmers": "سباحو تزلج حر ذكور",
    "male golfers": "لاعبو غولف ذكور",
    "male guitarists": "عازفو قيثارة ذكور",
    "male ice dancers": "راقصو جليد ذكور",
    "male jazz musicians": "موسيقيو جاز ذكور",
    "male journalists": "صحفيون ذكور",
    "male judoka": "لاعبو جودو ذكور",
    "male kabaddi players": "لاعبو كابادي ذكور",
    "male karateka": "ممارسو كاراتيه ذكور",
    "male kickboxers": "مقاتلو كيك بوكسنغ ذكور",
    "male long-distance runners": "عداؤو مسافات طويلة ذكور",
    "male lugers": "زاحفون ثلجيون ذكور",
    "male mandolinists": "عازفو مندولين ذكور",
    "male martial artists": "ممارسو فنون قتالية ذكور",
    "male middle-distance runners": "عداؤو مسافات متوسطة ذكور",
    "male mixed martial artists": "مقاتلو فنون قتالية مختلطة ذكور",
    "male models": "عارضو أزياء ذكور",
    "male modern pentathletes": "متسابقو خماسي حديث ذكور",
    "male muay thai practitioners": "ممارسو موياي تاي ذكور",
    "male musical theatre actors": "ممثلو مسرحيات موسيقية ذكور",
    "male musicians": "موسيقيون ذكور",
    "male non-fiction writers": "كتاب غير روائيين ذكور",
    "male nordic combined skiers": "متزحلقو تزلج نوردي مزدوج ذكور",
    "male novelists": "روائيون ذكور",
    "male opera composers": "ملحنو أوبرا ذكور",
    "male opera singers": "مغنو أوبرا ذكور",
    "male painters": "رسامون ذكور",
    "male pair skaters": "متزلجون فنيون على الجليد ذكور",
    "male photographers": "مصورون ذكور",
    "male pianists": "عازفو بيانو ذكور",
    "male poets": "شعراء ذكور",
    "male pop singers": "مغنو بوب ذكور",
    "male pornographic film actors": "ممثلو أفلام إباحية ذكور",
    "male professional wrestlers": "مصارعون محترفون ذكور",
    "male radio actors": "ممثلو راديو ذكور",
    "male rappers": "مغنو راب ذكور",
    "male rowers": "مجدفون ذكور",
    "male runners": "عداؤون ذكور",
    "male sailors (sport)": "بحارة رياضيون ذكور",
    "male screenwriters": "كتاب سيناريو ذكور",
    "male short story writers": "كتاب قصة قصيرة ذكور",
    "male silent film actors": "ممثلو أفلام صامتة ذكور",
    "male singer-songwriters": "مغنون وكتاب أغاني ذكور",
    "male singers": "مغنون ذكور",
    "male single skaters": "متزلجون فرديون ذكور",
    "male skeleton racers": "متزلجون صدريون ذكور",
    "male ski jumpers": "متزلجو قفز ذكور",
    "male skiers": "متزحلقون ذكور",
    "male snowboarders": "متزلجون على الثلج ذكور",
    "male soap opera actors": "ممثلو مسلسلات طويلة ذكور",
    "male songwriters": "كتاب أغان ذكور",
    "male speed skaters": "متزلجو سرعة ذكور",
    "male sport shooters": "لاعبو رماية ذكور",
    "male sport wrestlers": "مصارعون رياضيون ذكور",
    "male stage actors": "ممثلو مسرح ذكور",
    "male steeplechase runners": "عداؤو موانع ذكور",
    "male swimmers": "سباحون ذكور",
    "male synchronized swimmers": "سباحون إيقاعيون ذكور",
    "male table tennis players": "لاعبو كرة طاولة ذكور",
    "male taekwondo practitioners": "لاعبو تايكوندو ذكور",
    "male television actors": "ممثلو تلفزيون ذكور",
    "male tennis players": "لاعبو كرة مضرب ذكور",
    "male triathletes": "لاعبو ترياثلون ذكور",
    "male video game actors": "ممثلو ألعاب فيديو ذكور",
    "male violinists": "عازفو كمان ذكور",
    "male voice actors": "ممثلو أداء صوتي ذكور",
    "male water polo players": "لاعبو كرة ماء ذكور",
    "male web series actors": "ممثلو مسلسلات ويب ذكور",
    "male weightlifters": "رباعون ذكور",
    "male wheelchair basketball players": "لاعبو كرة سلة على كراسي متحركة ذكور",
    "male wrestlers": "مصارعون ذكور",
    "male writers": "كتاب ذكور",
}


@pytest.mark.parametrize("category, expected", test_mens_data.items(), ids=test_mens_data.keys())
@pytest.mark.fast
def test_prefix_bot_mens_1(category: str, expected: str) -> None:
    label = mens_resolver_labels(category)
    assert label == expected

    label2 = mens_resolver_labels(category)
    assert label2 == expected


@pytest.mark.parametrize("category, expected", test_mens_data2.items(), ids=test_mens_data2.keys())
@pytest.mark.fast
def test_prefix_bot_mens_2(category: str, expected: str) -> None:
    label = mens_resolver_labels(category)
    assert label == expected

    label2 = mens_resolver_labels(category)
    assert label2 == expected


@pytest.mark.parametrize("category, expected", test_mens_data_male.items(), ids=test_mens_data_male.keys())
@pytest.mark.fast
def test_prefix_bot_mens_male(category: str, expected: str) -> None:
    label = mens_resolver_labels(category)
    assert label == expected

    label2 = mens_resolver_labels(category)
    assert label2 == expected


TEMPORAL_CASES = [
    ("test_prefix_bot_mens_1", test_mens_data, mens_resolver_labels),
    ("test_prefix_bot_mens_2", test_mens_data2, mens_resolver_labels),
    ("test_prefix_bot_mens_male", test_mens_data_male, mens_resolver_labels),
]


@pytest.mark.dump
@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
