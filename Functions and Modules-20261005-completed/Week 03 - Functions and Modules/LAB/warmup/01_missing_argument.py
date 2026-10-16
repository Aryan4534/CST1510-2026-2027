def status_of(percent, warning_at=90):
    """Return the status for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    return "OK"

print(status_of(95))
