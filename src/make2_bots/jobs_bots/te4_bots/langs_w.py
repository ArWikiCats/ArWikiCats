#!/usr/bin/python3
"""
Language processing utilities for category translation.
"""
import functools

from ....helps.log import logger
from ....translations import (
    All_Nat,
    Films_key_333,
    Films_key_CAO,
    Films_key_For_nat,
    Films_keys_both_new,
    film_Keys_For_female,
    jobs_mens_data,
    lang_key_m,
    languages_key,
)


def _try_romanization(con_3: str) -> str:
    """Try to match romanization pattern and return formatted label.

    Args:
        con_3: Input string to check for romanization pattern

    Returns:
        Formatted romanization label or empty string
    """
    romanization_patterns = {"romanization of": "رومنة {}"}

    for prefix, template in romanization_patterns.items():
        if con_3.startswith(prefix):
            suffix = con_3[len(prefix) :].strip()
            lang_label = languages_key.get(f"{suffix} language", "")
            logger.info(suffix)
            if lang_label:
                return template.format(lang_label)
    return ""


def _try_films_pattern(con_3: str, lang: str, l_lab: str) -> str:
    """Try to match films pattern for a language.

    Args:
        con_3: Input string to check
        lang: Language key
        l_lab: Language label

    Returns:
        Formatted films label or empty string
    """
    lang_without_suffix = lang.replace("-language", "")
    films_pattern = f"{lang_without_suffix} films"

    if films_pattern == con_3:
        return f"أفلام ب{l_lab}"
    return ""


def _try_films_suffix(suffix: str, language_lab: str) -> str:
    """Try to match and process films suffix patterns.

    Args:
        suffix: The suffix part after language prefix
        language_lab: The language label

    Returns:
        Formatted label or empty string
    """
    if not suffix.endswith(" films"):
        return ""

    prefix = suffix[: -len("films")].strip().lower()
    film_label = Films_keys_both_new.get(prefix, {}).get("female", "")

    if film_label:
        result = f"أفلام {film_label} ب{language_lab}"
        logger.debug(f'<<lightblue>> _try_films_suffix Films_keys_both_new. result:"{result}"')
        return result
    return ""


def _lookup_in_dictionaries(suffix: str, language_lab: str) -> str:
    """Look up suffix in multiple film-related dictionaries.

    Args:
        suffix: The suffix to look up
        language_lab: The language label to format with

    Returns:
        Formatted label or empty string
    """
    dict_tabs = {
        "film_Keys_For_female": film_Keys_For_female,
        "Films_key_333": Films_key_333,
        "Films_key_CAO": Films_key_CAO,
    }

    for dict_name, dict_tab in dict_tabs.items():
        label = dict_tab.get(suffix)
        if label:
            result = f"{label} ب{language_lab}"
            logger.debug(f'<<lightblue>> _lookup_in_dictionaries {dict_name}. result:"{result}"')
            return result
    return ""


@functools.lru_cache(maxsize=None)
def Lang_work(con_3: str) -> str:
    """Process and retrieve language-related information based on input.

    This function takes a string input representing a language or a related
    term, processes it to determine the appropriate language label, and
    returns the corresponding label. It checks against predefined
    dictionaries to find matches and formats the output accordingly. The
    function also caches results for efficiency.

    Args:
        con_3: A string representing a language or related term.

    Returns:
        The corresponding language label or an empty string if no match is found.
    """
    logger.debug(f'<<lightblue>> Lang_work :"{con_3}"')

    # Direct lookup in languages_key
    lang_lab = languages_key.get(con_3, "")
    if lang_lab:
        return lang_lab

    # Try romanization pattern
    lang_lab = _try_romanization(con_3)
    if lang_lab:
        return lang_lab

    # Try language prefix matching
    for lang, l_lab in languages_key.items():
        # Check films pattern
        lang_lab = _try_films_pattern(con_3, lang, l_lab)
        if lang_lab:
            return lang_lab

        # Check language prefix
        lang_prefix = f"{lang} "
        if con_3.startswith(lang_prefix):
            logger.debug(f"<<lightblue>> con_3.startswith(lang:{lang_prefix})")
            lang_lab = lab_from_lang_keys(con_3, lang, l_lab, lang_prefix)
            if lang_lab:
                return lang_lab

    return ""


def lab_from_lang_keys(con_3: str, lang: str, l_lab: str, lang_prefix: str) -> str:
    """Extract and format label based on language prefix match.

    This function processes a category string that starts with a language prefix
    and attempts to find the appropriate Arabic translation by looking up the
    suffix in various dictionaries.

    Args:
        con_3: The full category string
        lang: The language key
        l_lab: The language label (unused, kept for compatibility)
        lang_prefix: The language prefix with trailing space

    Returns:
        Formatted Arabic label or empty string if no match found
    """
    # Skip if language is in nationality dictionary
    if All_Nat.get(lang, False):
        nat_label = All_Nat[lang]["mens"]
        logger.debug(f'<<lightred>> skip lang:"{lang}" in All_Nat, l_lab:"{l_lab}", nat_label:"{nat_label}" ')
        return ""

    language_lab = languages_key[lang]
    suffix = con_3[len(lang_prefix) :]

    # Try jobs_mens_data lookup
    label = jobs_mens_data.get(suffix, "")
    if label:
        result = f"{label} ب{language_lab}"
        logger.debug(f'<<lightblue>> jobs_mens_data({suffix}): result:"{result}"')
        return result

    # Try lang_key_m lookup with formatting
    template = lang_key_m.get(suffix, "")
    if template:
        result = template.format(language_lab)
        logger.debug(f'<<lightblue>> lang_key_m({suffix}), template:"{template}"')
        return result

    # Try Films_key_For_nat lookup
    logger.debug(f"no match for :({suffix}), {language_lab=}")
    template = Films_key_For_nat.get(suffix)
    if template:
        result = template.format(f"ب{language_lab}")
        logger.debug(f'<<lightblue>> Films_key_For_nat. result:"{result}"')
        return result

    # Try films suffix pattern
    result = _try_films_suffix(suffix, language_lab)
    if result:
        return result

    # Try multiple film dictionaries
    result = _lookup_in_dictionaries(suffix, language_lab)
    if result:
        return result

    return ""
