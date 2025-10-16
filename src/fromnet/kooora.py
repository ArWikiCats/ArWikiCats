#!/usr/bin/python3
"""

محاولة إيجاد تسميات من كوووورة

python3 core8/pwb.py make/kooora test Al-Arabi SC


python3 core8/pwb.py make/testmain testfile:koo

Usage:

from ..fromnet import kooora
# kooora.kooora_team(entitle)
# kooora.kooora_player(entitle)

"""

import re
import sys
from typing import Dict, Any
from .. import printe

try:
    from API import open_url
except BaseException:
    open_url = None
# ---
Teamse_ko_done: Dict[str, str] = {}
pprindt: Dict[int, bool] = {1: False}


def gettheurl(url: str) -> str:
    return open_url.open_the_url(url) if open_url else ""


def log_kooora(t: str, dj: str) -> None:
    try:
        with open(dj, "a", encoding="utf-8") as f:
            f.write(t)

    except BaseException:
        print("log_kooora Error writing")


def kooora_player(EnName: str) -> str:
    EnName2 = EnName.replace(" ", "+")
    # ---
    # if re.sub(r"\p{L}" , "" ,  EnName ) != EnName  :
    # printe.output("unicode: %s " % EnName)
    # EnName = ""
    # ---
    # eee = "https://www.kooora.com/?searchplayer=%s&showplayers=true" % EnName2
    eee = f"https://kooora.com/?searchplayer={EnName2}&showplayers=true"
    # ---
    if EnName == "" or "nokooora" in sys.argv:
        return ""
    # ---
    if EnName.lower() in Teamse_ko_done:
        return Teamse_ko_done[EnName.lower()]
    # ---
    printe.output(f'*kooora_player EnName : "{EnName}" ')
    tas = gettheurl(eee)
    # ---
    arlabel = ""
    if tas:
        if "var teams_list = new Array(" in tas:
            tas = tas.split("var teams_list = new Array(")[1]
            tas = tas.split("0,0 );")[0]
            # ---
            tas = re.sub(r'[\n\r"]', "", tas)
            # tas = re.sub(r"\n" , "" ,  tas)
            # tas = re.sub(r"\r" , "" ,  tas)
            # tas = re.sub(r"\"" , "" ,  tas)
            # ---
            tas4 = tas.split(",")
            # ---
            if pprindt[1]:
                printe.output(tas4)
            # ---
            if len(tas4) == 8:
                # ---
                entest = tas4[4]
                # ---
                if EnName.lower().replace(".", "") == entest.lower().replace(".", ""):
                    arlabel = tas4[5]
                else:
                    printe.output(f'*kooora_player EnName:"{EnName}" != entest:"{entest}" , tas4[5]:"{tas4[5]}" ')
                    if pprindt[1]:
                        printe.output("====\n" + "\n".join(tas4) + "====")

                # ---
                if arlabel:
                    # ---
                    printe.output(f'*kooora_player arlabel:"{arlabel}". ')
                    lline = f'\n"{EnName.lower()}":"{arlabel}",'
                    log_kooora(lline, "make2_new/0kooora_player.log.csv")
            elif pprindt[1]:
                printe.output(len(tas4))
    Teamse_ko_done[EnName.lower()] = arlabel
    # ---
    return arlabel


def kooora_team(EnName: str, Local: bool = True) -> str:
    EnName2 = EnName.replace(" ", "+")
    # ---
    if EnName.lower() == "israel":
        return "إسرائيل"
    # ---
    if Local is True:
        return ""
    # ---
    # eee = "https://www.kooora.com/?searchplayer=%s&showplayers=true" % EnName2
    eee = f"https://kooora.com/?searchteam={EnName2}&searchcountry=&showteams=3"
    eee = f"https://goalzz.com/?searchteam={EnName2}&searchcountry=&showteams=3"
    # ---
    if EnName == "" or "nokooora" in sys.argv or "local" in sys.argv:
        return ""
    # ---
    if Teamse_ko_done.get(EnName.lower()):
        return Teamse_ko_done.get(EnName.lower(), "")
    # ---
    if EnName.lower() in Teamse_ko_done:
        return Teamse_ko_done[EnName.lower()]
    # ---
    if pprindt[1]:
        printe.output(f'*kooora_team EnName : "{EnName}" ')
    # ---
    tas = gettheurl(eee)
    # ---
    arlabel = ""
    if tas:
        if "var teams_list = new Array(" in tas:
            tas = tas.split("var teams_list = new Array(")[1]
            tas = tas.split("0,0 );")[0]
            # ---
            tas = re.sub(r'[\n\r"]', "", tas)
            # ---
            tas4 = tas.split(",")  # 38471,1,8,5,"العربي","العربي","الكويت",
            # ---
            if pprindt[1]:
                printe.output(tas4)
            # ---
            if len(tas4) == 8:
                # ---
                entest = tas4[4]
                # ---
                if EnName.lower() == entest.lower():
                    arlabel = tas4[5]
                else:
                    printe.output(f'*kooora_team EnName:"{EnName}" != entest:"{entest}" , tas4[5]:"{tas4[5]}" ')
                    if pprindt[1]:
                        printe.output("====\n" + "\n".join(tas4) + "====")
                # ---
                if arlabel:
                    # ---
                    printe.output(f'*kooora_team arlabel:"{arlabel}". ')
                    lline = f'\n"{EnName.lower()}":"{arlabel}",'
                    log_kooora(lline, "make2_new/0kooora_team.log.csv")
            elif pprindt[1]:
                printe.output(len(tas4))
    # ---
    Teamse_ko_done[EnName.lower()] = arlabel
    # ---
    return arlabel


def main() -> None:
    # ---
    pprindt[1] = True
    # python3 core8/pwb.py make/kooora test Osceola, Fond du Lac County, Wisconsin
    # python3 core8/pwb.py make/kooora test kristianstad
    # ---
    if sys.argv:
        if "team" in sys.argv:
            Olist = sys.argv
            Olist.remove(sys.argv[0])
            Olist.remove("team")
            # ---
            Name = " ".join(Olist)
            printe.output(f'Name: "{Name}"')
            kooora_team(Name)
        # python3 core8/pwb.py make/kooora player Lasse Nilsson
        elif "player" in sys.argv:
            Olist = sys.argv
            Olist.remove(sys.argv[0])
            Olist.remove("player")
            # ---
            Name = " ".join(Olist)
            printe.output(f'Name: "{Name}"')
            kooora_player(Name)
    # ---


if __name__ == "__main__":
    main()
