import os
import re

LINE = "A toaster that apologises out loud every time it burns your bread, then writes a formal complaint to the bakery on your behalf."

# The entry must be exactly one sentence of 1-220 characters, with no
# leading or trailing whitespace.
assert 1 <= len(LINE) <= 220, f"line is {len(LINE)} chars"
assert "\n" not in LINE
assert LINE == LINE.strip(), "line has leading or trailing whitespace"
sentences = [s for s in re.split(r"[.!?]+", LINE) if s.strip()]
assert len(sentences) == 1, f"entry has {len(sentences)} sentences, must be exactly one"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
