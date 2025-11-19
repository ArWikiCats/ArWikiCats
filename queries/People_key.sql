
SELECT DISTINCT (CONCAT("   \"", ?page_en, "\":\"", ?page_ar, "\",") AS ?itemscds) WHERE {
  ?human wdt:P31 wd:Q5;
         wdt:P910 ?cat.
  #{
  #?cat rdfs:label ?page_ar.
  #FILTER((LANG(?page_ar)) = "ar")
  #} UNION {
  ?article2 schema:about ?cat;
            schema:isPartOf <https://ar.wikipedia.org/>;
            schema:name ?page_ar.
  #}
  ?article schema:about ?cat;
           schema:isPartOf <https://en.wikipedia.org/>;
           schema:name ?page_en.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en". }
  FILTER(STRSTARTS(STR(?page_en), "Category"))
}
LIMIT 10000
