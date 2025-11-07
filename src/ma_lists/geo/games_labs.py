#!/usr/bin/python3
"""

from __future__ import annotations

from .games_labs import summer_winter_tabs, summer_winter_games

"""
summer_winter_tabs = {}

summer_winter_games = {
    "african games" : "الألعاب الإفريقية",
    "asian beach games" : "دورة الألعاب الآسيوية الشاطئية",
    "asian games" : "الألعاب الآسيوية",
    "asian para games" : "دورة الألعاب الآسيوية البارالمبية",
    "asian summer games" : "الألعاب الآسيوية الصيفية",
    "asian winter games" : "الألعاب الآسيوية الشتوية",
    "bolivarian games" : "الألعاب البوليفارية",
    "central american and caribbean games" : "ألعاب أمريكا الوسطى والكاريبي",
    "central american games" : "ألعاب أمريكا الوسطى",
    "commonwealth games" : "ألعاب الكومنولث",
    "commonwealth youth games" : "ألعاب الكومنولث الشبابية",
    "european games" : "الألعاب الأوروبية",
    "european youth olympic winter" : "الألعاب الأولمبية الشبابية الأوروبية الشتوية",
    "european youth olympic" : "الألعاب الأولمبية الشبابية الأوروبية",
    "fis nordic world ski championships" : "بطولة العالم للتزلج النوردي على الثلج",
    "friendship games" : "ألعاب الصداقة",
    "goodwill games" : "ألعاب النوايا الحسنة",
    "islamic solidarity games" : "ألعاب التضامن الإسلامي",
    "maccabiah games" : "الألعاب المكابيه",
    "mediterranean games" : "الألعاب المتوسطية",
    "micronesian games" : "الألعاب الميكرونيزية",
    "military world games" : "دورة الألعاب العسكرية",
    "asian indoor games" : "دورة الألعاب الآسيوية داخل الصالات",
    "pan american games" : "دورة الألعاب الأمريكية",
    "pan arab games" : "دورة الألعاب العربية",
    "pan asian games" : "دورة الألعاب الآسيوية",
    "paralympic" : "الألعاب البارالمبية",
    "paralympics" : "الألعاب البارالمبية",
    "parapan american games" : "ألعاب بارابان الأمريكية",
    "sea games" : "ألعاب البحر",
    "south american games" : "ألعاب أمريكا الجنوبية",
    "south asian beach games" : "دورة ألعاب جنوب أسيا الشاطئية",
    "south asian games" : "ألعاب جنوب أسيا",
    "south asian winter games" : "ألعاب جنوب آسيا الشتوية",
    "southeast asian games" : "ألعاب جنوب شرق آسيا",
    "summer olympics" : "الألعاب الأولمبية الصيفية",
    "summer universiade" : "الألعاب الجامعية الصيفية",
    "summer world university games" : "ألعاب الجامعات العالمية الصيفية",
    "the universiade" : "الألعاب الجامعية",
    "universiade" : "الألعاب الجامعية",
    "winter olympics" : "الألعاب الأولمبية الشتوية",
    "winter universiade" : "الألعاب الجامعية الشتوية",
    "winter world university games" : "ألعاب الجامعات العالمية الشتوية",
    "world championships" : "بطولات العالم",
    # "world games" : "",
    "youth olympic" : "الألعاب الأولمبية الشبابية",
    "youth olympics games" : "الألعاب الأولمبية الشبابية",
    "youth olympics" : "الألعاب الأولمبية الشبابية",
    "deaflympic games" : "ألعاب ديفلمبياد",
}

seasonal_game_labels: dict[str, str] = {}

BASE_GAME_LABELS = {
    "african games" : "الألعاب الإفريقية",
    "all-africa games" : "ألعاب عموم إفريقيا",
    "asian games" : "الألعاب الآسيوية",
    "central american games" : "ألعاب أمريكا الوسطى",
    "commonwealth games" : "دورة ألعاب الكومنولث",
    "deaflympic games" : "ألعاب ديفلمبياد",
    "european youth olympic winter" : "الألعاب الأولمبية الشبابية الأوروبية الشتوية",
    "european youth olympic" : "الألعاب الأولمبية الشبابية الأوروبية",
    "jeux de la francophonie" : "الألعاب الفرانكوفونية",
    "olympic games" : "الألعاب الأولمبية",
    "olympics" : "الألعاب الأولمبية",
    "paralympics games" : "الألعاب البارالمبية",
    "south american games" : "ألعاب أمريكا الجنوبية",
    "universiade" : "الألعاب الجامعية",
    "world games" : "دورة الألعاب العالمية",
    "youth olympic games" : "الألعاب الأولمبية الشبابية",
    "youth olympics" : "الألعاب الأولمبية الشبابية",
}

seasonal_game_labels.update(summer_winter_games)

for base_game_key, base_game_label in BASE_GAME_LABELS.items():
    seasonal_game_labels[base_game_key] = base_game_label
    # ---
    seasonal_game_labels[f"winter {base_game_key}"] = (
        f"{base_game_label} الشتوية"
    )
    seasonal_game_labels[f"summer {base_game_key}"] = (
        f"{base_game_label} الصيفية"
    )
    seasonal_game_labels[f"west {base_game_key}"] = (
        f"{base_game_label} الغربية"
    )

GAME_CATEGORY_LABELS = {
    "competitions" : "منافسات",
    "events" : "أحداث",
    "festival" : "مهرجانات",
    "bids" : "عروض",
    "templates" : "قوالب",
}

for game_key, game_label in seasonal_game_labels.items():
    summer_winter_tabs[game_key] = game_label
    for category_key, category_label in GAME_CATEGORY_LABELS.items():
        category_entry_key = f"{game_key} {category_key}"
        category_entry_label = f"{category_label} {game_label}"
        summer_winter_tabs[category_entry_key] = category_entry_label

# --- backwards compatibility -------------------------------------------------
pop_Summer = seasonal_game_labels
Params = BASE_GAME_LABELS
Game_s = GAME_CATEGORY_LABELS
