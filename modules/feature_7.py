# Feature 7.py implementation here
from typing import Dict, Any, Optional

def extract_gps_from_metadata(metadata: Dict[str, Any]) -> Optional[Dict[str, float]]:
    """
    Extract GPS coordinates from image/video metadata.
    Args:
        metadata: Dict containing EXIF or similar metadata
    Returns:
        Dict with 'latitude' and 'longitude'
    """
    lat = metadata.get('GPSLatitude')
    lon = metadata.get('GPSLongitude')
    if lat and lon:
        return {'latitude': float(lat), 'longitude': float(lon)}
    return None

def feature_7_func():
    return extract_gps_from_metadata