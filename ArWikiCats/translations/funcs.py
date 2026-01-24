"""
Data translations and mappings for the ArWikiCats project.
This package aggregates translation data for various categories including
geography, jobs, languages, nationalities, sports, and media.
"""

from .geo.labels_country import (
    get_and_label,
    get_from_new_p17_final,
)
from .mixed.all_keys2 import (
    get_from_pf_keys2,
)
from .utils import apply_pattern_replacements
from .utils.json_dir import open_json_file
from .utils.match_sport_keys import match_sport_key

__all__ = [
    "open_json_file",
    "get_and_label",
    "apply_pattern_replacements",
    "match_sport_key",
    "get_from_new_p17_final",
    "get_from_pf_keys2",
]
