"""Cycling specific lookup tables used by the sports translation modules."""

from __future__ import annotations

from typing import Final

BASE_CYCLING_EVENTS: Final[dict[str, str]] = {
    "tour de france": "سباق طواف فرنسا",
    "grand tour": "الطوافات الكبرى",
    "grand tour (cycling)": "الطوافات الكبرى",
    "vuelta a españa": "طواف إسبانيا",
    "giro d'italia": "طواف إيطاليا",
    "presidential cycling tour of turkey": "طواف تركيا",
    "tour de suisse": "طواف سويسرا",
    "vuelta a colombia": "طواف كولومبيا",
    "vuelta a venezuela": "فويلتا فنزويلا",
}


def build_cycling_templates() -> dict[str, str]:
    """Generate derivative keys for cycling tournaments.

    Returns:
        A mapping keyed by lower-case identifiers with Arabic labels covering
        media, squads, and other related variations for every race.
    """

    templates: dict[str, str] = {}
    for english_name, arabic_label in BASE_CYCLING_EVENTS.items():
        normalized_name = english_name.lower()
        templates[normalized_name] = arabic_label
        templates[f"{normalized_name} media"] = f"إعلام {arabic_label}"
        templates[f"{normalized_name} squads"] = f"تشكيلات {arabic_label}"
        templates[f"{normalized_name} cyclists"] = f"دراجو {arabic_label}"
        templates[f"{normalized_name} directors"] = f"مدراء {arabic_label}"
        templates[f"{normalized_name} journalists"] = f"صحفيو {arabic_label}"
        templates[f"{normalized_name} people"] = f"أعلام {arabic_label}"
        templates[f"{normalized_name} stages"] = f"مراحل {arabic_label}"
        templates[f"{normalized_name} stage winners"] = f"فائزون في مراحل {arabic_label}"
    return templates


CYCLING_TEMPLATES: Final[dict[str, str]] = build_cycling_templates()

# Backwards-compatible exports -------------------------------------------------

# NOTE: Older callers import ``CYCLING_TEMPLATES`` and ``CYCLING_TEMPLATES`` directly from this
# module.  They expect a mapping identical to ``CYCLING_TEMPLATES``.  Expose both
# aliases so the refactor remains a drop-in replacement for those consumers.
CYCLING_TEMPLATES: Final[dict[str, str]] = CYCLING_TEMPLATES

__all__ = [
    "BASE_CYCLING_EVENTS",
    "CYCLING_TEMPLATES",
    "build_cycling_templates",
    "CYCLING_TEMPLATES",
    "CYCLING_TEMPLATES",
]
