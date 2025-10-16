#!/usr/bin/python3
"""
محاولة إيجاد تسميات من ويكي بيانات
"""

import re
import json

#
import requests
from .. import printe
import sys

# ---
pprint = {1: False}


def Priiint(text):
    if pprint[1]:
        printe.output(text)


# ---
# https://en.wikipedia.org/wiki/Special:ApiSandbox#action=query&format=json&prop=langlinks&generator=search&utf8=1&lllang=ar&gsrsearch=Osceola%2C%20Fond%20du%20Lac%20County%2C%20Wisconsin&gsrnamespace=0&gsrwhat=text
v56 = {
    "action": "query",
    "format": "json",
    "prop": "langlinks",
    "generator": "search",
    "utf8": 1,
    "lllang": "ar",
    "gsrsearch": "osceola, fond du lac county, wisconsin",
    "gsrnamespace": "0",
    "gsrwhat": "text",
}
# ---
Cashens = {}
# ---
#
api_url = "https://www.wikidata.org/w/api.php"
session_wd = {1: False}
# ---
en_literes = "[abcdefghijklmnopqrstuvwxyz]"
ar_literes = "[ابتثجحخدذرزسشصضطظعغفقكلمنهوية]"


def find_name_from_wikidata(text, lang, Local=False):
    # ---
    if "nowikidata" in sys.argv or "local" in sys.argv or Local:
        return {}
    # ---
    if text in Cashens:
        return {text: Cashens[text]}
    # ---
    if not session_wd[1]:
        session_wd[1] = requests.Session()
    # ---
    # printe.output(text)
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
    json1 = {}
    printe.output(f"find_name_from_wikidata: '{text}'")
    # ---
    try:
        check = session_wd[1].post(api_url, data=params, timeout=10)
        json1 = json.loads(check.text)
    except Exception as e:
        printe.output(f"<<lightred>> find_name_from_wikidata can't session.post. {e}")
    Priiint(json1)
    tab = json1["search"] if json1 and json1["search"] else []
    La = {}
    # ---
    Priiint(len(tab))
    if len(tab) != 0:
        for x in tab:
            Priiint(x)
            if x["label"] and x["match"] and x["match"]["text"]:
                if x["match"]["type"] != "alias":
                    La[x["match"]["text"]] = x["label"]
    # ---
    if La:
        printe.output(La)
    # ---
    Cashens[text] = La
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
    # ---


tase = """
fort worth, texas
technical universities and colleges
genoa
the early modern era
corvettes
the sword
football cup competitions
south asia
law alumni
the future
populated coastal places
business
overseas france
disease-related deaths
tribes
lgbt rights
the midwestern united states
arabs
market towns
world rowing championships medalists
athletics (track and field)
social groups
historic sites
arts and letters
isotopes
video gaming
gender
hemiptera
the san francisco bay area
orange-nassau
the peerage
by oblast
colonizer and former colony
screenplays
endemic fauna of
fellows of
event venues
non-profit organizations
the north sea
forest lawn memorial park (hollywood hills)
relations of
by state or union territory
abu dhabi
newfoundland and labrador
ships built
chicago
municipalities
invertebrates
medical and health organisations
ports and harbours
the mediterranean sea
the year winners
sindh
representatives
protostomes
for deletion
music alumni
computer-related introductions
victoria (australia)
broadcasting
films scored
disasters
controversies
mayors of places
songs written
taxa named
terrorism
people educated
fame inductees
the new york metropolitan area
sport
by district
"""
# ---
# for t in tase.split("\n"):
# if t.strip() :
# find_name_from_wikidata(t.strip())


def mainae():
    # ---
    pprint[1] = True
    # python3 core8/pwb.py make/s test Osceola, Fond du Lac County, Wisconsin
    # python3 core8/pwb.py make/s test kristianstad
    if sys.argv and "test" in sys.argv:
        Olist = sys.argv
        Olist.remove(sys.argv[0])
        Olist.remove("test")
        # ---
        Name = " ".join(Olist)
        printe.output(f'Name: "{Name}"')
        find_name_from_wikidata(Name, "en")
    # ---


if __name__ == "__main__":
    mainae()
# ---
