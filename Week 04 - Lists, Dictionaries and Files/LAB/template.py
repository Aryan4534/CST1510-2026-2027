"""Record Check mini-project — Week 4."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "records_data.txt"
RESULTS_PATH = BASE_DIR / "results.txt"


def check_record(value, limit):
    """Calculate difference, percentage of limit, and status."""
    if limit == 0:
        raise ValueError("limit must not be zero")
    difference = value - limit
    percent = value / limit * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report for one record."""
    print("=" * 38)
    print(f"RECORD CHECK - {label}")
    print(f"Value       : {value:10.2f}")
    print(f"Limit       : {limit:10.2f}")
    print(f"Difference  : {difference:+10.2f}")
    print(f"Of limit    : {percent:9.1f}%")
    print(f"Status      : {status}")
    print("=" * 38)


def load_records(path):
    """Load label,value,limit rows from a text file."""
    records = []
    with open(path, encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            parts = line.strip().split(",")
            if len(parts) != 3:
                raise ValueError(f"line {line_number} must contain label,value,limit")
            label, value, limit = parts
            records.append({"label": label, "value": float(value), "limit": float(limit)})
    return records


def main():
    """Load records, report results, and save statuses."""
    try:
        records = load_records(DATA_PATH)
    except FileNotFoundError:
        print(f"Records file not found: {DATA_PATH}")
        records = []
    except ValueError as error:
        print(f"Could not load records: {error}")
        records = []

    over_limit_count = 0
    results = []
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        print_report(record["label"], record["value"], record["limit"], difference, percent, status)
        results.append(f"{record['label']},{status}")
        if status == "OVER LIMIT":
            over_limit_count += 1

    RESULTS_PATH.write_text("\n".join(results) + ("\n" if results else ""), encoding="utf-8")
    print(f"Checked {len(records)} records. {over_limit_count} were over limit.")
    print(f"Results saved to {RESULTS_PATH.name}")


if __name__ == "__main__":
    main()
