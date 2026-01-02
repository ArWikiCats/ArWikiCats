import functools
import re

REGEX_MENS = re.compile(r"\b(men)\b", re.I)
REGEX_THE = re.compile(r"\b(the)\b", re.I)


@functools.lru_cache(maxsize=10000)
def fix_keys(category: str) -> str:
    category = category.lower().replace("category:", "")
    category = category.replace("'", "")

    replacements = {
        "expatriates": "expatriate",
        "canadian football": "canadian-football",
    }

    for old, new in replacements.items():
        category = category.replace(old, new)

    category = REGEX_THE.sub("", category)
    category = REGEX_MENS.sub("mens", category)
    return category.strip()
