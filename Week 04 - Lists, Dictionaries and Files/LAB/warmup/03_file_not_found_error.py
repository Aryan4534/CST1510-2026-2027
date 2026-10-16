# Fixed: catch FileNotFoundError and show a helpful message.
from pathlib import Path
path = Path(__file__).resolve().parent / "not_a_real_file.txt"
try:
    print(path.read_text(encoding="utf-8"))
except FileNotFoundError:
    print(f"File not found: {path.name}")
