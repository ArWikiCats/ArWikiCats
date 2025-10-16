#!/usr/bin/python3
"""

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

pop_Summer = {}

Params = {
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

pop_Summer.update(summer_winter_games)

for para, para_lab in Params.items():
    pop_Summer[para] = para_lab
    # ---
    pop_Summer[f"winter {para}"] = f"{para_lab} الشتوية"
    pop_Summer[f"summer {para}"] = f"{para_lab} الصيفية"
    pop_Summer[f"west {para}"] = f"{para_lab} الغربية"

Game_s = {
    "competitions" : "منافسات",
    "events" : "أحداث",
    "festival" : "مهرجانات",
    "bids" : "عروض",
    "templates" : "قوالب",
}

for po_3, lab in pop_Summer.items():
    summer_winter_tabs[po_3] = lab
    for g_s, g_s_lab in Game_s.items():
        G_la = f"{po_3} {g_s}"
        G_label = f"{g_s_lab} {lab}"
        summer_winter_tabs[G_la] = G_label
