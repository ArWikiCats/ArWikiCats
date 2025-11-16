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

# yyx = r"(\w+\s*\d+|\d+(th|st|rd)|\d+s\s*|\d+|)(\s*BCE|\s*BC|)(\s*century|\s*millennium)"

ddd = r"category\:(january|february|march|april|may|june|july|august|september|october|november|december|)\s*"

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
    "ddd",
    "tita_year_no_month",
    "RE1_compile",
    "RE2_compile",
    "RE3_compile",
    "re_sub_year",
    "RE33_compile",
]
