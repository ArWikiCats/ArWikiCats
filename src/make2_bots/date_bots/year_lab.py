import re
from ..matables_bots.bot import MONTH_table
from ...helps.log import logger

en_literes = "[abcdefghijklmnopqrstuvwxyz]"


def make_year_lab(year: str) -> str:  # 21st century
    # ---
    tata = (
        r"\d+(th century BCE|th millennium BCE|th century BC|th millennium BC|th century|th millennium"
        + "|st century BCE|st millennium BCE|st century BC|st millennium BC|st century|st millennium"
        + "|rd century BCE|rd millennium BCE|rd century BC|rd millennium BC|rd century|rd millennium"
        + "|nd century BCE|nd millennium BCE|nd century BC|nd millennium BC|nd century|nd millennium"
        + "| century BCE| millennium BCE| century BC| millennium BC| century| millennium|s BCE| BCE"
        + "|s BC| BC|s)"
    )

    su = ""
    _ye_ = re.sub(tata.lower(), r"\g<1>", year)

    if " bc" in year or " bce" in year:
        su = " ق م "

    year2 = year.split(" bce")[0].split(" bc")[0]
    test_2 = re.sub(r"\d+", "", year2).strip()

    y_l = ""
    if not test_2:
        y_l = _ye_ + su

    elif test_2.lower() in MONTH_table:
        fa2 = re.sub(test_2, "", year2).strip()
        y_l = f"{MONTH_table[test_2]} {fa2}{su}"
        logger.debug(f' test_2 "{y_l}":')

    elif test_2 == "s":
        y_l = f"عقد {_ye_}{su}"

    elif "century" in year:
        y_l = f"القرن {_ye_}{su}"

    elif "millennium" in year:
        y_l = f"الألفية {_ye_}{su}"

    tst3 = re.sub(r"\d+", "", year.strip())
    test3_results = ["", "-", "–", "−"]
    if tst3 in test3_results:
        y_l = year

    kaka = re.sub(en_literes, "", y_l, flags=re.IGNORECASE)
    if kaka != y_l:
        y_l = ""

    if y_l:
        logger.info(f'>>>> make_year_lab: "{year}", "{y_l}":')
    return y_l


def make_month_lab(year: str) -> str:  # 21st century
    y_l = ""

    tata = r"(January |February |March |April |May |June |July |August |September |October |November |December |)(\d+)".lower()

    if re.match(r"^\d+$", year.strip()):
        return year.strip()

    _ye_ = re.sub(tata.lower(), r"\g<1>", year)
    if _ye_ == year:
        _ye_ = ""
    logger.info(f' _ye_ "{_ye_}":')

    year2 = year
    test_2 = re.sub(r"\d+$", "", year2).strip()
    if test_2.lower() in MONTH_table:
        fa2 = re.sub(test_2, "", year2).strip()
        y_l = f"{MONTH_table[test_2.lower()]} {fa2}"
        logger.debug(f' test_2 "{y_l}":')

    # if y_l != year:

    tst3 = re.sub(r"\d+", "", year.strip())
    test3_results = ["", "-", "–", "−"]
    if tst3 in test3_results:
        y_l = year

    kaka = re.sub(en_literes, "", y_l, flags=re.IGNORECASE)
    if kaka != y_l:
        y_l = ""

    if y_l:
        logger.info(f'>>>> year_lab.make_month_lab: "{year}", "{y_l}":')
    return y_l
