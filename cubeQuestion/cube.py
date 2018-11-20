#!/usr/bin/env python3
#Given an int variable n that has been initialized to a positive value and, 
#in addition, int variables x and total that have already been declared, 
#use a for loop to compute the sum of the cubes of the first n whole numbers 
#and store this value in total. Use no variables other than n, x, and total.


print("cube summation, sorta like factorial but with cubes")

n = 0
while (n <= 0):
	n = int(input("Please enter a positive integer: "))

total = 0
for x in range(1,n+1):
	total += x * x * x
print(total)