"""Write one roast of an everyday gadget to /output/entry.txt.

The line is a single original line of at most 200 characters roasting a
gadget or app used every day, picked to be funny, fresh and neatly worded.
"""

import os

LINE = (
    "My phone only charges if the cable is bent at one exact angle, "
    "like I'm cracking a safe every night before bed."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
