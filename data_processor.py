# data_processor.py

import numpy as np

def normalize_features(data):
    """Simple Min-Max scaling using NumPy"""
    arr = np.array(data)
    if arr.size == 0:
        return []
    normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))
    return normalized.tolist()

if __name__ == "__main__":
    sample_data = [10, 20, 30, 40, 50]
    print("Original Data:", sample_data)
    print("Normalized Data:", normalize_features(sample_data))