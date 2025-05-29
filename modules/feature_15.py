# Feature 15.py implementation here
import numpy as np

def simulate_water_flow(river_profile: np.ndarray, rainfall: float, model) -> np.ndarray:
    """
    Simulate river water flow based on river profile and rainfall using hydrological model.
    Args:
        river_profile: np.ndarray representing river cross-sections
        rainfall: Rainfall amount (mm)
        model: Hydrological simulation model
    Returns:
        np.ndarray with simulated flow values
    """
    simulation = model.simulate(river_profile, rainfall)
    return simulation

def feature_15_func():
    return simulate_water_flow