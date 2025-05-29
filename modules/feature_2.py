# Feature 2.py implementation here

from typing import List
import numpy as np
import pandas as pd

def monitor_river_width(time_series_images: List[np.ndarray], model) -> pd.DataFrame:
    """
    Observe river width changes over time using images and AI.
    Args:
        time_series_images: List of np.ndarray images (ordered by time)
        model: AI model for extracting river boundaries
    Returns:
        DataFrame with date and measured width
    """
    widths = []
    for idx, img in enumerate(time_series_images):
        boundaries = model.segment_river(img)
        width = calculate_river_width_from_boundaries(boundaries)
        widths.append({"date": idx, "width": width})
    return pd.DataFrame(widths)

def calculate_river_width_from_boundaries(boundaries) -> float:
    # Dummy implementation; replace with real calculation using boundaries
    import numpy as np
    return float(np.random.uniform(100, 200))

def feature_2_func():
    # এই ফাংশন তোমার অ্যাপের main entrypoint হিসাবে কাজ করবে
    return monitor_river_width