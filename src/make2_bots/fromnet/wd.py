#!/usr/bin/python3
"""
محاولة إيجاد تسميات من ويكي بيانات
"""

import re
import sys

from ... import printe
from .open_url import open_url_json

PRINT_PREFERENCES = {1: False}


def debug_print(text):
    if PRINT_PREFERENCES[1]:
        printe.output(text)


WIKIDATA_CACHE = {}
# ---
api_url = "https://www.wikidata.org/w/api.php"
# ---
en_literes = "[abcdefghijklmnopqrstuvwxyz]"
ar_literes = "[ابتثجحخدذرزسشصضطظعغفقكلمنهوية]"


def find_name_from_wikidata(text, lang, Local=False):
    # ---
    if "nowikidata" in sys.argv or "local" in sys.argv or Local:
        return {}
    # ---
    if text in WIKIDATA_CACHE:
        return {text: WIKIDATA_CACHE[text]}
    # ---
    params = {
        "action": "wbsearchentities",
        "format": "json",
        "search": text,
        "language": lang,
        "strictlanguage": 1,
        "type": "item",
        "limit": "1",
        # "props": "url",
        "utf8": 1,
    }
    # ---
    json1 = open_url_json(api_url, data=params)
    # ---
    printe.output(f"find_name_from_wikidata: '{text}'")
    # ---
    tab = json1["search"] if json1 and json1["search"] else []
    La = {}
    # ---
    for x in tab:
        if x["label"] and x["match"] and x["match"]["text"]:
            if x["match"]["type"] != "alias":
                La[x["match"]["text"]] = x["label"]
    # ---
    if La:
        printe.output(La)
    # ---
    WIKIDATA_CACHE[text] = La
    # ---
    La2 = {}
    # ---
    for tf, tf_lab in La.items():
        # ---
        if re.sub(en_literes, "", tf_lab, flags=re.IGNORECASE) != tf_lab:
            continue
        # ---
        if re.sub(ar_literes, "", tf_lab, flags=re.IGNORECASE) == tf_lab:
            continue
        # ---
        La2[tf] = tf_lab
    # ---
    return La2
