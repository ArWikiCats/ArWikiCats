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

    for tat, tatb in party_end_keys.items():
        fafaf = f" {tat}"
        if party.endswith(fafaf) and party_lab == "":
            party_uu = party[: -len(fafaf)]
            logger.debug(f'party_uu:"{party_uu}", tat:"{tat}" ')
            label = Parties.get(party_uu, "")
            if label:
                party_lab = tatb % label if tatb.find("%s") != -1 else tatb.format(label)
                break

    if party_lab:
        logger.info(f'get_parties_lab party:"{party}", party_lab:"{party_lab}"')

    return party_lab
