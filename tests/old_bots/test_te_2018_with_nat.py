"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.old_bots.bot_te_4_nat import te_2018_with_nat, nat_match

nat_match_data = {
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

data_2018_with_nat = {
    "american culture": "ثقافة أمريكية",
    "argentine grand prix": "جائزة الأرجنتين الكبرى",
    "argentine tennis": "كرة مضرب أرجنتينية",
    "armenian television": "التلفزة الأرمينية",
    "armenian world music groups": "فرق موسيقى العالم أرمينية",
    "asian-american people": "أمريكيون آسيويون",
    "austrian musical groups": "مجموعات موسيقية نمساوية",
    "austrian television series": "مسلسلات تلفزيونية نمساوية",
    "bangladeshi films": "أفلام بنغلاديشية",
    "bangladeshi politics": "السياسة البنغلاديشية",
    "belgian companies": "شركات بلجيكية",
    "bhutanese sport": "رياضة بوتانية",
    "brazilian football club seasons": "مواسم أندية كرة قدم برازيلية",
    "british open": "المملكة المتحدة المفتوحة",
    "british women's sport": "رياضة بريطانية نسائية",
    "burmese names": "أسماء بورمية",
    "byzantine titles": "ألقاب بيزنطية",
    "canadian films": "أفلام كندية",
    "canadian labour law": "قانون العمل الكندي",
    "canadian music": "موسيقى كندية",
    "central american football": "كرة القدم الأمريكية الأوسطية",
    "chinese hip-hop groups": "فرق هيب هوب صينية",
    "chinese music": "موسيقى صينية",
    "christian saints": "قديسون",
    "christian texts": "نصوص مسيحية",
    "croatian ice hockey league": "الدوري الكرواتي لهوكي الجليد",
    "croatian music": "موسيقى كرواتية",
    "czech thrash metal musical groups": "فرق موسيقى ثراش ميتال تشيكية",
    "czech women's sport": "رياضة تشيكية نسائية",
    "danish books": "كتب دنماركية",
    "dutch tennis": "كرة مضرب هولندية",
    "east german sport": "رياضة ألمانية شرقية",
    "electro musicians": "موسيقيو موسيقى كهربائية",
    "emirati sport": "رياضة إماراتية",
    "eritrean premier league": "الدوري الإريتري الممتاز",
    "estonian music people": "شخصيات موسيقية إستونية",
    "european american culture": "ثقافة أمريكية أوروبية",
    "european-argentine culture": "ثقافة أرجنتينية أوروبية",
    "filipino-american culture": "ثقافة أمريكية فلبينية",
    "film editors": "محررو أفلام",
    "french rugby union leagues": "اتحاد دوري الرجبي الفرنسي",
    "gardeners": "مزارعو حدائق",
    "gothic architecture": "عمارة قوطية",
    "greek television series": "مسلسلات تلفزيونية يونانية",
    "hungarian sport": "رياضة مجرية",
    "hungarian websites": "مواقع ويب مجرية",
    "indian companies": "شركات هندية",
    "indonesian online encyclopedias": "موسوعات إنترنت إندونيسية",
    "irish comedy": "كوميديا أيرلندية",
    "irish league": "الدوري الأيرلندي",
    "irish paintings": "لوحات أيرلندية",
    "irish universities": "جامعات أيرلندية",
    "israeli architecture awards": "جوائز عمارة إسرائيلية",
    "italian black metal musical groups": "فرق موسيقى بلاك ميتال إيطالية",
    "ivorian companies": "شركات إيفوارية",
    "japanese war crimes": "جرائم حرب يابانية",
    "jewish scottish history": "تاريخ إسكتلندي يهودي",
    "kyrgyzstani sport": "رياضة قيرغيزستانية",
    "lebanese television series": "مسلسلات تلفزيونية لبنانية",
    "lithuanian films": "أفلام ليتوانية",
    "malawian websites": "مواقع ويب ملاوية",
    "mexican-american culture": "ثقافة أمريكية مكسيكية",
    "moroccan television series": "مسلسلات تلفزيونية مغربية",
    "moroccan tennis": "كرة مضرب مغربية",
    "music journalists": "صحفيون موسيقيون",
    "nepali television": "التلفزة النيبالية",
    "nigerian football": "كرة القدم النيجيرية",
    "norwegian folk music groups": "فرق موسيقى تقليدية نرويجية",
    "norwegian jews": "يهود نرويجيون",
    "olympic beach volleyball players": "لاعبو كرة طائرة شاطئية أولمبيون",
    "olympic divers": "غواصون أولمبيون",
    "olympic handball players": "لاعبو كرة يد أولمبيون",
    "olympic judoka": "لاعبو جودو أولمبيون",
    "olympic nordic combined skiers": "متزحلقو تزلج نوردي مزدوج أولمبيون",
    "pakistani football": "كرة القدم الباكستانية",
    "philippine football": "كرة القدم الفلبينية",
    "philippine presidential election": "انتخابات الرئاسة الفلبينية",
    "philippine television commercials": "إعلانات تجارية تلفزيونية فلبينية",
    "polo players": "لاعبو بولو",
    "portuguese tennis": "كرة مضرب برتغالية",
    "qatari football ": "كرة القدم القطرية",
    "romanian clothing": "ملابس رومانية",
    "romanian restaurants": "مطاعم رومانية",
    "romanian sport": "رياضة رومانية",
    "russian politics": "السياسة الروسية",
    "saudi super cup": "كأس السوبر السعودي",
    "scottish islands": "جزر إسكتلندية",
    "slovak eurodance groups": "فرق يورودانس سلوفاكية",
    "slovenian sport": "رياضة سلوفينية",
    "south korean tennis": "كرة مضرب كورية جنوبية",
    "soviet navy": "البحرية السوفيتية",
    "soviet war crimes": "جرائم حرب سوفيتية",
    "spanish films": "أفلام إسبانية",
    "spanish jews": "يهود إسبان",
    "surinamese sport": "رياضة سورينامية",
    "swedish air force": "القوات الجوية السويدية",
    "swedish motorsport": "رياضة محركات سويدية",
    "swedish tennis": "كرة مضرب سويدية",
    "swiss businesspeople": "شخصيات أعمال سويسرية",
    "syrian websites": "مواقع ويب سورية",
    "thai television": "التلفزة التايلندية",
    "traditional pop music singers": "مغنو موسيقى بوب تقليدية",
    "trinidad and tobago football": "كرة القدم الترنيدادية",
    "turkish cookbooks": "كتب طبخ تركية",
    "turkish musical groups": "مجموعات موسيقية تركية",
    "ukrainian-jewish descent": "أصل يهودي أوكراني",
    "vietnamese sport": "رياضة فيتنامية",
    "voice actresses": "ممثلات أداء صوتي",
    "yemeni civil war": "الحرب الأهلية اليمنية",
    "yemeni executions": "إعدامات يمنية",
    "yemeni sport": "رياضة يمنية",
    "yoruba names": "أسماء يوروبية",
    "zimbabwean musical groups": "مجموعات موسيقية زيمبابوية",
}


@pytest.mark.parametrize("category, expected", data_2018_with_nat.items(), ids=data_2018_with_nat.keys())
@pytest.mark.fast
def test_te_2018_with_nat(category: str, expected: str) -> None:
    label = te_2018_with_nat(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", nat_match_data.items(), ids=nat_match_data.keys())
@pytest.mark.fast
def te_nat_match_data(category: str, expected: str) -> None:
    label = nat_match(category)
    assert label == expected


ENTERTAINMENT_CASES = [
    ("te_2018_with_nat", data_2018_with_nat, te_2018_with_nat),
    ("te_nat_match_data", nat_match_data, nat_match),
]


@pytest.mark.parametrize("name,data,callback", ENTERTAINMENT_CASES)
@pytest.mark.dump
def test_entertainment(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
