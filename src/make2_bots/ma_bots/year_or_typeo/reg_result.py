
import re
from dataclasses import dataclass
from ...format_bots import category_relation_mapping
from ....translations.type_tables import basedtypeTable
from ....translations.utils.patterns import load_keys_to_pattern_new

# These patterns depend on dynamically generated values and are compiled at runtime
yy = (
    r"\d+(?:th|st|rd|nd)[−–\- ](?:millennium|century)?\s*(?:BCE*)?"
    r"|\d+(?:th|st|rd|nd)[−–\- ](?:millennium|century)?"
    r"|\d+[−–\-]\d+"
    r"|\d+s\s*(?:BCE*)?"
    r"|\d+\s*(?:BCE*)?"
).lower()

MONTHSTR3 = "(?:january|february|march|april|may|june|july|august|september|october|november|december)? *"

typeo_pattern = load_keys_to_pattern_new(list(basedtypeTable))
in_pattern = load_keys_to_pattern_new(category_relation_mapping.keys(), by=" |")

reg_line_1_match = (
    rf"(?P<monthyear>{MONTHSTR3}(?:{yy})|)\s*"
    r"(?P<typeo>" + typeo_pattern.lower() + r"|)\s*"
    r"(?P<in>" + in_pattern.lower() + r"|)\s*"
    r"(?P<country>.*|).*"
)

REGEX_SEARCH_REG_LINE_1 = re.compile(reg_line_1_match, re.I)

# Precompiled Regex Patterns
REGEX_SUB_MILLENNIUM_CENTURY = re.compile(r"[−–\-](millennium|century)", re.I)
REGEX_SUB_CATEGORY_LOWERCASE = re.compile(r"category:", re.IGNORECASE)


@dataclass
class Typies:
    year_at_first: str
    typeo: str
    In: str
    country: str
    cat_test: str


def get_cats(category_r):
    cate = REGEX_SUB_MILLENNIUM_CENTURY.sub(r"-\g<1>", category_r)
    cate3 = REGEX_SUB_CATEGORY_LOWERCASE.sub("", cate.lower())
    return cate, cate3


def get_reg_result(category_r: str) -> Typies:
    cate, cate3 = get_cats(category_r)
    cate = REGEX_SUB_CATEGORY_LOWERCASE.sub("", cate)
    cate_gory = cate.lower()
    cat_test = cate3
    match_it = REGEX_SEARCH_REG_LINE_1.search(cate_gory)
    year_at_first = ""
    typeo = ""
    country = ""
    In = ""
    if match_it:
        year_at_first = match_it.group('monthyear')
        typeo = match_it.group("typeo")
        country = match_it.group("country")
        In = match_it.group("in")
    if year_at_first and cate_gory.startswith(year_at_first):
        cat_test = cat_test.replace(year_at_first.lower(), "")
    if In == cate_gory or In == cate3:
        In = ""
    if In.strip() == "by":
        country = f"by {country}"
    if not year_at_first and not typeo:
        country = ""
    # if country.lower() == cate_gory.lower().replace("category:", ""): country = ""
    # Category:january 2025 disasters during Covid-19
    # year_at_first='january 2025 ', typeo='disasters', In='during ', country='covid-19', cat_test='january 2025 disasters during covid-19'
    # print(f"{year_at_first=}, {typeo=}, {In=}, {country=}, {cat_test=}\n" * 10)
    return Typies(
        year_at_first=year_at_first,
        typeo=typeo,
        In=In,
        country=country,
        cat_test=cat_test,
    )
