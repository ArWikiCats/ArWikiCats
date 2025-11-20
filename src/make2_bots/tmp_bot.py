"""
Template-based category label generation.

This module provides functionality to generate Arabic category labels
by matching English category names against predefined templates based
on suffixes and prefixes.
"""

import functools
from typing import Optional

from ..helps.log import logger
from .date_bots import with_years_bot
from .format_bots import pp_ends_with, pp_ends_with_pase, pp_start_with
from .ma_bots import country2_lab, ye_ts_bot


def _resolve_label(label: str) -> str:
    """Try multiple resolution strategies for a label.

    Args:
        label: The label to resolve

    Returns:
        Resolved Arabic label or empty string
    """
    resolved_label = country2_lab.get_lab_for_country2(label)
    if not resolved_label:
        resolved_label = with_years_bot.Try_With_Years(label)
    if not resolved_label:
        resolved_label = ye_ts_bot.translate_general_category(label)
    return resolved_label


@functools.lru_cache(maxsize=10000)
def Work_Templates(input_label: str) -> str:
    """Generate Arabic category labels based on predefined templates.

    This function attempts to match the input label against predefined
    templates based on suffixes and prefixes, using multiple resolution
    strategies to generate appropriate Arabic labels.

    Args:
        input_label: The input string for which the template-based label
                    is to be generated.

    Returns:
        The formatted Arabic label based on matching templates, or an
        empty string if no matching template is found.
    """
    # Normalize input for consistent caching
    input_label = input_label.lower().strip()
    logger.info(f">> ----------------- start Work_ Templates ----------------- input_label:{input_label}")

    template_label = ""

    # Merge pp_ends_with_pase and pp_ends_with for efficiency
    combined_suffix_mappings = {**pp_ends_with_pase, **pp_ends_with}

    # Try suffix matching - more efficient iteration
    for suffix, format_template in combined_suffix_mappings.items():
        if input_label.endswith(suffix.lower()):
            base_label = input_label[: -len(suffix)]
            logger.info(f'>>>><<lightblue>> Work_ Templates.endswith suffix("{suffix}"), base_label:"{base_label}"')

            resolved_label = _resolve_label(base_label)
            logger.info(f'>>>><<lightblue>> Work_ Templates :"{input_label}", base_label :"{base_label}"')

            if resolved_label:
                logger.info(f'>>>><<lightblue>> Work_ Templates.endswith suffix("{suffix}"), resolved_label:"{resolved_label}"')
                template_label = format_template.format(resolved_label)
                logger.info(f'>>>> template_label:"{template_label}"')
                break

    if template_label:
        return template_label

    # Try prefix matching
    for prefix, format_template in pp_start_with.items():
        if input_label.startswith(prefix.lower()):
            remaining_label = input_label[len(prefix):]

            resolved_label = _resolve_label(remaining_label)
            logger.info(f'>>>><<lightblue>> Work_ Templates :"{input_label}", remaining_label :"{remaining_label}"')

            if resolved_label:
                logger.info(f'>>>><<lightblue>> Work_ Templates.startswith prefix("{prefix}"), resolved_label:"{resolved_label}"')
                template_label = format_template.format(resolved_label)
                logger.info(f'>>>> template_label:"{template_label}"')
                break

    logger.info(">> ----------------- end Work_ Templates ----------------- ")
    return template_label
