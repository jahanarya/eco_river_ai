# Feature 21.py implementation here

from typing import List, Dict, Any

def feature_21_func(records: List[Dict[str, Any]], relevance_field: str = "relevance") -> List[Dict[str, Any]]:
    """
    Prioritize records based on a relevance score or field.
    Args:
        records: List of dicts containing record data
        relevance_field: The field on which to sort (higher = more relevant)
    Returns:
        List of records sorted by relevance
    """
    return sorted(records, key=lambda x: x.get(relevance_field, 0), reverse=True)