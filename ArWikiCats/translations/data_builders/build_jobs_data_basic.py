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
    """Generate gendered labels for religious roles.

    Args:
        religions: Mapping of religion identifiers to their gendered labels.
        roles: Mapping of religious roles to gendered labels.

    Returns:
        A dictionary keyed by string templates representing the combination of
        religion and role, matching the original dataset used by downstream
        modules.
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
    """Construct gendered labels for painting and artistic roles.

    Args:
        painter_styles: Mapping of painter descriptors (e.g. ``symbolist``) to
            their gendered Arabic forms.
        painter_roles: Mapping of artistic roles associated with painting.
        painter_categories: Additional label categories that are appended as
            human-readable Arabic strings.

    Returns:
        A dictionary containing both base roles and combined painter role
        variants.
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
    """Construct gendered labels for military related jobs.

    Args:
        military_prefixes: Base labels that modify the general military roles.
        military_roles: Roles that can be combined with each prefix.
        excluded_prefixes: Prefix keys that should not be added directly to the
            result set but are still used for composite roles.

    Returns:
        A dictionary of gendered labels covering both base roles and composite
        role names.
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
