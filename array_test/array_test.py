#!/usr/bin/env python3
#Array Test
#python doesn't support constants per se
#so I am declaring a one-item tuple instead
#because of the immutability of tuples
#(I am convering an old Java program of mine to Python)
MAXSIZE = (12,)
count = 0
total = 0
average = ""
values = [None]*MAXSIZE[0]
#this looks a little wonky but I am trying to make it close to my Java program
#in Java, you'd do something like this:
#int [] values = new int[MAXSIZE]
#but it's very different in python

num = float(input("Enter a value to pass into the array element: "))
while (count >= 0 and count < (len(values) - 1)):
    values[count] = num
    count+= 1
    num = float(input("Enter a value to pass into the array element: "))
values[count] = num

for i in range(0,MAXSIZE[0]):
    print(str(values[i]) + " ", end="")
    total += values[i]
average = total / len(values)
print("")
print("\nAverage is: " + str(average))

#I should really do proper string formatting later,
#but not now
#(original java program had string/table formatting for spacing)

for x in range(0,(count+1)):
    print(" " * 10, end="")
    print(str(values[x]), end="")
    if (x % 4 == 3):
        print("")

highest = 0

#one difference: in java, you can declare and define the function after it's called
#but here you have to specify the function before invoking it
#different order from my Java version of the same program
def findHighest(a, count):
    highest = a[0]
    for i in range(0,count):
        if (a[i] > highest):
            highest = a[i]
    return highest



