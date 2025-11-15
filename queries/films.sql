SELECT DISTINCT (CONCAT("\"", ?en, "\"") AS ?ss) (CONCAT(":") AS ?ss2) (CONCAT("  \"", ?ar, "\",") AS ?ss3) WHERE {
  ?item (wdt:P31/(wdt:P279*)) wd:Q201658;
    wdt:P910 ?cat.
  ?cat rdfs:label ?en.
  FILTER((LANG(?en)) = "en")
  ?cat rdfs:label ?ar.
  FILTER((LANG(?ar)) = "ar")
  OPTIONAL {
    ?item rdfs:label ?itemaa.
    FILTER((LANG(?itemaa)) = "ar")
  }
  OPTIONAL {
    ?cat rdfs:label ?catar.
    FILTER((LANG(?catar)) = "ar")
  }
}
