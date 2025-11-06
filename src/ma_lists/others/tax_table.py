#!/usr/bin/python3
"""

"""
from ..utils.json_dir import open_json_file

tax_q = """
    SELECT DISTINCT #?item ?humanLabel
    #?ar
    #?page_en ?page_ar
    (concat('   "' , ?page_en , '":"' , ?page_ar  , '",')  as ?itemscds)
    WHERE {
    ?human wdt:P31 wd:Q16521.
    ?human wdt:P910 ?item .
    ?item wdt:P301 ?human.
    ?article schema:about ?item ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?page_en .
    ?article2 schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> ; schema:name ?page_ar .
    #FILTER NOT EXISTS {?article schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> . }.
    SERVICE wikibase:label {
        bd:serviceParam wikibase:language "ar,en" .
    }
    ?item rdfs:label ?ar .  FILTER((LANG(?ar)) = "ar")

        }
    #LIMIT 100
"""
# ---
Taxons_table = {}
Taxons = {}
Taxons2 = {}
Taxons3 = {}
# ---
# "brachiopods":"ذوات القوائم الذراعية",
# "waterbears":"دب الماء",
# "asterids":"",
# ---
Taxons = open_json_file("Taxons") or {}
# ---
Taxons2 = open_json_file("Taxons2") or {}
# ---
Taxons3 = open_json_file("Taxons3") or {}
# ---
Taxons.update(Taxons2)
Taxons.update(Taxons3)
# ---
Taxons_table.update(Taxons)
# ---
for tax, taxlab in Taxons.items():
    # typeTable_7["{} described in".format(tax)] = "{} وصفت في".format(taxlab)
    Taxons_table[f"{tax} of"] = taxlab
    # Fossil
    fossil_lab = f"{taxlab} أحفورية"
    Taxons_table[f"fossil {tax}"] = fossil_lab
    Taxons_table[f"fossil {tax} of"] = fossil_lab
# ---
for taxe, lab in Taxons2.items():
    # typeTable_7["{} described in".format(taxe)] = "{} وصفت في".format(lab)
    Taxons_table[f"{taxe} of"] = f"{lab} في"
# ---
del Taxons
del Taxons2
del Taxons3
