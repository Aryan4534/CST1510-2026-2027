"""Week 2 Record Check mini-project."""

# ==================================================================== INPUT / PROCESS / OUTPUT
# Excellent version: repeat until the user types quit.

over_count = 0

while True:
    label = input("Label (or quit): ")
    if label.lower() == "quit":
        break

    value = float(input("Value: "))
    limit = float(input("Limit: "))

    difference = limit - value
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
        over_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:10.2f}")
    print(f"  Total       : {limit:10.2f}")
    print(f"  Free        : {difference:10.2f}")
    print(f"  Percent     : {percent:9.2f} %")
    print(f"  Status      : {status:>13}")
    print("=" * 34)

print(f"OVER LIMIT records: {over_count}")
