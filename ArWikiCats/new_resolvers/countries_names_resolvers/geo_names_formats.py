"""
Resolve geo names categories translations
NOTE: planned to replace pop_format in format_bots/__init__.py
"""

from __future__ import annotations

import functools
import logging
from typing import Dict

from ...translations import COUNTRY_LABEL_OVERRIDES, raw_region_overrides
from ...translations_formats import FormatData
from ..base_worker import BaseResolversWorker
from .countries_names_data import formatted_data_en_ar_only

logger = logging.getLogger(__name__)


def load_geo_data() -> Dict[str, str]:
    """Build and return the full translation pattern dict."""
    formatted_data_updated = dict(formatted_data_en_ar_only)

    geo_keys: Dict[str, str] = {
        "sanaa": "صنعاء",
        "manitoba": "مانيتوبا",
        "bologna": "بولونيا",
        "hubei": "خوبي",
        "west virginia": "فرجينيا الغربية",
    }

    geo_data: Dict[str, str] = COUNTRY_LABEL_OVERRIDES | raw_region_overrides | geo_keys

    return formatted_data_updated, geo_data


class GeoNamesResolver(BaseResolversWorker):
    """Resolver for geo names category translations."""

    def load_bot(self) -> None:
        """Initialize the translation bot."""
        formatted_data_updated, geo_data = load_geo_data()
        self.bot: FormatData = FormatData(
            formatted_data_updated,
            geo_data,
            key_placeholder="{en}",
            value_placeholder="{ar}",
            text_before="the ",
            regex_filter=r"[\w-]",
        )

    def process(self, category: str) -> str:
        """Process the category and return raw translation."""
        return self.bot.search_all_category(category)

    def after_run(self) -> None:
        """No post-processing needed for geo names."""


@functools.lru_cache(maxsize=1)
def load_class() -> GeoNamesResolver:
    """Get singleton instance of the resolver."""
    return GeoNamesResolver("resolve_by_geo_names")


@functools.lru_cache(maxsize=10000)
def resolve_by_geo_names(category: str) -> str:
    return load_class().run(category)


__all__ = [
    "resolve_by_geo_names",
]
