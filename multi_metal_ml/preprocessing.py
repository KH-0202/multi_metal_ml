import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Default microstructure phase mapping (can be overridden by user input)
default_label_mapping = {
    "Material1": {"Pearlite": (600, 550), "Bainite": (400, 55), "Martensite": (None, None)},
    "Material2": {"Ferrite": (500, 300), "Austenite": (700, 450), "Martensite": (None, None)}
}

def preprocess_data(X):
    """Scales and reshapes input data for the ML model."""
    scaler = MinMaxScaler(feature_range=(0, 1))
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler  # Return scaled data & scaler for later use

def generate_microstructure_labels(X, time_values, material_ids, user_defined_mapping=None):
    """
    Generates microstructure labels based on temperature, time thresholds, and material type.

    Parameters:
    - X: Temperature data array (NumPy array of shape (n_samples, n_features))
    - time_values: Corresponding time values (NumPy array of shape (n_samples,))
    - material_ids: Array indicating which material each row belongs to (NumPy array of shape (n_samples,))
    - user_defined_mapping: Optional dictionary for custom microstructure mappings

    Returns:
    - labels: Array of predicted microstructure phases (same shape as X)
    """
    # Use user-defined mapping if provided, else default mapping
    phase_mapping = user_defined_mapping if user_defined_mapping else default_label_mapping

    labels = np.full(X.shape, "Martensite", dtype=object)  # Default phase for all

    # Ensure time_values is reshaped to align with X
    time_values = np.array(time_values).reshape(-1, 1)  # (n_samples, 1)

    for material in np.unique(material_ids):  # Iterate over unique materials
        material_mask = material_ids == material  # Boolean mask for current material

        if material in phase_mapping:
            for phase, (temp_threshold, time_threshold) in phase_mapping[material].items():
                if temp_threshold is not None and time_threshold is not None:
                    # Apply conditions only to rows where material_mask is True
                    labels[np.ix_(material_mask, X[0].shape[0] * [True])] = np.where(
                        (X[material_mask] > temp_threshold) & (time_values[material_mask] >= time_threshold),
                        phase,
                        labels[material_mask]
                    )

    return labels
