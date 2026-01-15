"""
Template-based category label generation.

This module provides functionality to generate Arabic category labels
by matching English category names against predefined templates based
on suffixes and prefixes.
"""

import functools
from ..helps import logger
from ..ma_bots import ye_ts_bot
from ..time_resolvers import with_years_bot
from .format_bots.ends_keys import pp_ends_with, pp_ends_with_pase, pp_start_with
from ..make_bots.films_and_others_bot import te_films
from ..make_bots.lazy_data_bots.bot_2018 import get_pop_All_18
from ..make_bots.matables_bots.table1_bot import get_KAKO
from ..make_bots.o_bots import parties_bot, univer
from ..make_bots.o_bots.peoples_resolver import work_peoples
from ..make_bots.reslove_relations.rele import resolve_relations_label
from ..make_bots.sports_bots import sport_lab_suffixes, team_work
from ..new_resolvers.countries_names_resolvers.us_states import resolve_us_states
from ..new_resolvers.sports_resolvers.sport_lab_nat import sport_lab_nat_load_new
from ..time_resolvers.time_to_arabic import convert_time_to_arabic
from ..translations import get_from_pf_keys2


def _resolve_label(label: str) -> str:
    """Try multiple resolution strategies for a label.

    Args:
        label: The label to resolve

    Returns:
        Resolved Arabic label or empty string
    """
    resolved_label = (
        resolve_relations_label(label)
        or get_from_pf_keys2(label)
        or get_pop_All_18(label)
        or te_films(label)
        or sport_lab_nat_load_new(label)
        or sport_lab_suffixes.get_teams_new(label)
        or parties_bot.get_parties_lab(label)
        or team_work.Get_team_work_Club(label)
        or univer.te_universities(label)
        or resolve_us_states(label)
        or work_peoples(label)
        or get_KAKO(label)
        or convert_time_to_arabic(label)
        or get_pop_All_18(label)
        or with_years_bot.Try_With_Years(label)
        or ye_ts_bot.translate_general_category(label, fix_title=False)
        or ""
    )
    return resolved_label


def create_label_from_prefix(input_label):
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
    template_label = ""

    # Merge pp_ends_with_pase and pp_ends_with for efficiency
    combined_suffix_mappings = {**pp_ends_with_pase, **pp_ends_with}

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
    """
    """
    input_label = input_label.lower().strip()
    logger.info(f">> ----------------- start Work_ Templates ----------------- {input_label=}")

    template_label = (
        create_label_from_suffix(input_label)
        or create_label_from_prefix(input_label)
    )

    logger.info(">> ----------------- end Work_ Templates ----------------- ")
    return template_label
