"""
from .bots import tmp_bot
if not sub_ar_label:
    sub_ar_label = tmp_bot.Work_Templates(category)
"""

import functools

from ..format_bots import pp_start_with, pp_ends_with, pp_ends_with_pase
from ...helps.print_bot import print_put

from ..date_bots import with_years_bot

from ..ma_bots import country2_lab
from ..ma_bots import ye_ts_bot


@functools.lru_cache(maxsize=None)
def Work_Templates(input_label: str) -> str:
    """Generate work templates based on the provided input string.

    This function takes an input string, processes it to determine if it
    matches any predefined templates based on its suffix or prefix. It
    attempts to extract relevant information and format the output
    accordingly. The function checks both suffixes and prefixes against a
    set of predefined mappings and utilizes helper functions to retrieve
    additional data as needed.

    Args:
        input_label (str): The input string for which the work template is to be generated.

    Returns:
        str: The formatted work template based on the input string, or an empty
            string
        if no matching template is found.
    """

    # Normalize input for consistent caching
    input_label = input_label.lower().strip()
    # ---
    print_put(f">> ----------------- start Work_ Templates ----------------- input_label:{input_label}")
    template_label = ""
    # pp_ends_with =  in pop_format

    # pp_ends_with_pase
    # pp_ends_with
    # merege pp_ends_with_pase and pp_ends_with
    combined_suffix_mappings = {**pp_ends_with_pase, **pp_ends_with}

    for suffix, format_template in combined_suffix_mappings.items():
        if not input_label.lower().endswith(suffix.lower()):
            continue
        base_label = input_label[:-len(suffix)]
        print_put(f'>>>><<lightblue>> Work_ Templates.endswith suffix("{suffix}"), base_label:"{base_label}"')

        resolved_label = country2_lab.get_lab_for_country2(base_label)
        if not resolved_label:
            resolved_label = with_years_bot.Try_With_Years(base_label)

        if resolved_label == "":
            # print("translate_general_category 2")
            resolved_label = ye_ts_bot.translate_general_category(base_label)

        print_put(f'>>>><<lightblue>> Work_ Templates :"{input_label}", base_label :"{base_label}"')
        # ---
        if resolved_label:
            print_put(f'>>>><<lightblue>> Work_ Templates.endswith suffix("{suffix}"), resolved_label:"{resolved_label}"')
            template_label = format_template.format(resolved_label)
            print_put(f'>>>> template_label:"{template_label}"')
            break

    # pp_ends_with
    if template_label:
        return template_label

    # pp_start_with
    for prefix, format_template in pp_start_with.items():
        if not input_label.startswith(prefix):
            continue
        remaining_label = input_label[len(prefix):]

        resolved_label = country2_lab.get_lab_for_country2(remaining_label)

        if not resolved_label:
            resolved_label = with_years_bot.Try_With_Years(remaining_label)

        if resolved_label == "":
            # print("translate_general_category 3")
            resolved_label = ye_ts_bot.translate_general_category(remaining_label)

        print_put(f'>>>><<lightblue>> Work_ Templates :"{input_label}", remaining_label :"{remaining_label}"')
        if resolved_label:
            print_put(f'>>>><<lightblue>> Work_ Templates.startswith prefix("{prefix}"), resolved_label:"{resolved_label}"')
            template_label = format_template.format(resolved_label)
            print_put(f'>>>> template_label:"{template_label}"')
            break

    print_put(">> ----------------- end Work_ Templates ----------------- ")
    # ---
    return template_label
