# Feature 8.py implementation here
import numpy as np

def classify_river_area(image_data: np.ndarray, model) -> str:
    """
    Classify river area (urban, rural, industrial, protected, etc.).
    Args:
        image_data: np.ndarray image of river area
        model: AI classifier
    Returns:
        Area class as string
    """
    classification = model.classify(image_data)
    return classification

def feature_8_func():
    return classify_river_area