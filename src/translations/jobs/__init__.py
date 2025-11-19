"""Canonical public API for gendered job datasets.

This package aggregates the typed datasets exposed across the refactored job
modules and publishes a stable import surface for downstream callers.  Importers
can rely on :mod:`translations.jobs` to retrieve commonly used mappings without
pulling in individual module internals.
"""

from __future__ import annotations
