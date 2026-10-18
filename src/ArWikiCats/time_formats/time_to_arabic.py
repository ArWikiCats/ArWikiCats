"""
This module provides functions to identify and convert English time-related
expressions (such as years, decades, centuries, and millennia) into their
Arabic equivalents.

It includes regular expressions for matching time expressions in both English
and Arabic, and a conversion function to translate English expressions.
"""

import functools
import re

MONTH_MAP = {
    "january": "يناير",
    "february": "فبراير",
    "march": "مارس",
    "april": "أبريل",
    "may": "مايو",
    "june": "يونيو",
    "july": "يوليو",
    "august": "أغسطس",
    "september": "سبتمبر",
    "october": "أكتوبر",
    "november": "نوفمبر",
    "december": "ديسمبر",
}
century_millennium_regex = r"(\d+)(?:st|nd|rd|th)(?:[−–\- ])(century|millennium)\s*(BCE|BC)?"
decade_regex = r"(\d{1,4})s\s*(BCE|BC)?"

REG_YEAR_EN = re.compile(
    r"\b"
    r"(?:January|February|March|April|May|June|July|August|September|October|November|December)?\s*"
    r"("
    r"\d+[−–\-]\d+"
    rf"|{decade_regex}"
    r"|\d{1,4}\s*(?:BCE|BC)?"
    r")"
    r"\b",
    re.I,
)
REG_CENTURY_EN = re.compile(rf"\b{century_millennium_regex}\b", re.I)

REG_YEAR_AR = re.compile(
    r"\b"
    r"(?:يناير|فبراير|مارس|أبريل|مايو|يونيو|يوليو|أغسطس|سبتمبر|أكتوبر|نوفمبر|ديسمبر)?\s*"
    r"("
    r"\d+[−–\-]\d+"
    r"|عقد \d{1,4} *(?:ق\.م|ق م|قبل الميلاد)?"
    r"|(?:القرن|الألفية)? \d{1,4} *(?:ق\.م|ق م|قبل الميلاد)?"
    r")"
    r"\b",
    re.I,
)

REG_CENTURY_AR = re.compile(r"\bب*(?:القرن|الألفية) \d+ *(?:ق\.م|ق م|قبل الميلاد)?\b", re.I)

# Additional precompiled regex patterns
REG_SUB_CATEGORY = re.compile(r"^Category:", re.I)
REG_YEAR_BC_PATTERN = re.compile(r"^(\d+)\s*(BCE|BC)$", re.I)
REG_YEAR_RANGE_PATTERN = re.compile(r"^\d+[−–\-]\d+$", re.I)

# Month-related patterns
MONTH_STR = "|".join(MONTH_MAP.keys())
REG_MONTH_YEAR = re.compile(rf"^({MONTH_STR})\s*(\d+)\s*$", re.I)
REG_MONTH_YEAR_BC = re.compile(rf"^({MONTH_STR})\s*" + r"(\d{1,4})\s*(BCE|BC)$", re.I)
REG_DECADE = re.compile(rf"^{decade_regex}$", re.I)
REG_CENTURY_MILLENNIUM = re.compile(rf"^{century_millennium_regex}$", re.I)

# --- Numeric range ---


def expand_range(year_text: str) -> str:
    """Expand shorthand year ranges like ``1990-92`` into full spans."""
    parts = year_text.split("-")
    if len(parts) == 1:
        return year_text
    try:
        first = int(parts[0].rstrip("s"))
        second = parts[1].rstrip("s")
        if len(second) == 2:
            prefix = str(first)[: len(str(first)) - 2]
            second = int(prefix + second)
        else:
            second = int(second)
        return f"{first}-{second}"
    except ValueError:
        return year_text


def match_time_ar(ar_value: str) -> list[str]:
    """Find Arabic year-like expressions within a string."""
    ar_matches = [m.group().strip() for m in REG_YEAR_AR.finditer(f" {ar_value} ")]
    # ar_matches.extend([m.group().strip() for m in REG_CENTURY_AR.finditer(f" {ar_value} ")])
    return ar_matches


def match_time_ar_first(ar_key: str) -> str:
    """Return the first English time match or an empty string."""
    ar_matches = match_time_ar(ar_key)
    return ar_matches[0] if ar_matches else ""


def match_time_en(en_key: str) -> list[str]:
    """Locate English year or century expressions within a string."""
    en_key = REG_SUB_CATEGORY.sub("", en_key)
    en_matches = [m.group().strip() for m in REG_YEAR_EN.finditer(f" {en_key} ")]
    en_matches.extend([m.group().strip() for m in REG_CENTURY_EN.finditer(f" {en_key} ")])
    return en_matches


def match_time_en_first(en_key: str) -> str:
    """Return the first English time match or an empty string."""
    en_matches = match_time_en(en_key)
    return en_matches[0] if en_matches else ""


def convert_time_to_arabic(en_year: str) -> str:
    """Convert an English time expression into its Arabic equivalent."""
    en_year = en_year.strip()  # .replace("–", "-").replace("−", "-")

    if en_year.lower().startswith("the "):
        en_year = en_year[4:]

    if en_year.isdigit():
        return en_year

    # --- Month ---
    if MONTH_MAP.get(en_year.lower()):
        return MONTH_MAP[en_year.lower()]

    # --- Month + Year ---
    m = REG_MONTH_YEAR.match(en_year)
    if m:
        month = MONTH_MAP[m.group(1).lower()]
        result = f"{month} {m.group(2)}"
        return result

    # --- Month + Year + BC ---
    m = REG_MONTH_YEAR_BC.match(en_year)
    if m:
        month = MONTH_MAP[m.group(1).lower()]
        bc = " ق م"
        result = f"{month} {m.group(2)}{bc}"
        return result

    # --- Year + BC ---
    m = REG_YEAR_BC_PATTERN.match(en_year)
    if m:
        result = f"{m.group(1)} ق م"
        return result

    # --- Decade (with optional BC/BCE) ---
    m = REG_DECADE.match(en_year)
    if m:
        bc = " ق م" if m.group(2) else ""
        result = f"عقد {m.group(1)}{bc}"
        return result

    # --- Century/Millennium ---
    m = REG_CENTURY_MILLENNIUM.match(en_year)
    if m:
        num = int(m.group(1))
        bc = " ق م" if m.group(3) else ""
        ty = "القرن" if m.group(2) == "century" else "الألفية"
        result = f"{ty} {num}{bc}"
        return result

    if REG_YEAR_RANGE_PATTERN.match(en_year):
        # --- (no expansion wanted) ---
        # return expand_range(en_year)
        return en_year

    # --- Fallback ---
    return ""


@functools.lru_cache(maxsize=10000)
def match_en_return_ar(category: str) -> dict[str, str]:
    """Convert an English time expression into its Arabic equivalent."""
    en_years = match_time_en(category)
    data = {year: convert_time_to_arabic(year) for year in en_years}
    return data


__all__ = [
    "match_time_ar",
    "match_time_en",
    "match_time_en_first",
    "match_time_ar_first",
    "convert_time_to_arabic",
    "match_en_return_ar",
]
