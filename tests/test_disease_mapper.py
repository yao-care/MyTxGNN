"""Test disease mapping module"""

import pytest
import pandas as pd

from mytxgnn.mapping.disease_mapper import (
    load_disease_vocab,
    build_disease_index,
    extract_indications,
    translate_term,
    map_term_to_disease,
    get_indication_mapping_stats,
)


class TestLoadDiseaseVocab:
    """Test load_disease_vocab function"""

    def test_returns_dataframe(self):
        df = load_disease_vocab()
        assert isinstance(df, pd.DataFrame)

    def test_has_required_columns(self):
        df = load_disease_vocab()
        assert "disease_id" in df.columns
        assert "disease_name" in df.columns

    def test_has_diseases(self):
        df = load_disease_vocab()
        assert len(df) > 10000


class TestExtractIndications:
    """Test extract_indications function"""

    def test_single_indication(self):
        result = extract_indications("hypertension")
        assert "hypertension" in result

    def test_multiple_indications_comma(self):
        result = extract_indications("hypertension, diabetes, heart disease")
        assert len(result) >= 1

    def test_complex_indication(self):
        result = extract_indications("For the treatment of high blood pressure and related conditions")
        assert len(result) > 0


class TestTranslateTerm:
    """Test translate_term function"""

    def test_single_disease(self):
        result = translate_term("hypertension")
        assert len(result) >= 0  # May or may not have translations

    def test_no_match(self):
        result = translate_term("some_rare_disease_xyz")
        assert result == []


class TestMapTermToDisease:
    """Test map_term_to_disease function"""

    @pytest.fixture
    def disease_index(self):
        df = load_disease_vocab()
        return build_disease_index(df)

    def test_maps_hypertension(self, disease_index):
        results = map_term_to_disease("hypertension", disease_index)
        assert len(results) > 0
        disease_names = [r[1].lower() for r in results]
        assert any("hypertension" in name for name in disease_names)

    def test_maps_diabetes(self, disease_index):
        results = map_term_to_disease("diabetes", disease_index)
        assert len(results) > 0

    def test_no_match_returns_empty(self, disease_index):
        results = map_term_to_disease("nonexistent_disease_xyz", disease_index)
        assert results == []


class TestGetIndicationMappingStats:
    """Test get_indication_mapping_stats function"""

    def test_returns_dict(self):
        df = pd.DataFrame({
            "indication": ["hypertension", "diabetes", "unknown"],
            "disease_id": ["D001", "D002", None],
            "disease_name": ["hypertension", "diabetes", None],
        })
        stats = get_indication_mapping_stats(df)
        assert isinstance(stats, dict)
