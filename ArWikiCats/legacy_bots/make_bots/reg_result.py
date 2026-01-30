import functools
import re
from dataclasses import dataclass

from ...format_bots.relation_mapping import translation_category_relations
from ..utils.regex_hub import REGEX_SUB_CATEGORY_LOWERCASE, REGEX_SUB_MILLENNIUM_CENTURY


@functools.lru_cache(maxsize=1)
def _load_pattern() -> re.Pattern:
    """Load the regex pattern for the first line of categories."""
    # These patterns depend on dynamically generated values and are compiled at runtime
    _yy = (
        r"\d+(?:th|st|rd|nd)[−–\- ](?:millennium|century)?\s*(?:BCE*)?"
        r"|\d+(?:th|st|rd|nd)[−–\- ](?:millennium|century)?"
        r"|\d+[−–\-]\d+"
        r"|\d+s\s*(?:BCE*)?"
        r"|\d+\s*(?:BCE*)?"
    ).lower()

    _MONTHSTR3 = "(?:january|february|march|april|may|june|july|august|september|october|november|december)? *"

    _sorted_mapping = sorted(
        translation_category_relations.keys(),
        key=lambda k: (-k.count(" "), -len(k)),
    )
    _in_pattern = " |".join(map(re.escape, [n.lower() for n in _sorted_mapping]))

    _reg_line_1_match = (
        rf"(?P<monthyear>{_MONTHSTR3}(?:{_yy})|)\s*(?P<in>{_in_pattern}|)\s*(?P<country>.*|).*"
    )
    return re.compile(_reg_line_1_match, re.I)


REGEX_SEARCH_REG_LINE_1 = _load_pattern()


@dataclass
class TypiesResult:
    year_at_first: str
    year_at_first_strip: str
    in_str: str
    country: str
    cat_test: str


def get_cats(category_r: str) -> tuple[str, str]:
    """Normalize category strings and return raw and lowercase variants."""
    cate = REGEX_SUB_MILLENNIUM_CENTURY.sub(r"-\g<1>", category_r)
    cate3 = REGEX_SUB_CATEGORY_LOWERCASE.sub("", cate.lower())
    return cate, cate3


def get_reg_result(category_r: str) -> TypiesResult:
    """Extract structured pieces from categories that start with a year."""
    cate, cate3 = get_cats(category_r)
    cate = REGEX_SUB_CATEGORY_LOWERCASE.sub("", cate)

    cate_gory = cate.lower()
    cat_test = cate3
    match_it = REGEX_SEARCH_REG_LINE_1.search(cate_gory)

    year_first = ""
    country = ""
    in_str = ""

    if match_it:
        year_first = match_it.group("monthyear")
        country = match_it.group("country")
        in_str = match_it.group("in")

    if year_first and cate_gory.startswith(year_first):
        cat_test = cat_test.replace(year_first.lower(), "")

    if in_str == cate_gory or in_str == cate3:
        in_str = ""

    if in_str.strip() == "by":
        country = f"by {country}"

    if not year_first:
        country = ""

    return TypiesResult(
        year_at_first=year_first,
        year_at_first_strip=year_first.strip(),
        in_str=in_str,
        country=country,
        cat_test=cat_test,
    )
