"""
RECORD CHECK - completed Week 3 version
"""


def status_of(percent):
    """Return the status for a percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    return "OK"


def check(value, limit):
    """Return the difference and percentage for a record."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print a bordered report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Value       : {value:>10.2f}")
    print(f"  Limit       : {limit:>10.2f}")
    print(f"  Difference  : {difference:>+10.2f}")
    print(f"  Of limit    : {percent:>9.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


def main():
    """Read records until quit and report the results."""
    over_limit_count = 0

    while True:
        label = input("Record/name (or 'quit'): ")
        if label.strip().lower() == "quit":
            break

        value = float(input("Value: "))
        limit = float(input("Limit: "))

        if limit == 0:
            print("Limit cannot be 0 because the percentage would be undefined.")
            continue

        difference, percent = check(value, limit)
        status = status_of(percent)
        print_report(label, value, limit, difference, percent, status)

        if status == "OVER LIMIT":
            over_limit_count += 1

    print(f"Records over limit: {over_limit_count}")
    print("Done.")


if __name__ == "__main__":
    main()
