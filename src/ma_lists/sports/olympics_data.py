#!/usr/bin/python3
"""

"""

from typing import Dict
from ...helps import len_print
from .games_labs import summer_winter_games

olympics: Dict[str, str] = {
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
    "%s gold medalists": "فائزون بميداليات ذهبية %s",
    "%s silver medalists": "فائزون بميداليات فضية %s",
    "%s bronze medalists": "فائزون بميداليات برونزية %s",
}

for tty, tty_lab in medalists_type.items():
    for k, v in summer_winter_games.items():
        olympics[tty % k] = tty_lab % v
    olympics[tty % "world athletics indoor championships"] = tty_lab % "بطولة العالم لألعاب القوى داخل الصالات"
    olympics[tty % "olympics"] = tty_lab % "أولمبية"

    # olympics[tty % " games"] = tty_lab % "في "


olympics["fis nordic world ski championships medalists"] = "فائزون بميداليات بطولة العالم للتزلج النوردي على الثلج"

len_print.data_len("sports/olympicss_data.py", {
    "olympics" : olympics
})
