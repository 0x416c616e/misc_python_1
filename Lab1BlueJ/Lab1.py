#!/usr/bin/env python3
#Lab1.py
#used to be a Java program, about calculating the area of a triangle, just for learning java
#Now I'm remaking it in python

import math

print("This program computes the area of a triangle.")
a = float(input("Enter the length of the first side of the triangle: "))
b = float(input("Enter the length of the second side of the triangle: "))
c = float(input("Enter the length of the third side of the triandle: "))
#input is string by default, but I am converting them to floating point numbers


# p is half of the perimeter
p = (a + b + c ) / 2.0
print("p is %.2f" % p) #formatted float string to only show 2 dec places
#heron's formula: https://www.mathopenref.com/heronsformula.html
# area = sqrt(p(p-a)(p-b)(p-c))
area = float(math.sqrt(p*(p-a)*(p-b)*(p-c)))

print("The area of the triangle is %.2f." % area)
print("Results are rounded to clean up the output (nobody wants to see tons of decimal places).")


