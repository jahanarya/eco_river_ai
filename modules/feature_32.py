# Feature 32.py implementation here
import json

def feature_32_func(data: dict = None, file_path: str = "offline_data.json", mode: str = "save") -> dict:
    """
    Save or load data locally for offline usage.
    Args:
        data: Data to be saved (used in 'save' mode)
        file_path: Local file path
        mode: 'save' to save data, 'load' to load data
    Returns:
        Loaded data dict if mode is 'load', else None
    """
    if mode == "save":
        if data is None:
            raise ValueError("No data provided to save.")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return None
    elif mode == "load":
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        raise ValueError("Invalid mode. Use 'save' or 'load'.")