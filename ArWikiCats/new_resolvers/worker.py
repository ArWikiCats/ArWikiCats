"""
Central worker module for all new_resolvers sub-packages.

This module provides a unified resolver engine that all sub-package __init__.py
files can import and use to run their resolver functions.
"""

import functools
import logging
from typing import Callable, List, Optional, Tuple

logger = logging.getLogger(__name__)


class ResolverWorker:
    """
    Worker class that orchestrates resolver execution across all sub-packages.

    Each sub-package registers its resolver functions with this worker,
    which then executes them in a prioritized order.
    """

    def __init__(self):
        self._resolver_chains: List[Tuple[str, Callable[[str], str]]] = []

    def register_resolver(self, name: str, resolver: Callable[[str], str], priority: int = 0) -> None:
        """
        Register a resolver function with the worker.

        Parameters:
            name: Unique identifier for the resolver
            resolver: Callable that takes a category string and returns a resolved label
            priority: Lower numbers run first (default: 0)
        """
        self._resolver_chains.append((name, resolver))
        self._resolver_chains.sort(key=lambda x: priority)

    def resolve(self, category: str, chain_name: Optional[str] = None) -> str:
        """
        Execute registered resolvers in order and return the first non-empty result.

        Parameters:
            category: Category string to resolve
            chain_name: Optional filter to only run resolvers matching this name prefix

        Returns:
            Resolved Arabic label, or empty string if no resolver matched
        """
        category = category.strip().lower().replace("category:", "")
        logger.debug("--" * 20)
        logger.debug(f"<><><><><><> <<green>> {category=}")

        result = ""
        for name, resolver in self._resolver_chains:
            if chain_name and not name.startswith(chain_name):
                continue
            try:
                result = resolver(category)
                if result:
                    break
            except Exception as e:
                logger.error(f"Resolver {name} failed: {e}")
                continue

        logger.log(20 if result else 10, f"<<yellow>> end {category=}, {result=}")
        return result

    def resolve_with_fallback(
        self,
        category: str,
        resolvers: List[Callable[[str], str]],
    ) -> str:
        """
        Execute a list of resolvers in order and return the first non-empty result.

        Parameters:
            category: Category string to resolve
            resolvers: List of resolver callables to try in order

        Returns:
            Resolved Arabic label, or empty string if no resolver matched
        """
        category = category.strip().lower().replace("category:", "")

        for resolver in resolvers:
            try:
                result = resolver(category)
                if result:
                    return result
            except Exception as e:
                logger.error(f"Resolver failed: {e}")
                continue

        return ""


@functools.lru_cache(maxsize=1)
def get_worker() -> ResolverWorker:
    """Get or create the global ResolverWorker instance."""
    _worker: Optional[ResolverWorker] = ResolverWorker()
    return _worker


def run_resolvers(category: str, resolvers: List[Callable[[str], str]]) -> str:
    """
    Run a list of resolver functions in order and return the first non-empty result.

    This is the main function that __init__.py files should use.

    Parameters:
        category: Category string to resolve
        resolvers: List of resolver callables to try in order

    Returns:
        Resolved Arabic label, or empty string if no resolver matched
    """
    return get_worker().resolve_with_fallback(category, resolvers)


__all__ = [
    "ResolverWorker",
    "run_resolvers",
]
