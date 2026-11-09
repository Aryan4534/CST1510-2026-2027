# Fixed: validate conversion and report a useful message instead of crashing.
raw_line = "srv-01,used=unknown,total=100"
hostname_part, rest = raw_line.split(",", 1)
for piece in rest.split(","):
    key, value = piece.split("=", 1)
    try:
        number = float(value.strip())
        print(key.strip(), number)
    except ValueError:
        print(f"Could not convert {key.strip()!r}: {value.strip()!r} is not a number")
