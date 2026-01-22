"""
=== Import Chain Analysis ===

country_bot.py imports:
    from . import general_resolver

general_resolver.py imports:
    from .ar_lab_bot import find_ar_label

ar_lab_bot.py imports:
    from . import country_bot

=== Circular Dependency ===
country_bot -> general_resolver -> ar_lab_bot -> country_bot


"""
