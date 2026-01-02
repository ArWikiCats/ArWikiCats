"""Resolve labels for relations between countries."""

from __future__ import annotations

import functools
import re
from typing import Mapping, Tuple

from ...helps.log import logger
from ...translations import (
    COUNTRY_LABEL_OVERRIDES,
    Nat_men,
    Nat_the_female,
    Nat_the_male,
    Nat_women,
    NationalityEntry,
    all_country_ar,
    countries_nat_en_key,
    get_from_new_p17_final,
)
from ..o_bots.utils import apply_arabic_article
from .utils import sort_by_empty_space

P17_PREFIXES: Mapping[str, str] = {
    " conflict": "صراع {}",
    " proxy conflict": "صراع {} بالوكالة",
    " relations": "علاقات {}",
    " sports relations": "علاقات {} الرياضية",
}

RELATIONS_FEMALE: Mapping[str, str] = {
    " military relations": "العلاقات {} العسكرية",
    " sports relations": "العلاقات {} الرياضية",
    " joint economic efforts": "الجهود الاقتصادية المشتركة {}",
    " relations": "العلاقات {}",
    " border crossings": "معابر الحدود {}",
    " border towns": "بلدات الحدود {}",
    " border": "الحدود {}",
    " clashes": "الاشتباكات {}",
    " wars": "الحروب {}",
    " war": "الحرب {}",
    " border war": "حرب الحدود {}",
    " war films": "أفلام الحرب {}",
    " war video games": "ألعاب فيديو الحرب {}",
}

RELATIONS_MALE: Mapping[str, str] = {
    " conflict video games": "ألعاب فيديو الصراع {}",
    " conflict legal issues": "قضايا قانونية في الصراع {}",
    " conflict": "الصراع {}",
    " football rivalry": "التنافس {} في كرة القدم",
}

P17_PREFIXES = sort_by_empty_space(P17_PREFIXES)
RELATIONS_FEMALE = sort_by_empty_space(RELATIONS_FEMALE)
RELATIONS_MALE = sort_by_empty_space(RELATIONS_MALE)

RELATIONS_END_KEYS = list(P17_PREFIXES.keys()) + list(RELATIONS_FEMALE.keys()) + list(RELATIONS_MALE.keys())
# ".*?–.*? (joint economic efforts|conflict video games|conflict legal issues|proxy conflict|military relations|border crossings|border towns|football rivalry|conflict|relations|relations|border|clashes|wars|war|conflict)"


def _load_all_country_labels() -> dict[str, str]:
    all_country_labels = dict(all_country_ar)
    all_country_labels.update(
        {
            "nato": "الناتو",
            "european union": "الاتحاد الأوروبي",
        }
    )

    all_country_labels.update(COUNTRY_LABEL_OVERRIDES)
    return all_country_labels


@functools.lru_cache(maxsize=1)
def _load_countries_data() -> dict[str, NationalityEntry]:
    data = dict(countries_nat_en_key)
    data.update(
        {
            "ireland": {
                "male": "أيرلندي",
                "males": "أيرلنديون",
                "female": "أيرلندية",
                "females": "أيرلنديات",
                "en": "ireland",
                "ar": "أيرلندا",
                "the_female": "الأيرلندية",
                "the_male": "الأيرلندي",
            }
        }
    )
    return data


def _split_pair(expression: str) -> Tuple[str, str]:
    """Split ``expression`` into two country identifiers."""

    match = re.match(r"^(.*?)(?:–|−)(.*?)$", expression)
    if match:
        return match.group(1).strip(), match.group(2).strip()

    match2 = re.match(r"^(.*?)-(.*?)$", expression)
    if match2:
        return match2.group(1).strip(), match2.group(2).strip()

    return "", ""


def _lookup_country_label(key: str, gender_key: str, nat_table: Mapping[str, str]) -> str:
    """Return the gender-specific label for ``key``."""

    normalized = key.strip()
    if not normalized:
        return ""
    countries_data = _load_countries_data()
    if gender_key:
        details = countries_data.get(normalized, {})
        label = details.get(gender_key, "")
        if label:
            return label

    label = nat_table.get(normalized, "")

    if not label and not gender_key:
        label = get_from_new_p17_final(normalized)

    return label


def _combine_labels(labels: Tuple[str, str], joiner: str = " ") -> str:
    """Combine ``labels`` with sorting and optional article insertion."""
    sorted_labels = sorted(labels)

    return joiner.join(sorted_labels)


def get_nato_relation_template(template, counterpart_label):
    template = f"علاقات {template}" if "علاقات" not in template else template
    sorted_labels = sorted(["الناتو", counterpart_label])
    combined = " و".join(sorted_labels)

    return template, combined


def get_suffix_and_template(normalized_value, suffixes):
    for suffix, template in suffixes.items():
        if not normalized_value.endswith(suffix):
            continue
        return suffix, template

    return "", ""


def _resolve_relations(
    normalized_value: str,
    suffixes: Mapping[str, str],
    gender_key: str,
    nat_table: Mapping[str, str],
    *,
    joiner: str = " ",
) -> str:
    """Resolve a relation label using ``suffixes`` and ``nat_table``."""

    suffix, template = get_suffix_and_template(normalized_value, suffixes)
    if not suffix:
        return ""

    prefix = normalized_value[: -len(suffix)].strip()
    logger.debug(f"\t\t>>>>{suffix=} -> {prefix=}")

    first_key, second_key = _split_pair(prefix)
    if not first_key or not second_key:
        return ""

    first_label = _lookup_country_label(first_key, gender_key, nat_table)
    second_label = _lookup_country_label(second_key, gender_key, nat_table)

    logger.debug(f"\t\t>>>>{first_key=} -> {first_label=}")
    logger.debug(f"\t\t>>>>{second_key=} -> {second_label=}")

    if not first_label or not second_label:
        logger.info(f'\t\t>>>><<lightblue>> missing label for: "{first_key}" or "{second_key}"')
        return ""

    combined = _combine_labels((first_label, second_label), joiner=joiner)

    if suffix.strip() != "relations" or "nato" not in {first_key, second_key}:
        return template.format(combined)

    # counterpart = first_key if second_key == "nato" else second_key
    # counterpart_label = all_country_labels.get(counterpart, "")
    # if counterpart_label:
    #     template, combined = get_nato_relation_template(template, counterpart_label)

    result = template.format(combined)

    return result


def fix_key(category: str) -> str:
    category = category.lower().replace("category:", "")
    category = category.replace("'", "")
    # category = category.replace(" the ", "")

    replacements = {}

    for old, new in replacements.items():
        category = category.replace(old, new)

    return category.strip()


def resolve_relations_label(value: str) -> str:
    """Return the label for relations between two countries.

    Args:
        value: Category describing the relationship between two countries.

    Returns:
        The resolved Arabic label or an empty string when the relation cannot
        be interpreted.
    """

    normalized = fix_key(value)
    logger.debug(f"start resolve_relations_label: value:{normalized}")

    resolved = _resolve_relations(
        normalized,
        RELATIONS_FEMALE,
        # "female",
        "the_female",
        Nat_the_female,
    )
    if resolved:
        logger.info(f"resolve_relations_label (female): cat: {value}, {resolved=}")
        return resolved

    resolved = _resolve_relations(
        normalized,
        RELATIONS_MALE,
        # "male",
        "the_male",
        Nat_the_male,
    )
    if resolved:
        logger.info(f"resolve_relations_label (male): cat: {value}, {resolved=}")
        return resolved

    all_country_labels = _load_all_country_labels()
    resolved = _resolve_relations(
        normalized,
        P17_PREFIXES,
        "",
        all_country_labels,
        joiner=" و",
    )

    if resolved:
        logger.info(f"resolve_relations_label (): cat: {value}, {resolved=}")

    return resolved


__all__ = [
    "resolve_relations_label",
]
