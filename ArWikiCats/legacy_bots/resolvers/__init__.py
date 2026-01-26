"""
Resolvers Package

This package provides a clean, non-circular architecture for category label resolution.
It replaces the legacy `circular_dependency/` package with a proper Directed Acyclic Graph (DAG)
of imports.

Architecture:
    - `interface.py`: Protocol definitions for resolvers
    - `country_resolver.py`: Country-based label resolution (no circular imports)
    - `arabic_label_builder.py`: Arabic label construction (imports from country_resolver)
    - `separator_based_resolver.py`: Separator-based resolution (imports from arabic_label_builder)
    - `factory.py`: Wires everything together and sets up callbacks
    - `sub_resolver.py`: Sub-category resolution utilities

Import DAG (no cycles):
    factory -> separator_based_resolver -> arabic_label_builder -> country_resolver
                                        -> sub_resolver

IMPORTANT: After importing from this package, call `initialize_resolvers()` to set up
the callback dependencies. This is typically done in `legacy_bots/__init__.py`.
"""

from .arabic_label_builder import find_ar_label
from .country_resolver import (
    Get_country2,
    event2_d2,
    fetch_country_term_label,
    get_country,
)
from .factory import initialize_resolvers, translate_general_category_wrap
from .separator_based_resolver import work_separator_names
from .sub_resolver import sub_translate_general_category

__all__ = [
    "find_ar_label",
    "Get_country2",
    "event2_d2",
    "fetch_country_term_label",
    "get_country",
    "work_separator_names",
    "sub_translate_general_category",
    "translate_general_category_wrap",
    "initialize_resolvers",
]
