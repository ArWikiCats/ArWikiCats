"""
Category normalization and formatting utilities.
This package provides functions to transform and normalize English Wikipedia
category names before they are processed by the resolvers.
"""

import logging
import re

from .pf_keys import change_key_mappings_replacements

logger = logging.getLogger(__name__)

# Precompiled Regex Patterns
REGEX_SUB_WHITESPACE = re.compile(r"[\s\t]+", re.IGNORECASE)
REGEX_SUB_CENTURY = re.compile(r"[−–\-]century", re.IGNORECASE)
REGEX_SUB_MILLENNIUM = re.compile(r"[−–\-]millennium", re.IGNORECASE)
REGEX_SUB_MILLENNIUM_CENTURY = re.compile(r"[−–\-](millennium|century)", re.I)
REGEX_SUB_ROYAL_DEFENCE_FORCE = re.compile(r"royal (.*?) defence force", re.IGNORECASE)
REGEX_SUB_ROYAL_NAVAL_FORCE = re.compile(r"royal (.*?) naval force", re.IGNORECASE)
REGEX_SUB_ROYAL_NAVY = re.compile(r"royal (.*?) navy", re.IGNORECASE)
REGEX_SUB_ROYAL_AIR_FORCE = re.compile(r"royal (.*?) air force", re.IGNORECASE)
REGEX_SUB_EXPATRIATE_PEOPLE = re.compile(r"(\w+) expatriate (\w+) people in ", re.IGNORECASE)
REGEX_SUB_ORGANISATIONS = re.compile(r"organisations", re.IGNORECASE)
REGEX_SUB_RUS = re.compile(r"rus'", re.IGNORECASE)
REGEX_SUB_THE_KINGDOM_OF = re.compile(r"the kingdom of", re.IGNORECASE)
REGEX_SUB_AUSTRIA_HUNGARY = re.compile(r"austria-hungary", re.IGNORECASE)
REGEX_SUB_AUSTRIA_HUNGARY_2 = re.compile(r"austria hungary", re.IGNORECASE)
REGEX_SUB_UNMANNED_MILITARY_AIRCRAFT = re.compile(r"unmanned military aircraft of", re.IGNORECASE)
REGEX_SUB_UNMANNED_AERIAL_VEHICLES = re.compile(r"unmanned aerial vehicles of", re.IGNORECASE)
REGEX_SUB_DEMOCRATIC_REPUBLIC_CONGO = re.compile(r"democratic republic of congo", re.IGNORECASE)
REGEX_SUB_REPUBLIC_CONGO = re.compile(r"republic of congo", re.IGNORECASE)
REGEX_SUB_ATHLETICS = re.compile(r"athletics \(track and field\)", re.IGNORECASE)
REGEX_SUB_TWIN_PEOPLE = re.compile(r"twin people", re.IGNORECASE)
REGEX_SUB_PERCENT27 = re.compile(r"\%27", re.IGNORECASE)
REGEX_SUB_CATEGORY_MINISTERS = re.compile(r"category\:ministers of ", re.IGNORECASE)
REGEX_SUB_ASSOCIATION_FOOTBALL_AFC = re.compile(r"association football afc", re.IGNORECASE)
REGEX_SUB_ASSOCIATION_FOOTBALL = re.compile(r"association football", re.IGNORECASE)

replaces = {
    "election, ": "election ",
    "national women's youth": "national youth women's",
    "national youth women's": "national youth women's",
    "women's youth national": "national youth women's",
    "women's national youth": "national youth women's",
    "youth national women's": "national youth women's",
    "youth women's national": "national youth women's",
    "national women's junior": "national junior women's",
    "national junior women's": "national junior women's",
    "women's junior national": "national junior women's",
    "women's national junior": "national junior women's",
    "junior women's national": "national junior women's",
    "national men's junior": "national junior men's",
    "national junior men's": "national junior men's",
    "men's junior national": "national junior men's",
    "men's national junior": "national junior men's",
    "junior men's national": "national junior men's",
    " men's national": " national men's",
    "women's national": "national women's",
    "junior national": "national junior",
    "youth national": "national youth",
    "amateur national": "national amateur",
    "heads of mission ": "heads-of-mission ",
    "house of commons of canada": "house-of-commons-of-canada",
}


def change_cat(cat_orginal: str) -> str:
    """
    Transform and normalize category names by applying various regex patterns and replacements.

    Args:
        cat_orginal: Original category string to transform

    Returns:
        Transformed category string
    """
    cat_orginal = cat_orginal.lower().strip()
    category = cat_orginal

    category = re.sub(r"\bthe\b", "", category, flags=re.IGNORECASE).strip()

    # Normalize whitespace
    category = REGEX_SUB_WHITESPACE.sub(" ", category)

    # Normalize century and millennium formatting
    category = REGEX_SUB_CENTURY.sub(" century", category)
    category = REGEX_SUB_MILLENNIUM.sub(" millennium", category)
    category = REGEX_SUB_MILLENNIUM_CENTURY.sub(r" \g<1>", category)

    # Reorder royal military force names
    category = REGEX_SUB_ROYAL_DEFENCE_FORCE.sub(r"\g<1> royal defence force", category)
    category = REGEX_SUB_ROYAL_NAVAL_FORCE.sub(r"\g<1> royal naval force", category)
    category = REGEX_SUB_ROYAL_NAVY.sub(r"\g<1> royal navy", category)
    category = REGEX_SUB_ROYAL_AIR_FORCE.sub(r"\g<1> royal air force", category)

    # Apply various normalization patterns
    category = REGEX_SUB_EXPATRIATE_PEOPLE.sub(r"\g<1> expatriate \g<2> peoplee in ", category)
    category = REGEX_SUB_ORGANISATIONS.sub("organizations", category)
    category = REGEX_SUB_RUS.sub("rus", category)
    category = REGEX_SUB_THE_KINGDOM_OF.sub(" kingdom of", category)
    category = REGEX_SUB_AUSTRIA_HUNGARY.sub("austria hungary", category)
    category = REGEX_SUB_AUSTRIA_HUNGARY_2.sub("austria hungary", category)
    category = REGEX_SUB_UNMANNED_MILITARY_AIRCRAFT.sub("unmanned military aircraft-of", category)
    category = REGEX_SUB_UNMANNED_AERIAL_VEHICLES.sub("unmanned aerial vehicles-of", category)
    category = REGEX_SUB_DEMOCRATIC_REPUBLIC_CONGO.sub("democratic-republic-of-congo", category)
    category = REGEX_SUB_REPUBLIC_CONGO.sub("republic-of-congo", category)
    category = REGEX_SUB_ATHLETICS.sub("track-and-field athletics", category)
    category = REGEX_SUB_TWIN_PEOPLE.sub("twinpeople", category)
    category = REGEX_SUB_PERCENT27.sub("'", category)

    # Apply simple string replacements
    simple_replacements = {
        "secretaries of ": "secretaries-of ",
        "sportspeople": "sports-people",
        "roller hockey (quad)": "roller hockey",
        "victoria (australia)": "victoria-australia",
        "party of ": "party-of ",
        " uu-16 ": " u-16 ",
    }
    for old, new in simple_replacements.items():
        category = category.replace(old, new)

    # Apply replaces dictionary
    for x, d in replaces.items():
        category = category.replace(x, d)

    category = change_key_mappings_replacements(category)

    # Final transformations
    category = REGEX_SUB_CATEGORY_MINISTERS.sub("category:ministers-of ", category)
    category = REGEX_SUB_ASSOCIATION_FOOTBALL_AFC.sub("association-football afc", category)
    category = REGEX_SUB_ASSOCIATION_FOOTBALL.sub("football", category)

    # Log changes if any
    if category != cat_orginal:
        logger.info(f' to :"{category}", orginal: {cat_orginal}.')

    return category


__all__ = [
    "change_cat",
]
