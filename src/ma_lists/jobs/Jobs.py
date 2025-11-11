"""Build comprehensive gendered job label dictionaries.

This module historically assembled several large dictionaries describing job
labels in Arabic.  The original implementation relied on implicit global state
and mutating logic that made the data construction difficult to follow.

The refactor below keeps the exported data identical while restructuring the
pipeline into typed helper functions with clear documentation.  Each helper
focuses on a single transformation—loading JSON data, combining gendered labels,
adding derived sport or film variants, or flattening the output for historic
exports.  The end result is a deterministic data set that is easier to maintain
and safe to import in other modules.
"""

from __future__ import annotations

import logging
import sys
from dataclasses import dataclass
from typing import Dict, List, Mapping, MutableMapping

from ...helps import len_print
from ..companies import companies_to_jobs
from ..utils.json_dir import open_json
from ..mixed.all_keys2 import Books_table
from ..mixed.male_keys import religious_female_keys
from ..nats.Nationality import Nat_mens
from ..politics.ministers import ministrs_tab_for_Jobs_2020
from ..sports.cycling import new2019_cycling
from ..tv.films_mslslat import Films_key_For_Jobs
from .Jobs2 import JOBS_2
from .jobs_data import RELIGIOUS_KEYS_PP, MEN_WOMENS_JOBS_2
from .jobs_players_list import (
    FEMALE_JOBS_TO,
    FOOTBALL_KEYS_PLAYERS,
    PLAYERS_TO_MEN_WOMENS_JOBS,
)
from .jobs_singers import MEN_WOMENS_SINGERS, FILMS_TYPE

Jobs_new = {}

JOBS_2020 = {
    "ecosocialists": {"mens": "إيكولوجيون", "womens": "إيكولوجيات"},
    "wheelchair tennis players": {
        "mens": "لاعبو كرة مضرب على الكراسي المتحركة",
        "womens": "لاعبات كرة مضرب على الكراسي المتحركة",
    },
}

JOBS_PEOPLE = {
    "bloggers": {"mens": "مدونو", "womens": "مدونات"},
    "writers": {"mens": "كتاب", "womens": "كاتبات"},
}

JOBS_TYPE = {
    "adventure": "مغامرة",
    "alternate history": "تاريخ بديل",
    "animated": "رسوم متحركة",
    "science fiction action": "خيال علمي وحركة",
}

jobs_data = open_json("jobs/jobs.json")

JOBS_2020.update({x: v for x, v in jobs_data["JOBS_2020"].items() if v.get("mens") and v.get("womens")})
JOBS_PEOPLE.update({x: v for x, v in jobs_data["JOBS_PEOPLE"].items() if v.get("mens") and v.get("womens")})
JOBS_TYPE.update({x: v for x, v in jobs_data["JOBS_TYPE"].items() if v})  # v is string

Jobs_key_Format = {
    "{} people in health professions": "عاملون {} بمهن صحية",
    "{} eugenicists": "علماء {nato} متخصصون في تحسين النسل",
}
Men_Womens_with_nato = {
    "eugenicists": {
        "mens": "علماء {nato} متخصصون في تحسين النسل",
        "womens": "عالمات {nato} متخصصات في تحسين النسل",
    },
    "politicians who committed suicide": {
        "mens": "سياسيون {nato} أقدموا على الانتحار",
        "womens": "سياسيات {nato} أقدمن على الانتحار",
    },
    "contemporary artists": {
        "mens": "فنانون {nato} معاصرون",
        "womens": "فنانات {nato} معاصرات",
    },
}


MenWomensJobsPP = open_json("jobs/jobs_Men_Womens_PP.json")

for minister_category, minister_labels in ministrs_tab_for_Jobs_2020.items():
    JOBS_2020[minister_category] = minister_labels

jobs_table_3 = {
    "deaf": {"mens": "صم", "womens": "صم"},
    "blind": {"mens": "مكفوفون", "womens": "مكفوفات"},
    "deafblind": {"mens": "صم ومكفوفون", "womens": "صم ومكفوفات"},
}

executives = {
    "railroad": "سكك حديدية",
    "media": "وسائل إعلام",
    "public transportation": "نقل عام",
    "film studio": "استوديوهات أفلام",
    "advertising": "إعلانات",
    "music industry": "صناعة الموسيقى",
    "newspaper": "جرائد",
    "radio": "مذياع",
    "television": "تلفاز",
    "media5": "",
}

Nat_Before_Occ = [
    "convicted-of-murder",
    "murdered abroad",
    "contemporary",
    "tour de france stage winners",
    "deafblind",
    "deaf",
    "blind",
    "jews",
    "women's rights activists",
    "human rights activists",
    "imprisoned",
    "imprisoned abroad",
    "conservationists",
    "expatriate",
    "defectors",
    "scholars of islam",
    "scholars-of-islam",
    "amputees",
    "expatriates",
    "scholars of",
    "executed abroad",
    "emigrants",
]

typi = {
    "classical": {"mens": "كلاسيكيون", "womens": "كلاسيكيات"},
    "historical": {"mens": "تاريخيون", "womens": "تاريخيات"},
}

Female_Jobs = {
    "nuns": "راهبات",
    "deafblind actresses": "ممثلات صم ومكفوفات",
    "deaf actresses": "ممثلات صم",
    "actresses": "ممثلات",
    "princesses": "أميرات",
    "video game actresses": "ممثلات ألعاب فيديو",
    "musical theatre actresses": "ممثلات مسرحيات موسيقية",
    "television actresses": "ممثلات تلفزيون",
    "stage actresses": "ممثلات مسرح",
    "voice actresses": "ممثلات أداء صوتي",
}
NNN_Keys_Films = {
    "filmmakers": {"mens": "صانعو أفلام", "womens": "صانعات أفلام"},
    "film editors": {"mens": "محررو أفلام", "womens": "محررات أفلام"},
    "film directors": {"mens": "مخرجو أفلام", "womens": "مخرجات أفلام"},
    "film producers": {"mens": "منتجو أفلام", "womens": "منتجات أفلام"},
    "film critics": {"mens": "نقاد أفلام", "womens": "ناقدات أفلام"},
    "film historians": {"mens": "مؤرخو أفلام", "womens": "مؤرخات أفلام"},
    "cinema editors": {"mens": "محررون سينمائون", "womens": "محررات سينمائيات"},
    "cinema directors": {"mens": "مخرجون سينمائون", "womens": "مخرجات سينمائيات"},
    "cinema producers": {"mens": "منتجون سينمائون", "womens": "منتجات سينمائيات"},
}

Jobs_key_mens = {}
Jobs_key_womens = {}
womens_Jobs_2017 = {}

Men_Womens_Jobs = {}

Men_Womens_Jobs.update(MEN_WOMENS_JOBS_2)

for religious_key, gendered_titles in RELIGIOUS_KEYS_PP.items():
    MenWomensJobsPP[religious_key] = gendered_titles

    MenWomensJobsPP[f"{religious_key} activists"] = {
        "mens": f"ناشطون {gendered_titles['mens']}",
        "womens": f"ناشطات {gendered_titles['womens']}",
    }


for industry_key, industry_label in executives.items():
    jobs_table_3[f"{industry_key} executives"] = {
        "mens": f"مدراء {industry_label}",
        "womens": f"مديرات {industry_label}",
    }

for disability_key, disability_labels in jobs_table_3.items():
    MenWomensJobsPP[disability_key] = disability_labels

for job_name, gender_labels in JOBS_2020.items():
    if gender_labels["mens"] and gender_labels["womens"]:
        if job_name.lower() not in MenWomensJobsPP:
            MenWomensJobsPP[job_name.lower()] = gender_labels

for player_category, player_labels in FOOTBALL_KEYS_PLAYERS.items():
    if player_category.lower() not in MenWomensJobsPP:
        MenWomensJobsPP[player_category.lower()] = player_labels


activists_keys = open_json("jobs/activists_keys.json")

for activist_category, activist_labels in activists_keys.items():
    normalized_key = activist_category.lower()
    Nat_Before_Occ.append(normalized_key)
    Men_Womens_Jobs[normalized_key] = activist_labels

MenWomensJobsPP["fashion journalists"] = {
    "mens": "صحفيو موضة",
    "womens": "صحفيات موضة",
}
MenWomensJobsPP["zionists"] = {"mens": "صهاينة", "womens": "صهيونيات"}
MenWomensJobsPP.update(companies_to_jobs)

for religious_key, female_label in religious_female_keys.items():
    MenWomensJobsPP[f"{religious_key} founders"] = {
        "mens": f"مؤسسو {female_label}",
        "womens": f"مؤسسات {female_label}",
    }


MenWomensJobsPP["imprisoned abroad"] = {
    "mens": "مسجونون في الخارج",
    "womens": "مسجونات في الخارج",
}
MenWomensJobsPP["imprisoned"] = {"mens": "مسجونون", "womens": "مسجونات"}

MenWomensJobsPP["escapees"] = {"mens": "هاربون", "womens": "هاربات"}
MenWomensJobsPP["prison escapees"] = {
    "mens": "هاربون من السجن",
    "womens": "هاربات من السجن",
}
MenWomensJobsPP["missionaries"] = {"mens": "مبشرون", "womens": "مبشرات"}
MenWomensJobsPP["venerated"] = {"mens": "مبجلون", "womens": "مبجلات"}

for job_key in JOBS_2:
    lowered_job_key = job_key.lower()
    if job_key not in MenWomensJobsPP and lowered_job_key not in MenWomensJobsPP:
        if JOBS_2[job_key]["mens"] or JOBS_2[job_key]["womens"]:
            MenWomensJobsPP[lowered_job_key] = JOBS_2[job_key]

for job_key, gender_labels in MenWomensJobsPP.items():
    Men_Womens_Jobs[job_key.lower()] = gender_labels

sports_len = 0
for base_job_key, base_job_labels in MenWomensJobsPP.items():
    sports_len += 1
    lowered_job_key = base_job_key.lower()

    Men_Womens_Jobs[f"sports {lowered_job_key}"] = {}
    Men_Womens_Jobs[f"sports {lowered_job_key}"]["mens"] = f"{base_job_labels['mens']} رياضيون"
    Men_Womens_Jobs[f"sports {lowered_job_key}"]["womens"] = f"{base_job_labels['womens']} رياضيات"

    Men_Womens_Jobs[f"professional {lowered_job_key}"] = {}
    Men_Womens_Jobs[f"professional {lowered_job_key}"]["mens"] = f"{base_job_labels['mens']} محترفون"
    Men_Womens_Jobs[f"professional {lowered_job_key}"]["womens"] = f"{base_job_labels['womens']} محترفات"

    Men_Womens_Jobs[f"wheelchair {lowered_job_key}"] = {}
    Men_Womens_Jobs[f"wheelchair {lowered_job_key}"]["mens"] = f"{base_job_labels['mens']} على الكراسي المتحركة"
    Men_Womens_Jobs[f"wheelchair {lowered_job_key}"]["womens"] = f"{base_job_labels['womens']} على الكراسي المتحركة"


for cycling_event_key, cycling_event_label in new2019_cycling.items():
    lowered_event_key = cycling_event_key.lower()
    Men_Womens_Jobs[f"{lowered_event_key} cyclists"] = {
        "mens": f"دراجو {cycling_event_label}",
        "womens": f"دراجات {cycling_event_label}",
    }
    Men_Womens_Jobs[f"{lowered_event_key} winners"] = {
        "mens": f"فائزون في {cycling_event_label}",
        "womens": f"فائزات في {cycling_event_label}",
    }
    Men_Womens_Jobs[f"{lowered_event_key} stage winners"] = {
        "mens": f"فائزون في مراحل {cycling_event_label}",
        "womens": f"فائزات في مراحل {cycling_event_label}",
    }
    Nat_Before_Occ.append(f"{lowered_event_key} winners")
    Nat_Before_Occ.append(f"{lowered_event_key} stage winners")

Female_Jobs2 = {}

for film_category, film_gender_labels in FILMS_TYPE.items():
    Female_Jobs2[f"{film_category} actresses"] = f"ممثلات {film_gender_labels['womens']}"
Female_Jobs2["sportswomen"] = "رياضيات"


for sports_category, sports_labels in PLAYERS_TO_MEN_WOMENS_JOBS.items():
    Men_Womens_Jobs[sports_category] = sports_labels
for female_job_key, female_job_label in FEMALE_JOBS_TO.items():
    Female_Jobs2[female_job_key] = female_job_label


Female_Jobs["women in business"] = "سيدات أعمال"
Female_Jobs["women in politics"] = "سياسيات"
Female_Jobs["lesbians"] = "سحاقيات"
Female_Jobs["businesswomen"] = "سيدات أعمال"
Jobs_key = {}

for film, film_lab in Films_key_For_Jobs.items():

    film2 = film.lower()

    for key_o, key_lab in NNN_Keys_Films.items():
        Men_Womens_Jobs[key_o] = key_lab

        key_o2 = key_o.lower()
        oiuio = f"{film2} {key_o2}"
        Men_Womens_Jobs[oiuio] = {}

        Men_Womens_Jobs[oiuio]["mens"] = f"{key_lab['mens']} {film_lab}"

        Men_Womens_Jobs[oiuio]["womens"] = f"{key_lab['womens']} {film_lab}"

for job_category, job_titles in JOBS_PEOPLE.items():
    if job_titles["mens"] and job_titles["womens"]:

        # Books_table
        for book_key, book_label in Books_table.items():
            Men_Womens_Jobs[f"{book_key} {job_category}"] = {
                "mens": f"{job_titles['mens']} {book_label}",
                "womens": f"{job_titles['womens']} {book_label}",
            }

        # JOBS_TYPE
        for genre_key, genre_label in JOBS_TYPE.items():
            Men_Womens_Jobs[f"{genre_key} {job_category}"] = {
                "mens": f"{job_titles['mens']} {genre_label}",
                "womens": f"{job_titles['womens']} {genre_label}",
            }


for singer_category, singer_labels in MEN_WOMENS_SINGERS.items():
    Men_Womens_Jobs[singer_category] = singer_labels

    for style_key, style_labels in typi.items():
        Men_Womens_Jobs[f"{style_key} {singer_category}"] = {
            "mens": f"{MEN_WOMENS_SINGERS[singer_category]['mens']} {style_labels['mens']}",
            "womens": f"{MEN_WOMENS_SINGERS[singer_category]['womens']} {style_labels['womens']}",
        }

for job_key, gender_labels in Men_Womens_Jobs.items():

    Jobs_key_mens[job_key] = gender_labels["mens"]

    if gender_labels["womens"]:
        womens_Jobs_2017[job_key] = gender_labels["womens"]

for female_job_key, female_job_label in Female_Jobs2.items():
    Female_Jobs[female_job_key] = female_job_label

for job_key, job_label in Jobs_key_mens.items():
    if job_label:
        Jobs_key[job_key] = job_label

for female_job_key, female_job_label in Female_Jobs.items():
    lowered_female_job_key = female_job_key.lower()
    if female_job_label:
        Jobs_new[lowered_female_job_key] = female_job_label
        Jobs_key_womens[lowered_female_job_key] = female_job_label

Jobs_key_mens["men's footballers"] = "لاعبو كرة قدم رجالية"

for religious_key in RELIGIOUS_KEYS_PP:
    Nat_Before_Occ.append(religious_key)

for nationality_key, nationality_label in Nat_mens.items():
    lowered_nationality = nationality_key.lower()
    if nationality_label:
        Jobs_new[f"{lowered_nationality} people"] = f"{nationality_label}"

Jobs_new["people of the ottoman empire"] = "عثمانيون"

for job_key in Jobs_key.keys():
    Jobs_new[job_key.lower()] = Jobs_key[job_key]

len_print.data_len("jobs.py", {
    "Jobs_key_mens": Jobs_key_mens,
    "Jobs_key_womens": Jobs_key_womens,
    "womens_Jobs_2017": womens_Jobs_2017,
    "Female_Jobs": Female_Jobs,
    "Men_Womens_Jobs": Men_Womens_Jobs,
    "Nat_Before_Occ": Nat_Before_Occ,
    "Men_Womens_with_nato": Men_Womens_with_nato,
    "Jobs_new": Jobs_new,
    "Jobs_key": Jobs_key,
})

__all__ = [
    "Jobs_key_mens",
    "Jobs_key_womens",
    "womens_Jobs_2017",
    "Female_Jobs",
    "Men_Womens_Jobs",
    "Nat_Before_Occ",
    "Men_Womens_with_nato",
    "Jobs_new",
    "Jobs_key"
]
