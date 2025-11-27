#
import re
from ...helps.log import logger


def add_definite_article(label: str) -> str:
    """Prefix each word in ``label`` with the Arabic definite article."""
    label_without_article = re.sub(r" ", " ال", label)
    new_label = f"ال{label_without_article}"
    return new_label


def resolve_p17_2_label(category: str, templates: dict, nat_key: str, country_data: dict, add_article: bool = False) -> str:
    """Resolve gendered nationality templates for P17-style categories."""
    category = category.strip()
    if not category:
        return ""

    for suffix1, template in templates.items():
        suffix_key = f" {suffix1.strip().lower()}"

        if not category.lower().endswith(suffix_key):
            continue

        country_prefix = category[: -len(suffix_key)].strip()

        # nat_data = countries_nat_en_key.get(country_prefix) or countries_nat_en_key.get(country_prefix.lower(), {})
        nat_data = country_data.get(country_prefix) or country_data.get(country_prefix.lower(), {})
        nat_label = nat_data.get(nat_key, "")

        if not nat_label:
            logger.info(f"<<lightblue>>>>>> No {nat_key} label for {country_prefix}")
            continue

        if add_article:
            nat_label = add_definite_article(nat_label)

        logger.debug(f'<<lightblue>>>>>> {nat_key}: "{nat_label}" ')
        # resolved_label = template.format(nat_label)

        if "{nat}" in template:
            resolved_label = template.format(nat=nat_label)
        else:
            resolved_label = template.format(nat_label)

        logger.debug(f'<<lightblue>>>>>> {nat_key} template match: new cnt_la "{resolved_label}" ')
        return resolved_label

    return ""
