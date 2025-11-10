#!/usr/bin/python3
r"""

Usage:
from ...matables_bots import bot_2018
# bot_2018.pop_All_2018.get()


from ...matables_bots.bot_2018 import pop_All_2018
from ...matables_bots.bot_2018 import get_pop_All_18, Add_to_pop_All_18 # get_pop_All_18(key, "") #Add_to_pop_All_18(tab)


# pop_All_2018\.get\((.*?), (.*?)\)
# get_pop_All_18($1, $2)

or

# pop_All_2018\.get
# get_pop_All_18

"""

from typing import Dict
from ...helps import len_print
from ...ma_lists import pop_All_2018_bot


pop_All_2018 = pop_All_2018_bot.load_pop_All_2018()


def Add_to_pop_All_18(tab: Dict[str, str]) -> None:
    for key, lab in tab.items():
        pop_All_2018[key] = lab


def get_pop_All_18(key: str, default: str = "") -> str:
    return pop_All_2018.get(key, default)


len_print.data_len("make2_bots.matables_bots/bot_2018.py", {
    "pop_All_2018" : pop_All_2018
})
