#!/usr/bin/python3
"""

"""

import re
from typing import Dict

from .open_url import open_url_text
from ...helps.log import logger
from ... import app_settings, printe

TEAM_LOOKUP_CACHE: Dict[str, str] = {}


def kooora_player(english_name: str) -> str:
    encoded_name = english_name.replace(" ", "+")
    # ---
    # if re.sub(r"\p{L}" , "" ,  EnName ) != EnName  :
    # printe.output("unicode: %s " % EnName)
    # EnName = ""
    # ---
    # eee = "https://www.kooora.com/?searchplayer=%s&showplayers=true" % EnName2
    eee = f"https://kooora.com/?searchplayer={encoded_name}&showplayers=true"
    # ---
    if english_name == "" or not app_settings.enable_kooora:
        return ""
    # ---
    lowercase_name = english_name.lower()
    if lowercase_name in TEAM_LOOKUP_CACHE:
        return TEAM_LOOKUP_CACHE[lowercase_name]
    # ---
    printe.output(f'*kooora_player EnName : "{english_name}" ')
    response_text = open_url_text(eee)
    # ---
    arabic_label = ""
    if response_text:
        if "var teams_list = new Array(" in response_text:
            response_text = response_text.split("var teams_list = new Array(")[1]
            response_text = response_text.split("0,0 );")[0]
            # ---
            response_text = re.sub(r'[\n\r"]', "", response_text)
            # tas = re.sub(r"\n" , "" ,  tas)
            # tas = re.sub(r"\r" , "" ,  tas)
            # tas = re.sub(r"\"" , "" ,  tas)
            # ---
            team_fields = response_text.split(",")
            # ---
            logger.debug(team_fields)
            # ---
            if len(team_fields) == 8:
                # ---
                matched_name = team_fields[4]
                # ---
                if lowercase_name.replace(".", "") == matched_name.lower().replace(".", ""):
                    arabic_label = team_fields[5]
                else:
                    printe.output(
                        f'*kooora_player EnName:"{english_name}" != entest:"{matched_name}" , '
                        f'tas4[5]:"{team_fields[5]}" '
                    )
                    logger.debug("====\n" + "\n".join(team_fields) + "====")

                # ---
                if arabic_label:
                    # ---
                    printe.output(f'*kooora_player arlabel:"{arabic_label}". ')
            else:
                logger.debug(len(team_fields))
    TEAM_LOOKUP_CACHE[lowercase_name] = arabic_label
    # ---
    return arabic_label


def kooora_team(english_name: str) -> str:
    # ---
    encoded_name = english_name.replace(" ", "+")
    # ---
    if english_name.lower() == "israel":
        return "إسرائيل"
    # ---
    # eee = "https://www.kooora.com/?searchplayer=%s&showplayers=true" % EnName2
    eee = f"https://kooora.com/?searchteam={encoded_name}&searchcountry=&showteams=3"
    eee = f"https://goalzz.com/?searchteam={encoded_name}&searchcountry=&showteams=3"
    # ---
    if english_name == "" or not app_settings.enable_kooora:
        return ""
    # ---
    lowercase_name = english_name.lower()
    if TEAM_LOOKUP_CACHE.get(lowercase_name):
        return TEAM_LOOKUP_CACHE.get(lowercase_name, "")
    # ---
    if lowercase_name in TEAM_LOOKUP_CACHE:
        return TEAM_LOOKUP_CACHE[lowercase_name]
    # ---
    logger.debug(f'*kooora_team EnName : "{english_name}" ')
    # ---
    response_text = open_url_text(eee)
    # ---
    arabic_label = ""
    # ---
    if not response_text:
        return ""
    # ---
    if "var teams_list = new Array(" in response_text:
        response_text = response_text.split("var teams_list = new Array(")[1]
        response_text = response_text.split("0,0 );")[0]
        # ---
        response_text = re.sub(r'[\n\r"]', "", response_text)
        # ---
        team_fields = response_text.split(",")  # 38471,1,8,5,"العربي","العربي","الكويت",
        # ---
        logger.debug(team_fields)
        # ---
        if len(team_fields) == 8:
            # ---
            matched_name = team_fields[4]
            # ---
            if lowercase_name == matched_name.lower():
                arabic_label = team_fields[5]
            else:
                printe.output(
                    f'*kooora_team EnName:"{english_name}" != entest:"{matched_name}" , '
                    f'tas4[5]:"{team_fields[5]}" '
                )
                logger.debug("====\n" + "\n".join(team_fields) + "====")
            # ---
            if arabic_label:
                # ---
                printe.output(f'*kooora_team arlabel:"{arabic_label}". ')
        else:
            logger.debug(len(team_fields))
    # ---
    TEAM_LOOKUP_CACHE[lowercase_name] = arabic_label
    # ---
    return arabic_label
