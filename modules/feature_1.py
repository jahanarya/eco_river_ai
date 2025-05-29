# Feature 1.py implementation here
 
from typing import List, Dict, Any
import numpy as np

def detect_illegal_occupation(image_data: np.ndarray, model) -> List[Dict[str, Any]]:
    """
    Detect illegal occupation on riverbanks using AI model.
    Args:
        image_data: np.ndarray image (satellite/drone)
        model: Pre-trained AI model
    Returns:
        List of dict with detected occupations and their locations
    """
    results = model.predict(image_data)
    return [
        {"label": obj["label"], "confidence": obj["score"], "location": obj["box"]}
        for obj in results if obj["label"] == "illegal_occupation"
    ]

def feature_1_func():
    # এখানে তুমি যেভাবে চাও detect_illegal_occupation কল করতে পারো, অথবা শুধু ফাংশন রেফারেন্স ফেরত দিতে পারো
    return detect_illegal_occupation