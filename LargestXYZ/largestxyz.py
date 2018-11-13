#!/usr/bin/env python3
#gets inputs X, Y, and Z from the user
#and then figures out which one is the largest
largest = 0
print("This program figures out which value (X, Y, or Z) is the largest.")
x = int(input("Type -1 for exit\nEnter X: "))
while (x != -1):
    y = int(input("Enter Y: "))
    z = int(input("Enter Z: "))
    if (x > y):
        largest = x
    else:
        largest = y
    if (z > largest):
        largest = z
    else:
        largest = largest; #unnecessary but illustrative
    print("The largest is " + str(largest))
    x = int(input("Type -1 for exit\n Enter X: "))
print("Exiting...")
