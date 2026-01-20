"""
EventLab Bot - A class-based implementation to handle category labeling
"""

import functools
from typing import Tuple

from ..config import app_settings
from ..fix import fixtitle
from ..format_bots import change_cat
from ..helps import logger
from ..main_processers.main_utils import list_of_cat_func_foot_ballers, list_of_cat_func_new
from ..new.end_start_bots.fax2 import get_list_of_and_cat3
from ..new.end_start_bots.fax2_episodes import get_episodes
from ..new.end_start_bots.fax2_temp import get_templates_fo
from ..translations import Ambassadors_tab
from . import with_years_bot
from .common_resolver_chain import get_lab_for_country2
from .ma_bots import country_bot, general_resolver
from .ma_bots2 import country2_label_bot, year_or_typeo
from .make_bots.ends_keys import combined_suffix_mappings


@functools.lru_cache(maxsize=10000)
def event_label_work(country: str) -> str:
    country2 = country.lower().strip()

    if country2 == "people":
        return "أشخاص"

    resolved_label = (
        ""
        or get_lab_for_country2(country2)
        # or get_from_new_p17_final(country2, "")
        # or Ambassadors_tab.get(country2, "")
        or country_bot.event2_d2(country2)
        or with_years_bot.wrap_try_with_years(country2)
        or year_or_typeo.label_for_startwith_year_or_typeo(country2)
        or general_resolver.translate_general_category(country2)
    )
    return resolved_label


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
        Handle categories with special suffixes like episodes or templates.

        Args:
            category3 (str): The lowercase category string

        Returns:
            Tuple[str, str, bool]: List of category, updated category3, and whether Wikidata was found
        """

        list_of_cat: str = ""

        if category3.endswith(" episodes"):
            list_of_cat, category3 = get_episodes(category3)

        elif category3.endswith(" templates"):
            list_of_cat, category3 = get_templates_fo(category3)

        else:
            # Process with the main category processing function
            list_of_cat, self.foot_ballers, category3 = get_list_of_and_cat3(
                category3, find_stubs=app_settings.find_stubs
            )

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
        if list_of_cat == "لاعبو {}":
            category_lab = (
                ""
                or country2_label_bot.country_2_title_work(original_cat3)
                or get_lab_for_country2(original_cat3)
            )
            if category_lab:
                list_of_cat = ""

        return category_lab, list_of_cat

    def _apply_general_label_functions(self, category3: str) -> str:
        """
        Apply a series of general label resolvers to produce an Arabic label for a category.

        Attempts resolution in a prioritized sequence (university, time expressions, team/organization patterns, population-style labels, general translations, then country-specific/title fallbacks) and returns the first non-empty label found.

        Parameters:
            category3 (str): Category name to resolve (normalized text, typically without the "category:" prefix).

        Returns:
            str: Resolved Arabic label, or an empty string if no resolver produced a label.
        """
        # Try different label functions in sequence
        category_lab: str = (
            ""
            or general_resolver.translate_general_category(category3, fix_title=False)
            or country2_label_bot.country_2_title_work(category3)
            # or get_lab_for_country2(category3)
        )
        return category_lab

    def _handle_suffix_patterns(self, category3: str) -> Tuple[str, str]:
        """
        Handle categories that match predefined suffix patterns.

        Args:
            category3 (str): The category string to process

        Returns:
            Tuple[str, str]: List of category and updated category string
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
        Compute the Arabic label for a category string by applying special-case handlers, country-specific resolution, suffix/list processing, event/template resolvers, and general translation fallbacks.

        Parameters:
            category3 (str): The (possibly normalized) category string to resolve.
            cate_r (str): The original/raw category string used as context for list formatting and error messages.

        Returns:
            str: The resolved Arabic label for the category, or an empty string if no label could be determined.
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

        if list_of_cat and category3.lower().strip() == "sports events":
            category_lab = "أحداث رياضية"

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
        category_lab = f"تصنيف:{fixed}"

    if category_lab.strip() == "تصنيف:":
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
