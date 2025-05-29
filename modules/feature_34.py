# Feature 34.py implementation here

from typing import Tuple, List

def feature_34_func(location: Tuple[float, float], geofence: List[Tuple[float, float]]) -> bool:
    """
    Determine if a GPS location is inside a geofenced polygon.
    Args:
        location: (latitude, longitude) tuple
        geofence: List of (latitude, longitude) tuples forming polygon
    Returns:
        True if inside, False otherwise
    """
    from shapely.geometry import Point, Polygon
    point = Point(location[1], location[0])
    poly = Polygon([(lng, lat) for lat, lng in geofence])
    return poly.contains(point)