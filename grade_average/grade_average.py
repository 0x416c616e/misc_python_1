#!/usr/bin/env python3

print("remaking my GradeAverage assignment in Python instead of Java")

test1 = input("Enter the 1st test score: ")
#for some reason, sublime text doesn't run this properly
#but it runs just fine in a terminal
test2 = input("Enter the 2nd test score: ")

average = ((int(test1) + int(test2)) / 2.0 )

print("The average of test1 (" + str(test1) + ") and test2 (" + str(test2) + ") is " + str(average))

if (average >= 59.5):
	print("You passed the class.")
	print("Congratulations! Good job! Bravissimo!")
else:
	print("You failed.")
	print("Try harder next time!")


