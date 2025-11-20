"""Additional key-label mappings for companies, media and professions."""

from __future__ import annotations

from ...helps import len_print
from ..companies import companies_keys3, typeTable_update
from ..sports.games_labs import SUMMER_WINTER_TABS
from ..structures import pop_final_3_update, tab2
from ..utils.json_dir import open_json_file

TYPE_TABLE_7_BASE: dict[str, str] = {
    "air force": "قوات جوية",
    "people executed by": "أشخاص أعدموا من قبل",
    "executions": "إعدامات",
    "executed-burning": "أعدموا شنقاً",
    "executed-hanging": "أعدموا حرقاً",
    "executed-decapitation": "أعدموا بقطع الرأس",
    "executed-firearm": "أعدموا بسلاح ناري",
    "people executed-by-burning": "أشخاص أعدموا شنقاً",
    "people executed-by-hanging": "أشخاص أعدموا حرقاً",
    "people executed-by-decapitation": "أشخاص أعدموا بقطع الرأس",
    "people executed-by-firearm": "أشخاص أعدموا بسلاح ناري",
}

ALBUMS_TYPE: dict[str, str] = {
    "folktronica": "فولكترونيكا",
    "concept": "مفاهيمية",
    "surprise": "مفاجئة",
    "comedy": "كوميدية",
    "mixtape": "ميكستايب",
    "remix": "ريمكس",
    "animation": "رسوم متحركة",
    "video": "فيديو",
    "compilation": "تجميعية",
    "live": "مباشرة",
    "jazz": "جاز",
    "eps": "أسطوانة مطولة",
    "folk": "فولك",
}

BUSINESSPEOPLE_INDUSTRIES: dict[str, str] = {
    "video game": "ألعاب الفيديو",
    "real estate": "العقارات",
    "financial": "المالية",
    "metals": "المعادن",
    "entertainment": "الترفيه",
    "fashion": "الأزياء",
    "computer": "كمبيوتر",
    "cosmetics": "مستحضرات التجميل",
}

FILM_PRODUCTION_COMPANY: dict[str, str] = {
    "Yash Raj": "ياش راج",
    "Illumination Entertainment": "إليمونيشن للترفيه",
    "Walt Disney Animation Studios": "استديوهات والت ديزني للرسوم المتحركة",
    "Carolco Pictures": "كارلوكو بيكشرز",
    "Aardman Animations": "آردمان انيمشنز",
    "Soyuzmultfilm": "سويز مولتفيلم",
    "Weinstein Company": "شركة وينشتاين",
    "Castle Rock Entertainment": "كاسل روك للترفيه",
    "United Artists": "يونايتد آرتيست",
    "Mosfilm": "موسفيلم",
    "National Geographic Society": "منظمة ناشيونال جيوغرافيك",
    "Showtime (TV network)": "شوتايم",
    "Touchstone Pictures": "توتشستون بيكشرز",
    "Rooster Teeth": "أسنان الديك",
    "Blue Sky Studios": "استديوهات بلو سكاي",
    "Bad Robot Productions": "باد روبوت للإنتاج",
    "TMS Entertainment": "تي أم أس إنترتنيمنت",
    "Sony Pictures Entertainment": "سوني بيكشرز إنترتنمنت",
    "sony pictures animation": "سوني بيكشرز أنيماشين",
    "Toei Company": "شركة توي",
    "Toho": "توهو",
    "Universal Studios": "يونيفرسل ستوديوز",
    "Walt Disney Company": "ديزني",
    "Paramount Pictures": "باراماونت بيكتشرز",
    "20th Century Fox": "تونتيث سينتشوري فوكس",
    "DreamWorks Animation": "دريمووركس أنيماشين",
    "Pixar": "بيكسار",
    "Metro-Goldwyn-Mayer": "مترو غولدوين ماير",
    "Lucasfilm": "لوكاس فيلم",
    "Amblin Entertainment": "أمبلين للترفيه",
    "DreamWorks": "دريم ووركس",
    "Funimation": "شركة فنميشن للترفيه",
    "Columbia Pictures": "كولومبيا بيكتشرز",
    "Marvel Studios": "استوديوهات مارفل",
    "HBO": "هوم بوكس أوفيس",
    "Warner Bros.": "وارنر برذرز",
}

NN_TABLE_GENDERED: dict[str, dict[str, str]] = {
    "south african": {"men": "جنوب إفريقي", "women": "جنوب إفريقية"},
    "democratic republic of the congo": {
        "men": "كونغوي الديمقراطي",
        "women": "كونغوية الديمقراطية",
    },
    "bissau-guinean": {"men": "غيني البيساوي", "women": "غينية البيساوية"},
    "south american": {"men": "أمريكي الجنوبي", "women": "أمريكية الجنوبية"},
    "north american": {"men": "أمريكي الشمالي", "women": "أمريكية الشمالية"},
    "northern ireland": {"men": "أيرلندي الشمالي", "women": "أيرلندية الشمالية"},
    "hong kong": {"men": "هونغ كونغي", "women": "هونغ كونغية"},
    "equatoguinean": {"men": "غيني الاستوائي", "women": "غينية الاستوائية"},
    "east timorese": {"men": "تيموري الشرقي", "women": "تيمورية الشرقية"},
    "south korean": {"men": "كوري الجنوبي", "women": "كورية الجنوبية"},
    "north korean": {"men": "كوري الشمالي", "women": "كورية الشمالية"},
}


def build_pop_final_3() -> dict[str, str]:
    """Build the main mapping used for pop culture categories."""

    registry = open_json_file("population/pop_final_3") or {}

    for industry, label in BUSINESSPEOPLE_INDUSTRIES.items():
        registry[f"{industry} businesspeople"] = f"شخصيات أعمال في {label}"
        registry[f"{industry} industry businesspeople"] = f"شخصيات أعمال في صناعة {label}"

    for company, label in FILM_PRODUCTION_COMPANY.items():
        registry[company] = label
        registry[f"{company} films"] = f"أفلام {label}"

    registry.update(SUMMER_WINTER_TABS)
    registry.update(companies_keys3)
    registry.update(tab2)
    registry.update(pop_final_3_update)

    return registry


pop_final_3: dict[str, str] = build_pop_final_3()
typeTable_7: dict[str, str] = {**TYPE_TABLE_7_BASE, **typeTable_update}

Ambassadors_tab: dict[str, str] = {}

NN_table: dict[str, str] = {}

NN_table2: dict[str, dict[str, str]] = dict(NN_TABLE_GENDERED)

len_print.data_len(
    "all_keys3.py",
    {
        "pop_final_3": pop_final_3,
        "typeTable_7": typeTable_7,
        "ALBUMS_TYPE": ALBUMS_TYPE,
        "FILM_PRODUCTION_COMPANY": FILM_PRODUCTION_COMPANY,
        "NN_table2": NN_table2,
        "BUSINESSPEOPLE_INDUSTRIES": BUSINESSPEOPLE_INDUSTRIES,
    },
)

__all__ = [
    "pop_final_3",
    "typeTable_7",
    "ALBUMS_TYPE",
    "FILM_PRODUCTION_COMPANY",
    "Ambassadors_tab",
    "NN_table",
    "NN_table2",
    "BUSINESSPEOPLE_INDUSTRIES",
]
