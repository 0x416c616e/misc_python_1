#!/usr/bin/env python3
import secrets #secure random numbers

numberOfSides = int(input("What kind of dice would you like to use? Ex: enter 6 for d6: "))
print("You have chosen d{0} dice".format(numberOfSides))

numberOfRolls = 1
while (numberOfRolls % 10 != 0):
	numberOfRolls = int(input("How many dice would you like to roll? Must be a multiple of 10: "))



for i in range(1, numberOfRolls + 1):
	if (i % 10 != 0):
		diceRoll = secrets.randbelow(numberOfSides)
		diceRoll += 1 #now it's 1-6 instead of 0-5
		print(str(diceRoll) + " ", end="")
	else:
		diceRoll = secrets.randbelow(numberOfSides)
		diceRoll += 1 #now it's 1-6 instead of 0-5
		print(str(diceRoll))