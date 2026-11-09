# Fixed: split only once so the value may contain another "=".
piece = "note=server=east"
key, value = piece.split("=", 1)
print(key, value)
