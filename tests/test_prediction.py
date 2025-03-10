import pytest
import numpy as np
from multi_metal_ml.prediction import predict_microstructure
from multi_metal_ml.preprocessing import preprocess_data
from multi_metal_ml.model import load_or_train_model

@pytest.fixture
def sample_prediction_data():
    """Generates a sample dataset for predictions."""
    X = np.random.rand(5, 3)  # 5 time steps, 3 areas
    time_values = np.linspace(10, 100, 5)  # Simulated time values
    return X, time_values

def test_predict_microstructure(sample_prediction_data):
    X, time_values = sample_prediction_data
    X_scaled, scaler = preprocess_data(X)

    model = load_or_train_model(X_scaled, time_values, time_steps=3)

    try:
        predict_microstructure(X_scaled, model, scaler)
        assert True  # If it runs, the test passes
    except Exception as e:
        pytest.fail(f"Prediction failed with error: {e}")
