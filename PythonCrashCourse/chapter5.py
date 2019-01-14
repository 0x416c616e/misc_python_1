# chapter 5 of python crash course
# by alan

# this chapter covers if statements
'''
you know what? I'm tired of doing super simple programming exercises
I already know how to program and this book is geared towards people who
have never programmed before, so I am going to skip a lot of the stuff
I already understand instead of wasting my time
I will only go over stuff occasionally to save time because it's annoying
how basic this stuff is so far
'''

# this isn't in the book, but let me write a fizzbuzz here
# because why not?

fizz_buzz = ""
for i in range(1, 101):
    if i % 3 == 0:
        fizz_buzz += "fizz"
    if i % 5 == 0:
        fizz_buzz += "buzz"
    if fizz_buzz == "":
        print(i)
    else:
        print(fizz_buzz)
    fizz_buzz = ""

# I've demonstrated that I know how if statements work
# the rest of this chapter is a waste of time and I can just skim over it

if 1 == 1 and 2 == 2:
    print("here is an and example")
if 1 < 0 or 5 > 4:
    print("or example: at least one of these is true")

# booleans
# I already know booleans, but here is an example
i_am_learning_new_stuff = False
chapter_easiness = True
if chapter_easiness:
    print("this only prints if the boolean is true")

number = 500
if number >= 500:
    print("greater than or equal to example")

# if elif else
# easy

# checking if a list is empty:
some_list = []
if some_list:
    print("this means the list is not empty")
    # notice how it didn't go to the print statement because it evaluated to false
else:
    print("empty")


true_thing = True
if not true_thing:
    print("negation example")

false_thing = False
if not false_thing:
    print("false being negated is true")

# the book didn't even go over negation, but it's important for booleans
# simple stuff though

