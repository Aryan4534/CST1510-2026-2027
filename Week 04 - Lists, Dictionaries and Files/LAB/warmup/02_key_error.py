# Fixed: check for a key or use dict.get() before accessing an optional key.
record = {"label": "R-001", "value": 87.0}
print(record.get("status", "unknown"))
