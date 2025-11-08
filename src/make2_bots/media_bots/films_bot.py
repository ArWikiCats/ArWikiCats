#!/usr/bin/python3
"""Resolve media-related categories to their Arabic labels."""

import re
from typing import Dict

from ...helps.print_bot import main_output_preferences, output_test, print_def_head
from ..jobs_bots.test4_bots.t4_2018_jobs import test4_2018_Jobs
from ..jobs_bots.test_4 import Jobs_in_Multi_Sports, nat_match, test4_2018_with_nat
from ..matables_bots.bot import Add_to_main2_tab, Films_O_TT, New_players
from ..media_bots.film_keys_bot import get_Films_key_CAO
from ..o_bots import fax
from ..o_bots.army import test_army
from ..p17_bots import p17_bot

RESOLVED_CATEGORY_CACHE: Dict[str, str] = {}


def test_films(category: str, reference_category: str = "") -> str:
    normalized_category = category.lower()
    if normalized_category in RESOLVED_CATEGORY_CACHE:
        cached_label = RESOLVED_CATEGORY_CACHE[normalized_category]
        output_test(f'>>>> normalized_category: "{normalized_category}" already resolved, label:"{cached_label}"')
        return cached_label

    print_def_head(f"<<lightblue>>>> xxxxxxxxxx test_films normalized_category:{normalized_category} xxxxxxxxxxx ")
    resolved_label = ""

    if re.match(r"^\d+$", normalized_category.strip()):
        resolved_label = normalized_category.strip()

    if not resolved_label:
        resolved_label = get_Films_key_CAO(normalized_category)

    if not resolved_label:
        resolved_label = Jobs_in_Multi_Sports(normalized_category, out=main_output_preferences[1])
        if resolved_label:
            New_players[normalized_category] = resolved_label
            Add_to_main2_tab(normalized_category, resolved_label)
            output_test(f'>>>> Jobs_in_Multi Sports: New_players[{normalized_category}] ="{resolved_label}"')

    if not resolved_label:
        resolved_label = test4_2018_with_nat(normalized_category, out=main_output_preferences[1], reference_category=reference_category)
        if resolved_label:
            Add_to_main2_tab(normalized_category, resolved_label)
            Films_O_TT[normalized_category] = resolved_label

    if not resolved_label:
        resolved_label = test4_2018_Jobs(normalized_category, out=main_output_preferences[1])
        if resolved_label:
            New_players[normalized_category] = resolved_label
            Add_to_main2_tab(normalized_category, resolved_label)
            output_test(f'>>>> test_4 2018 Jobs: New_players[{normalized_category}] ="{resolved_label}"')

    if not resolved_label:
        resolved_label = nat_match(normalized_category)
        if resolved_label:
            Add_to_main2_tab(normalized_category, resolved_label)
            output_test(f'>>>> nat_match: [{normalized_category}] ="{resolved_label}"')
    if not resolved_label:
        resolved_label = p17_bot.Get_P17(normalized_category)

    if not resolved_label:
        resolved_label = p17_bot.Get_P17_2(normalized_category)

    if not resolved_label:
        resolved_label = fax.test_language(normalized_category)

    if not resolved_label:
        resolved_label = test_army(normalized_category)

    if not resolved_label:
        resolved_label = test4_2018_Jobs(normalized_category, out=main_output_preferences[1])

    RESOLVED_CATEGORY_CACHE[normalized_category] = resolved_label
    print_def_head(f"<<lightblue>>>> xxxxxxxxx test_films end xxxxxxxxxxx resolved_label:{resolved_label}")
    return resolved_label
