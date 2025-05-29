# Feature 35.py implementation here

import numpy as np
from typing import List, Dict, Any

def feature_35_func(sensor_data: List[Dict[str, Any]], anomaly_threshold: float = 2.5) -> Dict[str, Any]:
    """
    Advanced Feature: Real-Time Anomaly Detection in River Sensor Data

    This feature analyzes time-series sensor data (e.g., temperature, pH, turbidity)
    from river monitoring stations and detects anomalies using Z-score statistical analysis.

    Args:
        sensor_data: List of dicts, each with 'timestamp', 'sensor_id', and sensor readings (float)
        anomaly_threshold: Z-score threshold for anomaly detection (default: 2.5)

    Returns:
        Dict with 'anomalies' (list of detected anomaly records),
        'summary' (total analyzed, total anomalies), and
        'recommendations' (string)
    Example sensor_data element:
        {
            'timestamp': '2025-05-29T08:00:00Z',
            'sensor_id': 'station_1',
            'temperature': 28.4,
            'ph': 7.3,
            'turbidity': 22.1
        }
    """
    if not sensor_data:
        return {"anomalies": [], "summary": "No data provided.", "recommendations": "Check sensor network."}

    # Extract sensor keys (excluding timestamp and sensor_id)
    keys = [k for k in sensor_data[0] if k not in ['timestamp', 'sensor_id']]
    anomalies = []

    for key in keys:
        values = np.array([row[key] for row in sensor_data if key in row and isinstance(row[key], (int, float))])
        if len(values) < 2:
            continue  # Not enough data for anomaly detection

        mean = np.mean(values)
        std = np.std(values)
        if std == 0:
            continue  # No variation, no anomalies possible

        for idx, val in enumerate(values):
            z_score = abs((val - mean) / std)
            if z_score > anomaly_threshold:
                anomalies.append({
                    "timestamp": sensor_data[idx]['timestamp'],
                    "sensor_id": sensor_data[idx]['sensor_id'],
                    "metric": key,
                    "value": val,
                    "z_score": round(z_score, 2)
                })

    summary = f"Total records analyzed: {len(sensor_data)} | Total anomalies detected: {len(anomalies)}"
    recommendations = "Investigate sensor calibration or possible environmental incidents." if anomalies else "All sensor readings within normal range."

    return {
        "anomalies": anomalies,
        "summary": summary,
        "recommendations": recommendations
    }