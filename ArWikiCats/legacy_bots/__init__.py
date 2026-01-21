"""
Wrapper for legacy category resolvers.
This module coordinates several older resolution strategies to provide
backward compatibility for category translation logic.
"""

from __future__ import annotations

import functools
import re

from ..helps import logger


class LegacyBotsResolver:
    """
    A class-based resolver that encapsulates all legacy category resolution logic.

    This class replaces the previous RESOLVER_PIPELINE list-based approach with
    a structured, object-oriented design. Each resolver method is tried in sequence
    until one returns a non-empty result.

    The resolution order is:
    1. University categories (highest priority)
    2. Country and event-based patterns
    3. Year-based categories
    4. Year prefix patterns and typo handling
    5. General event labeling
    6. General category translation (lowest priority, catch-all)
    """

    # Common blocked words that certain resolvers check
    _COMMON_BLOCKED_WORDS = ("in", "of", "from", "by", "at")

    def __init__(self) -> None:
        """Initialize the LegacyBotsResolver."""
        # Pre-compile or cache any resources needed by resolvers
        pass

    def _normalize_input(self, text: str) -> str:
        """
        Normalize the input text for processing.

        This method provides a common normalization step that can be used
        by multiple resolvers to avoid code duplication.

        Args:
            text: The raw input text to normalize

        Returns:
            The normalized text
        """
        return text.strip()

    def _has_blocked_prepositions(self, text: str) -> bool:
        """
        Check if text contains common English prepositions.

        This is a shared utility used by multiple resolvers (country_bot.event2_d2
        and with_years_bot.wrap_try_with_years) to filter out categories with
        certain English prepositions.

        Args:
            text: The text to check (should be lowercase)

        Returns:
            True if any blocked preposition is found, False otherwise
        """
        text_lower = text.lower()
        return any(f" {word} " in text_lower for word in self._COMMON_BLOCKED_WORDS)

    def _resolve_university_category(self, text: str) -> str:
        """
        Resolve university-related categories.

        This resolver handles specialized university category patterns,
        including university names with cities and academic subjects.

        Args:
            text: Category text to resolve

        Returns:
            Arabic university label or empty string if no match
        """
        from ..sub_new_resolvers import university_resolver

        logger.debug(f"LegacyBotsResolver: Trying university resolver for '{text}'")
        result = university_resolver._university_bot.search(university_resolver._normalise_category(text))
        if result:
            logger.info(f"LegacyBotsResolver: University resolver found: {result}")
        return result

    def _resolve_country_event(self, text: str) -> str:
        """
        Resolve country and event-based categories.

        This resolver handles categories related to countries and events,
        blocking those with common English prepositions.

        Args:
            text: Category text to resolve

        Returns:
            Arabic country/event label or empty string if no match
        """
        from .legacy_resolvers_bots.country_bot import _retriever

        logger.debug(f"LegacyBotsResolver: Trying country event resolver for '{text}'")
        cat3 = text.lower().replace("category:", "").strip()
        logger.info(f'<<lightred>>>>>> category33:"{cat3}" ')

        # Reject strings that contain common English prepositions
        blocked = ("in", "of", "from", "by", "at")
        if any(f" {word} " in cat3.lower() for word in blocked):
            return ""

        category_lab = ""
        if re.sub(r"^\d", "", cat3) == cat3:
            category_lab = _retriever.get_country_label(cat3)

        if category_lab:
            logger.info(f"LegacyBotsResolver: Country event resolver found: {category_lab}")
        return category_lab

    def _resolve_with_years(self, text: str) -> str:
        """
        Resolve year-based categories.

        This resolver handles categories that start with years or contain
        year ranges, blocking those with common English prepositions.

        Args:
            text: Category text to resolve

        Returns:
            Arabic year-based label or empty string if no match
        """
        from .legacy_resolvers_bots.with_years_bot import Try_With_Years

        logger.debug(f"LegacyBotsResolver: Trying with_years resolver for '{text}'")
        cat3 = text.lower().replace("category:", "").strip()
        logger.info(f'<<lightred>>>>>> category33:"{cat3}" ')

        # Reject strings that contain common English prepositions
        blocked = ("in", "of", "from", "by", "at")
        if any(f" {word} " in cat3.lower() for word in blocked):
            return ""

        category_lab = ""
        if re.sub(r"^\d", "", cat3) != cat3:
            category_lab = Try_With_Years(cat3)

        if category_lab:
            logger.info(f"LegacyBotsResolver: With_years resolver found: {category_lab}")
        return category_lab

    def _resolve_year_or_typeo(self, text: str) -> str:
        """
        Resolve categories with year prefixes or typo patterns.

        This resolver handles categories that begin with years or type
        information, building complex labels from year and country components.

        Args:
            text: Category text to resolve

        Returns:
            Arabic year/type label or empty string if no match
        """
        from .legacy_resolvers_bots.year_or_typeo import _label_for_startwith_year_or_typeo
        from ..time_formats import match_time_en_first, convert_time_to_arabic

        logger.debug(f"LegacyBotsResolver: Trying year_or_typeo resolver for '{text}'")
        category_r = re.sub(r"category:", "", text.lower()).strip()

        if match_time_en_first(category_r):
            result = convert_time_to_arabic(category_r)
        else:
            result = _label_for_startwith_year_or_typeo(category_r)

        if result:
            logger.info(f"LegacyBotsResolver: Year_or_typeo resolver found: {result}")
        return result

    def _resolve_event_lab(self, text: str) -> str:
        """
        Resolve general event labeling.

        This is a comprehensive resolver that handles various event-related
        categories, including sports, templates, episodes, and more.

        Args:
            text: Category text to resolve

        Returns:
            Arabic event label or empty string if no match
        """
        from .legacy_resolvers_bots.event_lab_bot import _load_resolver, _process_category_formatting, _finalize_category_label

        logger.debug(f"LegacyBotsResolver: Trying event_lab resolver for '{text}'")
        cate_r = text.lower().replace("_", " ")
        category3 = _process_category_formatting(cate_r)

        resolver = _load_resolver()
        result = resolver.process_category(category3, cate_r)
        result = _finalize_category_label(result, cate_r)

        if result:
            logger.info(f"LegacyBotsResolver: Event_lab resolver found: {result}")
        return result

    def _resolve_general_category(self, text: str, start_get_country2: bool = True, fix_title: bool = True) -> str:
        """
        Resolve general category translation (catch-all).

        This is the final fallback resolver that attempts to translate
        any remaining categories using general translation strategies.

        Args:
            text: Category text to resolve
            start_get_country2: Whether to enable enhanced country lookup
            fix_title: Whether to apply title fixing to the result

        Returns:
            Arabic general label or empty string if no match
        """
        from .legacy_resolvers_bots.general_resolver import _translate_general_category
        from ..fix import fixtitle

        logger.debug(f"LegacyBotsResolver: Trying general resolver for '{text}'")
        category = text.replace("_", " ")
        category = re.sub(r"category:", "", category, flags=re.IGNORECASE)

        logger.info(f"<<lightyellow>>>> ^^^^^^^^^ translate_general_category start ^^^^^^^^^ ({category}) ")
        logger.debug(f"<<lightyellow>>>>>> category_r={text}, {start_get_country2=}, {fix_title=}")

        arlabel = _translate_general_category(text, category, start_get_country2)

        if arlabel and fix_title:
            arlabel = fixtitle.fixlabel(arlabel, en=text)
            logger.info(f'>>>>>> <<green>>test: cat "{text}", {arlabel=}')

        if arlabel:
            logger.debug(f"<<lightyellow>>>> translate_general_category {arlabel=}  ")
            logger.info(f"LegacyBotsResolver: General resolver found: {arlabel}")

        logger.debug("<<lightyellow>>>> ^^^^^^^^^ translate_general_category end ^^^^^^^^^ ")
        return arlabel

    @functools.lru_cache(maxsize=None)
    def resolve(self, text: str) -> str:
        """
        Resolve a category label using the legacy resolver chain in priority order.

        This method implements a pipeline pattern, iterating through registered
        resolvers until one returns a non-empty result. The resolvers are tried
        in the order defined by the class methods.

        Args:
            text: Category name or identifier to resolve

        Returns:
            The resolved category label, or an empty string if no legacy
            resolver produces a value
        """
        # Normalize input once for all resolvers
        normalized_text = self._normalize_input(text)

        logger.debug(f"LegacyBotsResolver: Starting resolution for '{normalized_text}'")

        # Try each resolver in sequence (priority order)
        resolvers = [
            self._resolve_university_category,
            self._resolve_country_event,
            self._resolve_with_years,
            self._resolve_year_or_typeo,
            self._resolve_event_lab,
            self._resolve_general_category,
        ]

        for resolver_method in resolvers:
            category_label = resolver_method(normalized_text)
            if category_label:
                logger.info(f"LegacyBotsResolver: Resolved '{normalized_text}' to '{category_label}'")
                return category_label

        logger.debug(f"LegacyBotsResolver: No resolution found for '{normalized_text}'")
        return ""


# Create a singleton instance of the resolver
_resolver_instance = LegacyBotsResolver()


@functools.lru_cache(maxsize=None)
def legacy_resolvers(changed_cat: str) -> str:
    """
    Resolve a category label using the legacy resolver chain in priority order.

    This function provides backward compatibility by delegating to the
    LegacyBotsResolver class instance.

    Parameters:
        changed_cat (str): Category name or identifier to resolve.

    Returns:
        category_label (str): The resolved category label, or an empty string
            if no legacy resolver produces a value.
    """
    return _resolver_instance.resolve(changed_cat)


__all__ = [
    "legacy_resolvers",
    "LegacyBotsResolver",
]
