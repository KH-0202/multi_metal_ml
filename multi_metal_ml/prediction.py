import numpy as np
from multi_metal_ml.model import load_or_train_model

def predict_microstructure(X, model, scaler):
    """Predicts microstructure based on input temperatures."""

    # Ensure input data is scaled
    X_scaled = scaler.transform(X)
    X_scaled = X_scaled.reshape(-1, X.shape[1], 1)

    # Predict
    prediction = model.predict(X_scaled)
    predicted_labels = np.argmax(prediction, axis=2)[0]  # Get class indices

    # Convert predictions back to label names
    label_mapping = {0: "Pearlite", 1: "Bainite", 2: "Martensite"}
    decoded_labels = [label_mapping[i] for i in predicted_labels]

    # **Fix: Convert back to original temperatures**
    original_temperature = scaler.inverse_transform(X)  # FIXED: Use original X

    # Print results
    print("\nTime, Temperature Profile and Predicted Microstructure:")
    for time, temp, microstructure in zip(range(len(decoded_labels)), original_temperature.flatten(), decoded_labels):
        print(f"Time Step: {time}, Temperature: {temp:.2f}, Predicted Microstructure: {microstructure}")
