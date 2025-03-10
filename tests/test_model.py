import os
import pytest
import numpy as np
from multi_metal_ml.model import build_model, train_model, load_or_train_model

@pytest.fixture
def sample_training_data():
    """Generates small training dataset."""
    X = np.random.rand(10, 3)  # 10 time steps, 3 areas
    y = np.zeros((10, 3, 3))  # One-hot labels
    y[:, :, 1] = 1  # Simulate all as class 1 (Bainite)
    return X, y

def test_build_model():
    model = build_model(time_steps=3)
    assert model is not None
    assert len(model.layers) == 3  # Should have 3 layers

def test_train_model(sample_training_data):
    X, y = sample_training_data
    model = train_model(X, y, time_steps=3)

    assert os.path.exists("multi_metal_ml/trained_model.keras")

def test_load_or_train_model(sample_training_data):
    X, y = sample_training_data
    model = load_or_train_model(X, np.arange(10), time_steps=3)  # Dummy time values

    assert model is not None
