# Feature 5.py implementation here

from typing import List, Dict, Any
import numpy as np

def detect_floating_waste(image_data: np.ndarray, model) -> List[Dict[str, Any]]:
    """
    Detect floating plastic/waste in river images using AI.
    Args:
        image_data: np.ndarray image from camera/drone
        model: Pre-trained waste detection model
    Returns:
        List of dicts with detected waste objects
    """
    detections = model.detect(image_data)
    return [
        {"type": obj["label"], "confidence": obj["score"], "location": obj["box"]}
        for obj in detections if obj["label"] in ["plastic", "waste", "debris"]
    ]

def feature_5_func():
    return detect_floating_waste