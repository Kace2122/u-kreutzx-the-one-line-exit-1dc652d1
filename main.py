#!/usr/bin/env python3
"""One-Line Exit entry: writes one funny resignation letter to /output/entry.txt."""

import os

LETTER = "Dear boss, I quit. My last day is today, my replacement is the intern, and the Wi-Fi password dies with me."

# Self-check: the entry must stay exactly one line, with no leading or
# trailing whitespace padding the letter.
assert "\n" not in LETTER and len(LETTER) > 0
assert LETTER == LETTER.strip()

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)
    # Self-check: the file on disk must hold exactly the validated line.
    assert open("/output/entry.txt", encoding="utf-8").read() == LETTER

if __name__ == "__main__":
    main()
