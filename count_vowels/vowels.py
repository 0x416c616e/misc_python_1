#!/usr/bin/env python3

import sys

def count_vowels(str_to_check):
    num = 0
    vowels = "a e i o u".split(" ")
    for char in str_to_check:
        if char in vowels:
            num += 1
    return num

def main():
    if (len(sys.argv) == 1):
        print("Error: lacking CLI args")
        print("Use it like this: vowels.py hello world ok")
        sys.exit(1)
    else:
        total = 0
        print(sys.argv[1])
        for i in range(1, len(sys.argv)):
            total += count_vowels(sys.argv[i])
    print(str(total) + " vowel", end="")
    if (total > 1):
        print("s")
    else:
        print("")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()
