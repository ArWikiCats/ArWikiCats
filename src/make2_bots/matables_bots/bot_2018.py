#!/usr/bin/python3
r"""

Usage:
from ..make2_bots.matables_bots import bot_2018
# bot_2018.pop_All_2018.get()


from ..make2_bots.matables_bots.bot_2018 import pop_All_2018
from ..make2_bots.matables_bots.bot_2018 import get_pop_All_18, Add_to_pop_All_18 # get_pop_All_18(key, "") #Add_to_pop_All_18(tab)


# pop_All_2018\.get\((.*?), (.*?)\)
# get_pop_All_18($1, $2)

or

# pop_All_2018\.get
# get_pop_All_18

"""

import sys
from typing import Dict, Any
from ..helps import len_print
from ..ma_lists import summer_winter_games
from ..ma_lists import pf_keys2
from ..ma_lists import New_P17_Finall
from ..ma_lists import films_mslslat_tab
from ..ma_lists import Jobs_new, Jobs_key
from ..ma_lists import Sports_Keys_For_Label
from ..ma_lists import By_table

from ..ma_lists import Teams_new
from ..ma_lists import pop_All_2018

pop_All_2018["country"] = "البلد"


def Add_to_pop_All_18(tab: Dict[str, str]) -> None:
    for key, lab in tab.items():
        pop_All_2018[key] = lab


def get_pop_All_18(key: str, va: str = "") -> str:
    return pop_All_2018.get(key, va)


for gg, gg_lab in pf_keys2.items():
    gg2 = gg.lower()
    if not pop_All_2018.get(gg2):
        pop_All_2018[gg2] = gg_lab

for pla in Jobs_new:
    pla2 = pla.lower()
    if Jobs_new[pla]:
        if not pop_All_2018.get(pla2):
            pop_All_2018[pla2] = Jobs_new[pla]
for pla in Jobs_key:
    pla2 = pla.lower()
    if Jobs_key[pla]:
        if not pop_All_2018.get(pla2):
            pop_All_2018[pla2] = Jobs_key[pla]

for cyi in films_mslslat_tab:
    cyi2 = cyi.lower()
    if not pop_All_2018.get(cyi2):
        pop_All_2018[cyi2] = films_mslslat_tab[cyi]

for by in By_table:
    by2 = by.lower()
    if By_table[by]:
        if not pop_All_2018.get(by2):
            pop_All_2018[by2] = By_table[by]

for paa, taba in Teams_new.items():
    paa2 = paa.lower()
    if taba:
        if not pop_All_2018.get(paa2):
            pop_All_2018[paa2] = taba

for xo in list(New_P17_Finall):
    xo2 = xo.lower()
    if not pop_All_2018.get(xo2):
        pop_All_2018[xo2] = New_P17_Finall[xo]

for paa in Sports_Keys_For_Label:
    paa2 = paa.lower()
    if Sports_Keys_For_Label[paa]:
        if not pop_All_2018.get(paa2):
            pop_All_2018[paa2] = Sports_Keys_For_Label[paa]

# pop_All_2018["conflicts"] = "نزاعات"
pop_All_2018["by country"] = "حسب البلد"
pop_All_2018["in"] = "في"
pop_All_2018["films"] = "أفلام"
pop_All_2018["decades"] = "عقود"
pop_All_2018["women"] = "المرأة"
pop_All_2018["women in"] = "المرأة في"

pop_All_2018["medalists"] = "فائزون بميداليات"
pop_All_2018["gold medalists"] = "فائزون بميداليات ذهبية"
pop_All_2018["silver medalists"] = "فائزون بميداليات فضية"
pop_All_2018["bronze medalists"] = "فائزون بميداليات برونزية"

pop_All_2018["kingdom of"] = "مملكة"
pop_All_2018["kingdom-of"] = "مملكة"

olympicss: Dict[str, str] = {
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
        olympicss[tty % k] = tty_lab % v
    olympicss[tty % "world athletics indoor championships"] = tty_lab % "بطولة العالم لألعاب القوى داخل الصالات"
    olympicss[tty % "olympics"] = tty_lab % "أولمبية"

    # olympicss[tty % " games"] = tty_lab % "في "


olympicss["fis nordic world ski championships medalists"] = "فائزون بميداليات بطولة العالم للتزلج النوردي على الثلج"

for olmp, olmp_lab in olympicss.items():
    pop_All_2018[olmp] = olmp_lab

Lenth: Dict[str, int] = {}
Lenth["pop_All_2018"] = sys.getsizeof(pop_All_2018)
len_print.lenth_pri("make2_bots.matables_bots/bot_2018.py", Lenth, Max=10)
