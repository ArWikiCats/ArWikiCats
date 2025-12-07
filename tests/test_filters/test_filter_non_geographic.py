"""Tests for the filter_non_geographic script."""

import json
import pytest
from pathlib import Path
from help_scripts.filter_non_geographic import is_non_geographic, filter_json_file


class TestIsNonGeographic:
    """Test cases for the is_non_geographic function."""

    def test_university_in_key(self, jsons_geography_dir):
        """Test that university keywords are detected."""
        assert is_non_geographic("alfaisal university", "جامعة الفيصل") is True
        assert is_non_geographic("brown university", "جامعة براون") is True

    def test_college_in_key(self, jsons_geography_dir):
        """Test that college keywords are detected."""
        assert is_non_geographic("bard college", "كلية بارد") is True
        assert is_non_geographic("medical college of wisconsin", "كلية طب ويسكونسن") is True

    def test_bridge_in_key(self, jsons_geography_dir):
        """Test that bridge keywords are detected."""
        assert is_non_geographic("tacoma narrows bridge", "جسر تكوما ناروس") is True

    def test_fc_club_in_key(self, jsons_geography_dir):
        """Test that sports clubs are detected."""
        assert is_non_geographic("akonangui fc", "نادي أكونانغي") is True
        assert is_non_geographic("al-fayha fc", "نادي الفيحاء") is True
        assert is_non_geographic("harbour view f.c.", "نادي هاربور فيو") is True

    def test_company_in_key(self, jsons_geography_dir):
        """Test that companies are detected."""
        assert is_non_geographic("bristol aeroplane company", "شركة طائرات بريستول") is True
        assert is_non_geographic("artland (company)", "أرتلاند") is True

    def test_museum_in_key(self, jsons_geography_dir):
        """Test that museums are detected."""
        assert is_non_geographic("museum of london", "متحف لندن") is True
        assert is_non_geographic("national museum of china", "المتحف الوطني الصيني") is True

    def test_library_in_key(self, jsons_geography_dir):
        """Test that libraries are detected."""
        assert is_non_geographic("library of ashurbanipal", "مكتبة آشوربانيبال") is True

    def test_association_in_key(self, jsons_geography_dir):
        """Test that associations are detected."""
        assert is_non_geographic("freedom of association", "حرية التنظيم") is True
        assert is_non_geographic("world boxing association", "رابطة الملاكمة العالمية") is True

    def test_organization_in_key(self, jsons_geography_dir):
        """Test that organizations are detected."""
        assert is_non_geographic("economic cooperation organization", "منظمة التعاون الاقتصادي") is True
        assert is_non_geographic("indian space research organisation", "منظمة البحوث الفضائية الهندية") is True

    def test_arabic_university_in_value(self, jsons_geography_dir):
        """Test that Arabic 'جامعة' is detected in value."""
        assert is_non_geographic("some key", "جامعة القاهرة") is True

    def test_arabic_club_in_value(self, jsons_geography_dir):
        """Test that Arabic 'نادي' is detected in value."""
        assert is_non_geographic("some key", "نادي الأهلي") is True

    def test_arabic_company_in_value(self, jsons_geography_dir):
        """Test that Arabic 'شركة' is detected in value."""
        assert is_non_geographic("some key", "شركة طائرات") is True

    def test_geographic_entries_not_flagged(self, jsons_geography_dir):
        """Test that genuine geographic entries are not flagged."""
        assert is_non_geographic("africa", "إفريقيا") is False
        assert is_non_geographic("alberta", "ألبرتا") is False
        assert is_non_geographic("alice springs", "أليس سبرينغز") is False
        assert is_non_geographic("aland islands", "جزر أولاند") is False


class TestFilterJsonFile:
    """Test cases for the filter_json_file function."""

    def test_filter_separates_correctly(self, tmp_path):
        """Test that filtering correctly separates geographic and non-geographic entries."""
        # Create test data
        test_data = {
            "africa": "إفريقيا",
            "brown university": "جامعة براون",
            "alberta": "ألبرتا",
            "akonangui fc": "نادي أكونانغي",
            "alice springs": "أليس سبرينغز",
        }

        # Create input file
        input_file = tmp_path / "input.json"
        with open(input_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, ensure_ascii=False)

        # Define output files
        output_geo = tmp_path / "geographic.json"
        output_non_geo = tmp_path / "non_geographic.json"

        # Run filter
        stats = filter_json_file(input_file, output_geo, output_non_geo)

        # Verify statistics
        assert stats['total_entries'] == 5
        assert stats['geographic_entries'] == 3
        assert stats['non_geographic_entries'] == 2

        # Verify geographic file
        with open(output_geo, 'r', encoding='utf-8') as f:
            geo_data = json.load(f)
        assert len(geo_data) == 3
        assert "africa" in geo_data
        assert "alberta" in geo_data
        assert "alice springs" in geo_data

        # Verify non-geographic file
        with open(output_non_geo, 'r', encoding='utf-8') as f:
            non_geo_data = json.load(f)
        assert len(non_geo_data) == 2
        assert "brown university" in non_geo_data
        assert "akonangui fc" in non_geo_data

    def test_preserves_unicode(self, tmp_path):
        """Test that Arabic text is preserved correctly."""
        test_data = {
            "test university": "جامعة الاختبار",
            "test city": "مدينة الاختبار",
        }

        input_file = tmp_path / "input.json"
        with open(input_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, ensure_ascii=False)

        output_geo = tmp_path / "geographic.json"
        output_non_geo = tmp_path / "non_geographic.json"

        filter_json_file(input_file, output_geo, output_non_geo)

        # Verify Arabic text is preserved
        with open(output_non_geo, 'r', encoding='utf-8') as f:
            non_geo_data = json.load(f)
        assert non_geo_data["test university"] == "جامعة الاختبار"


@pytest.fixture
def jsons_geography_dir() -> Path:
    return Path(__file__).parent.parent.parent / 'ArWikiCats' / 'translations' / 'jsons' / 'geography'


class TestRealDataIntegrity:
    """Test cases that verify the real data files."""

    def test_p17_files_exist(self, jsons_geography_dir):
        """Test that the output files exist after filtering."""

        geo_file = jsons_geography_dir / 'P17_2_final_ll.json'
        non_geo_file = jsons_geography_dir / 'P17_2_final_ll_non_geographic.json'

        assert geo_file.exists(), "Geographic file should exist"
        assert non_geo_file.exists(), "Non-geographic file should exist"

    def test_p17_files_have_correct_counts(self, jsons_geography_dir):
        """Test that the files have the expected number of entries."""

        geo_file = jsons_geography_dir / 'P17_2_final_ll.json'
        non_geo_file = jsons_geography_dir / 'P17_2_final_ll_non_geographic.json'

        with open(geo_file, 'r', encoding='utf-8') as f:
            geo_data = json.load(f)

        with open(non_geo_file, 'r', encoding='utf-8') as f:
            non_geo_data = json.load(f)

        # Total should be 1720 (original count)
        total = len(geo_data) + len(non_geo_data)
        assert total == 1720, f"Total entries should be 1720, got {total}"

        # Non-geographic should have universities, clubs, etc.
        assert len(non_geo_data) > 0, "Non-geographic file should have entries"

        # Geographic should be the majority
        assert len(geo_data) > len(non_geo_data), "Geographic entries should be more than non-geographic"

    def test_non_geographic_contains_expected_entries(self, jsons_geography_dir):
        """Test that specific known non-geographic entries are in the right file."""

        non_geo_file = jsons_geography_dir / 'P17_2_final_ll_non_geographic.json'

        with open(non_geo_file, 'r', encoding='utf-8') as f:
            non_geo_data = json.load(f)

        # Check for known non-geographic entries
        expected_entries = [
            "brown university",
            "akonangui fc",
            "tacoma narrows bridge",
            "museum of london",
        ]

        for entry in expected_entries:
            assert entry in non_geo_data, f"Expected '{entry}' to be in non-geographic file"

    def test_geographic_contains_expected_entries(self, jsons_geography_dir):
        """Test that specific known geographic entries remain in the geographic file."""

        geo_file = jsons_geography_dir / 'P17_2_final_ll.json'

        with open(geo_file, 'r', encoding='utf-8') as f:
            geo_data = json.load(f)

        # Check for known geographic entries
        expected_entries = [
            "africa",
            "alberta",
            "alice springs",
            "aland islands",
        ]

        for entry in expected_entries:
            assert entry in geo_data, f"Expected '{entry}' to be in geographic file"
