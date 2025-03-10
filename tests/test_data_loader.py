import os
import pytest
import numpy as np
from multi_metal_ml.data_loader import load_data

@pytest.fixture
def sample_csv(tmp_path):
    """Creates a temporary CSV file for testing."""
    csv_content = "time,temp1,temp2,temp3\n0,100,200,300\n20,400,500,600\n"
    file_path = tmp_path / "test_data.csv"
    file_path.write_text(csv_content)
    return str(file_path)

def test_load_data(sample_csv):
    X, y, time_values, material_ids = load_data(os.path.dirname(sample_csv))  # Unpack the returned tuple

    assert isinstance(X, np.ndarray)  # Ensure X is a NumPy array
    assert isinstance(y, np.ndarray)  # Ensure y is a NumPy array (labels)
    assert isinstance(time_values, np.ndarray)  # Ensure time_values is a NumPy array
    assert isinstance(material_ids, np.ndarray) # Ensure material_ids is a NumPy array

    assert X.shape == (2, 3)  # 2 rows, 3 temp columns
    assert y.shape == (2, 3)  # Labels should match X's shape
    assert time_values.shape == (2,)  # 2 time values expected

