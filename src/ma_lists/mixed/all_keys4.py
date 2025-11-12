"""
Supplementary mappings for educational, sporting and political contexts.
"""

from ..sports.cycling import new_cy
from .keys2 import new_2019

CAMBRIDGE_COLLEGES: dict[str, str] = {
    "christ's": "كريست",
    "churchill": "تشرشل",
    "corpus christi": "كوربوس كريستي",
    "darwin": "داروين",
    "downing": "داونينج",
    "gonville and caius": "غونفيل وكايوس",
    "jesus": "يسوع",
    "king's": "كينجز",
    "lucy cavendish": "لوسي كافنديش",
    "magdalene": "المجدلية",
    "murray edwards": "موراي إدواردز",
    "pembroke": "بمبروك",
    "queens'": "كوينز",
    "st catharine's": "سانت كاثارين",
    "st john's": "سانت جونز",
    "trinity": "ترينيتي",
    "oriel": "أوريل",
    "fitzwilliam": "فيتزويليام",
    "newnham": "نونهم",
    "peterhouse": "بترهووس",
    "robinson": "روبنسون",
    "selwyn": "سلوين",
    "sidney sussex": "سيدني ساسكس",
    "st edmund's": "سانت ادموند",
    "trinity hall": "قاعة الثالوث",
    "hughes hall": "هيوز هول",
    "clare hall": "كلير هول",
    "wolfson": "وولفسون",
    "homerton": "هومرتون",
    "girton": "غيرتون",
}

INTER_FEDERATIONS: dict[str, str] = {
    "fifa women's world cup qualification": "تصفيات كأس العالم لكرة القدم للسيدات",
    "world athletics indoor championships": "بطولة العالم لألعاب القوى داخل الصالات",
    "fil world luge championships": "كأس العالم للزحف الثلجي",
    "fil under 23 world luge championships": "كأس العالم للزحف الثلجي تحت 23 سنة",
    "ncaa": "الرابطة الوطنية لرياضة الجامعات",
    "ncaa men's water polo championship": "بطولة كرة الماء للرجال للجامعات",
    "ncaa women's water polo championship": "بطولة كرة الماء للسيدات للجامعات",
    "national collegiate athletic association": "الرابطة الوطنية لرياضة الجامعات",
    "bwf world championships": "بطولة العالم لكرة الريشة",
    "bwf world junior championships": "بطولة العالم لكرة الريشة للناشئين",
    "conifa world football cup": "كأس العالم لاتحاد الجمعيات المستقلة لكرة القدم",
    "psa world tour": "بطولات العالم للاتحاد الدولي لمحترفي الاسكواش",
    "atp tour": "رابطة محترفي التنس",
    "atp tour tournaments": "بطولات رابطة محترفي التنس",
    "atp world tour": "بطولات العالم لرابطة محترفات التنس",
    "atp challenger tour": "بطولات تشالنجر لرابطة محترفات التنس",
    "wta auckland open": "أوكلاند المفتوحة للسيدات",
    "wta madrid open (tennis)": "مدريد المفتوحة للسيدات (تنس)",
    "wta tour tournaments": "بطولات رابطة محترفات التنس",
    "wta tour": "رابطة محترفات التنس",
    "uci professional continental teams": "فرق ركوب دراجات قارية محترفة",
    "uci continental teams": "الفرق القارية للاتحاد الدولي للدراجات",
    "uci continental teams (asia)": "الفرق القارية للاتحاد الدولي للدراجات (آسيا)",
    "uci continental teams (africa)": "الفرق القارية للاتحاد الدولي للدراجات (إفريقيا)",
    "uci continental teams (america)": "الفرق القارية للاتحاد الدولي للدراجات (أمريكا)",
    "uci continental teams (europe)": "الفرق القارية للاتحاد الدولي للدراجات (أوروبا)",
    "uci continental teams (oceania)": "الفرق القارية للاتحاد الدولي للدراجات (أوقيانوسيا)",
    "uci under 23 nations' cup": "كؤوس وطنية لسباقات الدراجات",
    "uci world championships": "بطولات العالم للدراجات",
    "uci world tour": "طواف العالم للدراجات",
    "uci america tour": "طواف أمريكا للدراجات",
    "uci asia tour": "طواف آسيا للدراجات",
    "uci africa tour": "طواف إفريقيا للدراجات",
    "uci oceania tour": "طواف أوقيانوسيا للدراجات",
    "uci women's world tour": "طواف العالم للدراجات للسيدات",
    "uci europe tour": "طواف أوروبا للدراجات",
    "former uci worldteams": "فرق دراجات هوائية عالمية سابقة",
    "uci worldteam riders": "دراجو فرق دراجات هوائية عالمية",
    "uci worldteams": "فرق دراجات هوائية عالمية",
    "uci track cycling world championships": "بطولة العالم للدراجات على المضمار",
    "uci mountain bike world cup": "كأس العالم للدراجات الجبلية",
    "uci road world championships": "بطولة العالم لسباق الدراجات على الطريق",
    "uci road world cup": "كأس العالم لسباق الدراجات على الطريق",
    "uci women's road world cup": "كأس العالم لسباق الدراجات على الطريق للسيدات",
    "uci track cycling world cup": "كأس العالم لسباق الدراجات على المضمار",
    "uci track cycling world cup classics": "كأس العالم لسباق الدراجات على المضمار",
    "uci road world championships – men's road race": "سباق الطريق في بطولة العالم لسباق الدراجات على الطريق",
    "uci road world championships – men's team time trial": "سباق الطريق ضد الساعة للفرق في بطولة العالم لسباق الدراجات على الطريق",
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
    "ofc u-17 championship": "كأس أوقيانوسيا للأمم تحت 17 سنة",
    "ofc nations cup": "كأس أوقيانوسيا للأمم",
    "ofc u-20 championship": "كأس أوقيانوسيا للأمم تحت 20 سنة",
    "ofc champions league": "دوري أبطال أوقيانوسيا",
    "concacaf championship": "بطولة أمريكا الشمالية",
    "concacaf gold cup": "كأس الكونكاكاف الذهبية",
    "concacaf u17 championship": "الكأس الذهبية تحت 17 سنة لكرة القدم",
    "concacaf under-20 championship": "الكأس الذهبية تحت 20 سنة لكرة القدم",
    "concacaf women's championship": "بطولة أمريكا الشمالية للسيدات",
    "concacaf women's u-10 championship": "بطولة أمريكا الشمالية للسيدات تحت 10 سنة",
    "concacaf women's u-17 championship": "بطولة أمريكا الشمالية للسيدات تحت 17 سنة",
    "concacaf champions league": "دوري أبطال الكونكاكاف",
    "aff u-23 championship": "بطولة اتحاد آسيان تحت 23 سنة",
    "aff u-23 youth championship": "بطولة اتحاد آسيان تحت 23 سنة للشباب",
    "aff championship": "بطولة اتحاد آسيان لكرة القدم",
    "ehf champions league": "دوري أبطال أوروبا لكرة اليد",
    "women's ehf champions league": "دوري أبطال أوروبا لكرة اليد للسيدات",
    "ehf cup": "كأس أوروبا لكرة اليد",
    "women's ehf cup": "كأس أوروبا لكرة اليد للسيدات",
    "women's ehf challenge cup": "كأس التحدي الأوروبية لكرة اليد للسيدات",
    "women's ehf cup winners' cup": "كأس أبطال الكؤوس الأوروبية لكرة اليد للسيدات",
    "ehf women's cup winners' cup": "كأس أبطال الكؤوس الأوروبية لكرة اليد للسيدات",
    "ehf women's champions league": "دوري أبطال أوروبا لكرة اليد للسيدات",
    "asean football championship": "بطولة اتحاد آسيان لكرة القدم",
    "fiba eurobasket": "بطولة أمم أوروبا لكرة السلة",
    "fiba basketball world cup": "كأس العالم لكرة السلة",
    "fiba women's basketball world cup": "كأس العالم لكرة السلة للسيدات",
    "fiba european champions cup": "كأس أبطال أوروبا لكرة السلة",
    "fiba women's european champions cup": "كأس أبطال أوروبا لكرة السلة للسيدات",
    "fiba women's world cup": "كأس العالم لكرة السلة للسيدات",
    "fiba world cup": "كأس العالم لكرة السلة",
    "fiba asia under-18 championship": "بطولة فيبا آسيا تحت 18 سنة لكرة السلة",
    "fiba under-20 world championship": "بطولة العالم تحت 20 سنة لكرة السلة",
    "fiba under-19 world championship": "بطولة العالم تحت 19 سنة لكرة السلة",
    "fiba under-18 world championship": "بطولة العالم تحت 18 سنة لكرة السلة",
    "fiba under-17 world championship": "بطولة العالم تحت 17 سنة لكرة السلة",
    "fiba under-16 world championship": "بطولة العالم تحت 16 سنة لكرة السلة",
    "fiba competitions": "منافسات الاتحاد الدولي لكرة السلة",
    "fiba korać cup": "كأس كوراتش لكرة السلة",
    "fiba saporta cup": "كأس سابورتا",
    "fiba asia cup": "كأس أمم آسيا لكرة السلة",
    "fiba americas league": "دوري الأمريكتين لكرة السلة",
    "fiba americas championship": "بطولة أمم الأمريكتين لكرة السلة",
    "fiba": "الاتحاد الدولي لكرة السلة",
    "fiba americup": "بطولة أمم الأمريكتين لكرة السلة",
    "fiba africa championship": "بطولة أمم إفريقيا لكرة السلة",
    "fiba asia championship": "بطولة أمم آسيا لكرة السلة",
    "fiba world championship": "بطولة كأس العالم لكرة السلة",
    "fiba world championship for women": "بطولة كأس العالم لكرة السلة للسيدات",
    "fifa confederations cup": "كأس القارات",
    "fifa world cup": "كأس العالم لكرة القدم",
    "fifa women's world cup": "كأس العالم لكرة القدم للسيدات",
    "fifa u-17 world cup": "كأس العالم تحت 17 سنة لكرة القدم",
    "fifa u-17 women's world cup": "كأس العالم تحت 17 سنة لكرة القدم للسيدات",
    "fifa u-20 world cup": "كأس العالم تحت 20 سنة لكرة القدم",
    "fifa u-20 women's world cup": "كأس العالم تحت 20 سنة لكرة القدم للسيدات",
    "the fifa world cup": "كأس العالم لكرة القدم",
    "fifa club world cup": "كأس العالم للأندية",
    "fifa beach soccer world cup": "كأس العالم الشاطئية",
    "fifa futsal world cup ney": "بطولة كأس العالم داخل الصالات",
    "fifa futsal world cup players": "لاعبو كأس العالم لكرة الصالات",
    "fifa world cup players": "لاعبو كأس العالم لكرة القدم",
    "the best fifa football awards": "جوائز الفيفا للأفضل كرويا",
    "nme awards": "جوائز ان.ام.اي",
    "nme": "ان.ام.اي",
    "iaaf continental cup": "كأس العالم لألعاب القوى",
    "iaaf world u20 championships": "بطولة العالم للناشئين لألعاب القوى",
    "iaaf diamond league": "دوري ماسي",
    "iaaf world indoor championships in athletics": "بطولة العالم لألعاب القوى داخل الصالات",
    "iaaf world cross country championships": "بطولة العالم للعدو الريفي",
    "iaaf world indoor championships": "بطولة العالم لألعاب القوى داخل الصالات",
    "iaaf world indoor games": "بطولة العالم لألعاب القوى داخل الصالات",
    "iaaf world junior championships in athletics": "بطولة العالم للناشئين لألعاب القوى",
    "saff championship": "بطولة اتحاد جنوب آسيا لكرة القدم",
    "fis nordic world ski championships": "بطولة العالم للتزلج النوردي على الثلج",
    "fivb women's volleyball world championship": "بطولة العالم لكرة الطائرة للسيدات",
    "fivb volleyball world cup": "كأس العالم لكرة الطائرة",
    "fivb volleyball women's world cup": "كأس العالم لكرة الطائرة للسيدات",
    "fivb volleyball men's world championship": "بطولة العالم للكرة الطائرة",
    "fivb volleyball world championship": "بطولة العالم لكرة الطائرة",
    "fivb volleyball world league": "الدوري العالمي للكرة الطائرة",
    "iihf world championship": "بطولة العالم لهوكي الجليد",
    "iihf challenge cup of asia": "كأس التحدي الآسيوي لهوكي الجليد",
    "uefa women's euro": "بطولة أمم أوروبا لكرة القدم للسيدات",
    "uefa champions league": "دوري أبطال أوروبا",
    "uefa euro 2004 qualifying": "تصفيات بطولة أمم أوروبا لكرة القدم 2004",
    "uefa european championship video games": "ألعاب فيديو بطولة أمم أوروبا لكرة القدم",
    "uefa futsal euro 2012": "بطولة أوروبا لكرة الصالات 2012",
    "uefa women's euro 1993": "بطولة أمم أوروبا لكرة القدم للسيدات 1993",
    "uefa women's euro 1995": "بطولة أمم أوروبا لكرة القدم للسيدات 1995",
    "uefa women's euro 1997": "بطولة أمم أوروبا لكرة القدم للسيدات 1997",
    "uefa women's euro 2009": "بطولة أمم أوروبا لكرة القدم للسيدات 2009",
    "uefa women's euro 2013": "بطولة أمم أوروبا لكرة القدم للسيدات 2013",
    "uefa women's euro 2013 qualifying": "تصفيات بطولة أمم أوروبا لكرة القدم للسيدات 2013",
    "uefa women's euro 2017": "بطولة أمم أوروبا لكرة القدم للسيدات 2017",
    "uefa women's under-17 championship": "بطولة أوروبا تحت 17 سنة لكرة القدم للسيدات",
    "uefa europa league": "الدوري الأوروبي",
    "uefa women's championship": "بطولة أمم أوروبا للسيدات",
    "uefa futsal euro": "بطولة أوروبا لكرة الصالات",
    "uefa euro": "بطولة أمم أوروبا",
    "2017–18 uefa champions league": "دوري أبطال أوروبا 2017–18",
    "uefa nations league": "دوري الأمم الأوروبية",
    "uefa european championship qualifying": "تصفيات بطولة أمم أوروبا",
    "uefa super cup": "كأس السوبر الأوروبي",
    "uefa cup": "كأس الاتحاد الأوروبي",
    "uefa intertonto": "كأس إنترتوتو",
    "uefa cup winners' cup": "كأس الكؤوس الأوروبية",
    "uefa regions' cup": "كأس المقاطعات الأوروبية",
    "uefa european championship": "بطولة أمم أوروبا",
    "uefa european football championship": "بطولة أمم أوروبا",
    "uefa european under-10 championship": "بطولة أمم أوروبا تحت 10 سنة",
    "uefa youth league": "الدوري الأوروبي للشباب",
    "uefa futsal championship": "بطولة أمم أوروبا داخل الصالات",
    "uefa european under-16 football championship": "بطولة أوروبا تحت 16 سنة لكرة القدم",
    "uefa european under-17 football championship": "بطولة أوروبا تحت 17 سنة لكرة القدم",
    "uefa european under-19 football championship": "بطولة أوروبا تحت 19 سنة لكرة القدم",
    "uefa women's under-19 championship": "بطولة أوروبا تحت 19 سنة لكرة القدم للسيدات",
    "uefa european under-21 championship": "بطولة أوروبا تحت 21 سنة لكرة القدم",
    "uefa european under-21 football championship": "بطولة أوروبا تحت 21 سنة لكرة القدم",
    "caf confederation cup": "كأس الكونفيدرالية الإفريقية",
    "caf champions league": "دوري أبطال إفريقيا",
    "unaf u-17 tournament": "بطولة أمم شمال إفريقيا تحت 17 سنة",
    "unaf u-20 tournament": "بطولة أمم شمال إفريقيا تحت 20 سنة",
    "unaf club cup": "كأس اتحاد شمال إفريقيا",
    "unaf u-23 tournament": "بطولة أمم شمال إفريقيا تحت 23 سنة",
    "fina world aquatics championships": "بطولة العالم للألعاب المائية",
    "fina water polo world league": "الدوري العالمي لكرة الماء",
    "fina": "الاتحاد الدولي للسباحة",
    "fina world swimming championships (25 m)": "بطولة العالم للسباحة (25 متر)",
    "fina world swimming championships": "بطولة العالم للسباحة",
}

BATTLESHIP_CATEGORIES: dict[str, str] = {
    "patrol vessels": "سفن دورية",
    "ocean liners": "عابرات محيطات",
    "naval ships": "سفن قوات بحرية",
    "passenger ships": "سفن ركاب",
    "cargo ships": "سفن بضائع",
    "service vessels": "سفن خدمة",
    "tall ships": "سفن طويلة",
    "minesweepers": "كاسحات ألغام",
    "destroyers": "مدمرات",
    "corvettes": "فرقيطات",
    "ships": "سفن",
    "helicopters": "مروحيات",
    "aircrafts": "طائرات",
    "cargo aircraft": "طائرة شحن",
    "cargo aircrafts": "طائرة شحن",
    "unmanned military aircraft": "طائرات عسكرية بدون طيار",
    "unmanned aerial vehicles": "طائرات بدون طيار",
    "aircraft carriers": "حاملات طائرات",
    "amphibious warfare vessels": "سفن حربية برمائية",
    "auxiliary ships": "سفن مساعدة",
    "battlecruisers": "طرادات معركة",
    "battleships": "بوارج",
    "coastal defence ships": "سفن دفاع ساحلية",
    "cruisers": "طرادات",
    "escort ships": "سفن مرافقة",
    "Ship classes": "فئات سفن",
    "frigates": "فرقاطات",
    "gunboats": "زوارق حربية",
    "light cruisers": "طرادات خفيفة",
    "ships of the line": "سفن الخط",
    "mine warfare vessels": "سفن حرب ألغام",
    "missile boats": "قوارب صواريخ",
    "radar ships": "سفن رادار",
    "sloops": "سلوبات",
    "torpedo boats": "زوارق طوربيد",
    "troop ships": "سفن جنود",
}

RELIGIOUS_TRADITIONS: dict[str, dict[str, str]] = {
    "orthodox": {"singular": "الأرثوذكسية", "plural": "أرثوذكسية"},
    "eastern orthodox": {"singular": "الأرثوذكسية الشرقية", "plural": "أرثوذكسية شرقية"},
    "moravian": {"singular": "المورافية", "plural": "مورافية"},
    "catholic": {"singular": "الكاثوليكية", "plural": "كاثوليكية"},
}

UNITED_STATES_POLITICAL: dict[str, str] = {
    "united states senate": "مجلس الشيوخ الأمريكي",
    "united states house-of-representatives": "مجلس النواب الأمريكي",
    "united states house of representatives": "مجلس النواب الأمريكي",
    "united states vice-presidential": "نائب رئيس الولايات المتحدة",
    "united states vice presidential": "نائب رئيس الولايات المتحدة",
    "united states presidential": "الرئاسة الأمريكية",
    "vice-presidential": "نائب الرئيس",
    "vice presidential": "نائب الرئيس",
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
        plural = labels["plural"]
        base_key = tradition.lower()
        data[f"{base_key} cathedrals"] = f"كاتدرائيات {plural}"
        data[f"{base_key} monasteries"] = f"أديرة {plural}"
        data[f"{base_key} orders and societies"] = f"طوائف وتجمعات {plural}"
        data[f"{base_key} eparchies"] = f"أبرشيات {plural}"
        data[f"{base_key} religious orders"] = f"طوائف دينية {plural}"
        data[f"{base_key} religious communities"] = f"طوائف دينية {plural}"
        if tradition != "catholic":
            data[f"{base_key} catholic"] = f"{labels['singular']} الكاثوليكية"
            data[f"{base_key} catholic eparchies"] = f"أبرشيات {plural} كاثوليكية"

    data.update(new_cy)

    for key, label in UNITED_STATES_POLITICAL.items():
        base_key = key.lower()
        data[f"{base_key} electors"] = f"ناخبو {label}"
        data[f"{base_key} election,"] = f"انتخابات {label}"
        data[f"{base_key} election"] = f"انتخابات {label}"
        data[f"{base_key} elections"] = f"انتخابات {label}"
        data[f"{base_key} candidates"] = f"مرشحو {label}"

    return data


new2019: dict[str, str] = build_new2019()

__all__ = [
    "new2019",
    "INTER_FEDS_LOWER"
]
