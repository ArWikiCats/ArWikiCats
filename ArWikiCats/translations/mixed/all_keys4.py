"""
Supplementary mappings for educational, sporting and political contexts.
"""

from ...helps import len_print
from ..sports.cycling import CYCLING_TEMPLATES
from .keys2 import new_2019

CAMBRIDGE_COLLEGES: dict[str, str] = {
    "christ's": "كريست",
    "churchill": "تشرشل",
    "clare hall": "كلير هول",
    "corpus christi": "كوربوس كريستي",
    "darwin": "داروين",
    "downing": "داونينج",
    "fitzwilliam": "فيتزويليام",
    "girton": "غيرتون",
    "gonville and caius": "غونفيل وكايوس",
    "homerton": "هومرتون",
    "hughes hall": "هيوز هول",
    "jesus": "يسوع",
    "king's": "كينجز",
    "lucy cavendish": "لوسي كافنديش",
    "magdalene": "المجدلية",
    "murray edwards": "موراي إدواردز",
    "newnham": "نونهم",
    "oriel": "أوريل",
    "pembroke": "بمبروك",
    "peterhouse": "بترهووس",
    "queens'": "كوينز",
    "robinson": "روبنسون",
    "selwyn": "سلوين",
    "sidney sussex": "سيدني ساسكس",
    "st catharine's": "سانت كاثارين",
    "st edmund's": "سانت ادموند",
    "st john's": "سانت جونز",
    "trinity hall": "قاعة الثالوث",
    "trinity": "ترينيتي",
    "wolfson": "وولفسون",
}

INTER_FEDERATIONS: dict[str, str] = {
    "2017–18 uefa champions league": "دوري أبطال أوروبا 2017–18",
    "aff championship": "بطولة اتحاد آسيان لكرة القدم",
    "aff u-23 championship": "بطولة اتحاد آسيان تحت 23 سنة",
    "aff u-23 youth championship": "بطولة اتحاد آسيان تحت 23 سنة للشباب",
    "asean football championship": "بطولة اتحاد آسيان لكرة القدم",
    "atp challenger tour": "بطولات تشالنجر لرابطة محترفات التنس",
    "atp tour tournaments": "بطولات رابطة محترفي التنس",
    "atp tour": "رابطة محترفي التنس",
    "atp world tour": "بطولات العالم لرابطة محترفات التنس",
    "bwf world championships": "بطولة العالم لكرة الريشة",
    "bwf world junior championships": "بطولة العالم لكرة الريشة للناشئين",
    "caf champions league": "دوري أبطال إفريقيا",
    "caf confederation cup": "كأس الكونفيدرالية الإفريقية",
    "concacaf champions league": "دوري أبطال الكونكاكاف",
    "concacaf championship": "بطولة أمريكا الشمالية",
    "concacaf gold cup": "كأس الكونكاكاف الذهبية",
    "concacaf u17 championship": "الكأس الذهبية تحت 17 سنة لكرة القدم",
    "concacaf under-20 championship": "الكأس الذهبية تحت 20 سنة لكرة القدم",
    "concacaf women's championship": "بطولة أمريكا الشمالية للسيدات",
    "concacaf women's u-10 championship": "بطولة أمريكا الشمالية للسيدات تحت 10 سنة",
    "concacaf women's u-17 championship": "بطولة أمريكا الشمالية للسيدات تحت 17 سنة",
    "conifa world football cup": "كأس العالم لاتحاد الجمعيات المستقلة لكرة القدم",
    "ehf champions league": "دوري أبطال أوروبا لكرة اليد",
    "ehf cup": "كأس أوروبا لكرة اليد",
    "ehf women's champions league": "دوري أبطال أوروبا لكرة اليد للسيدات",
    "ehf women's cup winners' cup": "كأس أبطال الكؤوس الأوروبية لكرة اليد للسيدات",
    "fiba africa championship": "بطولة أمم إفريقيا لكرة السلة",
    "fiba americas championship": "بطولة أمم الأمريكتين لكرة السلة",
    "fiba americas league": "دوري الأمريكتين لكرة السلة",
    "fiba americup": "بطولة أمم الأمريكتين لكرة السلة",
    "fiba asia championship": "بطولة أمم آسيا لكرة السلة",
    "fiba asia cup": "كأس أمم آسيا لكرة السلة",
    "fiba asia under-18 championship": "بطولة فيبا آسيا تحت 18 سنة لكرة السلة",
    "fiba basketball world cup": "كأس العالم لكرة السلة",
    "fiba competitions": "منافسات الاتحاد الدولي لكرة السلة",
    "fiba eurobasket": "بطولة أمم أوروبا لكرة السلة",
    "fiba european champions cup": "كأس أبطال أوروبا لكرة السلة",
    "fiba korać cup": "كأس كوراتش لكرة السلة",
    "fiba saporta cup": "كأس سابورتا",
    "fiba under-16 world championship": "بطولة العالم تحت 16 سنة لكرة السلة",
    "fiba under-17 world championship": "بطولة العالم تحت 17 سنة لكرة السلة",
    "fiba under-18 world championship": "بطولة العالم تحت 18 سنة لكرة السلة",
    "fiba under-19 world championship": "بطولة العالم تحت 19 سنة لكرة السلة",
    "fiba under-20 world championship": "بطولة العالم تحت 20 سنة لكرة السلة",
    "fiba women's basketball world cup": "كأس العالم لكرة السلة للسيدات",
    "fiba women's european champions cup": "كأس أبطال أوروبا لكرة السلة للسيدات",
    "fiba women's world cup": "كأس العالم لكرة السلة للسيدات",
    "fiba world championship for women": "بطولة كأس العالم لكرة السلة للسيدات",
    "fiba world championship": "بطولة كأس العالم لكرة السلة",
    "fiba world cup": "كأس العالم لكرة السلة",
    "fiba": "الاتحاد الدولي لكرة السلة",
    "fifa beach soccer world cup": "كأس العالم الشاطئية",
    "fifa club world cup": "كأس العالم للأندية",
    "fifa confederations cup": "كأس القارات",
    "fifa futsal world cup ney": "بطولة كأس العالم داخل الصالات",
    "fifa futsal world cup players": "لاعبو كأس العالم لكرة الصالات",
    "fifa u-17 women's world cup": "كأس العالم تحت 17 سنة لكرة القدم للسيدات",
    "fifa u-17 world cup": "كأس العالم تحت 17 سنة لكرة القدم",
    "fifa u-20 women's world cup": "كأس العالم تحت 20 سنة لكرة القدم للسيدات",
    "fifa u-20 world cup": "كأس العالم تحت 20 سنة لكرة القدم",
    "fifa women's world cup qualification": "تصفيات كأس العالم لكرة القدم للسيدات",
    "fifa women's world cup": "كأس العالم لكرة القدم للسيدات",
    "fifa world cup players": "لاعبو كأس العالم لكرة القدم",
    "fifa world cup": "كأس العالم لكرة القدم",
    "fil under 23 world luge championships": "كأس العالم للزحف الثلجي تحت 23 سنة",
    "fil world luge championships": "كأس العالم للزحف الثلجي",
    "fina water polo world league": "الدوري العالمي لكرة الماء",
    "fina world aquatics championships": "بطولة العالم للألعاب المائية",
    "fina world swimming championships (25 m)": "بطولة العالم للسباحة (25 متر)",
    "fina world swimming championships": "بطولة العالم للسباحة",
    "fina": "الاتحاد الدولي للسباحة",
    "fis nordic world ski championships": "بطولة العالم للتزلج النوردي على الثلج",
    "fivb volleyball men's world championship": "بطولة العالم للكرة الطائرة",
    "fivb volleyball women's world cup": "كأس العالم لكرة الطائرة للسيدات",
    "fivb volleyball world championship": "بطولة العالم لكرة الطائرة",
    "fivb volleyball world cup": "كأس العالم لكرة الطائرة",
    "fivb volleyball world league": "الدوري العالمي للكرة الطائرة",
    "fivb women's volleyball world championship": "بطولة العالم لكرة الطائرة للسيدات",
    "former uci worldteams": "فرق دراجات هوائية عالمية سابقة",
    "iaaf continental cup": "كأس العالم لألعاب القوى",
    "iaaf diamond league": "دوري ماسي",
    "iaaf world cross country championships": "بطولة العالم للعدو الريفي",
    "iaaf world indoor championships in athletics": "بطولة العالم لألعاب القوى داخل الصالات",
    "iaaf world indoor championships": "بطولة العالم لألعاب القوى داخل الصالات",
    "iaaf world indoor games": "بطولة العالم لألعاب القوى داخل الصالات",
    "iaaf world junior championships in athletics": "بطولة العالم للناشئين لألعاب القوى",
    "iaaf world u20 championships": "بطولة العالم للناشئين لألعاب القوى",
    "iihf challenge cup of asia": "كأس التحدي الآسيوي لهوكي الجليد",
    "iihf world championship": "بطولة العالم لهوكي الجليد",
    "national collegiate athletic association": "الرابطة الوطنية لرياضة الجامعات",
    "ncaa men's water polo championship": "بطولة كرة الماء للرجال للجامعات",
    "ncaa women's water polo championship": "بطولة كرة الماء للسيدات للجامعات",
    "ncaa": "الرابطة الوطنية لرياضة الجامعات",
    "nme awards": "جوائز ان.ام.اي",
    "nme": "ان.ام.اي",
    "ofc champions league": "دوري أبطال أوقيانوسيا",
    "ofc nations cup": "كأس أوقيانوسيا للأمم",
    "ofc u-17 championship": "كأس أوقيانوسيا للأمم تحت 17 سنة",
    "ofc u-20 championship": "كأس أوقيانوسيا للأمم تحت 20 سنة",
    "psa world tour": "بطولات العالم للاتحاد الدولي لمحترفي الاسكواش",
    "saff championship": "بطولة اتحاد جنوب آسيا لكرة القدم",
    "the best fifa football awards": "جوائز الفيفا للأفضل كرويا",
    "the fifa world cup": "كأس العالم لكرة القدم",
    "uci africa tour": "طواف إفريقيا للدراجات",
    "uci america tour": "طواف أمريكا للدراجات",
    "uci asia tour": "طواف آسيا للدراجات",
    "uci continental teams (africa)": "الفرق القارية للاتحاد الدولي للدراجات (إفريقيا)",
    "uci continental teams (america)": "الفرق القارية للاتحاد الدولي للدراجات (أمريكا)",
    "uci continental teams (asia)": "الفرق القارية للاتحاد الدولي للدراجات (آسيا)",
    "uci continental teams (europe)": "الفرق القارية للاتحاد الدولي للدراجات (أوروبا)",
    "uci continental teams (oceania)": "الفرق القارية للاتحاد الدولي للدراجات (أوقيانوسيا)",
    "uci continental teams": "الفرق القارية للاتحاد الدولي للدراجات",
    "uci europe tour": "طواف أوروبا للدراجات",
    "uci mountain bike world cup": "كأس العالم للدراجات الجبلية",
    "uci oceania tour": "طواف أوقيانوسيا للدراجات",
    "uci professional continental teams": "فرق ركوب دراجات قارية محترفة",
    "uci road world championships – men's road race": "سباق الطريق في بطولة العالم لسباق الدراجات على الطريق",
    "uci road world championships – men's team time trial": "سباق الطريق ضد الساعة للفرق في بطولة العالم لسباق الدراجات على الطريق",
    "uci road world championships": "بطولة العالم لسباق الدراجات على الطريق",
    "uci road world cup": "كأس العالم لسباق الدراجات على الطريق",
    "uci track cycling world championships – men's 1 km time trial": "سباق الكيلو متر ضد الساعة في بطولة الدراجات على المضمار",
    "uci track cycling world championships – men's individual pursuit": "سباق المطاردة الفردية في بطولة الدراجات على المضمار",
    "uci track cycling world championships – men's keirin": "سباق الكيرين في بطولة الدراجات على المضمار",
    "uci track cycling world championships – men's madison": "سباق ماديسون في بطولة الدراجات على المضمار",
    "uci track cycling world championships – men's omnium": "سباق الأومنيوم في بطولة الدراجات على المضمار",
    "uci track cycling world championships – men's points race": "سباق النقاط في بطولة الدراجات على المضمار",
    "uci track cycling world championships – men's scratch": "سباق الخدش - السكراتش في بطولة الدراجات على المضمار",
    "uci track cycling world championships – men's sprint": "سباق السرعة الفردية في بطولة الدراجات على المضمار",
    "uci track cycling world championships – men's team pursuit": "سباق المطاردة الفرقية في بطولة الدراجات على المضمار",
    "uci track cycling world championships – men's team sprint": "سباق السرعة الفردية للفرق في بطولة الدراجات على المضمار",
    "uci track cycling world championships – women's 500 m time trial": "سباق 500 متر ضد الساعة للنساء في بطولة الدراجات على المضمار",
    "uci track cycling world championships – women's individual pursuit": "سباق المطاردة الفردية للنساء في بطولة الدراجات على المضمار",
    "uci track cycling world championships – women's keirin": "سباق الكيرين للنساء في بطولة الدراجات على المضمار",
    "uci track cycling world championships – women's madison": "سباق ماديسون للنساء في بطولة الدراجات على المضمار",
    "uci track cycling world championships – women's omnium": "سباق الأومنيوم للنساء في بطولة الدراجات على المضمار",
    "uci track cycling world championships – women's points race": "سباق النقاط للنساء في بطولة الدراجات على المضمار",
    "uci track cycling world championships – women's scratch": "سباق الخدش للنساء في بطولة الدراجات على المضمار",
    "uci track cycling world championships – women's sprint": "سباق السرعة الفردية للنساء في بطولة الدراجات على المضمار",
    "uci track cycling world championships – women's team pursuit": "سباق المطاردة الفرقية للنساء في بطولة الدراجات على المضمار",
    "uci track cycling world championships – women's team sprint": "سباق السرعة الفردية لفرق النساء في بطولة الدراجات على المضمار",
    "uci track cycling world championships": "بطولة العالم للدراجات على المضمار",
    "uci track cycling world cup classics": "كأس العالم لسباق الدراجات على المضمار",
    "uci track cycling world cup": "كأس العالم لسباق الدراجات على المضمار",
    "uci under 23 nations' cup": "كؤوس وطنية لسباقات الدراجات",
    "uci women's road world cup": "كأس العالم لسباق الدراجات على الطريق للسيدات",
    "uci women's world tour": "طواف العالم للدراجات للسيدات",
    "uci world championships": "بطولات العالم للدراجات",
    "uci world tour": "طواف العالم للدراجات",
    "uci worldteam riders": "دراجو فرق دراجات هوائية عالمية",
    "uci worldteams": "فرق دراجات هوائية عالمية",
    "uefa champions league": "دوري أبطال أوروبا",
    "uefa cup winners' cup": "كأس الكؤوس الأوروبية",
    "uefa cup": "كأس الاتحاد الأوروبي",
    "uefa euro 2004 qualifying": "تصفيات بطولة أمم أوروبا لكرة القدم 2004",
    "uefa euro": "بطولة أمم أوروبا",
    "uefa europa league": "الدوري الأوروبي",
    "uefa european championship qualifying": "تصفيات بطولة أمم أوروبا",
    "uefa european championship video games": "ألعاب فيديو بطولة أمم أوروبا لكرة القدم",
    "uefa european championship": "بطولة أمم أوروبا",
    "uefa european football championship": "بطولة أمم أوروبا",
    "uefa european under-10 championship": "بطولة أمم أوروبا تحت 10 سنة",
    "uefa european under-16 football championship": "بطولة أوروبا تحت 16 سنة لكرة القدم",
    "uefa european under-17 football championship": "بطولة أوروبا تحت 17 سنة لكرة القدم",
    "uefa european under-19 football championship": "بطولة أوروبا تحت 19 سنة لكرة القدم",
    "uefa european under-21 championship": "بطولة أوروبا تحت 21 سنة لكرة القدم",
    "uefa european under-21 football championship": "بطولة أوروبا تحت 21 سنة لكرة القدم",
    "uefa futsal championship": "بطولة أمم أوروبا داخل الصالات",
    "uefa futsal euro 2012": "بطولة أوروبا لكرة الصالات 2012",
    "uefa futsal euro": "بطولة أوروبا لكرة الصالات",
    "uefa intertonto": "كأس إنترتوتو",
    "uefa nations league": "دوري الأمم الأوروبية",
    "uefa regions' cup": "كأس المقاطعات الأوروبية",
    "uefa super cup": "كأس السوبر الأوروبي",
    "uefa women's championship": "بطولة أمم أوروبا للسيدات",
    "uefa women's euro 1993": "بطولة أمم أوروبا لكرة القدم للسيدات 1993",
    "uefa women's euro 1995": "بطولة أمم أوروبا لكرة القدم للسيدات 1995",
    "uefa women's euro 1997": "بطولة أمم أوروبا لكرة القدم للسيدات 1997",
    "uefa women's euro 2009": "بطولة أمم أوروبا لكرة القدم للسيدات 2009",
    "uefa women's euro 2013 qualifying": "تصفيات بطولة أمم أوروبا لكرة القدم للسيدات 2013",
    "uefa women's euro 2013": "بطولة أمم أوروبا لكرة القدم للسيدات 2013",
    "uefa women's euro 2017": "بطولة أمم أوروبا لكرة القدم للسيدات 2017",
    "uefa women's euro": "بطولة أمم أوروبا لكرة القدم للسيدات",
    "uefa women's under-17 championship": "بطولة أوروبا تحت 17 سنة لكرة القدم للسيدات",
    "uefa women's under-19 championship": "بطولة أوروبا تحت 19 سنة لكرة القدم للسيدات",
    "uefa youth league": "الدوري الأوروبي للشباب",
    "unaf club cup": "كأس اتحاد شمال إفريقيا",
    "unaf u-17 tournament": "بطولة أمم شمال إفريقيا تحت 17 سنة",
    "unaf u-20 tournament": "بطولة أمم شمال إفريقيا تحت 20 سنة",
    "unaf u-23 tournament": "بطولة أمم شمال إفريقيا تحت 23 سنة",
    "women's ehf challenge cup": "كأس التحدي الأوروبية لكرة اليد للسيدات",
    "women's ehf champions league": "دوري أبطال أوروبا لكرة اليد للسيدات",
    "women's ehf cup winners' cup": "كأس أبطال الكؤوس الأوروبية لكرة اليد للسيدات",
    "women's ehf cup": "كأس أوروبا لكرة اليد للسيدات",
    "world athletics indoor championships": "بطولة العالم لألعاب القوى داخل الصالات",
    "wta auckland open": "أوكلاند المفتوحة للسيدات",
    "wta madrid open (tennis)": "مدريد المفتوحة للسيدات (تنس)",
    "wta tour tournaments": "بطولات رابطة محترفات التنس",
    "wta tour": "رابطة محترفات التنس",
}

BATTLESHIP_CATEGORIES: dict[str, str] = {
    "aircraft carriers": "حاملات طائرات",
    "aircrafts": "طائرات",
    "amphibious warfare vessels": "سفن حربية برمائية",
    "auxiliary ships": "سفن مساعدة",
    "battlecruisers": "طرادات معركة",
    "battleships": "بوارج",
    "cargo aircraft": "طائرة شحن",
    "cargo aircrafts": "طائرة شحن",
    "cargo ships": "سفن بضائع",
    "coastal defence ships": "سفن دفاع ساحلية",
    "corvettes": "فرقيطات",
    "cruisers": "طرادات",
    "destroyers": "مدمرات",
    "escort ships": "سفن مرافقة",
    "frigates": "فرقاطات",
    "gunboats": "زوارق حربية",
    "helicopters": "مروحيات",
    "light cruisers": "طرادات خفيفة",
    "mine warfare vessels": "سفن حرب ألغام",
    "minesweepers": "كاسحات ألغام",
    "missile boats": "قوارب صواريخ",
    "naval ships": "سفن قوات بحرية",
    "ocean liners": "عابرات محيطات",
    "passenger ships": "سفن ركاب",
    "patrol vessels": "سفن دورية",
    "radar ships": "سفن رادار",
    "service vessels": "سفن خدمة",
    "Ship classes": "فئات سفن",
    "ships of the line": "سفن الخط",
    "ships": "سفن",
    "sloops": "سلوبات",
    "tall ships": "سفن طويلة",
    "torpedo boats": "زوارق طوربيد",
    "troop ships": "سفن جنود",
    "unmanned aerial vehicles": "طائرات بدون طيار",
    "unmanned military aircraft": "طائرات عسكرية بدون طيار",
}

RELIGIOUS_TRADITIONS: dict[str, dict[str, str]] = {
    "catholic": {"with_al": "الكاثوليكية", "no_al": "كاثوليكية"},
    "eastern orthodox": {"with_al": "الأرثوذكسية الشرقية", "no_al": "أرثوذكسية شرقية"},
    "moravian": {"with_al": "المورافية", "no_al": "مورافية"},
    "orthodox": {"with_al": "الأرثوذكسية", "no_al": "أرثوذكسية"},
}

UNITED_STATES_POLITICAL: dict[str, str] = {
    "united states house of representatives": "مجلس النواب الأمريكي",
    "united states house-of-representatives": "مجلس النواب الأمريكي",
    "united states presidential": "الرئاسة الأمريكية",
    "united states senate": "مجلس الشيوخ الأمريكي",
    "united states vice presidential": "نائب رئيس الولايات المتحدة",
    "united states vice-presidential": "نائب رئيس الولايات المتحدة",
    "vice presidential": "نائب الرئيس",
    "vice-presidential": "نائب الرئيس",
}

INTER_FEDS_LOWER: dict[str, str] = {key.lower(): value for key, value in INTER_FEDERATIONS.items()}


def build_new2019() -> dict[str, str]:
    """Assemble the 2019 key mapping including sports and political data."""

    data = dict(new_2019)

    for college_key, college_label in CAMBRIDGE_COLLEGES.items():
        data[f"{college_key}, Cambridge"] = f"{college_label} (جامعة كامبريدج)"
        data[f"{college_key} College, Cambridge"] = f"كلية {college_label} (جامعة كامبريدج)"
        data[f"{college_key} College, Oxford"] = f"كلية {college_label} جامعة أكسفورد"

    data.update(INTER_FEDS_LOWER)

    data.update({key.lower(): label for key, label in BATTLESHIP_CATEGORIES.items()})
    data.update({f"active {key.lower()}": f"{label} نشطة" for key, label in BATTLESHIP_CATEGORIES.items()})

    for tradition, labels in RELIGIOUS_TRADITIONS.items():
        no_al = labels["no_al"]
        base_key = tradition.lower()
        data[f"{base_key} cathedrals"] = f"كاتدرائيات {no_al}"
        data[f"{base_key} monasteries"] = f"أديرة {no_al}"
        data[f"{base_key} orders and societies"] = f"طوائف وتجمعات {no_al}"
        data[f"{base_key} eparchies"] = f"أبرشيات {no_al}"
        data[f"{base_key} religious orders"] = f"طوائف دينية {no_al}"
        data[f"{base_key} religious communities"] = f"طوائف دينية {no_al}"
        if tradition != "catholic":
            data[f"{base_key} catholic"] = f"{labels['with_al']} الكاثوليكية"
            data[f"{base_key} catholic eparchies"] = f"أبرشيات {no_al} كاثوليكية"

    data.update(CYCLING_TEMPLATES)

    for key, label in UNITED_STATES_POLITICAL.items():
        base_key = key.lower()
        data[f"{base_key} electors"] = f"ناخبو {label}"
        data[f"{base_key} election"] = f"انتخابات {label}"
        data[f"{base_key} elections"] = f"انتخابات {label}"
        data[f"{base_key} candidates"] = f"مرشحو {label}"

    return data


new2019: dict[str, str] = build_new2019()

__all__ = ["new2019", "INTER_FEDS_LOWER"]

len_print.data_len(
    "all_keys4.py",
    {
        "INTER_FEDS_LOWER": INTER_FEDS_LOWER,
        "new2019": new2019,
    },
)
