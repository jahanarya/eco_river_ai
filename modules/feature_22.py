from typing import List, Dict, Any
from datetime import datetime, timedelta

def feature_22_func(alerts: List[Dict[str, Any]], time_limit_hours: int = 24) -> List[Dict[str, Any]]:
    """
    Escalate alert level if not acted upon within a time limit.
    Args:
        alerts: List of alert dicts with 'created_at' and 'status'
        time_limit_hours: Hours after which to escalate
    Returns:
        Updated list with 'escalated' field set where appropriate
    """
    now = datetime.utcnow()
    for alert in alerts:
        escalated = False
        if alert.get('status') == 'pending':
            created = alert.get('created_at')
            created_dt = None
            if created:
                if isinstance(created, str):
                    try:
                        # Handle ISO string possibly ending with 'Z'
                        if created.endswith('Z'):
                            created = created.replace('Z', '+00:00')
                        created_dt = datetime.fromisoformat(created)
                    except Exception:
                        created_dt = None
                elif isinstance(created, datetime):
                    created_dt = created
            if created_dt and (now - created_dt) > timedelta(hours=time_limit_hours):
                escalated = True
        alert['escalated'] = escalated
    return alerts