"""Additional key-label mappings for companies, media and professions."""

from __future__ import annotations

from ..companies import companies_keys3, typeTable_update
from ..sports.games_labs import summer_winter_tabs
from ..structures import tab2, pop_final_3_update
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


def _build_businesspeople_entries(registry: KeyRegistry) -> None:
    """Add industry specific businesspeople mappings."""

    for industry, label in BUSINESSPEOPLE_INDUSTRIES.items():
        registry.data[f"{industry} businesspeople"] = f"شخصيات أعمال في {label}"
        registry.data[f"{industry} industry businesspeople"] = f"شخصيات أعمال في صناعة {label}"


def _build_film_company_entries(registry: KeyRegistry) -> None:
    """Add film production companies and their film catalogues."""

    for company, label in FILM_PRODUCTION_COMPANY.items():
        registry.data[company] = label
        registry.data[f"{company} films"] = f"أفلام {label}"


def build_pop_final_3() -> dict[str, str]:
    """Build the main mapping used for pop culture categories."""

    base_mapping = open_json_file("pop_final_3") or {}
    registry = KeyRegistry(base_mapping)

    _build_businesspeople_entries(registry)
    _build_film_company_entries(registry)

    registry.update(summer_winter_tabs)
    registry.update(companies_keys3)
    registry.update(tab2)
    registry.update(pop_final_3_update)

    return registry.data


pop_final_3 = open_json_file("pop_final_3") or {}

typeTable_7: dict[str, str] = {**TYPE_TABLE_7_BASE, **typeTable_update}


for iu in BUSINESSPEOPLE_INDUSTRIES:
    pop_final_3[f"{iu} businesspeople"] = f"شخصيات أعمال في {BUSINESSPEOPLE_INDUSTRIES[iu]}"
    pop_final_3[f"{iu} industry businesspeople"] = f"شخصيات أعمال في صناعة {BUSINESSPEOPLE_INDUSTRIES[iu]}"

for production, pro_lab in FILM_PRODUCTION_COMPANY.items():
    pop_final_3[production] = pro_lab
    pop_final_3[f"{production} films"] = f"أفلام {pro_lab}"


pop_final_3.update(summer_winter_tabs)
pop_final_3.update(companies_keys3)
pop_final_3.update(tab2)
pop_final_3.update(pop_final_3_update)

Ambassadors_tab: dict[str, str] = {}

NN_table: dict[str, str] = {}

NN_table2: dict[str, dict[str, str]] = dict(NN_TABLE_GENDERED)

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
