#!/usr/bin/python3
"""
from .arlabel_bots.bot_type_country import get_type_country

"""


import re
from typing import Tuple
from ...helps.print_bot import print_def_head, print_put


def get_type_country(category: str, tito: str) -> Tuple[str, str]:
    """Extract the type and country from a given category string.

    This function takes a category string and a delimiter (tito) to split
    the category into a type and a country. It processes the strings to
    ensure proper formatting and handles specific cases based on the value
    of tito. The function also performs some cleanup on the extracted
    strings to remove any unwanted characters or formatting issues.

    Args:
        category (str): The category string containing type and country information.
        tito (str): The delimiter used to separate the type and country in the category
            string.

    Returns:
        tuple: A tuple containing the processed type (str) and country (str).
    """

    Type = category.split(tito)[0]
    contry = category.split(tito)[1]
    contry = contry.lower()
    Mash = f"^(.*?)(?:{tito}?)(.*?)$"
    Type_t = re.sub(Mash, r"\g<1>", category.lower())
    contry_t = re.sub(Mash, r"\g<2>", category.lower())

    test_N = category.lower()
    try:
        test_N = re.sub(Type.lower(), "", test_N)
        test_N = re.sub(contry.lower(), "", test_N)

    except Exception:
        print_put("<<lightred>>>>>> except test_N ")
    test_N = test_N.strip()

    tito2 = tito.strip()

    if tito2 == "in" and Type.endswith(" playerss"):
        Type = Type.replace(" playerss", " players")

    titoends = f" {tito2}"
    titostarts = f"{tito2} "

    if tito2 == "of" and not Type.endswith(titoends):
        Type = f"{Type} of"
    elif tito2 == "spies for" and not Type.endswith(" spies"):
        Type = f"{Type} spies"

    elif tito2 == "by" and not contry.startswith(titostarts):
        contry = f"by {contry}"
    elif tito2 == "for" and not contry.startswith(titostarts):
        contry = f"for {contry}"

    print_def_head(f'>xx>>> Type: "{Type.strip()}", contry: "{contry.strip()}", tito: "{tito}" ')

    if test_N and test_N != tito2:
        print_put(f'>>>> test_N != "", Type_t:"{Type_t}", tito:"{tito}", contry_t:"{contry_t}" ')

        if tito2 == "of" and not Type_t.endswith(titoends):
            Type_t = f"{Type_t} of"
        elif tito2 == "by" and not contry_t.startswith(titostarts):
            contry_t = f"by {contry_t}"
        elif tito2 == "for" and not contry_t.startswith(titostarts):
            contry_t = f"for {contry_t}"
        Type = Type_t
        contry = contry_t

        print_put(f'>>>> yementest: Type_t:"{Type_t}", contry_t:"{contry_t}"')
    else:
        print_put(f'>>>> test_N:"{test_N}" == tito')

    return Type, contry
