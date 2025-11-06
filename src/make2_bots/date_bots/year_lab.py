import re
from ..matables_bots.bot import MONTH_table
from ...helps.log import logger
from ..reg_lines import regex_make_year_lab

en_letters = "[abcdefghijklmnopqrstuvwxyz]"

def make_year_lab(year_str: str) -> str:  # 21st century
    """Converts a year string into an Arabic label."""
    suffix = " ق م " if " bc" in year_str or " bce" in year_str else ""
    year_numeric = re.sub(regex_make_year_lab.lower(), r"\g<1>", year_str)
    year_no_bc = year_str.split(" bce")[0].split(" bc")[0]
    year_text = re.sub(r"\d+", "", year_no_bc).strip()

    lab_map = {
        "s": f"عقد {year_numeric}{suffix}",
        "century": f"القرن {year_numeric}{suffix}",
        "millennium": f"الألفية {year_numeric}{suffix}",
    }

    if not year_text:
        result = year_numeric + suffix
    elif year_text.lower() in MONTH_table:
        year_value = re.sub(year_text, "", year_no_bc).strip()
        result = f"{MONTH_table[year_text]} {year_value}{suffix}"
        logger.debug(f' test_2 "{result}":')
    elif year_text in lab_map:
        result = lab_map[year_text]
    elif re.sub(r"\d+", "", year_str.strip()) in ["", "-", "–", "−"]:
        result = year_str
    else:
        result = ""

    if re.search(en_letters, result, flags=re.IGNORECASE):
        result = ""

    if result:
        logger.info(f'>>>> make_year_lab: "{year_str}", "{result}":')
    return result

def make_month_lab(month_str: str) -> str:  # 21st century
    """Converts a month string into an Arabic label."""
    if re.match(r"^\d+$", month_str.strip()):
        return month_str.strip()

    result = ""
    month_text = re.sub(r"\d+$", "", month_str).strip()
    if month_text.lower() in MONTH_table:
        month_value = re.sub(month_text, "", month_str).strip()
        result = f"{MONTH_table[month_text.lower()]} {month_value}"
        logger.debug(f' test_2 "{result}":')

    if re.sub(r"\d+", "", month_str.strip()) in ["", "-", "–", "−"]:
        result = month_str

    if re.search(en_letters, result, flags=re.IGNORECASE):
        result = ""

    if result:
        logger.info(f'>>>> year_lab.make_month_lab: "{month_str}", "{result}":')
    return result
