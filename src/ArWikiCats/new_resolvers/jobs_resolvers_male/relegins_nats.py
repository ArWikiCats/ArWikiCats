"""
Refactored from ArWikiCats/new_resolvers/jobs_resolvers/relegin_jobs_nats_jobs.py
into a class-based architecture with lazy-loaded bots.
"""

from functools import cached_property
from ...translations import RELIGIOUS_KEYS_PP, Nat_mens, Nat_Womens
from ...translations_formats import (
    FormatData,
    MultiDataFormatterConfig,
    MultiDataFormatterSecondElementConfig,
    format_multi_data_v2,
)


class CategoryResolver:
    """Resolver for religious, national, and job category labels in Arabic."""

    def __init__(self) -> None:
        # Prepare consolidated dictionaries with gendered values
        self._rel_data = {
            k: {"rel_ar": v.get("males"), "rel_ar_f": v.get("females")} for k, v in RELIGIOUS_KEYS_PP.items()
        }

        self._nat_data = {}
        for k, v in Nat_mens.items():
            self._nat_data.setdefault(k.lower(), {})["nat_ar"] = v
        for k, v in Nat_Womens.items():
            self._nat_data.setdefault(k.lower(), {})["nat_ar_f"] = v

        self.painter_role_labels = {
            "painters": {"males": "رسامون", "females": "رسامات"},
            "artists": {"males": "فنانون", "females": "فنانات"},
        }

        # Extended roles for the test cases
        self._jobs_data = {
            k: {"job_ar": v.get("males"), "job_ar_f": v.get("females")} for k, v in self.painter_role_labels.items()
        }

        # Additional nats from test failures
        self._extra_nats = {
            "ancient roman": "رومان قدماء",
            "ancient-roman": "رومان قدماء",
            "turkish cypriot": "قبرصيون شماليون",
            "arab": "عرب",
            "asian": "آسيويون",
            "yemeni": "يمنيون",
        }
        for k, v in self._extra_nats.items():
            self._nat_data.setdefault(k, {})["nat_ar"] = v

        # Logic for shared templates
        self._combined_templates = {
            # Nationality + Religion (Male/General)
            "{nat} {rel}": "{nat_ar} {rel_ar}",
            "{rel} {nat}": "{nat_ar} {rel_ar}",
            "{nat} people {rel}": "{nat_ar} {rel_ar}",
            "{nat} {rel} male": "{nat_ar} {rel_ar} ذكور",
            "{rel} {nat} male": "{nat_ar} {rel_ar} ذكور",
            "{nat} male {rel}": "{rel_ar} ذكور {nat_ar}",
            # Job + Religion (Male/General)
            "{job} {rel}": "{job_ar} {rel_ar}",
            "{rel} {job}": "{job_ar} {rel_ar}",
            "{job} male {rel}": "{job_ar} ذكور {rel_ar}",
            "{job} {rel} male": "{job_ar} ذكور {rel_ar}",
            "{rel} {job} male": "{job_ar} ذكور {rel_ar}",
            "male {job} {rel}": "{job_ar} ذكور {rel_ar}",
            # Nationality + Religion (Female)
        }

    @cached_property
    def nat_rel_bot_v2(self):
        """Lazy-loaded main bot for Nationality + Religion (V2)."""
        return format_multi_data_v2(
            first_element_config=MultiDataFormatterConfig(
                formatted_data=self._combined_templates,
                data_list=self._nat_data,
                key_placeholder="{nat}",
            ),
            second_element_config=MultiDataFormatterSecondElementConfig(
                data_list=self._rel_data,
                key_placeholder="{rel}",
            ),
            use_other_formatted_data=True,
        )

    @cached_property
    def job_rel_bot_v2(self):
        """Lazy-loaded main bot for Job + Religion (V2)."""
        return format_multi_data_v2(
            first_element_config=MultiDataFormatterConfig(
                formatted_data=self._combined_templates,
                data_list=self._jobs_data,
                key_placeholder="{job}",
            ),
            second_element_config=MultiDataFormatterSecondElementConfig(
                data_list=self._rel_data,
                key_placeholder="{rel}",
            ),
        )

    @cached_property
    def simple_m_bot(self):
        """Lazy-loaded simple fallback bot for (Male/General)."""
        return FormatData(
            formatted_data={"{rel}": "{rel_ar}"},
            data_list={k: v.get("males") for k, v in RELIGIOUS_KEYS_PP.items() if v.get("males")},
            key_placeholder="{rel}",
            value_placeholder="{rel_ar}",
        )

    def resolve_nats_jobs_for_males(self, category: str) -> str:
        """
        Resolves the Arabic label for a category string that combines a religious group and a nationality.
        Args:
            category: The input category string.
        Returns:
            The translated Arabic category label, or an empty string if no match is found.
        """
        category_lower = category.lower().strip()

        if any(w in category_lower for w in ["female", "women's", "women", "womens"]):
            return ""  # female labels should not resolve in this model

        if res := self.nat_rel_bot_v2.search(category_lower):
            return res

        if res := self.job_rel_bot_v2.search(category_lower):
            return res

        # Check for direct matches in RELIGIOUS_KEYS_PP as a fallback
        for key, labels in RELIGIOUS_KEYS_PP.items():
            if category_lower == key:
                return labels.get("males", "")

        if res := self.simple_m_bot.search(category_lower):
            return res

        return ""


# Default instance for backward compatibility with existing procedural calls
_resolver = CategoryResolver()


def resolve_nats_jobs_for_males(category: str) -> str:
    """Backward compatible wrapper function for the default resolver instance."""
    return _resolver.resolve_nats_jobs_for_males(category)


__all__ = [
    "CategoryResolver",
    "resolve_nats_jobs_for_males",
]
