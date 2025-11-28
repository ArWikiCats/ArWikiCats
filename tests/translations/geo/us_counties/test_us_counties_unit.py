#
import pytest

from ArWikiCats.translations.geo.us_counties import (
    US_STATES_NAME_TRANSLATIONS,
    USA_PARTY_LABELS,
    _extend_state_suffix_templates,
    _build_party_derived_keys,
)


@pytest.mark.unit
class TestUSCountiesHelpers:
    def test_extend_state_suffix_templates_adds_party_variants(self):
        result = _extend_state_suffix_templates(
            {" base": "template %s"}, {"Democratic Party": "الحزب الديمقراطي"}
        )

        assert result[" base"] == "template %s"
        assert result[" democratic partys"] == "أعضاء الحزب الديمقراطي في %s"
        assert result[" democratics"] == "أعضاء الحزب الديمقراطي في %s"

    def test_build_party_derived_keys_skips_blank_labels(self):
        derived = _build_party_derived_keys({"Democratic Party": "الحزب الديمقراطي", "Blank Party": " "})

        assert "democratic party" in derived
        assert derived["democratic party members"] == "أعضاء الحزب الديمقراطي"
        assert "blank party" not in derived

    def test_get_state_name_translations_returns_copy(self):
        assert US_STATES_NAME_TRANSLATIONS["ohio"] == "أوهايو"

    def test_get_party_labels_returns_copy(self):
        assert USA_PARTY_LABELS["democratic party"] == "الحزب الديمقراطي"
