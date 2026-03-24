"""

"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, Final

logger = logging.getLogger(__name__)


class BaseResolversWorker(ABC):
    """
    Abstract base class for resolvers workers with standardized lifecycle.

    This base class provides:

    Subclasses must implement:

    Optional overrides:

    """

    def __init__(
        self,
        name: str="",
    ):
        self.name: Final[str] = name

    @abstractmethod
    def load_bot(self) -> Dict[str, Any]:
        """
        """
        ...

    @abstractmethod
    def process(self) -> str:
        """
        Execute the main processing logic.

        Returns:
            The result
        """
        ...

    # @abstractmethod
    def before_run(self, category) -> str:
        """
        """
        category = category.lower()
        return category

    @abstractmethod
    def after_run(self) -> None:
        pass

    def run(self, category) -> str:
        """
        Execute the resolvers

        This method orchestrates the entire resolver lifecycle:
        1. Calls before_run() to set up
        2. Calls process() to do the work
        3. Calls after_run() to clean up

        Returns:
            The final result
        """

        # Pre-processing setup
        category = self.before_run(category)

        # Main processing
        self.result = self.process(category)

        # Post-processing cleanup
        self.after_run()

        return self.result


__all__ = [
    "BaseResolversWorker",
]
