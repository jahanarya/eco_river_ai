# Feature 30.py implementation here


from typing import List, Dict, Any

def feature_30_func(report_list: List[Dict[str, Any]], new_report: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Submit a new public report to the system.
    Args:
        report_list: Existing list of reports
        new_report: Dict with new report data
    Returns:
        Updated list of reports
    """
    report_list.append(new_report)
    return report_list