#!/usr/bin/env python3
#Piecewise
print("Piecewise function demonstration, x and f(x)")
x = float(input("Enter value of x: "))
if (x <= -1):
	print("x <= -1")
	f_x = ((x*x) + (6*x))
elif (-1 < x and x <= 1):
	print("-1 < x <= 1")
	f_x = x
else: 
	print("x > 1")
	f_x = -1.0
print("When x = {0}, f(x) = {1}".format(str(x),str(f_x)))
