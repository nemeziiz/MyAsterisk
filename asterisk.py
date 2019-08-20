#!/usr/bin/env python3
# Print Asterisk

import time

chars = r"\|/-"
print("----------\r", end="")

for r in range(10):
    for t in range(5):
        for char in chars:
            print(char, end="", flush=True)
            time.sleep(0.1)
            print("\b", end="")
    print("*", end="")
print()
