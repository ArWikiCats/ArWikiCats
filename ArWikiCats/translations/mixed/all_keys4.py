"""
Supplementary mappings for educational, sporting and political contexts.
"""

from ..helps import len_print
from ..sports import CYCLING_TEMPLATES
from ..utils import open_json_file
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


def build_new2019(INTER_FEDS_LOWER, NEW_2019) -> dict[str, str]:
    """Assemble the 2019 key mapping including sports and political data."""

    data = dict(NEW_2019)

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


INTER_FEDERATIONS: dict[str, str] = open_json_file("sports/inter_federations.json")
INTER_FEDS_LOWER: dict[str, str] = {key.lower(): value for key, value in INTER_FEDERATIONS.items()}

new2019: dict[str, str] = build_new2019(INTER_FEDS_LOWER, new_2019)

clubs = open_json_file("sports/Clubs_key.json") or {}

clubs_index: dict[str, str] = {}
for club, label in clubs.items():
    if not club or not label:
        continue
    club_lower = club.lower()
    clubs_index[club_lower] = label

Clubs_key_2 = clubs_index

__all__ = [
    "new2019",
    "INTER_FEDS_LOWER",
    "Clubs_key_2",
]

len_print.data_len(
    "all_keys4.py",
    {
        "Clubs_key_2": Clubs_key_2,
        "INTER_FEDS_LOWER": INTER_FEDS_LOWER,
        "new2019": new2019,
    },
)
