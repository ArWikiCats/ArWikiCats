# -*- coding: utf-8 -*-
"""
This module provides functions to identify and convert English time-related
expressions (such as years, decades, centuries, and millennia) into their
Arabic equivalents.

It includes regular expressions for matching time expressions in both English
and Arabic, and a conversion function to translate English expressions.
"""
import re

REG_YEAR_EN = re.compile(
    r"\b"
    r"(?:January|February|March|April|May|June|July|August|September|October|November|December|)\s*"
    r"("
    r"\d+[−–-]\d+"
    r"|\d{1,4}s(?: BC| BCE|)?"
    r"|\d{4}"
    r")"
    r"\b",
    re.I
)


REG_CENTURY_EN = re.compile(
    r"\b\d+((?:st|nd|rd|th)(?:[- ])(?:century|millennium)(?: BCE| BC|))\b",
    re.I
)

REG_YEAR_AR = re.compile(
    r"\b"
    r"(?:يناير|فبراير|مارس|أبريل|مايو|يونيو|يوليو|أغسطس|سبتمبر|أكتوبر|نوفمبر|ديسمبر|)\s*"
    r"("
    r"\d+[−–-]\d+"
    r"|عقد \d{1,4} *(?:ق\.م|ق م|قبل الميلاد|)"
    r"|\d{4}"
    r")"
    r"\b",
    re.I
)

REG_CENTURY_AR = re.compile(
    r"\bب*(?:القرن|الألفية) \d+ *(?:ق\.م|ق م|قبل الميلاد|)\b",
    re.I
)


def match_time_ar(ar_value: str) -> list[str]:
    ar_matches = [m.group().strip() for m in REG_YEAR_AR.finditer(f" {ar_value} ")]
    ar_matches.extend([m.group().strip() for m in REG_CENTURY_AR.finditer(f" {ar_value} ")])
    return ar_matches


def match_time_en(en_key: str) -> list[str]:
    en_matches = [m.group().strip() for m in REG_YEAR_EN.finditer(f" {en_key} ")]
    en_matches.extend([m.group().strip() for m in REG_CENTURY_EN.finditer(f" {en_key} ")])
    return en_matches


def convert_time_to_arabic(en_year: str) -> str:
    """Convert an English time expression into its Arabic equivalent."""
    en_year = en_year.strip().replace("–", "-").replace("−", "-")
    month_map = {
        "january": "يناير", "february": "فبراير", "march": "مارس", "april": "أبريل",
        "may": "مايو", "june": "يونيو", "july": "يوليو", "august": "أغسطس",
        "september": "سبتمبر", "october": "أكتوبر", "november": "نوفمبر", "december": "ديسمبر",
    }

    # --- Month + Year ---
    m = re.match(r"^(%s)\s*(\d{4})" % "|".join(month_map.keys()), en_year, re.I)
    if m:
        month = month_map[m.group(1).lower()]
        return f"{month} {m.group(2)}"

    # --- Decade ---
    m = re.match(r"^(\d{1,4})s$", en_year)
    if m:
        return f"عقد {m.group(1)}"

    # --- Century ---
    m = re.match(r"^(\d+)(?:st|nd|rd|th)(?:[- ])century( BC| BCE)?$", en_year, re.I)
    if m:
        num = int(m.group(1))
        bc = " ق م" if m.group(2) else ""
        return f"القرن {num}{bc}"

    # --- Millennium ---
    m = re.match(r"^(\d+)(?:st|nd|rd|th)(?:[- ])millennium( BC| BCE)?$", en_year, re.I)
    if m:
        num = int(m.group(1))
        bc = " ق م" if m.group(2)  else ""
        return f"الألفية {num}{bc}"

    # --- Numeric range ---
    def expand_range(year_text: str) -> str:
        parts = year_text.split("-")
        if len(parts) == 1:
            return year_text
        try:
            first = int(parts[0].rstrip("s"))
            second = parts[1].rstrip("s")
            if len(second) == 2:
                prefix = str(first)[:len(str(first)) - 2]
                second = int(prefix + second)
            else:
                second = int(second)
            return f"{first}-{second}"
        except ValueError:
            return year_text

    if re.search(r"^\d+[-−–]\d+", en_year):
        return expand_range(en_year)

    # --- Fallback ---
    return en_year
