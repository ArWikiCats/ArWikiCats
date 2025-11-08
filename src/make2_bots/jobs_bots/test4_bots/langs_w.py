"""Language specific helpers for job labels."""

from __future__ import annotations

from ....helps.print_bot import print_put
from ....ma_lists import All_Nat, Films_key_333, Films_key_CAO, Films_key_For_nat, Films_keys_both_new, Jobs_key_mens, film_Keys_For_female, lang_key_m, languages_key
from ..utils import cached_lookup, log_debug, normalize_cache_key

LANG_WORK_CACHE: dict[str, str] = {}

__all__ = ["Lang_work"]


def Lang_work(con_3: str) -> str:  # noqa: N802
    """Process and retrieve language-related information based on input."""

    cache_key = normalize_cache_key(con_3)
    return cached_lookup(
        LANG_WORK_CACHE,
        (cache_key,),
        lambda: _resolve_language_label(con_3),
    )


def _resolve_language_label(con_3: str) -> str:
    """Resolve a label for :func:`Lang_work` without cache lookups."""

    log_debug('<<lightblue>> Lang_work :"%s"', con_3)

    direct_match = languages_key.get(con_3, "")
    if direct_match:
        return direct_match

    label = _romanization_label(con_3)
    if label:
        return label

    for lang, translation in languages_key.items():
        candidate = f"{lang} "
        films_label = _films_match(con_3, lang, translation)
        if films_label:
            return films_label
        if con_3.startswith(candidate):
            log_debug("<<lightblue>> con_3.startswith(lang:%s)", candidate)
            label = lab_from_lang_keys(con_3, lang, translation, candidate)
            if label:
                return label
    return ""


def _romanization_label(con_3: str) -> str:
    """Handle romanization labels that follow a structured prefix."""

    prefix = "romanization of"
    if con_3.startswith(prefix):
        remainder = con_3[len(prefix) :].strip()
        language_value = languages_key.get(f"{remainder} language", "")
        print_put(remainder)
        if language_value:
            return f"رومنة {language_value}"
    return ""


def _films_match(con_3: str, lang: str, translation: str) -> str:
    """Handle simple film related matches before the more complex logic."""

    target = f"{lang.replace('-language', '')} films"
    if con_3 == target:
        return f"أفلام ب{translation}"
    return ""


def lab_from_lang_keys(con_3: str, lang: str, l_lab: str, lang2: str) -> str:
    """Resolve labels using the language specific helper dictionaries."""

    if All_Nat.get(lang):
        nat_label = All_Nat[lang]["mens"]
        log_debug(
            '<<lightred>> skip lang:"%s" in All_Nat,l_lab:"%s",nat_labe:"%s" ',
            lang,
            l_lab,
            nat_label,
        )
        return ""

    language_lab = languages_key[lang]
    con_8 = con_3[len(lang2) :]

    label = _label_from_jobs_key(con_8, language_lab, lang2)
    if label:
        return label

    label = _label_from_language_keys(con_8, language_lab)
    if label:
        return label

    label = _label_from_film_keys(con_8, language_lab)
    if label:
        return label

    for name, dictionary in {
        "film_Keys_For_female": film_Keys_For_female,
        "Films_key_333": Films_key_333,
        "Films_key_CAO": Films_key_CAO,
    }.items():
        if con_8 in dictionary:
            result = f"{dictionary[con_8]} ب{language_lab}"
            log_debug('<<lightblue>> lab_from_lang_keys %s. it_lab:"%s"', name, result)
            return result
    return ""


def _label_from_jobs_key(con_8: str, language_lab: str, lang2: str) -> str:
    """Return a label derived from job keys when available."""

    jobs_label = Jobs_key_mens.get(con_8, "")
    if jobs_label:
        result = f"{jobs_label} ب{language_lab}"
        log_debug(
            '<<lightblue>> Jobs_key_mens(%s): con_3.startswith_priff2("%s"), it_lab:"%s"',
            con_8,
            lang2,
            result,
        )
        return result
    return ""


def _label_from_language_keys(con_8: str, language_lab: str) -> str:
    """Return labels derived from language specific helper dictionaries."""

    language_key = lang_key_m.get(con_8, "")
    if language_key:
        log_debug('<<lightblue>> lang_key_m(%s), con_78_lab:"%s"', con_8, language_key)
        return language_key.format(language_lab)
    return ""


def _label_from_film_keys(con_8: str, language_lab: str) -> str:
    """Derive labels from film keys when possible."""

    if Films_key_For_nat.get(con_8):
        result = Films_key_For_nat[con_8].format(f"ب{language_lab}")
        log_debug('<<lightblue>> lab_from_lang_keys Films_key_For_nat. it_lab:"%s"', result)
        return result

    if con_8.endswith(" films"):
        con_9 = con_8[: -len("films")].strip().lower()
        con_9_lab = Films_keys_both_new.get(con_9, {}).get("female", "")
        if con_9_lab:
            result = f"أفلام {con_9_lab} ب{language_lab}"
            log_debug('<<lightblue>> lab_from_lang_keys Films_key_333. it_lab:"%s"', result)
            return result
    return ""
