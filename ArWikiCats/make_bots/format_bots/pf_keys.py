#!/usr/bin/python3
"""
!
"""
import re
from typing import Dict

from ...translations import New_Company

# Cache for compiled regex patterns
_change_key_compiled = {}

# Cache for compiled regex patterns
_change_key2_compiled = {}

CHANGE_KEY_MAPPINGS: Dict[str, str] = {
    # TODO: find why this used in the code
    "players in": "playerss in",

    "bodies of water" : "bodies-of-water",
    "canadian football" : "canadian-football",
    "’": "'",

    " – men's tournament": " mens tournament",
    " – women's tournament": " womens tournament",

    " - women's tournament": " womens tournament",
    " - men's tournament": " mens tournament",

    "publishers (people)": "publisherspeople",
    "football (soccer)": "football",
    "us open (tennis)": "us open tennis",
    "(tennis)": "tennis",

    "adaptations of works": "adaptations-of-works",
    # "people of ottoman empire" :"people-of-ottoman-empire",
    # "sentenced to death" :"sentenced-to-death",
    "africa cup of nations": "africa cup-of-nations",
    "health care": "healthcare",
    "child soldiers": "child-soldiers",
    "labour and social security": "labour-and-social security",
    "accidents and incidents": "accidents-and-incidents",
    "for member of parliament": "for member-of-parliament",
    "in northern ireland": "in northern-ireland",
    "manufactured in": "manufactured-in",
    "manufactured by": "manufactured-by",
    "association football afc": "association-football afc",
    "imprisoned in": "imprisoned-in",
    "launched in": "launched-in",
    "launched by": "launched-by",
    "transferred from": "transferred-from",
    "built in": "built-in",
    "built by": "built-by",
    "caribbean people": "caribbeans people",
    "world war ii": "world-war-ii",
    "world war i": "world-war-i",
    "killed in action": "killed-in-action",
    "city of liverpool f.c.": "city-of-liverpool f.c.",
    "medallists": "medalists",
    "saudi arabian": "saudiarabian",
    "athletes (track and field)": "track and field athletes",
    "world championships in athletics": "world championships-in-athletics",
    "murderers of children": "murderersofchildren",
    "prisoners of conscience": "prisoners-of-conscience",
    "convicted of murder by ": "convicted-of-murder-by ",
    "convicted-of-murder by ": "convicted-of-murder-by ",
    "university of reading": "university-of-reading",
    "university of science and technology": "university-of-science and technology",
    "governance of policing": "governance policing",
    # "university of " :"university-of ",
    "university of technology": "university-of-technology",
    "refusing to convert to christianity": "refusing-to-convert-to-christianity",
    "refusing to convert to islam": "refusing-to-convert-to-islam",
    # "austria-hungary" :"austriahungary",
    "convicted of murder": "convicted-of-murder",
    # "university of" :"university-of",
    "presidential elections": "presidential-elections",
    "presidential primaries": "presidential-primaries",
    "general elections": "general-elections",
    "local elections": "local-elections",
    "early modern": "early-modern",
    "sports culture": "sprts culture",
    "by firearm in": "by-firearm-in",
    "military equipment": "military-equipment",
    "military terminology": "military-terminology",
    "shot dead by law enforcement officers": "shot dead-by-law enforcement officers",
    "west coast of united states": "west coast-of-united states",
    "future elections": "future-elections",
    "sports media": "sports-media",
    "by car bomb": "by-car-bomb",
    "television series endings": "television series-endings",
    "television series debuts": "television series-debuts",
    "television miniseries endings": "television miniseries-endings",
    "television miniseries debuts": "television miniseries-debuts",
    "television films endings": "television films-endings",
    "television films debuts": "television films-debuts",
    "basedon non-": "basedon non ",
    "television seasons": "television-seasons",
    "ministers for": "ministers-for",
    "sport ministers": "sport-ministers",
    "sports ministers": "sports-ministers",
    "british hong kong": "british-hong-kong",
    "scholars of islam": "scholars-of-islam",
    # "sports events" : "sports-events",
    "united states house of representatives": "united states house-of-representatives",
    "sports events": "sports-events",
    "war of ": "war-of ",
    # "paintings by" : "paintings-by",
    "sportspeople": "sports-people",
    "architecture schools": "architecture-schools",
    " labor ": " labour ",
    "elections, ": "elections ",
    "harrow on hill": "harrow-on-hill",
    "city of london": "city-of-london",
    "executions by": "executions in",
    "african american": "africanamerican",
    "african-american": "africanamerican",
    "in sports in": "in-sports-in",
    # "ancient romans" :"ancient-romans",
    "ancient roman": "ancient-roman",
    "ancient greek": "ancient-greek",
    "ancient macedonian": "ancient-macedonian",
    "in sport in": "in-sport-in",
    "kingdom of": "kingdom-of",
    "national register of historic places": "national-register-of-historic-places",
    # "executed by guillotine" : "executed-guillotine",
    "executed by burning": "executed-burning",
    "executed by hanging": "executed-hanging",
    "executed by decapitation": "executed-decapitation",
    "executed by firearm": "executed-firearm",
    # " executed by " :" executed-by ",
    "emirate of": "emirate-of",
    "republic of": "republic-of",
    "duchy of": "duchy-of",
    "states of": "states-of",
    "comedy-": "comedy ",
    "domain of": "domain-of",
    "crown of": "crown-of",
    "county of": "county-of",
    "protectorate of": "protectorate-of",
    "canton of": "canton-of",
    "march of": "march-of",
    "margraviate of": "margraviate-of",
    "colony of": "colony-of",
    # "province of" :"province-of",
    "realm of": "realm-of",
    "isle of": "isle-of",
    "viceroyalty of": "viceroyalty-of",

    "labor": "labour",
}

for x in New_Company:
    CHANGE_KEY_MAPPINGS[f"defunct {x} companies"] = f"defunct-{x}-companies"


def change_key_mappings_replacements(category):
    # Apply CHANGE_KEY_MAPPINGS regex patterns (cached)
    for chk, chk_lab in CHANGE_KEY_MAPPINGS.items():
        key = (chk, chk_lab)
        if key not in _change_key_compiled:
            _change_key_compiled[key] = {
                "0": re.compile(rf"^category\:{chk} ", flags=re.IGNORECASE),
                "1": re.compile(rf"^{chk} ", flags=re.IGNORECASE),
                "2": re.compile(rf" {chk} ", flags=re.IGNORECASE),
                "3": re.compile(rf" {chk}$", flags=re.IGNORECASE),
                "4": re.compile(rf"category\:{chk} ", flags=re.IGNORECASE),
                # "5": re.compile(rf"\b{chk}\b", flags=re.IGNORECASE),
                "5": re.compile(rf"(?<!\w){chk}(?!\w)", flags=re.IGNORECASE),
            }

        patterns = _change_key_compiled[key]
        category = patterns["0"].sub(f"category:{chk_lab} ", category)
        category = patterns["1"].sub(f"{chk_lab} ", category)
        category = patterns["2"].sub(f" {chk_lab} ", category)
        category = patterns["3"].sub(f" {chk_lab}", category)
        category = patterns["4"].sub(f"category:{chk_lab} ", category)
        category = patterns["5"].sub(chk_lab, category)

    return category


CHANGE_KEY_SECONDARY: Dict[str, str] = {
    "charter airlines": "charter-airlines",
    " for blind ": " for-blind ",
    " for deaf ": " for-deaf ",
    "term of Iranian Majlis": "Iranian Majlis",
    "orgadnisation for prohibition of chemical weapons": "opcw",
    "country of residence": "country-of-residence",
    "serbia and montenegro": "serbia-and-montenegro",
    " at 2": " in 2",
    "game of thrones": "game-of-thrones",
    "green party of quebec": "green party-of-quebec",
    "libertarian party of canada": "libertarian party-of-canada",
    "declarations of independence": "declarations-of-independence",
    "united states declaration of independence": "united-states-declaration-of-independence",
    "house of commons": "house-of-commons",
    "house of representatives": "house-of-representatives",
    " at 1": " in 1",
    " - men's tournament": " mens tournament",
    " - women's tournament": " womens tournament",
    "historians of philosophy": "historians-of-philosophy",
    " at ": " in ",
    " remade in ": " remadein ",
    " based on ": " basedon ",

    r"^tour de ": "tour of ",
    r"^women's footballers ": "female footballers ",
    r"^women's footballers": "female footballers",
    r"^men\’s events ": "mensvents",

    r" women's footballers$": " female footballers",
    r" executed people$": " executed-people",
    r" for deafblind$": " for-deafblind",
    r" for blind$": " for-blind",
    r" for deaf$": " for-deaf",
}


def change_key_secondary_replacements(category):

    # Apply CHANGE_KEY_SECONDARY regex patterns (cached)
    for chk2, chk2_lab in CHANGE_KEY_SECONDARY.items():

        if chk2 not in _change_key2_compiled:
            _change_key2_compiled[chk2] = re.compile(chk2, flags=re.IGNORECASE)

        category = _change_key2_compiled[chk2].sub(chk2_lab, category)

    return category
