#!/usr/bin/python3
"""
!
"""
from typing import Dict
from ....translations import (
    All_Nat,
    Films_keys_both_new,
    Films_key_333,
    film_Keys_For_female,
    Films_key_CAO,
    Films_key_For_nat,
    jobs_mens_data,
    languages_key,
    lang_key_m,
)
from ....helps.print_bot import output_test4, print_put
import functools


from pathlib import Path
from ....helps.jsonl_dump import save_data


@save_data(Path(__file__).parent / "Lang_work.jsonl", ["con_3"])
@functools.lru_cache(maxsize=None)
def Lang_work(con_3: str) -> str:
    """Process and retrieve language-related information based on input.

    This function takes a string input representing a language or a related
    term, processes it to determine the appropriate language label, and
    returns the corresponding label. It checks against predefined
    dictionaries to find matches and formats the output accordingly. The
    function also caches results for efficiency.

    Args:
        con_3 (str): A string representing a language or related term.

    Returns:
        str: The corresponding language label or an empty string if no match is
            found.
    """

    output_test4(f'<<lightblue>> Lang_work :"{con_3}"')
    lang_lab = ""
    # ---
    if not lang_lab:
        lang_lab = languages_key.get(con_3, "")
    # ---
    tta = {"romanization of": "رومنة {}"}
    # ---
    for wriff, Wriff_lab in tta.items():
        if con_3.startswith(wriff) and lang_lab == "":
            con_43 = con_3[len(wriff) :].strip()
            lang_lac = languages_key.get(f"{con_43} language", "")
            print_put(con_43)
            if lang_lac:
                lang_lab = Wriff_lab.format(lang_lac)
                break
    # ---
    for lang, l_lab in languages_key.items():
        # ---
        if lang_lab:
            break
        # ---
        lang2 = f"{lang} "
        # ---
        lang3 = f"{lang.replace('-language', '')} films"
        if lang3 == con_3:
            lang_lab = f"أفلام ب{l_lab}"
            break
        # ---
        if con_3.startswith(lang2):
            output_test4(f"<<lightblue>> con_3.startswith(lang:{lang2})")
            # ---
            lang_lab = lab_from_lang_keys(con_3, lang, l_lab, lang2)
    # ---

    # ---
    return lang_lab


def lab_from_lang_keys(con_3: str, lang: str, l_lab: str, lang2: str) -> str:
    # ---
    if All_Nat.get(lang, False):
        nat_labe = All_Nat[lang]["mens"]
        output_test4(f'<<lightred>> skip lang:"{lang}" in All_Nat,l_lab:"{l_lab}",nat_labe:"{nat_labe}" ')
        return ""
    # ---
    language_lab = languages_key[lang]
    # ---
    con_8 = con_3[len(lang2) :]
    con_78_lab = jobs_mens_data.get(con_8, "")
    # ---
    it_lab = ""
    # ---
    if con_78_lab:
        it_lab = f"{con_78_lab} ب{language_lab}"
        output_test4(f'<<lightblue>> jobs_mens_data({con_8}): con_3.startswith_priff2("{lang2}"), it_lab:"{it_lab}"')
    # ---
    if not it_lab:
        con_78_lab = lang_key_m.get(con_8, "")
        # ---
        if con_78_lab:
            output_test4(f'<<lightblue>> lang_key_m({con_8}), con_78_lab:"{con_78_lab}"')
            it_lab = lang_key_m[con_8].format(language_lab)
    # ---
    if not it_lab:
        output_test4(f"no match for :({con_8}), {language_lab=}")
        if Films_key_For_nat.get(con_8):
            it_lab = Films_key_For_nat[con_8].format(f"ب{language_lab}")
            output_test4(f'<<lightblue>> lab_from_lang_keys Films_key_For_nat. it_lab:"{it_lab}"')
    # ---
    if not it_lab:
        if con_8.endswith(" films"):
            # ---
            con_9 = con_8[: -len("films")].strip().lower()
            con_9_lab = Films_keys_both_new.get(con_9, {}).get("female", "")
            # ---
            if con_9_lab:
                it_lab = f"أفلام {con_9_lab} ب{language_lab}"
                output_test4(f'<<lightblue>> lab_from_lang_keys Films_key_333. it_lab:"{it_lab}"')
    # ---
    dict_tabs = {
        "film_Keys_For_female": film_Keys_For_female,
        "Films_key_333": Films_key_333,
        "Films_key_CAO": Films_key_CAO,
    }
    # ---
    if not it_lab:
        for key, dict_tab in dict_tabs.items():
            con_78_lab = dict_tab.get(con_8)
            if con_78_lab:
                # ---
                it_lab = f"{con_78_lab} ب{language_lab}"
                output_test4(f'<<lightblue>> lab_from_lang_keys {key}. it_lab:"{it_lab}"')
                break
    # ---
    return it_lab
