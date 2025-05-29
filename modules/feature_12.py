# Feature 12.py implementation here
import pandas as pd

def compare_annual_river_health(yearly_data: pd.DataFrame) -> pd.DataFrame:
    """
    Compare river health metrics across years.
    Args:
        yearly_data: DataFrame with columns ['year', 'metric1', 'metric2', ...]
    Returns:
        DataFrame with year-over-year comparison
    """
    comparison = yearly_data.set_index('year').diff().dropna().reset_index()
    return comparison

def feature_12_func():
    return compare_annual_river_health