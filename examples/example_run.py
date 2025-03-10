import os
from multi_metal_ml.data_loader import load_data
from multi_metal_ml.preprocessing import preprocess_data
from multi_metal_ml.model import load_or_train_model
from multi_metal_ml.prediction import predict_microstructure

# === Get Training Folder from User ===
print("Enter the folder path containing your training CSV files:")
training_folder = input().strip()

# === Get Prediction File from User ===
print("Enter the path to your prediction CSV file:")
prediction_file = input().strip()

# === User-Defined Microstructure Phases ===
user_defined_mapping = {}
for material in ["Material1", "Material2"]:
    user_defined_mapping[material] = {}
    while True:
        print(f"Define microstructure phases for {material} (or type 'done' to finish):")
        phase_name = input("Phase Name: ").strip()
        if phase_name.lower() == "done":
            break
        temp_threshold = input(f"Temperature threshold for {phase_name}: ").strip()
        time_threshold = input(f"Time threshold for {phase_name}: ").strip()
        user_defined_mapping[material][phase_name] = (float(temp_threshold), float(time_threshold))

# === Load and Preprocess Data ===
X_train, y_train, time_values_train, material_ids_train = load_data(training_folder, user_defined_mapping)
X_scaled, scaler = preprocess_data(X_train)

# === Train or Load Model ===
time_steps = X_scaled.shape[1]  # Get time steps from scaled data
model = load_or_train_model(X_scaled, y_train, time_steps)

# === Load Prediction Data ===
X_pred, time_values_pred, _, _ = load_data(prediction_file, user_defined_mapping)
X_pred_scaled, _ = preprocess_data(X_pred)

# === Run Predictions ===
predict_microstructure(X_pred_scaled, model, scaler)
