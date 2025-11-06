#!/usr/bin/python3
r"""
\s*['"]\{\} \{\}['"]\.format\(\s*(.*?)\s*,\s*(.*?)\s*\)
f"{$1} {$2}"


['"]\{\} \{\}['"]\.format\(\s*([\w\d]+)\s*,\s*([\w\d]+)\s*\)
f"{$1} {$2}"

"""


# ---
from .utils.json_dir import open_json_file

from .geo.games_labs import summer_winter_tabs
from .companies import companies_keys3, typeTable_update
from .structures import tab2, pop_final_3_update
# ---
pop_final_3 = open_json_file("pop_final_3") or {}
# ---
# 'extradited people': "أشخاص تم تسليمهم",
# 'people extradited': "أشخاص تم تسليمهم",
# 'programs\xe2\x80\x8e': "برامج",
# "the louvre":"متحف اللوفر",
# "the paralympics":"الألعاب البارالمبية",
# "heavy metal musical groups":"فرق موسيقى هيفي ميتال",
# "black metal musical groups":"فرق موسيقى بلاك ميتال" ,
# ---
typeTable_7 = {
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
# ---
typeTable_7.update(typeTable_update)
# ---
albums_type = {
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
# ---
businesspeoples = {
    "video game": "ألعاب الفيديو",
    "real estate": "العقارات",
    "financial": "المالية",
    "metals": "المعادن",
    "entertainment": "الترفيه",
    "fashion": "الأزياء",
    "computer": "كمبيوتر",
    "cosmetics": "مستحضرات التجميل",
}
# ---
for iu in businesspeoples:
    pop_final_3[f"{iu} businesspeople"] = f"شخصيات أعمال في {businesspeoples[iu]}"
    pop_final_3[f"{iu} industry businesspeople"] = f"شخصيات أعمال في صناعة {businesspeoples[iu]}"
# ---
film_production_company = {
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
for production, pro_lab in film_production_company.items():
    pop_final_3[production] = pro_lab
    pop_final_3[f"{production} films"] = f"أفلام {pro_lab}"


pop_final_3.update(summer_winter_tabs)
pop_final_3.update(companies_keys3)
pop_final_3.update(tab2)
pop_final_3.update(pop_final_3_update)
# ---
Ambassadors_tab = {}

NN_table = {}
NN_table2 = {
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
