"""
EventLab Bot - A class-based implementation to handle category labeling
"""

from __future__ import annotations

import functools
from typing import Callable, Literal, Tuple

from ...config import app_settings
from ...fix import fixtitle
from ...format_bots import change_cat
from ...helps import getLogger

logger = getLogger(__name__)
from ...main_processers.main_utils import list_of_cat_func_foot_ballers, list_of_cat_func_new
from ...translations import Ambassadors_tab
from ...translations.funcs import get_from_new_p17_final
from .. import tmp_bot
from ..common_resolver_chain import get_lab_for_country2
from ..data.mappings import combined_suffix_mappings
from ..end_start_bots import get_episodes, get_list_of_and_cat3, get_templates_fo
from ..make_bots import get_KAKO
from ..resolvers.country_resolver import event2_d2
from ..resolvers.separator_based_resolver import work_separator_names
from ..resolvers.sub_resolver import sub_translate_general_category
from . import country2_label_bot, with_years_bot, year_or_typeo
from .bot_2018 import get_pop_All_18

# Constants
SUFFIX_EPISODES: Literal[" episodes"] = " episodes"
SUFFIX_TEMPLATES: Literal[" templates"] = " templates"
CATEGORY_PEOPLE: Literal["people"] = "people"
LABEL_PEOPLE_AR: Literal["أشخاص"] = "أشخاص"
CATEGORY_SPORTS_EVENTS: Literal["sports events"] = "sports events"
LABEL_SPORTS_EVENTS_AR: Literal["أحداث رياضية"] = "أحداث رياضية"
ARABIC_CATEGORY_PREFIX: Literal["تصنيف:"] = "تصنيف:"
LIST_TEMPLATE_PLAYERS: Literal["لاعبو {}"] = "لاعبو {}"

# Type alias for resolver functions
ResolverFn = Callable[[str], str]


def _resolve_via_chain(category: str, resolvers: list[ResolverFn]) -> str:
    """
    Resolve a category by trying each resolver in order until one produces a non-empty label.

    Parameters:
        category (str): Category string to resolve.
        resolvers (list[ResolverFn]): Ordered list of resolver callables to try; the first non-empty return value is used.

    Returns:
        str: The first non-empty resolver result, or an empty string if none match.
    """
    for resolver in resolvers:
        result = resolver(category)
        if result:
            return result
    return ""


def translate_general_category_wrap(category: str) -> str:
    """
    Produce an Arabic label for a general category using available translation strategies.

    Parameters:
        category (str): Category title to translate.

    Returns:
        str: Arabic label if a translation is found, otherwise an empty string.
    """
    arlabel = "" or sub_translate_general_category(category) or work_separator_names(category)
    return arlabel


# Standard resolver chain for country-based labels
_STANDARD_COUNTRY_RESOLVERS: list[ResolverFn] = [
    get_lab_for_country2,
    get_pop_All_18,
    get_KAKO,
]


@functools.lru_cache(maxsize=10000)
def event_label_work(country: str) -> str:
    """
    Resolve an Arabic label for a country or country-like category.

    Parameters:
        country (str): Country name or category string to resolve; input is normalized (lowercased and stripped) before lookup.

    Returns:
        str: The resolved Arabic label if found, otherwise an empty string. Special case: if `country` (after normalization) equals "people", returns the people label constant.
    """
    country2 = country.lower().strip()

    if country2 == CATEGORY_PEOPLE:
        return LABEL_PEOPLE_AR

    # Extended resolver chain for event labels
    event_resolvers: list[ResolverFn] = [
        *_STANDARD_COUNTRY_RESOLVERS,
        lambda c: get_from_new_p17_final(c, ""),
        lambda c: Ambassadors_tab.get(c, ""),
        event2_d2,
        with_years_bot.wrap_try_with_years,
        year_or_typeo.label_for_startwith_year_or_typeo,
        translate_general_category_wrap,
    ]

    return _resolve_via_chain(country2, event_resolvers)


class EventLabResolver:
    """
    A class to handle event labelling functionality.
    Processes category titles and generates appropriate Arabic labels.
    """

    def __init__(self) -> None:
        """Initialize the EventLabResolver with default values."""
        self.foot_ballers: bool = False

    def _handle_special_suffixes(self, category3: str) -> Tuple[str, str, bool]:
        """
        Detects and handle special category suffixes and returns a list template marker plus the adjusted category string.

        Parameters:
            category3 (str): Category text to examine (expected normalized/lowercase).

        Returns:
            tuple[list_of_cat (str), updated_category3 (str)]:
            - list_of_cat: a list template marker or empty string if none was detected.
            - updated_category3: the category string with the detected suffix removed when applicable.

        Notes:
            This method may update self.foot_ballers as a side effect when the category is identified as a list of football players.
        """

        list_of_cat: str = ""

        if category3.endswith(SUFFIX_EPISODES):
            list_of_cat, category3 = get_episodes(category3)

        elif category3.endswith(SUFFIX_TEMPLATES):
            list_of_cat, category3 = get_templates_fo(category3)

        else:
            # Process with the main category processing function
            list_of_cat, self.foot_ballers, category3 = get_list_of_and_cat3(category3)

        return list_of_cat, category3

    def _get_country_based_label(self, original_cat3: str, list_of_cat: str) -> Tuple[str, str]:
        """
        Resolve a country-specific Arabic label when the category represents players from a country and adjust the list marker accordingly.

        Parameters:
            original_cat3 (str): The original, unmodified category string used to derive a country-based label.
            list_of_cat (str): Current list template (e.g., "لاعبو {}") indicating a list form that may be replaced.

        Returns:
            Tuple[str, str]: A tuple of (category_lab, list_of_cat) where `category_lab` is the resolved Arabic label or an empty string, and `list_of_cat` is the possibly-updated list template (cleared when a country-based label is produced).
        """
        category_lab: str = ""

        # ايجاد تسميات مثل لاعبو  كرة سلة أثيوبيون (Find labels like Ethiopian basketball players)
        if list_of_cat == LIST_TEMPLATE_PLAYERS:
            # Extended resolver chain for country-based labels
            country_resolvers: list[ResolverFn] = [
                country2_label_bot.country_2_title_work,
                *_STANDARD_COUNTRY_RESOLVERS,
                lambda c: translate_general_category_wrap(c),
            ]
            category_lab = _resolve_via_chain(original_cat3, country_resolvers)

            if category_lab:
                list_of_cat = ""

        return category_lab, list_of_cat

    def _apply_general_label_functions(self, category3: str) -> str:
        """
        Resolve a category title into its Arabic label using the module's general resolver chain.

        Tries the configured general resolver functions in order and returns the first non-empty label.

        Parameters:
            category3 (str): Category name to resolve (normalized, typically without the "category:" prefix).

        Returns:
            str: Resolved Arabic label, or an empty string if no resolver produced a label.
        """
        general_resolvers: list[ResolverFn] = [
            lambda c: translate_general_category_wrap(c),
            country2_label_bot.country_2_title_work,
            *_STANDARD_COUNTRY_RESOLVERS,
        ]
        return _resolve_via_chain(category3, general_resolvers)

    def _handle_suffix_patterns(self, category3: str) -> Tuple[str, str]:
        """
        Match and strip known suffix patterns from a category title.

        If the category ends with any configured suffix in combined_suffix_mappings, return the corresponding list template and the category with that suffix removed; otherwise return an empty list template and the original category.

        Parameters:
            category3 (str): Category title to inspect.

        Returns:
            tuple[str, str]: (list_of_cat, category3) where `list_of_cat` is the matched list template or an empty string, and `category3` is the category with the matched suffix removed and trimmed.
        """
        list_of_cat: str = ""

        for pri_ff, vas in combined_suffix_mappings.items():
            suffix = pri_ff.lower()
            if category3.endswith(suffix):
                logger.info(f'>>>><<lightblue>> category3.endswith pri_ff("{pri_ff}")')
                list_of_cat = vas
                category3 = category3[: -len(suffix)].strip()
                break

        return list_of_cat, category3

    def _process_list_category(self, cate_r: str, category_lab: str, list_of_cat: str) -> str:
        """
        Process list categories and format them appropriately.

        Args:
            cate_r (str): Original category string
            category_lab (str): Current category label
            list_of_cat (str): List of category template

        Returns:
            str: Updated category label
        """
        if not list_of_cat or not category_lab:
            return category_lab

        if self.foot_ballers:
            category_lab = list_of_cat_func_foot_ballers(cate_r, category_lab, list_of_cat)
        else:
            category_lab = list_of_cat_func_new(cate_r, category_lab, list_of_cat)

        return category_lab

    def process_category(self, category3: str, cate_r: str) -> str:
        """
        Resolve a category title into its Arabic label using special-case handlers, country-specific resolution, suffix/list processing, event/template resolvers, and general translation fallbacks.

        Parameters:
                category3 (str): Normalized category string to resolve.
                cate_r (str): Original/raw category string used as context for list formatting and logging.

        Returns:
                category_lab (str): The resolved Arabic label, or an empty string if no label could be determined.
        """
        original_cat3 = category3

        # First, try to get squad-related labels
        category_lab = ""

        # Initialize flags
        self.foot_ballers = False
        list_of_cat = ""

        # Handle special suffixes
        if not category_lab:
            list_of_cat, category3 = self._handle_special_suffixes(category3)

        # Handle country-based labels (e.g., basketball players from a country)
        if not category_lab and list_of_cat:
            country_lab, list_of_cat = self._get_country_based_label(original_cat3, list_of_cat)
            if country_lab:
                category_lab = country_lab

        # Apply various general label functions
        if not category_lab:
            category_lab = self._apply_general_label_functions(category3)

        # Handle categories that match predefined suffix patterns
        if not category_lab and not list_of_cat:
            list_of_cat, category3 = self._handle_suffix_patterns(category3)

        # Process with event_label_work if no label found yet
        if not category_lab:
            category_lab = event_label_work(category3)

        if list_of_cat and category3.lower().strip() == CATEGORY_SPORTS_EVENTS:
            category_lab = LABEL_SPORTS_EVENTS_AR

        # Process list categories if both exist
        if list_of_cat and category_lab:
            # Debug before calling list_of_cat_func_new
            if not isinstance(category_lab, str):
                logger.error(f"[BUG] category_lab is dict for cate_r={cate_r} value={category_lab}")
                raise TypeError(f"category_lab must be string, got {type(category_lab)}: {category_lab}")

            category_lab = self._process_list_category(cate_r, category_lab, list_of_cat)

        # Handle case where list exists but no label
        if list_of_cat and not category_lab:
            list_of_cat = ""
            category_lab = event_label_work(original_cat3)

        # Try template processing if no label yet
        if not category_lab:
            category_lab = tmp_bot.Work_Templates(original_cat3)

        # Try general translation again if still no label
        if not category_lab:
            category_lab = translate_general_category_wrap(original_cat3)

        return category_lab


@functools.lru_cache(maxsize=1)
def _load_resolver() -> EventLabResolver:
    """
    Provide a cached EventLabResolver instance.

    Returns:
        EventLabResolver: The resolver instance (cached for reuse).
    """
    resolver = EventLabResolver()
    return resolver


def _finalize_category_label(category_lab: str, cate_r: str) -> str:
    """
    Format a resolved category label for final output.

    Uses the original category string `cate_r` as context when fixing the label's title, prefixes the result with "تصنيف:", and returns an empty string if the final result is just the prefix.

    Parameters:
        cate_r (str): Original category string used as context for title fixing.

    Returns:
        str: The finalized category label prefixed with "تصنيف:", or an empty string if no label remains.
    """
    if category_lab:
        # Apply final formatting and prefix
        fixed = fixtitle.fixlabel(category_lab, en=cate_r)
        category_lab = f"{ARABIC_CATEGORY_PREFIX}{fixed}"

    if category_lab.strip() == ARABIC_CATEGORY_PREFIX:
        return ""

    return category_lab


def _process_category_formatting(category: str) -> str:
    """
    Process and format the input category string.

    Args:
        category (str): The raw category string

    Returns:
        str: lowercase version without prefix
    """
    if category.startswith("category:"):
        category = category.split("category:")[1]

    category = change_cat(category)

    return category


def event_Lab(cate_r: str) -> str:
    """
    Backward compatibility function that wraps the EventLabResolver class.

    Args:
        cate_r (str): The raw category string to process

    Returns:
        str: The Arabic label for the category
    """
    cate_r = cate_r.lower().replace("_", " ")
    category3: str = _process_category_formatting(cate_r)

    resolver = _load_resolver()

    result = resolver.process_category(category3, cate_r)

    result = _finalize_category_label(result, cate_r)
    return result
