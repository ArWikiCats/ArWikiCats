"""
Key mappings and transformations for category normalization.
This module defines comprehensive mappings to normalize common English
phrases and entities in category titles, making them easier to match.
"""

import functools
import re
from typing import Dict

from ..translations.utils.json_dir import open_json_file

COMPANY_TYPE_TRANSLATIONS = open_json_file("keys/COMPANY_TYPE_TRANSLATIONS.json") or {}

# "motor vehicle manufacturers":"تصنيع السيارات",
# "law":"مؤسسات قانون",
# "entertainment":"ترفيهية",

# Cache for compiled regex patterns
_change_key_compiled = {
    "basedon non-": re.compile(r"\bbasedon non-(?!\S)", flags=re.IGNORECASE),
    "comedy-": re.compile(r"\bcomedy-(?!\S)", flags=re.IGNORECASE),
}

# Cache for compiled regex patterns
_change_key2_compiled = {}
_change_key3_compiled = {}

CHANGE_KEY_MAPPINGS: Dict[str, str] = {
    "diplomatic missions of": "diplomatic-missions-of",
    "fiba world championship for women": "fiba women's world championship",
    "central american and caribbean games": "central-american-and-caribbean-games",
    "elections,": "elections",
    "based on": "basedon",
    "basedon non-": "basedon non ",
    "based on non-": "basedon non ",
    "comedy-": "comedy ",
    "labor": "labour",
    "war of": "war-of",
    "- men's tournament": "mens tournament",
    "- women's tournament": "womens tournament",
    "– men's tournament": "mens tournament",
    "– women's tournament": "womens tournament",
    "(tennis)": "tennis",
    "accidents and incidents": "accidents-and-incidents",
    "adaptations of works": "adaptations-of-works",
    "africa cup of nations": "africa cup-of-nations",
    "african cup of nations": "african cup-of-nations",
    "african american": "africanamerican",
    "african-american": "africanamerican",
    "ancient greek": "ancient-greek",
    "ancient macedonian": "ancient-macedonian",
    "ancient roman": "ancient-roman",
    "architecture schools": "architecture-schools",
    "association football afc": "association-football afc",
    "athletes (track and field)": "track and field athletes",
    "bodies of water": "bodies-of-water",
    "british hong kong": "british-hong-kong",
    "built by": "built-by",
    "built in": "built-in",
    "by car bomb": "by-car-bomb",
    "by firearm in": "by-firearm-in",
    "canadian football": "canadian-football",
    "canton of": "canton-of",
    "caribbean people": "caribbeans people",
    "child soldiers": "child-soldiers",
    "city of liverpool f.c.": "city-of-liverpool f.c.",
    "city of london": "city-of-london",
    "colony of": "colony-of",
    "county of": "county-of",
    "crown of": "crown-of",
    "domain of": "domain-of",
    "duchy of": "duchy-of",
    "early modern": "early-modern",
    "emirate of": "emirate-of",
    "executed by burning": "executed-burning",
    "executed by decapitation": "executed-decapitation",
    "executed by firearm": "executed-firearm",
    "executed by hanging": "executed-hanging",
    "executions by": "executions in",
    "football (soccer)": "football",
    "for member of parliament": "for member-of-parliament",
    "future elections": "future-elections",
    "general elections": "general-elections",
    "governance of policing": "governance policing",
    "harrow on hill": "harrow-on-hill",
    "health care": "healthcare",
    "imprisoned in": "imprisoned-in",
    "in northern ireland": "in northern-ireland",
    "in sport in": "in-sport-in",
    "in sports in": "in-sports-in",
    "isle of": "isle-of",
    "killed in action": "killed-in-action",
    "kingdom of": "kingdom-of",
    "labour and social security": "labour-and-social security",
    "launched by": "launched-by",
    "launched in": "launched-in",
    "local elections": "local-elections",
    "published by": "published-by",
    "manufactured by": "manufactured-by",
    "manufactured in": "manufactured-in",
    "march of": "march-of",
    "margraviate of": "margraviate-of",
    "medallists": "medalists",
    "military equipment": "military-equipment",
    "military terminology": "military-terminology",
    "ministers for": "ministers-for",
    "murderers of children": "murderersofchildren",
    "national register of historic places": "national-register-of-historic-places",
    "presidential elections": "presidential-elections",
    "presidential primaries": "presidential-primaries",
    "prisoners of conscience": "prisoners-of-conscience",
    "protectorate of": "protectorate-of",
    "publishers (people)": "publisherspeople",
    "realm of": "realm-of",
    "refusing to convert to christianity": "refusing-to-convert-to-christianity",
    "refusing to convert to islam": "refusing-to-convert-to-islam",
    "republic of": "republic-of",
    "saudi arabian": "saudiarabian",
    "scholars of islam": "scholars-of-islam",
    "shot dead by law enforcement officers": "shot dead-by-law enforcement officers",
    "sport ministers": "sport-ministers",
    "sports culture": "sports-culture",
    "sports media": "sports-media",
    "sports ministers": "sports-ministers",
    "sportspeople": "sports-people",
    "states of": "states-of",
    "television films debuts": "television films-debuts",
    "television films endings": "television films-endings",
    "television miniseries debuts": "television miniseries-debuts",
    "television miniseries endings": "television miniseries-endings",
    "television seasons": "television-seasons",
    "television series debuts": "television series-debuts",
    "television series endings": "television series-endings",
    "transferred from": "transferred-from",
    "united states house of representatives": "united states house-of-representatives",
    "university of reading": "university-of-reading",
    "university of science and technology": "university-of-science and technology",
    "university of technology": "university-of-technology",
    "us open (tennis)": "us open tennis",
    "viceroyalty of": "viceroyalty-of",
    "west coast of united states": "west coast-of-united states",
    "world war i": "world-war-i",
    "world war ii": "world-war-ii",
    # " executed by " :" executed-by ",
    # "ancient romans" :"ancient-romans",
    # "austria-hungary" :"austriahungary",
    # "executed by guillotine" : "executed-guillotine",
    # "paintings by" : "paintings-by",
    # "people of ottoman empire" :"people-of-ottoman-empire",
    # "province of" :"province-of",
    # "sentenced to death" :"sentenced-to-death",
    # "university of " :"university-of ",
    # "university of" :"university-of",
}

for x in COMPANY_TYPE_TRANSLATIONS:
    CHANGE_KEY_MAPPINGS[f"defunct {x} companies"] = f"defunct-{x}-companies"

CHANGE_KEY_SECONDARY: Dict[str, str] = {
    " at ": " in ",
    " at 1": " in 1",
    " at 2": " in 2",
    "for deafblind": "for-deafblind",
    "for blind": "for-blind",
    "for deaf": "for-deaf",
    "remade in": "remade-in",
    "charter airlines": "charter-airlines",
    "country of residence": "country-of-residence",
    "declarations of independence": "declarations-of-independence",
    "game of thrones": "game-of-thrones",
    "green party of quebec": "green party-of-quebec",
    "historians of philosophy": "historians-of-philosophy",
    "house of commons": "house-of-commons",
    "house of representatives": "house-of-representatives",
    "libertarian party of canada": "libertarian party-of-canada",
    "orgadnisation for prohibition of chemical weapons": "opcw",
    "serbia and montenegro": "serbia-and-montenegro",
    "term of Iranian Majlis": "Iranian Majlis",
    "united states declaration of independence": "united-states-declaration-of-independence",
}

CHANGE_KEY_SECONDARY_REGEX = {
    r"^tour de ": "tour of ",
    r"^women's footballers ": "female footballers ",
    r"^women's footballers": "female footballers",
    r"men's events": "mens-events",
    r"mens events": "mens-events",
    r" women's footballers$": " female footballers",
    r" executed people$": " executed-people",
}

# @dump_data(1)


@functools.lru_cache(maxsize=10000)
def change_key_mappings_replacements(category):
    """Apply primary key mappings replacements to the category string.

    Args:
        category (str): The category string to process.

    Returns:
        str: The category string with primary mappings applied.
    """
    category = category.replace("’", "'")
    # Apply CHANGE_KEY_MAPPINGS regex patterns (cached)
    for chk, chk_lab in CHANGE_KEY_MAPPINGS.items():
        key = (chk, chk_lab)
        if key not in _change_key_compiled:
            chk_escape = re.escape(chk)
            # This single pattern robustly handles whole word/phrase replacements.
            _change_key_compiled[key] = re.compile(rf"(?<!\w){chk_escape}(?!\w)", flags=re.IGNORECASE)

        category = _change_key_compiled[key].sub(chk_lab, category)

    category = change_key_secondary_replacements(category)

    return category


# @dump_data(1)
@functools.lru_cache(maxsize=10000)
def change_key_secondary_replacements(category):
    """Apply secondary key mappings replacements to the category string.

    Args:
        category (str): The category string to process.

    Returns:
        str: The category string with secondary mappings applied.
    """
    category = category.replace("’", "'")

    # Apply CHANGE_KEY_SECONDARY regex patterns (cached)
    for chk2, chk2_lab in CHANGE_KEY_SECONDARY.items():
        if chk2 not in _change_key2_compiled:
            chk2_escape = re.escape(chk2)
            # _change_key2_compiled[chk2] = re.compile(rf"(?<!\w){chk2_escape}(?!\w)", flags=re.IGNORECASE)
            _change_key2_compiled[chk2] = re.compile(rf"\b{chk2_escape}\b", flags=re.IGNORECASE)

        category = _change_key2_compiled[chk2].sub(chk2_lab, category)

    # Apply CHANGE_KEY_SECONDARY_REGEX patterns
    for chk2_regex, chk2_lab in CHANGE_KEY_SECONDARY_REGEX.items():
        if chk2_regex not in _change_key3_compiled:
            _change_key3_compiled[chk2_regex] = re.compile(chk2_regex, flags=re.IGNORECASE)

        category = _change_key3_compiled[chk2_regex].sub(chk2_lab, category)

    return category
