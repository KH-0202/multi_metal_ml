import os
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, TimeDistributed

def build_model(time_steps):
    """Builds an LSTM model for sequence prediction."""
    model = Sequential([
        LSTM(32, return_sequences=True, input_shape=(time_steps, 1)),
        LSTM(16, return_sequences=True),
        TimeDistributed(Dense(3, activation="softmax"))
    ])
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    return model

def train_model(X, y, time_steps):
    """Trains a new LSTM model and saves it."""
    model = build_model(time_steps)
    model.fit(X, y, epochs=50, batch_size=16, validation_split=0.2)
    model.save("multi_metal_ml/trained_model.keras")
    return model

def load_or_train_model(X, y, time_steps):
    """Loads an existing model or trains a new one if not found."""
    model_path = "multi_metal_ml/trained_model.keras"
    
    if os.path.exists(model_path):
        print("Loading saved model...")
        model = load_model(model_path)
    else:
        print("No saved model found. Training a new model...")
        model = train_model(X, y, time_steps)

    return model
