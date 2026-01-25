"""
jobs data
"""

from __future__ import annotations

from typing import Iterable, Mapping

from .jobs_defs import GenderedLabel, GenderedLabelMap, combine_gender_labels


def _build_religious_job_labels(
    religions: Mapping[str, GenderedLabel],
    roles: Mapping[str, GenderedLabel],
) -> GenderedLabelMap:
    """
    Builds a mapping of gendered labels for every valid combination of religion and religious role.
    
    Parameters:
        religions (Mapping[str, GenderedLabel]): Mapping of religion keys to their gendered labels.
        roles (Mapping[str, GenderedLabel]): Mapping of religious role keys to their gendered labels.
    
    Returns:
        GenderedLabelMap: A dictionary whose keys are "{religion} {role}" and whose values are gendered label objects with "males" and "females". Entries are created only for pairs where at least one gender label exists; pairs with empty keys or empty label objects are skipped.
    """

    combined_roles: GenderedLabelMap = {}
    for religion_key, religion_labels in religions.items():
        if not religion_key or not religion_labels:
            continue
        for role_key, role_labels in roles.items():
            if not role_key or not role_labels:
                continue
            females_label = combine_gender_labels(role_labels["females"], religion_labels["females"])
            males_label = combine_gender_labels(role_labels["males"], religion_labels["males"])

            if males_label or females_label:
                combined_roles[f"{religion_key} {role_key}"] = {
                    "males": males_label,
                    "females": females_label,
                }

    return combined_roles


def _build_painter_job_labels(
    painter_styles: Mapping[str, GenderedLabel],
    painter_roles: Mapping[str, GenderedLabel],
    painter_categories: Mapping[str, str],
) -> GenderedLabelMap:
    """
    Build gendered label mappings for painter styles, roles, and categories.
    
    Parameters:
        painter_styles (Mapping[str, GenderedLabel]): Mapping of style keys (e.g., "symbolist") to their gendered Arabic labels.
        painter_roles (Mapping[str, GenderedLabel]): Mapping of role keys to their gendered Arabic labels.
        painter_categories (Mapping[str, str]): Mapping of category keys to human-readable Arabic category labels.
    
    Returns:
        GenderedLabelMap: Mapping of composite job keys to gendered labels. Keys include base roles, style keys (except "history"), style+role composites (e.g., "symbolist painter"), and category-based entries like "{category} painters" and "{category} artists". Each value is a dict with "males" and "females" Arabic labels.
    """
    # _build_painter_job_labels(PAINTER_STYLES, PAINTER_ROLE_LABELS, PAINTER_CATEGORY_LABELS)
    combined_data: GenderedLabelMap = {role_key: role_labels for role_key, role_labels in painter_roles.items()}

    combined_data.update({_style: _labels for _style, _labels in painter_styles.items() if _style != "history"})
    for style_key, style_labels in painter_styles.items():
        for role_key, role_labels in painter_roles.items():
            composite_key = f"{style_key} {role_key}"

            males_label = combine_gender_labels(role_labels["males"], style_labels["males"])
            females_label = combine_gender_labels(role_labels["females"], style_labels["females"])

            combined_data[composite_key] = {
                "males": males_label,
                "females": females_label,
            }
    for painter_category, category_label in painter_categories.items():
        if not painter_category or not category_label:
            continue
        combined_data[f"{painter_category} painters"] = {
            "males": f"رسامو {category_label}",
            "females": f"رسامات {category_label}",
        }
        combined_data[f"{painter_category} artists"] = {
            "males": f"فنانو {category_label}",
            "females": f"فنانات {category_label}",
        }

    return combined_data


def _build_military_job_labels(
    military_prefixes: Mapping[str, GenderedLabel],
    military_roles: Mapping[str, GenderedLabel],
    excluded_prefixes: Iterable[str],
) -> GenderedLabelMap:
    """
    Builds a mapping of military job names (including prefix+role composites) to their gendered labels.
    
    Parameters:
        military_prefixes: Mapping of prefix keys to gendered labels used to modify roles.
        military_roles: Mapping of role keys to base gendered labels.
        excluded_prefixes: Iterable of prefix keys that should not be inserted as standalone keys in the result but will still be used to form composite prefix+role entries.
    
    Returns:
        GenderedLabelMap: A dictionary whose keys are role names or "prefix role" composites and whose values are gendered label objects with "males" and "females" entries.
    """
    excluded = set(excluded_prefixes)

    combined_roles: GenderedLabelMap = {role_key: role_labels for role_key, role_labels in military_roles.items()}

    combined_roles.update(
        {
            prefix_key: prefix_labels
            for prefix_key, prefix_labels in military_prefixes.items()
            if prefix_key not in excluded
        }
    )

    for military_key, prefix_labels in military_prefixes.items():
        for role_key, role_labels in military_roles.items():
            composite_key = f"{military_key} {role_key}"
            males_label = combine_gender_labels(role_labels["males"], prefix_labels["males"])
            females_label = combine_gender_labels(role_labels["females"], prefix_labels["females"])
            combined_roles[composite_key] = {
                "males": males_label,
                "females": females_label,
            }

    return combined_roles


__all__ = [
    "_build_religious_job_labels",
    "_build_painter_job_labels",
    "_build_military_job_labels",
]