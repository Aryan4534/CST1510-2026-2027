"""
RECORD CHECK - IT lane
=====================
Name  : ____________________
Lane  : IT
Date  : ____________________

Run it from this folder: python template.py
"""

def parse_line(raw_line):
    """Clean and parse one messy server usage record."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=", 1)
        fields[key.strip().lower()] = value.strip()
    return {
        "hostname": hostname_part.strip().lower(),
        "used": float(fields["used"]),
        "total": float(fields["total"]),
    }


def status_of(used, total, warning_at=90):
    """Classify server usage as OVER LIMIT, WARNING or OK."""
    if total <= 0:
        raise ValueError("total must be greater than zero")
    percentage = used / total * 100
    if percentage >= 100:
        return "OVER LIMIT"
    if percentage >= warning_at:
        return "WARNING"
    return "OK"


# Five deliberately messy records are saved in messy_lines.txt.
# Loading from a file meets the Excellent requirement.
records = []
with open("messy_lines.txt", "r", encoding="utf-8") as input_file:
    for raw_record in input_file:
        if raw_record.strip():
            try:
                records.append(parse_line(raw_record))
            except (ValueError, KeyError) as error:
                print("Could not parse:", raw_record.strip(), "-", error)

flagged_count = 0
for record in records:
    status = status_of(record["used"], record["total"])
    print(record, "|", status)
    if status != "OK":
        flagged_count += 1

print(f"Summary: {len(records)} records, {flagged_count} flagged.")
