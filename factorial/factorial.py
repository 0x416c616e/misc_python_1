#!/usr/bin/env python3

import sys

def fact(num):
    num = int(num)
    if (num <= 0):
        print("error")
        sys.exit(1)
    elif (num > 1):
        num = num * fact(num - 1)
    return num

def main():
    if (len(sys.argv) == 1):
        print("Error: needs command line args")
        print("i.e. factorial.py 10 to get the factorial of 10")
        print("or factorial.py 10 5 7 to get the factorials of 3 nums instead")
    else:
        for i in range(1, len(sys.argv)):
            print("Factorial of " + str(sys.argv[i]) + "is: ", end="")
            print(str(fact(sys.argv[i])))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()
