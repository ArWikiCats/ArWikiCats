"""

This module goal is to collect all `male` resolvers so it can replaced later by genders_resolvers.

"""

from .mens import males_resolver_labels
from .relegins import new_religions_jobs_for_males
from .relegins_nats import resolve_nats_jobs_for_males

__all__ = [
    "males_resolver_labels",
    "new_religions_jobs_for_males",
    "resolve_nats_jobs_for_males",
]
