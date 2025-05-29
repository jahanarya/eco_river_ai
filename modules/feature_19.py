# Feature 19.py implementation here

from typing import Dict, Any

def tag_urgent_level(report: Dict[str, Any], urgency_rules: Dict[str, Any]) -> str:
    """
    Tag report with urgency level based on rules.
    Args:
        report: Report dict
        urgency_rules: Dict with criteria for urgency
    Returns:
        Urgency level tag ('high', 'medium', 'low')
    """
    level = 'low'
    for rule, value in urgency_rules.items():
        if report.get(rule) == value:
            level = 'high'
            break
    report['urgency'] = level
    return level

def feature_19_func():
    return tag_urgent_level