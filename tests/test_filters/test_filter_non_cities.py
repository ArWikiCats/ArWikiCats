"""Tests for filtering non-city entries from yy2.json."""

import json
import pytest
from pathlib import Path


@pytest.fixture
def jsons_cities_dir() -> Path:
    return Path(__file__).parent.parent.parent / 'ArWikiCats' / 'translations' / 'jsons' / 'cities'


class TestYY2FilesIntegrity:
    """Test cases that verify the yy2.json files after filtering."""

    def test_yy2_files_exist(self, jsons_cities_dir):
        """Test that the output files exist after filtering."""

        cities_file = jsons_cities_dir / 'yy2.json'
        non_cities_file = jsons_cities_dir / 'yy2_non_cities.json'

        assert cities_file.exists(), "Cities file should exist"
        assert non_cities_file.exists(), "Non-cities file should exist"

    def test_yy2_files_have_correct_counts(self, jsons_cities_dir):
        """Test that the files have the expected number of entries."""

        cities_file = jsons_cities_dir / 'yy2.json'
        non_cities_file = jsons_cities_dir / 'yy2_non_cities.json'

        with open(cities_file, 'r', encoding='utf-8') as f:
            cities_data = json.load(f)

        with open(non_cities_file, 'r', encoding='utf-8') as f:
            non_cities_data = json.load(f)

        # Total should be 5166 (original count)
        total = len(cities_data) + len(non_cities_data)
        assert total == 5166, f"Total entries should be 5166, got {total}"

        # Non-cities should have universities, clubs, etc.
        assert len(non_cities_data) > 0, "Non-cities file should have entries"

        # Cities should be the majority
        assert len(cities_data) > len(non_cities_data), "City entries should be more than non-city"

    def test_non_cities_contains_expected_entries(self, jsons_cities_dir):
        """Test that specific known non-city entries are in the right file."""

        non_cities_file = jsons_cities_dir / 'yy2_non_cities.json'

        with open(non_cities_file, 'r', encoding='utf-8') as f:
            non_cities_data = json.load(f)

        # Check for known non-city entries
        expected_entries = [
            "london metropolitan university",
            "loughborough university",
            "lions clubs international",
        ]

        for entry in expected_entries:
            assert entry in non_cities_data, f"Expected '{entry}' to be in non-cities file"

    def test_cities_contains_expected_entries(self, jsons_cities_dir):
        """Test that specific known city entries remain in the cities file."""

        cities_file = jsons_cities_dir / 'yy2.json'

        with open(cities_file, 'r', encoding='utf-8') as f:
            cities_data = json.load(f)

        # Check for known city entries
        expected_entries = [
            "dallas-fort worth metroplex",
            "lions bay",
            "lisieux",
        ]

        for entry in expected_entries:
            assert entry in cities_data, f"Expected '{entry}' to be in cities file"

    def test_universities_are_filtered(self, jsons_cities_dir):
        """Test that universities are properly filtered to non-cities file."""

        non_cities_file = jsons_cities_dir / 'yy2_non_cities.json'

        with open(non_cities_file, 'r', encoding='utf-8') as f:
            non_cities_data = json.load(f)

        # Count universities
        universities = [k for k in non_cities_data.keys() if 'university' in k.lower()]
        assert len(universities) > 100, f"Should have filtered many universities, got {len(universities)}"

    def test_clubs_are_filtered(self, jsons_cities_dir):
        """Test that clubs/associations are properly filtered."""

        non_cities_file = jsons_cities_dir / 'yy2_non_cities.json'

        with open(non_cities_file, 'r', encoding='utf-8') as f:
            non_cities_data = json.load(f)

        # Check for clubs/associations
        clubs = [k for k in non_cities_data.keys() if 'club' in k.lower() or 'نادي' in non_cities_data[k]]
        assert len(clubs) > 0, "Should have filtered some clubs/associations"
