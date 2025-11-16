"""

Group of regex expressions used in the bot for later improvements

"""
import re

YEARS_REGEX = (
    r"\d+[−–\-]\d+"
    # r"|\d+\s*(ق[\s\.]م|قبل الميلاد)*"
    r"|(?:عقد|القرن|الألفية)*\s*\d+\s*(ق[\s\.]م|قبل الميلاد)*"
)

regex_make_year_lab = (
    r"(\d+[−–\-]\d+|\d+)("
    r"th century BCE|th millennium BCE|th century BC|th millennium BC|th century|th millennium"
    r"|st century BCE|st millennium BCE|st century BC|st millennium BC|st century|st millennium"
    r"|rd century BCE|rd millennium BCE|rd century BC|rd millennium BC|rd century|rd millennium"
    r"|nd century BCE|nd millennium BCE|nd century BC|nd millennium BC|nd century|nd millennium"
    r"| century BCE| millennium BCE| century BC| millennium BC| century| millennium|s BCE| BCE"
    r"|s BC| BC|s"
    r")"
)


regex_make_year_lab_old = (
    r"(\d+[−–\-]\d+|\d+)("
    r"th century BCE|th millennium BCE|th century BC|th millennium BC|th century|th millennium"
    r"|st century BCE|st millennium BCE|st century BC|st millennium BC|st century|st millennium"
    r"|rd century BCE|rd millennium BCE|rd century BC|rd millennium BC|rd century|rd millennium"
    r"|nd century BCE|nd millennium BCE|nd century BC|nd millennium BC|nd century|nd millennium"
    r"| century BCE| millennium BCE| century BC| millennium BC| century| millennium|s BCE| BCE"
    r"|s BC| BC|s"
    r")"
)

yy = (
    r"\d+(?:th|st|rd|nd)[−–\- ](?:millennium|century)?\s*(?:BCE*)?"
    r"|\d+(?:th|st|rd|nd)[−–\- ](?:millennium|century)?"
    r"|\d+[−–\-]\d+"
    r"|\d+s\s*(?:BCE*)?"
    r"|\d+\s*(?:BCE*)?"
)

yy_old = (
    r"\d+th century BCE|\d+th millennium BCE|\d+th century BC|\d+th millennium BC|\d+th century|\d+th millennium"
    r"|\d+st century BCE|\d+st millennium BCE|\d+st century BC|\d+st millennium BC|\d+st century|\d+st millennium"
    r"|\d+rd century BCE|\d+rd millennium BCE|\d+rd century BC|\d+rd millennium BC|\d+rd century|\d+rd millennium"
    r"|\d+nd century BCE|\d+nd millennium BCE|\d+nd century BC|\d+nd millennium BC|\d+nd century|\d+nd millennium"
    r"|\d+ century BCE|\d+ millennium BCE|\d+ century BC|\d+ millennium BC"
    r"|\d+ century|\d+ millennium|\d+s BCE|\d+ BCE"
    r"|\d+s BC|\d+ BC"
    r"|\d+s"
    r"|\d+[−–\-]\d+"
    r"|\d+"
)

# yyx = r"(\w+\s*\d+|\d+(th|st|rd)|\d+s\s*|\d+|)(\s*BCE|\s*BC|)(\s*century|\s*millennium)"

MONTHSTR2 = "(january |february |march |april |may |june |july |august |september |october |november |december |)"
tita_year = r"Category\:" + MONTHSTR2 + "(" + yy + "|).*"
tita_year = tita_year.lower()

tita = r"Category\:" + MONTHSTR2 + "(" + yy.lower() + "|)"

ddd = r"category\:(january|february|march|april|may|june|july|august|september|october|november|december|)\s*"

tita_year_no_month = r"category\:(|)\s*(" + yy + ").*"

tita_year_no_month = tita_year_no_month.lower()

# ----------------------------


RE1_compile = re.compile(r"^(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d).*", re.I)
RE2_compile = re.compile(r"^.*?\s*(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d)$", re.I)
RE3_compile = re.compile(r"^.*?\s*\((\d+\-\d+|\d+\–\d+|\d+\–present|\d+\−\d+|\d\d\d\d)\)$", re.I)

# ----------------------------

re_sub_year = r"^(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d)\s.*$"

# Category:American Soccer League (1933–83)
RE33_compile = re.compile(r"^.*?\s*(\((?:\d\d\d\d|\d+\-\d+|\d+\–\d+|\d+\–present|\d+\−\d+)\))$", re.I)
# RE4_compile = re.compile(r"^.*?\s*(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d) season$", re.I)

# ----------------------------


__all__ = [
    "YEARS_REGEX",
    "regex_make_year_lab",
    "yy",
    "tita_year",
    "tita",
    "ddd",
    "tita_year_no_month",
    "RE1_compile",
    "RE2_compile",
    "RE3_compile",
    "re_sub_year",
    "RE33_compile",
]
