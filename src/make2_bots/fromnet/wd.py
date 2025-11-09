#!/usr/bin/python3
"""
"""

import re
from typing import Dict

from ... import printe
from .open_url import open_url_json

WIKIDATA_CACHE: Dict[str, Dict[str, str]] = {}
# ---
api_url = "https://www.wikidata.org/w/api.php"
# ---
ENGLISH_LETTER_PATTERN = "[abcdefghijklmnopqrstuvwxyz]"
ARABIC_LETTER_PATTERN = "[ابتثجحخدذرزسشصضطظعغفقكلمنهوية]"


def find_name_from_wikidata(text: str, lang: str) -> Dict[str, str]:
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
    json1 = open_url_json(api_url, params=params)
    # ---
    printe.output(f"find_name_from_wikidata: '{text}'")
    # ---
    search_results = json1["search"] if json1 and json1["search"] else []
    label_map = {}
    # ---
    for entry in search_results:
        if entry["label"] and entry["match"] and entry["match"]["text"]:
            if entry["match"]["type"] != "alias":
                label_map[entry["match"]["text"]] = entry["label"]
    # ---
    if label_map:
        printe.output(label_map)
    # ---
    WIKIDATA_CACHE[text] = label_map
    # ---
    arabic_labels = {}
    # ---
    for matched_text, label in label_map.items():
        # ---
        if re.sub(ENGLISH_LETTER_PATTERN, "", label, flags=re.IGNORECASE) != label:
            continue
        # ---
        if re.sub(ARABIC_LETTER_PATTERN, "", label, flags=re.IGNORECASE) == label:
            continue
        # ---
        arabic_labels[matched_text] = label
    # ---
    return arabic_labels
