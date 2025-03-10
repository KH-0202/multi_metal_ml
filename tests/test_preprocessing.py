import pytest
import numpy as np
from multi_metal_ml.preprocessing import generate_microstructure_labels

@pytest.fixture
def sample_data():
    """Creates a small dataset for testing."""
    X = np.array([[300, 500, 700], [100, 800, 1200]])
    time_values = np.array([50, 600])
    material_ids = np.array(["Material1", "Material2"])
    return X, time_values, material_ids

def test_generate_microstructure_labels(sample_data):
    X, time_values, material_ids = sample_data

    # Custom user-defined mapping
    user_defined_mapping = {
        "Material1": {"Pearlite": (600, 550), "Bainite": (400, 55), "Martensite": (None, None)},
        "Material2": {"Ferrite": (500, 300), "Austenite": (700, 450), "Martensite": (None, None)}
    }

    labels = generate_microstructure_labels(X, time_values, material_ids, user_defined_mapping)

    assert labels.shape == X.shape
    assert np.any(np.isin(labels, ["Martensite", "Bainite", "Pearlite"]))  # Allow multiple phases
