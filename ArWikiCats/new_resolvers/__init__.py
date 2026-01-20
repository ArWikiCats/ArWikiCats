"""
Main entry point for resolving Arabic Wikipedia category names using multiple specialized resolvers.
This function orchestrates the resolution process by attempting to match a category string
against a series of specific resolvers in a predefined priority order to ensure accuracy
and avoid common linguistic conflicts (e.g., distinguishing between job titles and sports,
or nationalities and country names).
Args:
    category (str): The category name (usually in English) to be resolved into its Arabic equivalent.
Returns:
    str: The resolved Arabic category name if any resolver succeeds; otherwise, an empty string.
Note:
    - Results are cached using @functools.lru_cache for performance.
    - The order of execution is critical (e.g., 'jobs' before 'sports', and 'nationalities'
      before 'countries') to prevent incorrect grammatical or semantic translations.
New resolvers for Arabic Wikipedia categories.
"""

import functools

from ..time_formats import convert_time_to_arabic

from ..helps import logger
from ..sub_new_resolvers import main_other_resolvers
from .countries_names_resolvers import main_countries_names_resolvers
from .countries_names_with_sports import main_countries_names_with_sports_resolvers
from .films_resolvers import main_films_resolvers
from .jobs_resolvers import main_jobs_resolvers
from .languages_resolves import resolve_languages_labels_with_time
from .nationalities_resolvers import main_nationalities_resolvers
from .relations_resolver import main_relations_resolvers
from .sports_resolvers import main_sports_resolvers
from .time_and_jobs_resolvers import time_and_jobs_resolvers_main


@functools.lru_cache(maxsize=None)
def all_new_resolvers(category: str) -> str:
    """Apply all new resolvers to translate a category string.

    Args:
        category (str): The category string to resolve.

    Returns:
        str: The resolved category label, or empty string if not resolved.
    """
    logger.info(f"<<purple>> all_new_resolvers: {category}")
    category_lab = (
        convert_time_to_arabic(category)
        # main_jobs_resolvers before sports, to avoid mis-resolving like:
        # incorrect:    "Category:American basketball coaches": "تصنيف:مدربو كرة سلة أمريكية"
        # correct:      "Category:American basketball coaches": "تصنيف:مدربو كرة سلة أمريكيون"
        # while this technique make issues like:
        # incorrect:    "american football executives": "تصنيف:مسيرو كرة قدم أمريكيون",
        # correct:      "american football executives": "تصنيف:مسيرو كرة قدم أمريكية",
        #
        or main_jobs_resolvers(category)
        or time_and_jobs_resolvers_main(category)
        or main_sports_resolvers(category)
        # NOTE: main_nationalities_resolvers must be before main_countries_names_resolvers to avoid conflicts like:
        # main_countries_names_resolvers> [Italy political leader]:  "قادة إيطاليا السياسيون"
        # main_nationalities_resolvers> [Italy political leader]:  "قادة سياسيون إيطاليون"
        or main_nationalities_resolvers(category)
        or main_countries_names_resolvers(category)
        or main_films_resolvers(category)
        or main_relations_resolvers(category)
        or main_countries_names_with_sports_resolvers(category)
        or resolve_languages_labels_with_time(category)
        or main_other_resolvers(category)
        or ""
    )
    logger.info(f"<<purple>> all_new_resolvers: {category} => {category_lab}")
    return category_lab
