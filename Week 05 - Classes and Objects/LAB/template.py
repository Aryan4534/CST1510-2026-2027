"""
RECORD CHECK - completed version
Lane: AI / Data Science
"""

from pathlib import Path

class Record:
    """Store and assess one record."""
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Store the record's label, value, and limit."""
        self.label = label
        self.value = float(value)
        self.limit = float(limit)

    def status(self):
        """Return OVER LIMIT, WARNING, or OK based on the limit."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        if percent >= 90:
            return "WARNING"
        return "OK"

def load_records(path):
    """Read comma-separated records from a text file."""
    records = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                label, value, limit = line.strip().split(",")
                records.append(Record(label, value, limit))
    return records

data_path = Path(__file__).with_name("my_records.txt")
if not data_path.exists():
    data_path.write_text(
        "survey_2026,1187,1200\n"
        "penguins_sample,350,300\n"
        "diamonds_sample,900,1000\n",
        encoding="utf-8"
    )

records = load_records(data_path)
over_limit_count = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print("=" * 34)
    print(f"  Value : {record.value:g}")
    print(f"  Limit : {record.limit:g}")
    print(f"  Status: {record.status()}")
    print("=" * 34)
    if record.status() == "OVER LIMIT":
        over_limit_count += 1

print(f"Summary: {over_limit_count} of {len(records)} records are OVER LIMIT.")
