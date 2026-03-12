"""Test ingredient normalization module"""

import pytest

from mytxgnn.mapping.normalizer import (
    normalize_ingredient,
    extract_ingredients,
    extract_primary_ingredient,
    get_all_synonyms,
)


class TestNormalizeIngredient:
    """Test normalize_ingredient function"""

    def test_simple_name(self):
        """Simple name unchanged"""
        assert normalize_ingredient("METRONIDAZOLE") == "METRONIDAZOLE"

    def test_removes_eq_to_synonym(self):
        """Removes EQ TO synonym"""
        result = normalize_ingredient("SODIUM BICARBONATE ( EQ TO SODIUM HYDROGEN CARBONATE)")
        assert result == "SODIUM BICARBONATE"

    def test_removes_vitamin_notation(self):
        """Removes vitamin notation"""
        result = normalize_ingredient("RIBOFLAVIN (VIT B2)")
        assert result == "RIBOFLAVIN"

    def test_uppercase(self):
        """Converts to uppercase"""
        assert normalize_ingredient("metronidazole") == "METRONIDAZOLE"

    def test_removes_extra_spaces(self):
        """Removes extra spaces"""
        result = normalize_ingredient("SODIUM   BICARBONATE")
        assert result == "SODIUM BICARBONATE"

    def test_empty_string(self):
        """Handles empty string"""
        assert normalize_ingredient("") == ""
        assert normalize_ingredient(None) == ""


class TestExtractIngredients:
    """Test extract_ingredients function"""

    def test_single_ingredient(self):
        """Single ingredient"""
        result = extract_ingredients("METRONIDAZOLE")
        assert result == ["METRONIDAZOLE"]

    def test_multiple_ingredients_semicolon(self):
        """Multiple ingredients (semicolon separated)"""
        result = extract_ingredients("DEXTROMETHORPHAN HBR;;DIPHENHYDRAMINE HCL")
        assert result == ["DEXTROMETHORPHAN HBR", "DIPHENHYDRAMINE HCL"]

    def test_multiple_ingredients_single_semicolon(self):
        """Multiple ingredients (single semicolon)"""
        result = extract_ingredients("VITAMIN A;VITAMIN C;VITAMIN E")
        assert result == ["VITAMIN A", "VITAMIN C", "VITAMIN E"]

    def test_removes_duplicates(self):
        """Removes duplicate ingredients"""
        result = extract_ingredients("SUCROSE;;SUCROSE;;SUCROSE")
        assert result == ["SUCROSE"]


class TestExtractPrimaryIngredient:
    """Test extract_primary_ingredient function"""

    def test_returns_first(self):
        """Returns first ingredient"""
        result = extract_primary_ingredient("VITAMIN A;;VITAMIN C")
        assert result == "VITAMIN A"

    def test_empty_returns_empty(self):
        """Empty input returns empty string"""
        assert extract_primary_ingredient("") == ""


class TestGetAllSynonyms:
    """Test get_all_synonyms function"""

    def test_single_eq_to(self):
        """Single EQ TO synonym"""
        result = get_all_synonyms(
            "SODIUM BICARBONATE ( EQ TO SODIUM HYDROGEN CARBONATE)"
        )
        assert len(result) == 1
        assert result[0][0] == "SODIUM BICARBONATE"
        assert "SODIUM HYDROGEN CARBONATE" in result[0][1]

    def test_no_synonyms(self):
        """No synonyms"""
        result = get_all_synonyms("METRONIDAZOLE")
        assert len(result) == 1
        assert result[0][0] == "METRONIDAZOLE"
        assert result[0][1] == []
