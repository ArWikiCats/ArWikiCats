import re

from ..matables_bots.bot import MONTH_table
from ...helps.log import logger
from ..reg_lines import regex_make_year_lab
# from ...new.time_to_arabic import convert_time_to_arabic

ENGLISH_LETTERS_PATTERN = "[abcdefghijklmnopqrstuvwxyz]"

# make_year_lab = convert_time_to_arabic
# make_month_lab = convert_time_to_arabic


def make_year_lab(year: str) -> str:  # 21st century
    year = year.strip()
    # ---
    if year.isdigit():
        return year

    suffix = ""
    normalized_year = re.sub(regex_make_year_lab.lower(), r"\g<1>", year)

    if " bc" in f" {year} " or " bce" in f" {year} ":
        suffix = " ق م "

    year_without_suffix = year.split(" bce")[0].split(" bc")[0]
    non_numeric_part = re.sub(r"\d+", "", year_without_suffix).strip()

    year_label = ""
    if not non_numeric_part:
        year_label = normalized_year + suffix

    elif non_numeric_part.lower() in MONTH_table:
        month_number_segment = re.sub(non_numeric_part, "", year_without_suffix).strip()
        year_label = f"{MONTH_table[non_numeric_part.lower()]} {month_number_segment}{suffix}"
        logger.debug(f' test_2 "{year_label}":')

    elif non_numeric_part == "s":
        year_label = f"عقد {normalized_year}{suffix}"

    elif "century" in year:
        year_label = f"القرن {normalized_year}{suffix}"

    elif "millennium" in year:
        year_label = f"الألفية {normalized_year}{suffix}"

    sanitized_year = re.sub(r"\d+", "", year.strip())
    allowed_suffixes = ["", "-", "–", "−"]
    if sanitized_year in allowed_suffixes:
        year_label = year

    arabic_label_candidate = re.sub(ENGLISH_LETTERS_PATTERN, "", year_label, flags=re.IGNORECASE)
    if arabic_label_candidate != year_label:
        year_label = ""

    if year_label:
        logger.info(f'>>>> make_year_lab: "{year}", "{year_label}":')
    return year_label


def make_month_lab(year: str) -> str:  # 21st century
    year = year.strip()
    if year.isdigit():
        return year

    year_label = ""

    year_without_numeric_suffix = year
    non_numeric_part = re.sub(r"\d+$", "", year_without_numeric_suffix).strip()
    if non_numeric_part.lower() in MONTH_table:
        month_number_segment = re.sub(non_numeric_part, "", year_without_numeric_suffix).strip()
        year_label = f"{MONTH_table[non_numeric_part.lower()]} {month_number_segment}"
        logger.debug(f' test_2 "{year_label}":')

    # if y_l != year:

    sanitized_year = re.sub(r"\d+", "", year.strip())
    allowed_suffixes = ["", "-", "–", "−"]
    if sanitized_year in allowed_suffixes:
        year_label = year

    arabic_label_candidate = re.sub(ENGLISH_LETTERS_PATTERN, "", year_label, flags=re.IGNORECASE)
    if arabic_label_candidate != year_label:
        year_label = ""

    if year_label:
        logger.info(f'>>>> year_lab.make_month_lab: "{year}", "{year_label}":')
    return year_label
