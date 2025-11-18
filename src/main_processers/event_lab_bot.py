"""
EventLab Bot - A class-based implementation to handle category labeling
"""
from typing import Tuple
from ..new.end_start_bots.fax2 import get_list_of_and_cat3
from ..new.end_start_bots.fax2_temp import get_templates_fo
from ..new.end_start_bots.fax2_episodes import get_episodes

from ..make2_bots.ma_bots.squad_title_bot import get_squad_title
from ..fix import fixtitle
from ..helps.log import logger
from ..translations import New_P17_Finall, Get_New_team_xo
from ..make2_bots import tmp_bot
from ..make2_bots.date_bots import year_lab
from ..make2_bots.format_bots import change_cat, pp_ends_with, pp_ends_with_pase
from ..make2_bots.lazy_data_bots.bot_2018 import get_pop_All_18
from ..make2_bots.o_bots import univer

from ..make2_bots.ma_bots import list_cat_format, ye_ts_bot
from ..make2_bots.ma_bots.country2_bot import Get_country2
from ..make2_bots.ma_bots.lab_seoo_bot import event_Lab_seoo
from ..config import app_settings


from pathlib import Path
from ..helps.jsonl_dump import save_data

# @functools.lru_cache(maxsize=None)


@save_data(Path(__file__).parent / "get_list_of_and_cat3_with_lab2.jsonl", ["category3_o"])
def get_list_of_and_cat3_with_lab2(category3_o: str) -> str:
    """
    Process squad-related category labels.

    Args:
        category3_o (str): The original category string

    Returns:
        str: The processed category label or empty string
    """
    category_lab = ""
    list_of_cat = ""
    category3 = category3_o.strip()

    if category3.endswith(" squad templates"):
        list_of_cat = "قوالب تشكيلات {}"
        category3 = category3[: -len(" squad templates")]
        cate_labs = get_squad_title(category3)
        if cate_labs:
            category_lab = f"قوالب {cate_labs}"

    elif category3.endswith(" squad navigational boxes"):
        list_of_cat = "صناديق تصفح تشكيلات {}"
        category3 = category3[: -len(" squad navigational boxes")]
        cate_labs = get_squad_title(category3)
        if cate_labs:
            category_lab = f"صناديق تصفح {cate_labs}"

    if category_lab:
        logger.debug(f'<<lightblue>>get_list_of_and_cat3_with_lab(): {list_of_cat=}, {category3=}, {category_lab=}')
        logger.debug(f"<<lightblue>>(): {category3_o=}, {category_lab=}")

    return category_lab


class EventLabResolver:
    """
    A class to handle event labelling functionality.
    Processes category titles and generates appropriate Arabic labels.
    """

    def __init__(self) -> None:
        """Initialize the EventLabResolver with default values."""
        self.foot_ballers: bool = False

    def _process_category_formatting(self, cate_r: str) -> Tuple[str, str, str]:
        """
        Process and format the input category string.

        Args:
            cate_r (str): The raw category string

        Returns:
            Tuple[str, str, str]: Formatted category, lowercase version without prefix, original without prefix
        """
        category: str = cate_r.lower()
        category = category.replace("_", " ")
        if not category.startswith("category:"):
            category = f"category:{category}"
        category = change_cat(category)

        category3_nolower: str = cate_r
        if category3_nolower.startswith("Category:"):
            category3_nolower = category3_nolower.split("Category:")[1]

        category3: str = category.lower()
        if category3.startswith("category:"):
            category3 = category3.split("category:")[1]

        return category, category3_nolower, category3

    def _handle_special_suffixes(self, category3: str, category3_nolower: str) -> Tuple[str, str, bool]:
        """
        Handle categories with special suffixes like episodes or templates.

        Args:
            category3 (str): The lowercase category string
            category3_nolower (str): The original category string without prefix

        Returns:
            Tuple[str, str, bool]: List of category, updated category3, and whether Wikidata was found
        """
        list_of_cat: str = ""

        if category3.endswith(" episodes"):
            list_of_cat, category3 = get_episodes(category3, category3_nolower)

        elif category3.endswith(" templates"):
            list_of_cat, category3 = get_templates_fo(category3)

        else:
            # Process with the main category processing function
            list_of_cat, self.foot_ballers, category3 = get_list_of_and_cat3(
                category3,
                category3_nolower,
                app_settings.find_stubs
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
            category_lab = Get_country2(original_category3)
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

        category_lab = year_lab.make_year_lab(category3)
        if category_lab:
            return category_lab

        category_lab = Get_New_team_xo(category3)
        if category_lab:
            return category_lab

        category_lab = get_pop_All_18(category3, "")
        if category_lab:
            return category_lab

        # If no label found yet, try general translation
        if not category_lab:
            category_lab = ye_ts_bot.translate_general_category(f"category:{category3}")
        if category_lab:
            return category_lab

        category_lab = Get_country2(category3)
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

        for data in [pp_ends_with_pase, pp_ends_with]:
            for pri_ff, vas in data.items():
                suffix = pri_ff.lower()
                if category3.endswith(suffix):
                    logger.info(f'>>>><<lightblue>> category3.endswith pri_ff("{pri_ff}")')
                    list_of_cat = vas
                    category3 = category3[: -len(suffix)].strip()
                    break
            if list_of_cat:
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
        if list_of_cat and category_lab:
            category_lab, list_of_cat = list_cat_format.list_of_cat_func(
                cate_r,
                category_lab,
                list_of_cat,
                self.foot_ballers
            )

        return category_lab

    def _handle_cricketer_categories(self, category3: str, category3_nolower: str) -> str:
        """
        Handle special cricket player categories.

        Args:
            category3 (str): The lowercase category string
            category3_nolower (str): The original category string without prefix

        Returns:
            str: The processed category label or empty string
        """
        category32: str = ""
        list_of_cat2: str = ""

        if category3.endswith(" cricketers"):
            list_of_cat2 = "لاعبو كريكت من {}"
            category32 = category3_nolower[: -len(" cricketers")]
        elif category3.endswith(" cricket captains"):
            list_of_cat2 = "قادة كريكت من {}"
            category32 = category3_nolower[: -len(" cricket captains")]

        if list_of_cat2 and category32:
            category3_lab = New_P17_Finall.get(category32.lower(), "")
            if category3_lab:
                return list_of_cat2.format(category3_lab)

        return ""

    def _finalize_category_label(self, category_lab: str, cate_r: str) -> str:
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
            fixed = fixtitle.fixlab(category_lab, en=cate_r)
            category_lab = f"تصنيف:{fixed}"

        return category_lab

    def process_category(self, cate_r: str) -> str:
        """
        Main method to process a category and return its Arabic label.

        Args:
            cate_r (str): The raw category string to process

        Returns:
            str: The Arabic label for the category
        """
        # Process and format the category
        category, category3_nolower, category3 = self._process_category_formatting(cate_r)
        original_category3 = category3

        # First, try to get squad-related labels
        category_lab = get_list_of_and_cat3_with_lab2(category3)

        # Initialize flags
        self.foot_ballers = False
        list_of_cat = ""

        # Handle special suffixes
        if not category_lab:
            list_of_cat, category3 = self._handle_special_suffixes(
                category3,
                category3_nolower
            )

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

        # Process with event_Lab_seoo if no label found yet
        if not category_lab:
            category_lab = event_Lab_seoo("", category3)

        # Process list categories if both exist
        if list_of_cat and category_lab:
            # Debug before calling list_of_cat_func
            if not isinstance(category_lab, str):
                logger.error(f"[BUG] category_lab is dict for cate_r={cate_r} value={category_lab}")
                raise TypeError(f"category_lab must be string, got {type(category_lab)}: {category_lab}")

            category_lab = self._process_list_category(cate_r, category_lab, list_of_cat)

        # Handle case where list exists but no label
        if list_of_cat and not category_lab:
            list_of_cat = ""
            category_lab = event_Lab_seoo(cate_r, original_category3)

        # Try template processing if no label yet
        if not category_lab:
            category_lab = tmp_bot.Work_Templates(original_category3)

        # Try general translation again if still no label
        if not category_lab:
            category_lab = ye_ts_bot.translate_general_category(original_category3)

        # Handle cricket player categories
        if not category_lab:
            cricket_label = self._handle_cricketer_categories(category3, category3_nolower)
            if cricket_label:
                category_lab = cricket_label

        # Finalize the label
        category_lab = self._finalize_category_label(category_lab, cate_r)

        return category_lab


# Create global instance for backward compatibility


resolver = EventLabResolver()


def event_Lab(cate_r: str) -> str:
    """
    Backward compatibility function that wraps the EventLabResolver class.

    Args:
        cate_r (str): The raw category string to process

    Returns:
        str: The Arabic label for the category
    """
    return resolver.process_category(cate_r)
