#!/usr/bin/python3
""" """

from typing import Dict

from ...helps import len_print
from .games_labs import SUMMER_WINTER_GAMES

olympic_event_translations: Dict[str, str] = {
    "universiade competitors": "منافسون في الألعاب الجامعية",
    "universiade medalists": "فائزون بميداليات الألعاب الجامعية",
    "olympic medalists": "فائزون بميداليات أولمبية",
    "olympic competitors": "منافسون أولمبيون",
    "olympic gold medalists": "فائزون بميداليات ذهبية أولمبية",
    "olympic silver medalists": "فائزون بميداليات فضية أولمبية",
    "olympic bronze medalists": "فائزون بميداليات برونزية أولمبية",
    "paralympic competitors": "منافسون بارالمبيون",
    "commonwealth games gold medalists": "فائزون بميداليات ذهبية في ألعاب الكومنولث",
    # "winter olympics competitors": "منافسون في الألعاب الأولمبية الشتوية",
    "winter olympics medalists": "فائزون بميداليات أولمبية شتوية",
    "summer olympics medalists": "فائزون بميداليات أولمبية صيفية",
    # "summer olympics competitors": "منافسون في الألعاب الأولمبية الصيفية",
    "winter olympics competitors": "منافسون أولمبيون شتويون",
    "summer olympics competitors": "منافسون أولمبيون صيفيون",
    "olympics competitors": "منافسون أولمبيون",
}

medalists_type: Dict[str, str] = {
    "%s competitors": "منافسون في %s",
    "%s medallists": "فائزون بميداليات %s",
    "%s medalists": "فائزون بميداليات %s",
    "%s gold medalists": "فائزون بميداليات ذهبية في %s",
    "%s silver medalists": "فائزون بميداليات فضية في %s",
    "%s bronze medalists": "فائزون بميداليات برونزية في %s",
}

for tty, tty_lab in medalists_type.items():
    for k, v in SUMMER_WINTER_GAMES.items():
        olympic_event_translations[tty % k] = tty_lab % v
    olympic_event_translations[tty % "world athletics indoor championships"] = tty_lab % "بطولة العالم لألعاب القوى داخل الصالات"

olympic_event_translations["olympics medallists"] = "فائزون بميداليات أولمبية"
olympic_event_translations["olympics medalists"] = "فائزون بميداليات أولمبية"


olympic_event_translations["fis nordic world ski championships medalists"] = "فائزون بميداليات بطولة العالم للتزلج النوردي على الثلج"

len_print.data_len("sports/olympicss_data.py", {"olympics": olympic_event_translations})
