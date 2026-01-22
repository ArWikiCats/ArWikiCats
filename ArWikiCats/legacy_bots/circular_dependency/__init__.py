"""
=== Import Chain Analysis ===

country_bot.py imports:
    from . import general_resolver

general_resolver.py imports:
    from .ar_lab_bot import find_ar_label

ar_lab_bot.py imports:
    from . import country_bot
    from ..legacy_resolvers_bots.con2_lab import ( get_con_lab, get_type_country, get_type_lab, )

con2_lab.py imports:
    from ..circular_dependency import country_bot

=== Circular Dependency ===
country_bot -> general_resolver -> ar_lab_bot -> country_bot


"""
