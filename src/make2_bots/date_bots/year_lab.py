import re
from ..matables_bots.bot import MONTH_table
from ...helps.log import logger
from ..reg_lines import regex_make_year_lab

en_letters = "[abcdefghijklmnopqrstuvwxyz]"


def get_year_label(year_string: str) -> str:  # 21st century
    # ---

    suffix = ""
    year_number = re.sub(regex_make_year_lab.lower(), r"\g<1>", year_string)

    if " bc" in year_string or " bce" in year_string:
        suffix = " ق م "

    year_string_no_suffix = year_string.split(" bce")[0].split(" bc")[0]
    non_digit_chars = re.sub(r"\d+", "", year_string_no_suffix).strip()

    label = ""
    if not non_digit_chars:
        label = year_number + suffix

    elif non_digit_chars.lower() in MONTH_table:
        year_number_only = re.sub(non_digit_chars, "", year_string_no_suffix).strip()
        label = f"{MONTH_table[non_digit_chars]} {year_number_only}{suffix}"
        logger.debug(f' non_digit_chars "{label}":')

    elif non_digit_chars == "s":
        label = f"عقد {year_number}{suffix}"

    elif "century" in year_string:
        label = f"القرن {year_number}{suffix}"

    elif "millennium" in year_string:
        label = f"الألفية {year_number}{suffix}"

    non_digit_chars_only = re.sub(r"\d+", "", year_string.strip())
    allowed_non_digit_chars = ["", "-", "–", "−"]
    if non_digit_chars_only in allowed_non_digit_chars:
        label = year_string

    cleaned_label = re.sub(en_letters, "", label, flags=re.IGNORECASE)
    if cleaned_label != label:
        label = ""

    if label:
        logger.info(f'>>>> get_year_label: "{year_string}", "{label}":')
    return label


def get_month_label(text: str) -> str:  # 21st century
    if re.match(r"^\d+$", text.strip()):
        return text.strip()

    label = ""

    text_no_digits = re.sub(r"\d+$", "", text).strip()
    if text_no_digits.lower() in MONTH_table:
        year_number = re.sub(text_no_digits, "", text).strip()
        label = f"{MONTH_table[text_no_digits.lower()]} {year_number}"
        logger.debug(f' text_no_digits "{label}":')

    # if label != text:

    non_digit_chars_only = re.sub(r"\d+", "", text.strip())
    allowed_non_digit_chars = ["", "-", "–", "−"]
    if non_digit_chars_only in allowed_non_digit_chars:
        label = text

    cleaned_label = re.sub(en_letters, "", label, flags=re.IGNORECASE)
    if cleaned_label != label:
        label = ""

    if label:
        logger.info(f'>>>> year_lab.get_month_label: "{text}", "{label}":')
    return label
