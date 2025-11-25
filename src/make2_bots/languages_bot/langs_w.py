#!/usr/bin/python3
"""
Language processing utilities for category translation.
"""

import functools
from typing import Dict, Mapping, Optional

from ...helps.log import logger
from ...translations import (
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


class FilmCategoryLabelResolver:
    """Handle film-related category patterns and lookups."""

    def __init__(
        self,
        *,
        films_for_nat: Mapping[str, str],
        films_keys_both: Mapping[str, Dict[str, str]],
        films_female: Mapping[str, str],
        films_333: Mapping[str, str],
        films_cao: Mapping[str, str],
    ) -> None:
        """Initialize film-related dictionaries."""
        self._films_for_nat = films_for_nat
        self._films_keys_both = films_keys_both
        self._films_female = films_female
        self._films_333 = films_333
        self._films_cao = films_cao

    # ---------- Direct "X-language films" pattern ----------

    def resolve_direct_language_films(
        self, suffix: str, lang_key: str, lang_label: str
    ) -> str:
        """Resolve patterns like 'arabic-language films'.

        Args:
            suffix: Full input category string.
            lang_key: Language key (e.g. 'arabic-language').
            lang_label: Arabic label of the language.

        Returns:
            Arabic label or empty string if no match.

        Example:
            arabic-language films -> "أفلام باللغة العربية"
        """
        lang_without_suffix = lang_key.replace("-language", "")
        films_pattern = f"{lang_without_suffix} films"

        if films_pattern == suffix:
            return f"أفلام ب{lang_label}"
        return ""

    # ---------- Suffix-based film resolution under a language prefix ----------

    def _try_films_suffix_pattern(self, suffix: str, language_label: str) -> str:
        """Try patterns like '3d anime films' with a language label.

        Example:
            suffix = '3d anime films', language_label = 'العربية'
            -> 'أفلام ثلاثية الأبعاد أنمي باللغة العربية'
        """
        if not suffix.endswith(" films"):
            return ""

        prefix = suffix[: -len("films")].strip().lower()
        film_label = self._films_keys_both.get(prefix, {}).get("female", "")

        if film_label:
            result = f"أفلام {film_label} ب{language_label}"
            logger.debug(
                f'<<lightblue>> FilmCategoryLabelResolver._try_films_suffix_pattern '
                f'result:"{result}"'
            )
            return result
        return ""

    def _lookup_in_film_dictionaries(self, suffix: str, language_label: str) -> str:
        """Lookup suffix in multiple film dictionaries."""
        dict_tabs = {
            "film_Keys_For_female": self._films_female,
            "Films_key_333": self._films_333,
            "Films_key_CAO": self._films_cao,
        }

        for dict_name, dict_tab in dict_tabs.items():
            label = dict_tab.get(suffix)
            if label:
                result = f"{label} ب{language_label}"
                logger.debug(
                    f'<<lightblue>> FilmCategoryLabelResolver._lookup_in_film_dictionaries '
                    f'{dict_name}. result:"{result}"'
                )
                return result
        return ""

    def resolve_with_suffix(self, suffix: str, language_label: str) -> str:
        """Resolve film-related label under a language prefix.

        This is used when the input looks like:
        '<lang> <suffix>' and suffix is film-related.

        Resolution order:
            1) Films_key_For_nat
            2) Films_keys_both_new (via films pattern)
            3) film_Keys_For_female / Films_key_333 / Films_key_CAO
        """
        # 1) Films_key_For_nat (template expects something like 'بالعربية')
        template = self._films_for_nat.get(suffix)
        if template:
            result = template.format(f"ب{language_label}")
            logger.debug(
                f'<<lightblue>> FilmCategoryLabelResolver.resolve_with_suffix '
                f'Films_key_For_nat({suffix}). result:"{result}"'
            )
            return result

        # 2) Pattern-based suffix ending with "films"
        result = self._try_films_suffix_pattern(suffix, language_label)
        if result:
            return result

        # 3) Lookup in other film dictionaries
        result = self._lookup_in_film_dictionaries(suffix, language_label)
        if result:
            return result

        return ""


class LanguageLabelResolver:
    """Resolve Arabic labels for language-related category strings."""

    def __init__(
        self,
        *,
        languages: Mapping[str, str],
        nationalities: Mapping[str, Dict[str, str]],
        jobs_mens: Mapping[str, str],
        lang_key_m_map: Mapping[str, str],
        film_resolver: FilmCategoryLabelResolver,
    ) -> None:
        """Initialize language resolver and inject film resolver."""
        self._languages = languages
        self._nationalities = nationalities
        self._jobs_mens = jobs_mens
        self._lang_key_m = lang_key_m_map
        self._film_resolver = film_resolver

        # Static romanization patterns for now; can be extended later.
        self._romanization_patterns = {
            "romanization of": "رومنة {}",
        }

    # ---------- Internal helpers ----------

    def _try_romanization(self, con_3: str) -> str:
        """Try to match romanization patterns like 'romanization of X'."""
        for prefix, template in self._romanization_patterns.items():
            if con_3.startswith(prefix):
                suffix = con_3[len(prefix) :].strip()
                lang_label = self._languages.get(f"{suffix} language", "")
                logger.info(suffix)
                if lang_label:
                    return template.format(lang_label)
        return ""

    def _lab_from_lang_keys(
        self,
        con_3: str,
        lang_key: str,
        lang_label: str,
        lang_prefix: str,
    ) -> str:
        """Resolve label for inputs starting with '<lang_key> ' prefix."""
        # 1) Skip if language is in nationality dictionary
        if self._nationalities.get(lang_key, False):
            nat_label = self._nationalities[lang_key]["mens"]
            logger.debug(
                f'<<lightred>> skip lang:"{lang_key}" in All_Nat, '
                f'lang_label:"{lang_label}", nat_label:"{nat_label}" '
            )
            return ""

        # 2) Ensure language label exists
        if not lang_label:
            return ""

        suffix = con_3[len(lang_prefix) :]
        logger.debug(
            f'LanguageLabelResolver._lab_from_lang_keys: '
            f'lang_prefix="{lang_prefix}", suffix="{suffix}", con_3="{con_3}"'
        )

        # 3) jobs_mens_data lookup
        job_label = self._jobs_mens.get(suffix, "")
        if job_label:
            result = f"{job_label} ب{lang_label}"
            logger.debug(
                f'<<lightblue>> jobs_mens_data({suffix}): result:"{result}"'
            )
            return result

        # 4) lang_key_m lookup with formatting
        template = self._lang_key_m.get(suffix, "")
        if template:
            result = template.format(lang_label)
            logger.debug(
                f'<<lightblue>> lang_key_m({suffix}), template:"{template}", '
                f'result:"{result}"'
            )
            return result

        logger.debug(f"no match for suffix: ({suffix}), language_label={lang_label}")

        # 5) Delegate film-related suffix resolution to FilmCategoryLabelResolver
        film_result = self._film_resolver.resolve_with_suffix(suffix, lang_label)
        if film_result:
            return film_result

        return ""
    # ---------- Public API ----------

    def resolve(self, suffix: str) -> str:
        """Resolve and retrieve language-related label based on input."""
        logger.debug(f'<<lightblue>> Lang_work/resolve :"{suffix}"')

        # 1) Direct lookup in languages_key
        lang_lab = self._languages.get(suffix, "")
        if lang_lab:
            return lang_lab

        # 2) Romanization pattern
        lang_lab = self._try_romanization(suffix)
        if lang_lab:
            return lang_lab

        # 3) Language-based patterns
        for lang_key, lang_label in self._languages.items():
            # 3.a) Film pattern: "{lang_without_suffix} films"
            films_label = self._film_resolver.resolve_direct_language_films(
                suffix, lang_key, lang_label
            )
            if films_label:
                return films_label

            # 3.b) Generic "<lang_key> <suffix>" patterns
            lang_prefix = f"{lang_key} "
            if suffix.startswith(lang_prefix):
                logger.debug(
                    f'<<lightblue>> suffix.startswith(lang:"{lang_prefix}")'
                )
                label = self._lab_from_lang_keys(
                    suffix,
                    lang_key,
                    lang_label,
                    lang_prefix,
                )
                if label:
                    return label

        return ""


# ---------- Module-level default resolver and API ----------

_film_resolver = FilmCategoryLabelResolver(
    films_for_nat=Films_key_For_nat,
    films_keys_both=Films_keys_both_new,
    films_female=film_Keys_For_female,
    films_333=Films_key_333,
    films_cao=Films_key_CAO,
)

_default_resolver = LanguageLabelResolver(
    languages=languages_key,
    nationalities=All_Nat,
    jobs_mens=jobs_mens_data,
    lang_key_m_map=lang_key_m,
    film_resolver=_film_resolver,
)


@functools.lru_cache(maxsize=None)
def Lang_work(suffix: str) -> str:
    """Process and retrieve language-related information based on input.

    This function provides backward compatibility by delegating to the
    LanguageProcessor class. It maintains the same interface as before.

    Args:
        suffix: A string representing a language or related term.

    Returns:
        The corresponding language label or an empty string if no match is found.
    """
    return _default_resolver.resolve(suffix)


__all__ = [
    "Lang_work",
    "LanguageLabelResolver",
    "FilmCategoryLabelResolver",
]
