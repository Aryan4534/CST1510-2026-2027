# Fixed: strip the text before converting it to a number.
value_text = " 87 "
cleaned = value_text.strip()
value = float(cleaned)
print(value)
