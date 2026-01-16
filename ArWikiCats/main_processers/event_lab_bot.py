"""
EventLab Bot - A class-based implementation to handle category labeling
"""
import functools
from typing import Tuple

from ..config import app_settings
from ..fix import fixtitle
from ..format_bots import change_cat
from ..helps import logger
from ..legacy_bots import sport_lab_suffixes, team_work, tmp_bot
from ..legacy_bots.films_and_others_bot import te_films
from ..legacy_bots.ma_bots import ye_ts_bot
from ..legacy_bots.ma_bots2.country2_label_bot import country_2_title_work
from ..legacy_bots.ma_bots.lab_seoo_bot import event_label_work
from ..legacy_bots.make_bots.bot_2018 import get_pop_All_18
from ..legacy_bots.make_bots.ends_keys import combined_suffix_mappings
from ..legacy_bots.matables_bots.table1_bot import get_KAKO
from ..legacy_bots.o_bots import parties_bot, univer
from ..legacy_bots.o_bots.peoples_resolver import work_peoples
from ..new.end_start_bots.fax2 import get_list_of_and_cat3
from ..new.end_start_bots.fax2_episodes import get_episodes
from ..new.end_start_bots.fax2_temp import get_templates_fo
from ..new_resolvers.reslove_all import new_resolvers_all
from ..new_resolvers.sports_resolvers.raw_sports import wrap_team_xo_normal_2025_with_ends
from ..time_resolvers import time_to_arabic
from ..time_resolvers.time_to_arabic import convert_time_to_arabic
from ..translations import get_from_new_p17_final, get_from_pf_keys2
from .main_utils import list_of_cat_func_foot_ballers, list_of_cat_func_new


@functools.lru_cache(maxsize=10000)
def wrap_lab_for_country2(country: str) -> str:
    """
    TODO: should be moved to functions directory.
    Retrieve laboratory information for a specified country.
    """

    country2 = country.lower().strip()

    resolved_label = (
        new_resolvers_all(country2)
        or get_from_pf_keys2(country2)
        or get_pop_All_18(country2)
        or te_films(country2)
        or sport_lab_suffixes.get_teams_new(country2)
        or parties_bot.get_parties_lab(country2)
        or team_work.Get_team_work_Club(country2)
        or univer.te_universities(country2)
        or work_peoples(country2)
        or get_KAKO(country2)
        or convert_time_to_arabic(country2)
        or get_pop_All_18(country2)
        or ""
    )
    logger.info(f'>> wrap_lab_for_country2 "{country2}": label: {resolved_label}')

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

    def _get_country_based_label(self, original_category3: str, list_of_cat: str) -> Tuple[str, str]:
        """
        Get country-based labels for specific categories like basketball players.

        Args:
            original_category3 (str): The original category string
            list_of_cat (str): Current list of category value

        Returns:
            Tuple[str, str]: Updated category label and list of category
        """
        category_lab: str = ""

        # ايجاد تسميات مثل لاعبو  كرة سلة أثيوبيون (Find labels like Ethiopian basketball players)
        if list_of_cat == "لاعبو {}":
            category_lab = (
                country_2_title_work(original_category3)
                or wrap_lab_for_country2(original_category3)
                or ye_ts_bot.translate_general_category(original_category3, start_get_country2=False, fix_title=False)
                or get_pop_All_18(original_category3.lower(), "")
                or ""
            )
            if category_lab:
                list_of_cat = ""

        return category_lab, list_of_cat

    def _apply_general_label_functions(self, category3: str) -> str:
        """
        Apply various general label functions in sequence.

        Args:
            category3 (str): The category string to process

        Returns:
            str: The processed category label or empty string
        """
        # Try different label functions in sequence
        category_lab: str = univer.te_universities(category3)
        if category_lab:
            return category_lab

        category_lab = time_to_arabic.convert_time_to_arabic(category3)
        if category_lab:
            return category_lab

        category_lab = wrap_team_xo_normal_2025_with_ends(category3) or new_resolvers_all(category3)
        if category_lab:
            return category_lab

        category_lab = get_pop_All_18(category3, "")
        if category_lab:
            return category_lab

        # If no label found yet, try general translation
        if not category_lab:
            category_lab = ye_ts_bot.translate_general_category(f"category:{category3}", fix_title=False)

        if category_lab:
            return category_lab

        category_lab = (
            country_2_title_work(category3)
            or wrap_lab_for_country2(category3)
            or ye_ts_bot.translate_general_category(category3, start_get_country2=False, fix_title=False)
            or get_pop_All_18(category3.lower(), "")
            or ""
        )
        if category_lab:
            return category_lab

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
        Main method to process a category and return its Arabic label.

        Args:
            cate_r (str): The raw category string to process

        Returns:
            str: The Arabic label for the category
        """
        original_category3 = category3

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
            country_lab, list_of_cat = self._get_country_based_label(original_category3, list_of_cat)
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
            category_lab = event_label_work(original_category3)

        # Try template processing if no label yet
        if not category_lab:
            category_lab = tmp_bot.Work_Templates(original_category3)

        # Try general translation again if still no label
        if not category_lab:
            category_lab = ye_ts_bot.translate_general_category(original_category3, fix_title=False)

        return category_lab


# Create global instance for backward compatibility


resolver = EventLabResolver()


def _finalize_category_label(category_lab: str, cate_r: str) -> str:
    """
    Finalize the category label by applying final formatting.

    Args:
        category_lab (str): The current category label
        cate_r (str): Original category string

    Returns:
        str: The final formatted category label
    """
    if category_lab:
        # Apply final formatting and prefix
        fixed = fixtitle.fixlabel(category_lab, en=cate_r)
        category_lab = f"تصنيف:{fixed}"

    return category_lab


def _handle_cricketer_categories(category3: str) -> str:
    """
    Handle special cricket player categories.

    Args:
        category3 (str): The lowercase category string

    Returns:
        str: The processed category label or empty string
    """
    category32: str = ""
    list_of_cat2: str = ""

    if category3.endswith(" cricketers"):
        list_of_cat2 = "لاعبو كريكت من {}"
        category32 = category3[: -len(" cricketers")]
    elif category3.endswith(" cricket captains"):
        list_of_cat2 = "قادة كريكت من {}"
        category32 = category3[: -len(" cricket captains")]

    if list_of_cat2 and category32:
        category3_lab = get_from_new_p17_final(category32)
        if category3_lab:
            return list_of_cat2.format(category3_lab)

    return ""


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

    result = ""

    if not result:
        result = resolver.process_category(cate_r, category3)

    # Handle cricket player categories
    if not result:
        result = _handle_cricketer_categories(category3)

    if not result:
        return ""

    result = _finalize_category_label(result, cate_r)
    if result == "تصنيف:":
        return ""

    return result
