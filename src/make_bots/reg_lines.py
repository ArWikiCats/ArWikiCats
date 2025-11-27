"""

Group of regex expressions used in the bot for later improvements

"""

import re

YEARS_REGEX_AR = (
    r"\d+[−–\-]\d+"
    # r"|\d+\s*(ق[\s\.]م|قبل الميلاد)*"
    r"|(?:عقد|القرن|الألفية)*\s*\d+\s*(ق[\s\.]م|قبل الميلاد)*"
)

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
    "YEARS_REGEX_AR",
    "RE1_compile",
    "RE2_compile",
    "RE3_compile",
    "re_sub_year",
    "RE33_compile",
]
