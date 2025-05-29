from typing import Dict, Any

def feature_26_func(health_metrics: Dict[str, Any]) -> str:
    """
    Rate a river from A (best) to F (worst) based on health metrics.
    Args:
        health_metrics: Dict with keys like 'pollution', 'biodiversity', etc.
    Returns:
        Rating string (A-F)
    """
    score = 0
    score += max(0, 100 - health_metrics.get("pollution", 0))
    score += health_metrics.get("biodiversity", 0)
    score += max(0, health_metrics.get("flow_quality", 0))
    total = score / 3
    if total >= 80:
        return "A"
    elif total >= 65:
        return "B"
    elif total >= 50:
        return "C"
    elif total >= 35:
        return "D"
    elif total >= 20:
        return "E"
    else:
        return "F"