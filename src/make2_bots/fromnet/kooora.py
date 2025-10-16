#!/usr/bin/python3
"""

"""

import re
import sys
from typing import Dict
from ... import printe
from .open_url import open_url_text


Teamse_ko_done: Dict[str, str] = {}
pprindt: Dict[int, bool] = {1: False}


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
    tas = open_url_text(eee)
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
    tas = open_url_text(eee)
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
            elif pprindt[1]:
                printe.output(len(tas4))
    # ---
    Teamse_ko_done[EnName.lower()] = arlabel
    # ---
    return arlabel
