# utils.py - Contains helper functions and label mappings

# Define label mapping for microstructure classifications
label_mapping = {
    "Pearlite": 0,
    "Bainite": 1,
    "Martensite": 2
}

def get_label_mapping():
    """Return the label mapping dictionary."""
    return label_mapping
