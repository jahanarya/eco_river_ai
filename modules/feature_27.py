# Feature 27.py implementation here
def feature_27_func(rainfall: float, river_level: float, threshold: float = 10.0) -> str:
    """
    Analyze flood risk based on rainfall and river level.
    Args:
        rainfall: Recent rainfall amount (mm)
        river_level: Current river water level (m)
        threshold: Water level threshold for flooding (m)
    Returns:
        Risk level ('low', 'medium', 'high')
    """
    risk = 'low'
    if river_level >= threshold or rainfall > 100:
        risk = 'high'
    elif river_level >= threshold * 0.8 or rainfall > 60:
        risk = 'medium'
    return risk