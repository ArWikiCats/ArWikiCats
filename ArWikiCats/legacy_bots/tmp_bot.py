"""
Template-based category label generation.

This module provides functionality to generate Arabic category labels
by matching English category names against predefined templates based
on suffixes and prefixes.
"""

import functools

from ..helps import logger
from ..new_resolvers import all_new_resolvers
from ..new_resolvers.languages_resolves import resolve_languages_labels_with_time
from ..time_formats.time_to_arabic import convert_time_to_arabic
from ..translations import People_key, get_from_pf_keys2
from . import sport_lab_suffixes, team_work, with_years_bot
from .ma_bots import general_resolver
from .make_bots.bot_2018 import get_pop_All_18
from .make_bots.ends_keys import combined_suffix_mappings
from .matables_bots.table1_bot import get_KAKO
from .o_bots import parties_resolver, university_resolver
from ..new_resolvers.other_resolvers.peoples_resolver import work_peoples

pp_start_with = {
    "wikipedia categories named after": "تصنيفات سميت بأسماء {}",
    "candidates for president of": "مرشحو رئاسة {}",
    # "candidates in president of" : "مرشحو رئاسة {}",
    "candidates-for": "مرشحو {}",
    # "candidates for" : "مرشحو {}",
    "categories named afters": "تصنيفات سميت بأسماء {}",
    "scheduled": "{} مقررة",
    # "defunct" : "{} سابقة",
}


def _resolve_label(label: str) -> str:
    """
    Resolve an English category label into Arabic using a sequence of resolver strategies.

    Parameters:
        label (str): English category label to resolve.

    Returns:
        str: Resolved Arabic label if any strategy matches, otherwise an empty string.
    """
    resolved_label = (
        all_new_resolvers(label)
        or get_from_pf_keys2(label)
        or get_pop_All_18(label)
        or resolve_languages_labels_with_time(label)
        or People_key.get(label)
        or sport_lab_suffixes.get_teams_new(label)
        or parties_resolver.get_parties_lab(label)
        or team_work.Get_team_work_Club(label)
        or university_resolver.resolve_university_category(label)
        or work_peoples(label)
        or get_KAKO(label)
        or convert_time_to_arabic(label)
        or get_pop_All_18(label)
        or with_years_bot.Try_With_Years(label)
        or general_resolver.translate_general_category(label, fix_title=False)
        or ""
    )
    return resolved_label


def create_label_from_prefix(input_label):
    """
    Generate an Arabic category label when the English input starts with a known prefix.

    Parameters:
        input_label (str): English category label to match against known prefixes; matching is case-insensitive.

    Returns:
        str: Arabic label formatted from the matching prefix template if a resolved base label is found, otherwise an empty string.
    """
    template_label = ""

    for prefix, format_template in pp_start_with.items():
        if input_label.startswith(prefix.lower()):
            remaining_label = input_label[len(prefix) :]

            resolved_label = _resolve_label(remaining_label)
            logger.info(f'>>>><<lightblue>> Work_ Templates :"{input_label}", {remaining_label=}')

            if resolved_label:
                logger.info(f'>>>><<lightblue>> Work_ Templates.startswith prefix("{prefix}"), {resolved_label=}')
                template_label = format_template.format(resolved_label)
                logger.info(f">>>> {template_label=}")
                break
    return template_label


def create_label_from_suffix(input_label):
    """
    Create an Arabic category label when the English input ends with a known suffix template.

    Parameters:
        input_label (str): English category label to match against known suffix templates.

    Returns:
        str: The formatted Arabic label if a suffix-based resolution succeeds, otherwise an empty string.
    """
    template_label = ""

    # Try suffix matching - more efficient iteration
    for suffix, format_template in combined_suffix_mappings.items():
        if input_label.endswith(suffix.lower()):
            base_label = input_label[: -len(suffix)]
            logger.info(f'>>>><<lightblue>> Work_ Templates.endswith suffix("{suffix}"), {base_label=}')

            resolved_label = _resolve_label(base_label)
            logger.info(f'>>>><<lightblue>> Work_ Templates :"{input_label}", {base_label=}')

            if resolved_label:
                logger.info(f'>>>><<lightblue>> Work_ Templates.endswith suffix("{suffix}"), {resolved_label=}')
                template_label = format_template.format(resolved_label)
                logger.info(f">>>> {template_label=}")
                break

    return template_label


@functools.lru_cache(maxsize=10000)
def Work_Templates(input_label: str) -> str:
    """Generate Arabic category labels using template-based matching.

    This function attempts to match input labels against predefined templates
    based on known prefixes and suffixes to generate appropriate Arabic labels.

    Args:
        input_label: The English category label to process

    Returns:
        The corresponding Arabic label if a match is found, otherwise an empty string
    """
    input_label = input_label.lower().strip()
    logger.info(f">> ----------------- start Work_ Templates ----------------- {input_label=}")
    data = {
        "sports leagues": "دوريات رياضية",
    }
    template_label = (
        data.get(input_label) or create_label_from_suffix(input_label) or create_label_from_prefix(input_label)
    )

    logger.info(">> ----------------- end Work_ Templates ----------------- ")
    return template_label
