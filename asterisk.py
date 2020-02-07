#!/usr/bin/env python3
# Print Asterisk


from time import sleep

print("----------\r", end="")
chars = r"\|/-"

for column in range(10):
    for field in range(2):
        for char in chars:
            print(char, end="", flush=True)
            sleep(0.1)
            print("\b", end="")
    print("*", end="")

print(" \b", end="")

for column in range(10):
    for field in range(2):
        for char in chars:
            print(char, end="", flush=True)
            sleep(0.1)
            print("\b", end="")
    print(" \b\b", end="")
