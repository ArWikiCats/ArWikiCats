#!/usr/bin/python3
"""
!
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
    country = category.split(tito)[1]
    country = country.lower()
    Mash = f"^(.*?)(?:{tito}?)(.*?)$"
    Type_t = re.sub(Mash, r"\g<1>", category.lower())
    country_t = re.sub(Mash, r"\g<2>", category.lower())

    test_N = category.lower()
    try:
        test_N = re.sub(Type.lower(), "", test_N)
        test_N = re.sub(country.lower(), "", test_N)

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

    elif tito2 == "by" and not country.startswith(titostarts):
        country = f"by {country}"
    elif tito2 == "for" and not country.startswith(titostarts):
        country = f"for {country}"

    print_def_head(f'>xx>>> Type: "{Type.strip()}", country: "{country.strip()}", {tito=} ')

    if test_N and test_N != tito2:
        print_put(f'>>>> test_N != "", Type_t:"{Type_t}", tito:"{tito}", country_t:"{country_t}" ')

        if tito2 == "of" and not Type_t.endswith(titoends):
            Type_t = f"{Type_t} of"
        elif tito2 == "by" and not country_t.startswith(titostarts):
            country_t = f"by {country_t}"
        elif tito2 == "for" and not country_t.startswith(titostarts):
            country_t = f"for {country_t}"
        Type = Type_t
        country = country_t

        print_put(f'>>>> yementest: Type_t:"{Type_t}", country_t:"{country_t}"')
    else:
        print_put(f'>>>> test_N:"{test_N}" == tito')

    return Type, country
