"""
Template-based category label generation.

This module provides functionality to generate Arabic category labels
by matching English category names against predefined templates based
on suffixes and prefixes.
"""

import functools
import logging

from .common_resolver_chain import get_lab_for_country2
from .data.mappings import combined_suffix_mappings, pp_start_with
from .legacy_resolvers_bots.bot_2018 import get_pop_All_18
from .make_bots import get_KAKO

logger = logging.getLogger(__name__)


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

            resolved_label = (
                get_lab_for_country2(remaining_label) or get_pop_All_18(remaining_label) or get_KAKO(remaining_label)
            )
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

            resolved_label = get_lab_for_country2(base_label) or get_pop_All_18(base_label) or get_KAKO(base_label)
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
