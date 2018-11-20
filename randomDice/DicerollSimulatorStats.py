#!/usr/bin/env python3
#converted from my Java 6M dice roll test that I eventually changed to support any number of rolls
#it also sort of doubles as a mediocre performance benchmark, so you can compare how long it takes
#one computer to complete the same amount of rolls vs. another because it measures how long it takes to do it

import secrets
import time

#just for D6, unlike the other one I made where the user gets to choose
#very simple here

frequency=[0,0,0,0,0,0,0] #0-6, but I will only use indices 1-6
						  #just so I don't get confused


#print("start time:{}".format(startTime))

numberOfRolls = int(input("How many D6 rolls would you like to simulate? "))
startTime = int(round(time.time() * 1000))
for i in range(1,numberOfRolls+1):
	diceRoll = secrets.randbelow(6)
	diceRoll += 1 #now it's 1-6 instead of 0-5
	#python doesn't have switch/case so I'm doing this differently from Java
	#if (diceRoll >= 1 and diceRoll <= 6):
		#print("valid")
	frequency[diceRoll] += 1 #increment the counter
	#else:
		#print("range error")
endTime = int(round(time.time() * 1000))
totalTimeInMs = endTime - startTime
totalTimeSeconds = totalTimeInMs / 1000
print("finished all dice simulations")
print("Frequency:")
for i in range(1, 7):
	print("Rolled a " + str(i) + ": "+ str(frequency[i]) + " times.")
print("Time taken: {0} seconds for {1} rolls".format(totalTimeSeconds, numberOfRolls))