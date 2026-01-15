#!/usr/bin/python3
"""
python3 core8/pwb.py -m cProfile -s ncalls make/make_bots.matables_bots/bot.py

"""

from ...helps import len_print
from ...translations import (
    ALBUMS_TYPE,
    Jobs_new,
    typeTable,
    olympic_event_translations_type_tables,
)

olympic_event_translations: dict[str, str] = {
    "african games bronze medalists": "فائزون بميداليات برونزية في الألعاب الإفريقية",
    "african games competitors": "منافسون في الألعاب الإفريقية",
    "african games gold medalists": "فائزون بميداليات ذهبية في الألعاب الإفريقية",
    "african games medalists": "فائزون بميداليات الألعاب الإفريقية",
    "african games medallists": "فائزون بميداليات الألعاب الإفريقية",
    "african games silver medalists": "فائزون بميداليات فضية في الألعاب الإفريقية",
    "asian beach games bronze medalists": "فائزون بميداليات برونزية في دورة الألعاب الآسيوية الشاطئية",
    "asian beach games competitors": "منافسون في دورة الألعاب الآسيوية الشاطئية",
    "asian beach games gold medalists": "فائزون بميداليات ذهبية في دورة الألعاب الآسيوية الشاطئية",
    "asian beach games medalists": "فائزون بميداليات دورة الألعاب الآسيوية الشاطئية",
    "asian beach games medallists": "فائزون بميداليات دورة الألعاب الآسيوية الشاطئية",
    "asian beach games silver medalists": "فائزون بميداليات فضية في دورة الألعاب الآسيوية الشاطئية",
    "asian games bronze medalists": "فائزون بميداليات برونزية في الألعاب الآسيوية",
    "asian games competitors": "منافسون في الألعاب الآسيوية",
    "asian games gold medalists": "فائزون بميداليات ذهبية في الألعاب الآسيوية",
    "asian games medalists": "فائزون بميداليات الألعاب الآسيوية",
    "asian games medallists": "فائزون بميداليات الألعاب الآسيوية",
    "asian games silver medalists": "فائزون بميداليات فضية في الألعاب الآسيوية",
    "asian indoor games bronze medalists": "فائزون بميداليات برونزية في دورة الألعاب الآسيوية داخل الصالات",
    "asian indoor games competitors": "منافسون في دورة الألعاب الآسيوية داخل الصالات",
    "asian indoor games gold medalists": "فائزون بميداليات ذهبية في دورة الألعاب الآسيوية داخل الصالات",
    "asian indoor games medalists": "فائزون بميداليات دورة الألعاب الآسيوية داخل الصالات",
    "asian indoor games medallists": "فائزون بميداليات دورة الألعاب الآسيوية داخل الصالات",
    "asian indoor games silver medalists": "فائزون بميداليات فضية في دورة الألعاب الآسيوية داخل الصالات",
    "asian para games bronze medalists": "فائزون بميداليات برونزية في الألعاب البارالمبية الآسيوية",
    "asian para games competitors": "منافسون في الألعاب البارالمبية الآسيوية",
    "asian para games gold medalists": "فائزون بميداليات ذهبية في الألعاب البارالمبية الآسيوية",
    "asian para games medalists": "فائزون بميداليات الألعاب البارالمبية الآسيوية",
    "asian para games medallists": "فائزون بميداليات الألعاب البارالمبية الآسيوية",
    "asian para games silver medalists": "فائزون بميداليات فضية في الألعاب البارالمبية الآسيوية",
    "asian summer games bronze medalists": "فائزون بميداليات برونزية في الألعاب الآسيوية الصيفية",
    "asian summer games competitors": "منافسون في الألعاب الآسيوية الصيفية",
    "asian summer games gold medalists": "فائزون بميداليات ذهبية في الألعاب الآسيوية الصيفية",
    "asian summer games medalists": "فائزون بميداليات الألعاب الآسيوية الصيفية",
    "asian summer games medallists": "فائزون بميداليات الألعاب الآسيوية الصيفية",
    "asian summer games silver medalists": "فائزون بميداليات فضية في الألعاب الآسيوية الصيفية",
    "asian winter games bronze medalists": "فائزون بميداليات برونزية في الألعاب الآسيوية الشتوية",
    "asian winter games competitors": "منافسون في الألعاب الآسيوية الشتوية",
    "asian winter games gold medalists": "فائزون بميداليات ذهبية في الألعاب الآسيوية الشتوية",
    "asian winter games medalists": "فائزون بميداليات الألعاب الآسيوية الشتوية",
    "asian winter games medallists": "فائزون بميداليات الألعاب الآسيوية الشتوية",
    "asian winter games silver medalists": "فائزون بميداليات فضية في الألعاب الآسيوية الشتوية",
    "bolivarian games bronze medalists": "فائزون بميداليات برونزية في الألعاب البوليفارية",
    "bolivarian games competitors": "منافسون في الألعاب البوليفارية",
    "bolivarian games gold medalists": "فائزون بميداليات ذهبية في الألعاب البوليفارية",
    "bolivarian games medalists": "فائزون بميداليات الألعاب البوليفارية",
    "bolivarian games medallists": "فائزون بميداليات الألعاب البوليفارية",
    "bolivarian games silver medalists": "فائزون بميداليات فضية في الألعاب البوليفارية",
    "central american and caribbean games bronze medalists": "فائزون بميداليات برونزية في ألعاب أمريكا الوسطى والكاريبي",
    "central american and caribbean games competitors": "منافسون في ألعاب أمريكا الوسطى والكاريبي",
    "central american and caribbean games gold medalists": "فائزون بميداليات ذهبية في ألعاب أمريكا الوسطى والكاريبي",
    "central american and caribbean games medalists": "فائزون بميداليات ألعاب أمريكا الوسطى والكاريبي",
    "central american and caribbean games medallists": "فائزون بميداليات ألعاب أمريكا الوسطى والكاريبي",
    "central american and caribbean games silver medalists": "فائزون بميداليات فضية في ألعاب أمريكا الوسطى والكاريبي",
    "central american games bronze medalists": "فائزون بميداليات برونزية في ألعاب أمريكا الوسطى",
    "central american games competitors": "منافسون في ألعاب أمريكا الوسطى",
    "central american games gold medalists": "فائزون بميداليات ذهبية في ألعاب أمريكا الوسطى",
    "central american games medalists": "فائزون بميداليات ألعاب أمريكا الوسطى",
    "central american games medallists": "فائزون بميداليات ألعاب أمريكا الوسطى",
    "central american games silver medalists": "فائزون بميداليات فضية في ألعاب أمريكا الوسطى",
    "commonwealth games bronze medalists": "فائزون بميداليات برونزية في ألعاب الكومنولث",
    "commonwealth games competitors": "منافسون في ألعاب الكومنولث",
    "commonwealth games gold medalists": "فائزون بميداليات ذهبية في ألعاب الكومنولث",
    "commonwealth games medalists": "فائزون بميداليات ألعاب الكومنولث",
    "commonwealth games medallists": "فائزون بميداليات ألعاب الكومنولث",
    "commonwealth games silver medalists": "فائزون بميداليات فضية في ألعاب الكومنولث",
    "commonwealth youth games bronze medalists": "فائزون بميداليات برونزية في ألعاب الكومنولث الشبابية",
    "commonwealth youth games competitors": "منافسون في ألعاب الكومنولث الشبابية",
    "commonwealth youth games gold medalists": "فائزون بميداليات ذهبية في ألعاب الكومنولث الشبابية",
    "commonwealth youth games medalists": "فائزون بميداليات ألعاب الكومنولث الشبابية",
    "commonwealth youth games medallists": "فائزون بميداليات ألعاب الكومنولث الشبابية",
    "commonwealth youth games silver medalists": "فائزون بميداليات فضية في ألعاب الكومنولث الشبابية",
    "deaflympic games bronze medalists": "فائزون بميداليات برونزية في ألعاب ديفلمبياد",
    "deaflympic games competitors": "منافسون في ألعاب ديفلمبياد",
    "deaflympic games gold medalists": "فائزون بميداليات ذهبية في ألعاب ديفلمبياد",
    "deaflympic games medalists": "فائزون بميداليات ألعاب ديفلمبياد",
    "deaflympic games medallists": "فائزون بميداليات ألعاب ديفلمبياد",
    "deaflympic games silver medalists": "فائزون بميداليات فضية في ألعاب ديفلمبياد",
    "european games bronze medalists": "فائزون بميداليات برونزية في الألعاب الأوروبية",
    "european games competitors": "منافسون في الألعاب الأوروبية",
    "european games gold medalists": "فائزون بميداليات ذهبية في الألعاب الأوروبية",
    "european games medalists": "فائزون بميداليات الألعاب الأوروبية",
    "european games medallists": "فائزون بميداليات الألعاب الأوروبية",
    "european games silver medalists": "فائزون بميداليات فضية في الألعاب الأوروبية",
    "european youth olympic bronze medalists": "فائزون بميداليات برونزية في الألعاب الأولمبية الشبابية الأوروبية",
    "european youth olympic competitors": "منافسون في الألعاب الأولمبية الشبابية الأوروبية",
    "european youth olympic gold medalists": "فائزون بميداليات ذهبية في الألعاب الأولمبية الشبابية الأوروبية",
    "european youth olympic medalists": "فائزون بميداليات الألعاب الأولمبية الشبابية الأوروبية",
    "european youth olympic medallists": "فائزون بميداليات الألعاب الأولمبية الشبابية الأوروبية",
    "european youth olympic silver medalists": "فائزون بميداليات فضية في الألعاب الأولمبية الشبابية الأوروبية",
    "european youth olympic winter bronze medalists": "فائزون بميداليات برونزية في الألعاب الأولمبية الشبابية الأوروبية الشتوية",
    "european youth olympic winter competitors": "منافسون في الألعاب الأولمبية الشبابية الأوروبية الشتوية",
    "european youth olympic winter gold medalists": "فائزون بميداليات ذهبية في الألعاب الأولمبية الشبابية الأوروبية الشتوية",
    "european youth olympic winter medalists": "فائزون بميداليات الألعاب الأولمبية الشبابية الأوروبية الشتوية",
    "european youth olympic winter medallists": "فائزون بميداليات الألعاب الأولمبية الشبابية الأوروبية الشتوية",
    "european youth olympic winter silver medalists": "فائزون بميداليات فضية في الألعاب الأولمبية الشبابية الأوروبية الشتوية",
    "fis nordic world ski championships bronze medalists": "فائزون بميداليات برونزية في بطولة العالم للتزلج النوردي على الثلج",
    "fis nordic world ski championships competitors": "منافسون في بطولة العالم للتزلج النوردي على الثلج",
    "fis nordic world ski championships gold medalists": "فائزون بميداليات ذهبية في بطولة العالم للتزلج النوردي على الثلج",
    "fis nordic world ski championships medalists": "فائزون بميداليات بطولة العالم للتزلج النوردي على الثلج",
    "fis nordic world ski championships medallists": "فائزون بميداليات بطولة العالم للتزلج النوردي على الثلج",
    "fis nordic world ski championships silver medalists": "فائزون بميداليات فضية في بطولة العالم للتزلج النوردي على الثلج",
    "friendship games bronze medalists": "فائزون بميداليات برونزية في ألعاب الصداقة",
    "friendship games competitors": "منافسون في ألعاب الصداقة",
    "friendship games gold medalists": "فائزون بميداليات ذهبية في ألعاب الصداقة",
    "friendship games medalists": "فائزون بميداليات ألعاب الصداقة",
    "friendship games medallists": "فائزون بميداليات ألعاب الصداقة",
    "friendship games silver medalists": "فائزون بميداليات فضية في ألعاب الصداقة",
    "goodwill games bronze medalists": "فائزون بميداليات برونزية في ألعاب النوايا الحسنة",
    "goodwill games competitors": "منافسون في ألعاب النوايا الحسنة",
    "goodwill games gold medalists": "فائزون بميداليات ذهبية في ألعاب النوايا الحسنة",
    "goodwill games medalists": "فائزون بميداليات ألعاب النوايا الحسنة",
    "goodwill games medallists": "فائزون بميداليات ألعاب النوايا الحسنة",
    "goodwill games silver medalists": "فائزون بميداليات فضية في ألعاب النوايا الحسنة",
    "islamic solidarity games bronze medalists": "فائزون بميداليات برونزية في ألعاب التضامن الإسلامي",
    "islamic solidarity games competitors": "منافسون في ألعاب التضامن الإسلامي",
    "islamic solidarity games gold medalists": "فائزون بميداليات ذهبية في ألعاب التضامن الإسلامي",
    "islamic solidarity games medalists": "فائزون بميداليات ألعاب التضامن الإسلامي",
    "islamic solidarity games medallists": "فائزون بميداليات ألعاب التضامن الإسلامي",
    "islamic solidarity games silver medalists": "فائزون بميداليات فضية في ألعاب التضامن الإسلامي",
    "maccabiah games bronze medalists": "فائزون بميداليات برونزية في الألعاب المكابيه",
    "maccabiah games competitors": "منافسون في الألعاب المكابيه",
    "maccabiah games gold medalists": "فائزون بميداليات ذهبية في الألعاب المكابيه",
    "maccabiah games medalists": "فائزون بميداليات الألعاب المكابيه",
    "maccabiah games medallists": "فائزون بميداليات الألعاب المكابيه",
    "maccabiah games silver medalists": "فائزون بميداليات فضية في الألعاب المكابيه",
    "mediterranean games bronze medalists": "فائزون بميداليات برونزية في الألعاب المتوسطية",
    "mediterranean games competitors": "منافسون في الألعاب المتوسطية",
    "mediterranean games gold medalists": "فائزون بميداليات ذهبية في الألعاب المتوسطية",
    "mediterranean games medalists": "فائزون بميداليات الألعاب المتوسطية",
    "mediterranean games medallists": "فائزون بميداليات الألعاب المتوسطية",
    "mediterranean games silver medalists": "فائزون بميداليات فضية في الألعاب المتوسطية",
    "micronesian games bronze medalists": "فائزون بميداليات برونزية في الألعاب الميكرونيزية",
    "micronesian games competitors": "منافسون في الألعاب الميكرونيزية",
    "micronesian games gold medalists": "فائزون بميداليات ذهبية في الألعاب الميكرونيزية",
    "micronesian games medalists": "فائزون بميداليات الألعاب الميكرونيزية",
    "micronesian games medallists": "فائزون بميداليات الألعاب الميكرونيزية",
    "micronesian games silver medalists": "فائزون بميداليات فضية في الألعاب الميكرونيزية",
    "military world games bronze medalists": "فائزون بميداليات برونزية في دورة الألعاب العسكرية",
    "military world games competitors": "منافسون في دورة الألعاب العسكرية",
    "military world games gold medalists": "فائزون بميداليات ذهبية في دورة الألعاب العسكرية",
    "military world games medalists": "فائزون بميداليات دورة الألعاب العسكرية",
    "military world games medallists": "فائزون بميداليات دورة الألعاب العسكرية",
    "military world games silver medalists": "فائزون بميداليات فضية في دورة الألعاب العسكرية",
    "olympic bronze medalists": "فائزون بميداليات برونزية أولمبية",
    "olympic competitors": "منافسون أولمبيون",
    "olympic gold medalists": "فائزون بميداليات ذهبية أولمبية",
    "olympic medalists": "فائزون بميداليات أولمبية",
    "olympic silver medalists": "فائزون بميداليات فضية أولمبية",
    "olympics competitors": "منافسون أولمبيون",
    "olympics medalists": "فائزون بميداليات أولمبية",
    "olympics medallists": "فائزون بميداليات أولمبية",
    "pan american games bronze medalists": "فائزون بميداليات برونزية في دورة الألعاب الأمريكية",
    "pan american games competitors": "منافسون في دورة الألعاب الأمريكية",
    "pan american games gold medalists": "فائزون بميداليات ذهبية في دورة الألعاب الأمريكية",
    "pan american games medalists": "فائزون بميداليات دورة الألعاب الأمريكية",
    "pan american games medallists": "فائزون بميداليات دورة الألعاب الأمريكية",
    "pan american games silver medalists": "فائزون بميداليات فضية في دورة الألعاب الأمريكية",
    "pan arab games bronze medalists": "فائزون بميداليات برونزية في دورة الألعاب العربية",
    "pan arab games competitors": "منافسون في دورة الألعاب العربية",
    "pan arab games gold medalists": "فائزون بميداليات ذهبية في دورة الألعاب العربية",
    "pan arab games medalists": "فائزون بميداليات دورة الألعاب العربية",
    "pan arab games medallists": "فائزون بميداليات دورة الألعاب العربية",
    "pan arab games silver medalists": "فائزون بميداليات فضية في دورة الألعاب العربية",
    "pan asian games bronze medalists": "فائزون بميداليات برونزية في دورة الألعاب الآسيوية",
    "pan asian games competitors": "منافسون في دورة الألعاب الآسيوية",
    "pan asian games gold medalists": "فائزون بميداليات ذهبية في دورة الألعاب الآسيوية",
    "pan asian games medalists": "فائزون بميداليات دورة الألعاب الآسيوية",
    "pan asian games medallists": "فائزون بميداليات دورة الألعاب الآسيوية",
    "pan asian games silver medalists": "فائزون بميداليات فضية في دورة الألعاب الآسيوية",
    "paralympic bronze medalists": "فائزون بميداليات برونزية في الألعاب البارالمبية",
    "paralympic competitors": "منافسون في الألعاب البارالمبية",
    "paralympic gold medalists": "فائزون بميداليات ذهبية في الألعاب البارالمبية",
    "paralympic medalists": "فائزون بميداليات الألعاب البارالمبية",
    "paralympic medallists": "فائزون بميداليات الألعاب البارالمبية",
    "paralympic silver medalists": "فائزون بميداليات فضية في الألعاب البارالمبية",
    "paralympics bronze medalists": "فائزون بميداليات برونزية في الألعاب البارالمبية",
    "paralympics competitors": "منافسون في الألعاب البارالمبية",
    "paralympics gold medalists": "فائزون بميداليات ذهبية في الألعاب البارالمبية",
    "paralympics medalists": "فائزون بميداليات الألعاب البارالمبية",
    "paralympics medallists": "فائزون بميداليات الألعاب البارالمبية",
    "paralympics silver medalists": "فائزون بميداليات فضية في الألعاب البارالمبية",
    "parapan american games bronze medalists": "فائزون بميداليات برونزية في ألعاب بارابان الأمريكية",
    "parapan american games competitors": "منافسون في ألعاب بارابان الأمريكية",
    "parapan american games gold medalists": "فائزون بميداليات ذهبية في ألعاب بارابان الأمريكية",
    "parapan american games medalists": "فائزون بميداليات ألعاب بارابان الأمريكية",
    "parapan american games medallists": "فائزون بميداليات ألعاب بارابان الأمريكية",
    "parapan american games silver medalists": "فائزون بميداليات فضية في ألعاب بارابان الأمريكية",
    "sea games bronze medalists": "فائزون بميداليات برونزية في ألعاب البحر",
    "sea games competitors": "منافسون في ألعاب البحر",
    "sea games gold medalists": "فائزون بميداليات ذهبية في ألعاب البحر",
    "sea games medalists": "فائزون بميداليات ألعاب البحر",
    "sea games medallists": "فائزون بميداليات ألعاب البحر",
    "sea games silver medalists": "فائزون بميداليات فضية في ألعاب البحر",
    "south american games bronze medalists": "فائزون بميداليات برونزية في ألعاب أمريكا الجنوبية",
    "south american games competitors": "منافسون في ألعاب أمريكا الجنوبية",
    "south american games gold medalists": "فائزون بميداليات ذهبية في ألعاب أمريكا الجنوبية",
    "south american games medalists": "فائزون بميداليات ألعاب أمريكا الجنوبية",
    "south american games medallists": "فائزون بميداليات ألعاب أمريكا الجنوبية",
    "south american games silver medalists": "فائزون بميداليات فضية في ألعاب أمريكا الجنوبية",
    "south asian beach games bronze medalists": "فائزون بميداليات برونزية في دورة ألعاب جنوب أسيا الشاطئية",
    "south asian beach games competitors": "منافسون في دورة ألعاب جنوب أسيا الشاطئية",
    "south asian beach games gold medalists": "فائزون بميداليات ذهبية في دورة ألعاب جنوب أسيا الشاطئية",
    "south asian beach games medalists": "فائزون بميداليات دورة ألعاب جنوب أسيا الشاطئية",
    "south asian beach games medallists": "فائزون بميداليات دورة ألعاب جنوب أسيا الشاطئية",
    "south asian beach games silver medalists": "فائزون بميداليات فضية في دورة ألعاب جنوب أسيا الشاطئية",
    "south asian games bronze medalists": "فائزون بميداليات برونزية في ألعاب جنوب أسيا",
    "south asian games competitors": "منافسون في ألعاب جنوب أسيا",
    "south asian games gold medalists": "فائزون بميداليات ذهبية في ألعاب جنوب أسيا",
    "south asian games medalists": "فائزون بميداليات ألعاب جنوب أسيا",
    "south asian games medallists": "فائزون بميداليات ألعاب جنوب أسيا",
    "south asian games silver medalists": "فائزون بميداليات فضية في ألعاب جنوب أسيا",
    "south asian winter games bronze medalists": "فائزون بميداليات برونزية في ألعاب جنوب آسيا الشتوية",
    "south asian winter games competitors": "منافسون في ألعاب جنوب آسيا الشتوية",
    "south asian winter games gold medalists": "فائزون بميداليات ذهبية في ألعاب جنوب آسيا الشتوية",
    "south asian winter games medalists": "فائزون بميداليات ألعاب جنوب آسيا الشتوية",
    "south asian winter games medallists": "فائزون بميداليات ألعاب جنوب آسيا الشتوية",
    "south asian winter games silver medalists": "فائزون بميداليات فضية في ألعاب جنوب آسيا الشتوية",
    "southeast asian games bronze medalists": "فائزون بميداليات برونزية في ألعاب جنوب شرق آسيا",
    "southeast asian games competitors": "منافسون في ألعاب جنوب شرق آسيا",
    "southeast asian games gold medalists": "فائزون بميداليات ذهبية في ألعاب جنوب شرق آسيا",
    "southeast asian games medalists": "فائزون بميداليات ألعاب جنوب شرق آسيا",
    "southeast asian games medallists": "فائزون بميداليات ألعاب جنوب شرق آسيا",
    "southeast asian games silver medalists": "فائزون بميداليات فضية في ألعاب جنوب شرق آسيا",
    "summer olympics bronze medalists": "فائزون بميداليات برونزية في الألعاب الأولمبية الصيفية",
    "summer olympics competitors": "منافسون في الألعاب الأولمبية الصيفية",
    "summer olympics gold medalists": "فائزون بميداليات ذهبية في الألعاب الأولمبية الصيفية",
    "summer olympics medalists": "فائزون بميداليات الألعاب الأولمبية الصيفية",
    "summer olympics medallists": "فائزون بميداليات الألعاب الأولمبية الصيفية",
    "summer olympics silver medalists": "فائزون بميداليات فضية في الألعاب الأولمبية الصيفية",
    "summer universiade bronze medalists": "فائزون بميداليات برونزية في الألعاب الجامعية الصيفية",
    "summer universiade competitors": "منافسون في الألعاب الجامعية الصيفية",
    "summer universiade gold medalists": "فائزون بميداليات ذهبية في الألعاب الجامعية الصيفية",
    "summer universiade medalists": "فائزون بميداليات الألعاب الجامعية الصيفية",
    "summer universiade medallists": "فائزون بميداليات الألعاب الجامعية الصيفية",
    "summer universiade silver medalists": "فائزون بميداليات فضية في الألعاب الجامعية الصيفية",
    "summer world university games bronze medalists": "فائزون بميداليات برونزية في ألعاب الجامعات العالمية الصيفية",
    "summer world university games competitors": "منافسون في ألعاب الجامعات العالمية الصيفية",
    "summer world university games gold medalists": "فائزون بميداليات ذهبية في ألعاب الجامعات العالمية الصيفية",
    "summer world university games medalists": "فائزون بميداليات ألعاب الجامعات العالمية الصيفية",
    "summer world university games medallists": "فائزون بميداليات ألعاب الجامعات العالمية الصيفية",
    "summer world university games silver medalists": "فائزون بميداليات فضية في ألعاب الجامعات العالمية الصيفية",
    "the universiade bronze medalists": "فائزون بميداليات برونزية في الألعاب الجامعية",
    "the universiade competitors": "منافسون في الألعاب الجامعية",
    "the universiade gold medalists": "فائزون بميداليات ذهبية في الألعاب الجامعية",
    "the universiade medalists": "فائزون بميداليات الألعاب الجامعية",
    "the universiade medallists": "فائزون بميداليات الألعاب الجامعية",
    "the universiade silver medalists": "فائزون بميداليات فضية في الألعاب الجامعية",
    "universiade bronze medalists": "فائزون بميداليات برونزية في الألعاب الجامعية",
    "universiade competitors": "منافسون في الألعاب الجامعية",
    "universiade gold medalists": "فائزون بميداليات ذهبية في الألعاب الجامعية",
    "universiade medalists": "فائزون بميداليات الألعاب الجامعية",
    "universiade medallists": "فائزون بميداليات الألعاب الجامعية",
    "universiade silver medalists": "فائزون بميداليات فضية في الألعاب الجامعية",
    "winter olympics bronze medalists": "فائزون بميداليات برونزية في الألعاب الأولمبية الشتوية",
    "winter olympics competitors": "منافسون في الألعاب الأولمبية الشتوية",
    "winter olympics gold medalists": "فائزون بميداليات ذهبية في الألعاب الأولمبية الشتوية",
    "winter olympics medalists": "فائزون بميداليات الألعاب الأولمبية الشتوية",
    "winter olympics medallists": "فائزون بميداليات الألعاب الأولمبية الشتوية",
    "winter olympics silver medalists": "فائزون بميداليات فضية في الألعاب الأولمبية الشتوية",
    "winter universiade bronze medalists": "فائزون بميداليات برونزية في الألعاب الجامعية الشتوية",
    "winter universiade competitors": "منافسون في الألعاب الجامعية الشتوية",
    "winter universiade gold medalists": "فائزون بميداليات ذهبية في الألعاب الجامعية الشتوية",
    "winter universiade medalists": "فائزون بميداليات الألعاب الجامعية الشتوية",
    "winter universiade medallists": "فائزون بميداليات الألعاب الجامعية الشتوية",
    "winter universiade silver medalists": "فائزون بميداليات فضية في الألعاب الجامعية الشتوية",
    "winter world university games bronze medalists": "فائزون بميداليات برونزية في ألعاب الجامعات العالمية الشتوية",
    "winter world university games competitors": "منافسون في ألعاب الجامعات العالمية الشتوية",
    "winter world university games gold medalists": "فائزون بميداليات ذهبية في ألعاب الجامعات العالمية الشتوية",
    "winter world university games medalists": "فائزون بميداليات ألعاب الجامعات العالمية الشتوية",
    "winter world university games medallists": "فائزون بميداليات ألعاب الجامعات العالمية الشتوية",
    "winter world university games silver medalists": "فائزون بميداليات فضية في ألعاب الجامعات العالمية الشتوية",
    "world athletics indoor championships bronze medalists": "فائزون بميداليات برونزية في بطولة العالم لألعاب القوى داخل الصالات",
    "world athletics indoor championships competitors": "منافسون في بطولة العالم لألعاب القوى داخل الصالات",
    "world athletics indoor championships gold medalists": "فائزون بميداليات ذهبية في بطولة العالم لألعاب القوى داخل الصالات",
    "world athletics indoor championships medalists": "فائزون بميداليات بطولة العالم لألعاب القوى داخل الصالات",
    "world athletics indoor championships medallists": "فائزون بميداليات بطولة العالم لألعاب القوى داخل الصالات",
    "world athletics indoor championships silver medalists": "فائزون بميداليات فضية في بطولة العالم لألعاب القوى داخل الصالات",
    "world championships bronze medalists": "فائزون بميداليات برونزية في بطولات العالم",
    "world championships competitors": "منافسون في بطولات العالم",
    "world championships gold medalists": "فائزون بميداليات ذهبية في بطولات العالم",
    "world championships medalists": "فائزون بميداليات بطولات العالم",
    "world championships medallists": "فائزون بميداليات بطولات العالم",
    "world championships silver medalists": "فائزون بميداليات فضية في بطولات العالم",
    "youth olympic bronze medalists": "فائزون بميداليات برونزية في الألعاب الأولمبية الشبابية",
    "youth olympic competitors": "منافسون في الألعاب الأولمبية الشبابية",
    "youth olympic gold medalists": "فائزون بميداليات ذهبية في الألعاب الأولمبية الشبابية",
    "youth olympic medalists": "فائزون بميداليات الألعاب الأولمبية الشبابية",
    "youth olympic medallists": "فائزون بميداليات الألعاب الأولمبية الشبابية",
    "youth olympic silver medalists": "فائزون بميداليات فضية في الألعاب الأولمبية الشبابية",
    "youth olympics bronze medalists": "فائزون بميداليات برونزية في الألعاب الأولمبية الشبابية",
    "youth olympics competitors": "منافسون في الألعاب الأولمبية الشبابية",
    "youth olympics games bronze medalists": "فائزون بميداليات برونزية في الألعاب الأولمبية الشبابية",
    "youth olympics games competitors": "منافسون في الألعاب الأولمبية الشبابية",
    "youth olympics games gold medalists": "فائزون بميداليات ذهبية في الألعاب الأولمبية الشبابية",
    "youth olympics games medalists": "فائزون بميداليات الألعاب الأولمبية الشبابية",
    "youth olympics games medallists": "فائزون بميداليات الألعاب الأولمبية الشبابية",
    "youth olympics games silver medalists": "فائزون بميداليات فضية في الألعاب الأولمبية الشبابية",
    "youth olympics gold medalists": "فائزون بميداليات ذهبية في الألعاب الأولمبية الشبابية",
    "youth olympics medalists": "فائزون بميداليات الألعاب الأولمبية الشبابية",
    "youth olympics medallists": "فائزون بميداليات الألعاب الأولمبية الشبابية",
    "youth olympics silver medalists": "فائزون بميداليات فضية في الألعاب الأولمبية الشبابية"
}

typeTable_7: dict[str, str] = {
    "air force": "قوات جوية",
    "airlines accidents": "حوادث طيران",
    "aviation accident": "حوادث طيران",
    "aviation accidents": "حوادث طيران",
    "design institutions": "مؤسسات تصميم",
    "distance education institutions": "مؤسسات تعليم عن بعد",
    "executed-burning": "أعدموا شنقاً",
    "executed-decapitation": "أعدموا بقطع الرأس",
    "executed-firearm": "أعدموا بسلاح ناري",
    "executed-hanging": "أعدموا حرقاً",
    "executions": "إعدامات",
    "people executed by": "أشخاص أعدموا من قبل",
    "people executed-by-burning": "أشخاص أعدموا شنقاً",
    "people executed-by-decapitation": "أشخاص أعدموا بقطع الرأس",
    "people executed-by-firearm": "أشخاص أعدموا بسلاح ناري",
    "people executed-by-hanging": "أشخاص أعدموا حرقاً",
    "railway accident": "حوادث سكك حديد",
    "railway accidents": "حوادث سكك حديد",
    "road accidents": "حوادث طرق",
    "transport accident": "حوادث نقل",
    "transport accidents": "حوادث نقل",
    "transport disasters": "كوارث نقل"
}


def _create_pp_prefix(albums_typies: dict[str, str]) -> dict[str, str]:
    Pp_Priffix = {
        " memorials": "نصب {} التذكارية",
        " video albums": "ألبومات فيديو {}",
        " albums": "ألبومات {}",
        " cabinet": "مجلس وزراء {}",
        " administration cabinet members": "أعضاء مجلس وزراء إدارة {}",
        " administration personnel": "موظفو إدارة {}",
        " executive office": "مكتب {} التنفيذي",
    }

    for io in albums_typies:
        Pp_Priffix[f"{io} albums"] = "ألبومات %s {}" % albums_typies[io]

    return Pp_Priffix


def _make_players_keys(Add_ar_in: dict[str, str]) -> dict:
    players_keys = {}
    players_keys["women"] = "المرأة"

    players_keys.update({x.lower(): v for x, v in Jobs_new.items() if v})

    players_keys.update({x.lower(): v for x, v in typeTable_7.items()})

    players_keys["national sports teams"] = "منتخبات رياضية وطنية"
    players_keys["people"] = "أشخاص"

    players_keys.update(Add_ar_in)
    return players_keys


Add_ar_in = dict(olympic_event_translations)
players_new_keys = _make_players_keys(Add_ar_in)
Pp_Priffix = _create_pp_prefix(ALBUMS_TYPE)


cash_2022 = {
    "category:japan golf tour golfers": "تصنيف:لاعبو بطولة اليابان للغولف",
    "category:asian tour golfers": "تصنيف:لاعبو بطولة آسيا للغولف",
    "category:european tour golfers": "تصنيف:لاعبو بطولة أوروبا للغولف",
    "category:ladies european tour golfers": "تصنيف:لاعبات بطولة أوروبا للغولف للسيدات",
}
# ---
All_P17 = {}
Films_O_TT = {}

Table_for_frist_word = {
    "olympic_event_translations_type_tables": olympic_event_translations_type_tables,
    "typetable": typeTable,
    "Films_O_TT": Films_O_TT,
    "New_players": players_new_keys,
}


def add_to_new_players(en: str, ar: str) -> None:
    """Add a new English/Arabic player label pair to the cache."""
    if not en or not ar:
        return

    if not isinstance(en, str) or not isinstance(ar, str):
        return

    players_new_keys[en] = ar


def add_to_Films_O_TT(en: str, ar: str) -> None:
    """Add a new English/Arabic player label pair to the cache."""
    if not en or not ar:
        return

    if not isinstance(en, str) or not isinstance(ar, str):
        return

    Films_O_TT[en] = ar


len_print.data_len(
    "make_bots.matables_bots/bot.py",
    {
        "players_new_keys": players_new_keys,  # 99517
        "All_P17": All_P17,
    },
)

__all__ = [
    "Table_for_frist_word",
    "cash_2022",
    "Films_O_TT",
    "Add_ar_in",
    "players_new_keys",
    "add_to_new_players",
    "add_to_Films_O_TT",
    "All_P17",
    "Pp_Priffix",
]
