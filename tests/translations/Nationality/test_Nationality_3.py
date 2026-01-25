import pytest

from ArWikiCats.translations.data_builders.build_nationalities import build_en_nat_entries

# from ArWikiCats.translations.nats.Nationality import build_en_nat_entries

# -------------------------------------------------------------------
# Tests for build_en_nat_entries
# -------------------------------------------------------------------


@pytest.mark.fast
def test_build_en_nat_entries() -> None:
    """build_en_nat_entries should process the entry for 'trinidad and tobago' and include 'trinidadian'."""

    data = {
        "trinidad and tobago": {
            "en_nat": "trinidadian",
            "male": "ترنيدادي",
            "males": "ترنيداديون",
            "female": "ترنيدادية",
            "females": "ترنيداديات",
            "the_male": "الترنيدادي",
            "the_female": "الترنيدادية",
            "en": "trinidad and tobago",
            "ar": "ترينيداد وتوباغو",
        }
    }

    result = build_en_nat_entries(data)

    assert isinstance(result, dict)
    assert "trinidadian" in result
    entry = result["trinidadian"]
    assert entry["male"] == "ترنيدادي"
    assert entry["en"] == "trinidad and tobago"
    assert entry["ar"] == "ترينيداد وتوباغو"
