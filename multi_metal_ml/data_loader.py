import os
import pandas as pd
import numpy as np
from multi_metal_ml.preprocessing import generate_microstructure_labels

def load_data(folder_path, user_defined_mapping=None):
    """Loads multiple CSVs from a folder and processes them for multi-material ML."""
    all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]

    data_list = []
    time_values_list = []

    for file in all_files:
        df = pd.read_csv(file)
        time_column = df.iloc[:, 0].values  # Extract time values
        data_values = df.iloc[:, 1:].values  # Extract temperature and other features

        data_list.append(data_values)
        time_values_list.append(time_column)

    # Stack all data together
    X = np.vstack(data_list)
    time_values = np.hstack(time_values_list)

    # Assign materials: First half = Material 1, Second half = Material 2
    material_ids = np.array(["Material1"] * (len(time_values) // 2) + ["Material2"] * (len(time_values) // 2))

    # Generate microstructure labels
    y = generate_microstructure_labels(X, time_values, material_ids, user_defined_mapping)

    return X, y, time_values, material_ids
