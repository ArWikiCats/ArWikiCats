"""
Tests
"""
import pytest

from src.make2_bots.p17_bots.nats import make_sport_formats_p17, find_nat_others

def test_make_sport_formats_p17():
    # Test with a known category key (may return empty string if key not in cache)
    result = make_sport_formats_p17("basketball")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = make_sport_formats_p17("")
    assert isinstance(result_empty, str)

    # Test with a typical sport category format
    result_example = make_sport_formats_p17("football_players")
    assert isinstance(result_example, str)

def test_find_nat_others():
    # Test with a basic category string
    result = find_nat_others("American basketball players")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = find_nat_others("")
    assert isinstance(result_empty, str)

    # Test with reference category
    result_with_ref = find_nat_others("French tennis players", "sport")
    assert isinstance(result_with_ref, str)
