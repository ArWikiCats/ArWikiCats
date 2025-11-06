"""
from  make.bots.parties_bot import get_parties_lab

"""

from ...ma_lists import party_end_keys
from ...ma_lists import Parties

from ...helps.log import logger


def get_parties_lab(party):
    # إيجاد لاحقات الأحزاب
    logger.info(f'get_parties_lab party:"{party}"')
    party_lab = ""

    for suffix, suffix_template in party_end_keys.items():
        suffix_with_space = f" {suffix}"
        if party.endswith(suffix_with_space) and party_lab == "":
            party_key = party[: -len(suffix_with_space)]
            logger.debug(f'party_uu:"{party_key}", tat:"{suffix}" ')
            label = Parties.get(party_key, "")
            if label:
                party_lab = (
                    suffix_template % label
                    if "%s" in suffix_template
                    else suffix_template.format(label)
                )
                break

    if party_lab:
        logger.info(f'get_parties_lab party:"{party}", party_lab:"{party_lab}"')

    return party_lab
