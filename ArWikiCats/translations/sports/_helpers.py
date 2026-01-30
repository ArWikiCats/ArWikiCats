"""Utility helpers shared across the :mod:`translations.sports` package.

The original sports modules relied on ad-hoc loops to generate large
collections of translated sports labels.  The helpers in this module
centralise the common logic so that the individual modules remain readable
and well typed.
"""

from __future__ import annotations

import logging
from collections.abc import Iterable, Mapping, MutableMapping
from string import Formatter
from typing import Any

logger = logging.getLogger(__name__)

# The list of age categories that appear throughout the sports templates.
# It is referenced from multiple modules, therefore it lives in a single
# shared location to keep definitions consistent.
YEARS: tuple[int, ...] = (13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24)


def _count_positional_fields(template: str) -> int:
    """Return the number of anonymous positional fields in ``template``."""

    formatter = Formatter()
    count = 0
    for _, field_name, _, _ in formatter.parse(template):
        if field_name == "":
            count += 1
    logger.debug(f"Template '{template}' has {count} positional fields")

    return count


def _render_template(template: str, **format_kwargs: Any) -> str:
    """Render ``template`` while preserving literal ``{}`` placeholders.

    Older datasets relied on bare ``{}`` placeholders to denote values that
    would be filled later when consumers supplied country names.  When the
    helpers were introduced we started rendering templates using keyword
    arguments, which triggered ``IndexError`` exceptions for those legacy
    placeholders.  The helper counts positional fields and injects literal
    ``"{}"`` strings so the placeholders survive the formatting step.
    """

    positional_count = _count_positional_fields(template)
    positional_args: tuple[str, ...] = ("{}",) * positional_count
    return template.format(*positional_args, **format_kwargs)


def extend_with_templates(
    target: MutableMapping[str, str],
    templates: Mapping[str, str],
    **format_kwargs: Any,
) -> None:
    """Populate ``target`` using ``templates`` and ``format_kwargs``.

    Args:
        target: Dictionary that receives the rendered templates.
        templates: Mapping of key template to label template.
        **format_kwargs: Parameters available during ``str.format``
            expansion for both template strings.
    """

    for key_template, value_template in templates.items():
        rendered_key = _render_template(key_template, **format_kwargs)
        rendered_value = _render_template(value_template, **format_kwargs)
        target[rendered_key] = rendered_value


def extend_with_year_templates(
    target: MutableMapping[str, str],
    templates: Mapping[str, str],
    *,
    years: Iterable[int] | None = None,
    **format_kwargs: Any,
) -> None:
    """Render ``templates`` for every year and update ``target``.

    Args:
        target: Dictionary that receives all rendered templates.
        templates: Mapping of key template to label template.
        years: Optional iterable of integer years.  When omitted the
            project wide :data:`YEARS` constant is used.
        **format_kwargs: Extra formatting arguments used for the template
            expansion.
    """

    for year in years or YEARS:
        extend_with_templates(target, templates, year=year, **format_kwargs)


__all__ = ["YEARS", "extend_with_templates", "extend_with_year_templates"]
