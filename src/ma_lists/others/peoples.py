#!/usr/bin/python3
"""
from .peoples import People_key

SELECT DISTINCT #?cat
#?ar  ?humanLabel
#?page_en ?page_ar
#(concat('   "' , ?page_en , '":"' , ?ar  , '",')  as ?itemscds)
(concat('   "' , ?page_en , '":"' , ?page_ar  , '",')  as ?itemscds)
WHERE {
    ?human wdt:P31 wd:Q5.#
    #?human wdt:P31/wdt:P279* wd:Q515.#
    #?human wdt:P31/wdt:P279* wd:Q486972.
    ?human wdt:P910 ?cat .
    #?cat wdt:P301 ?human.
    {?cat rdfs:label ?page_ar .  FILTER((LANG(?page_ar)) = "ar") } UNION {
    ?article2 schema:about ?cat ; schema:isPartOf <https://ar.wikipedia.org/> ; schema:name ?page_ar . }
    #OPTIONAL { ?sitelink schema:about ?cat . ?sitelink schema:isPartOf <https://ar.wikipedia.org/> }
    #OPTIONAL { ?sitelink schema:about ?cat . ?sitelink schema:inLanguage "ar" }
    # but select items with no such article
    #FILTER (!BOUND(?sitelink))
    ?article schema:about ?cat ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?page_en .
    SERVICE wikibase:label {
        bd:serviceParam wikibase:language "ar,en" .
    }
    }
LIMIT 10000
"""
# ---
import sys

from ..utils.json_dir import open_json_file
from ...helps import len_print


# ---
People_key = {}
# ---
People_key = open_json_file("peoples") or {}
# ---
# json.dump(People_key, open(f"{Dir2}/jsons/peoples.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
# ---
length_stats = {
    "People_key": sys.getsizeof(People_key),
}
# ---

len_print.lenth_pri("peoples.py", length_stats, Max=1000)
# ---
