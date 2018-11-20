#!/usr/bin/env python3
#finds highest value of numbers provided as
#command line arguments
#demonstrates sorting, and also taking 
#arguments from command line

import sys

#print(len(sys.argv))
#print(str(sys.argv))
#print(sys.argv[1])
def findHighest():
	high = 0
	for i in range(1,(len(sys.argv))):
		#print(int(sys.argv[i]))
		if (int(sys.argv[i]) > high):
			high = int(sys.argv[i])
	return high

if (len(sys.argv) > 1):
	print(findHighest())
else:
	print("not enough arguments provided")