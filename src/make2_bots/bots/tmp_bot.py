"""
from .bots import tmp_bot
if not sub_ar_label:
    sub_ar_label = tmp_bot.Work_Templates(category)
"""

from ..format_bots import pp_start_with, pp_ends_with, pp_ends_with_pase
from ...helps.print_bot import print_put

from ..date_bots import with_years_bot

from ..ma_bots import contry2_lab
from ..ma_bots import ye_ts_bot

Work_Templates_cash = {}


def Work_Templates(input_string):
    """Generate work templates based on the provided input string.

    This function takes an input string, processes it to determine if it
    matches any predefined templates based on its suffix or prefix. It
    attempts to extract relevant information and format the output
    accordingly. The function checks both suffixes and prefixes against a
    set of predefined mappings and utilizes helper functions to retrieve
    additional data as needed.

    Args:
        input_string (str): The input string for which the work template is to be generated.

    Returns:
        str: The formatted work template based on the input string, or an empty
            string
        if no matching template is found.
    """

    # ---
    cash_key = input_string.lower().strip()
    # ---
    if cash_key in Work_Templates_cash:
        return Work_Templates_cash[cash_key]
    # ---
    print_put(f">> ----------------- start Work_ Templates ----------------- input_string:{input_string}")
    template_label = ""
    # pp_ends_with =  in pop_format

    # pp_ends_with_pase
    # pp_ends_with
    # merege pp_ends_with_pase and pp_ends_with
    merged_templates = {**pp_ends_with_pase, **pp_ends_with}

    for suffix, template in merged_templates.items():
        if not input_string.lower().endswith(suffix.lower()):
            continue
        base_string = input_string[:-len(suffix)]
        print_put(f'>>>><<lightblue>> Work_ Templates.endswith suffix("{suffix}"), base_string:"{base_string}"')

        U_lab = contry2_lab.get_lab_for_contry2(base_string)
        if not U_lab:
            U_lab = with_years_bot.get_label_with_years(base_string)

        if U_lab == "":
            # print("translate_general_category 2")
            U_lab = ye_ts_bot.translate_general_category(base_string)

        print_put(f'>>>><<lightblue>> Work_ Templates :"{input_string}", base_string :"{base_string}"')
        # ---
        if U_lab:
            print_put(f'>>>><<lightblue>> Work_ Templates.endswith suffix("{suffix}"), U_lab:"{U_lab}"')
            template_label = template.format(U_lab)
            print_put(f'>>>> template_label:"{template_label}"')
            # ---
            break

    # pp_ends_with
    if template_label:
        return template_label

    # pp_start_with
    for prefix, template in pp_start_with.items():
        if not input_string.startswith(prefix):
            continue
        base_string = input_string[len(prefix):]

        U_lab = contry2_lab.get_lab_for_contry2(base_string)

        if not U_lab:
            U_lab = with_years_bot.get_label_with_years(base_string)

        if U_lab == "":
            # print("translate_general_category 3")
            U_lab = ye_ts_bot.translate_general_category(base_string)

        print_put(f'>>>><<lightblue>> Work_ Templates :"{input_string}", base_string :"{base_string}"')
        if U_lab:
            print_put(f'>>>><<lightblue>> Work_ Templates.startswith prefix("{prefix}"), U_lab:"{U_lab}"')
            template_label = template.format(U_lab)
            print_put(f'>>>> template_label:"{template_label}"')
            # ---
            break

    print_put(">> ----------------- end Work_ Templates ----------------- ")
    # ---
    return template_label
