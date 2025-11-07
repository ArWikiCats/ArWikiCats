"""Resolve labels for relations between countries."""

from __future__ import annotations

import re
from typing import Dict, Mapping, Tuple

from ... import printe
from ...helps.print_bot import print_put
from ...ma_lists import All_contry_ar, All_contry_with_nat_keys_is_en, Nat_men, Nat_women

P17_PREFIXES: Mapping[str, str] = {
    " conflict": "صراع {}",
    " proxy conflict": "صراع {} بالوكالة",
}

RELATIONS_FEMALE: Mapping[str, str] = {
    " military relations": "العلاقات {} العسكرية",
    " joint economic efforts": "الجهود الاقتصادية المشتركة {}",
    " relations": "العلاقات {}",
    " border crossings": "معابر الحدود {}",
    " border towns": "بلدات الحدود {}",
    " border": "الحدود {}",
    " clashes": "الاشتباكات {}",
    " wars": "الحروب {}",
    " war": "الحرب {}",
}

RELATIONS_MALE: Mapping[str, str] = {
    " conflict video games": "ألعاب فيديو الصراع {}",
    " conflict legal issues": "قضايا قانونية في الصراع {}",
    " conflict": "الصراع {}",
    " football rivalry": "التنافس {} في كرة القدم",
}


def _split_pair(expression: str) -> Tuple[str, str]:
    """Split ``expression`` into two country identifiers."""

    match = re.match(r"^(.*?)(?:–|-|−)(.*)$", expression)
    if not match:
        return "", ""
    return match.group(1).strip(), match.group(2).strip()


def _lookup_country_label(key: str, gender_key: str, nat_table: Mapping[str, str]) -> str:
    """Return the gender-specific label for ``key``."""

    normalized = key.strip()
    if not normalized:
        return ""

    if gender_key:
        details = All_contry_with_nat_keys_is_en.get(normalized, {})
        label = details.get(gender_key, "")
        if label:
            return label

    return nat_table.get(normalized, "")


def _combine_labels(labels: Tuple[str, str], add_article: bool, joiner: str = " ") -> str:
    """Combine ``labels`` with sorting and optional article insertion."""

    sorted_labels = sorted(labels)
    if add_article:
        combined = " ".join(sorted_labels)
        # Replicate the historical behaviour where each word receives an ``ال``
        # prefix and the combined string keeps the order alphabetical.
        combined = re.sub(r" ", " ال", f" {combined}").strip()
        return combined

    return joiner.join(sorted_labels)


def _resolve_relations(
    normalized_value: str,
    suffixes: Mapping[str, str],
    gender_key: str,
    nat_table: Mapping[str, str],
    *,
    add_article: bool,
    joiner: str = " ",
) -> str:
    """Resolve a relation label using ``suffixes`` and ``nat_table``."""

    for suffix, template in suffixes.items():
        if not normalized_value.endswith(suffix):
            continue

        prefix = normalized_value[: -len(suffix)].strip()
        first_key, second_key = _split_pair(prefix)
        if not first_key or not second_key:
            continue

        first_label = _lookup_country_label(first_key, gender_key, nat_table)
        second_label = _lookup_country_label(second_key, gender_key, nat_table)

        if not first_label or not second_label:
            printe.output(f'\t\t>>>><<lightblue>> missing label for: "{first_key}" or "{second_key}"')
            continue

        combined = _combine_labels((first_label, second_label), add_article, joiner=joiner)

        if suffix == " relations" and "nato" in {first_key, second_key}:
            counterpart = first_key if second_key == "nato" else second_key
            counterpart_label = All_contry_ar.get(counterpart, "")
            if counterpart_label:
                combined = f"علاقات الناتو و{counterpart_label}"

        return template.format(combined)

    return ""


def work_relations(value: str) -> str:
    """Return the label for relations between two countries.

    Args:
        value: Category describing the relationship between two countries.

    Returns:
        The resolved Arabic label or an empty string when the relation cannot
        be interpreted.
    """

    normalized = value.lower().strip()
    print_put(f"start work_relations: value:{normalized}")

    resolved = _resolve_relations(
        normalized,
        RELATIONS_FEMALE,
        "women",
        Nat_women,
        add_article=True,
    )
    if resolved:
        return resolved

    resolved = _resolve_relations(
        normalized,
        RELATIONS_MALE,
        "men",
        Nat_men,
        add_article=True,
    )
    if resolved:
        return resolved

    resolved = _resolve_relations(
        normalized,
        P17_PREFIXES,
        "",
        All_contry_ar,
        add_article=False,
        joiner=" و",
    )
    return resolved


# Backwards compatibility ----------------------------------------------------------------------
Work_relations = work_relations

__all__ = ["work_relations", "Work_relations"]
