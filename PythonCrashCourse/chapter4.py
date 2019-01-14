# chapter 4: working with lists
print("CHAPTER 4")
print("lööps")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    # for loop in python

# for i in whatever
# for cat in cats
# for dog in dog_list
# for item in grocery_list

'''
unlike other programming languages,
python requires indentation
'''

# you need to indent for loops
# be sure to remember the colon at the end too
# for cat in cats:
#   do(something)
# ==========================================
'''
exercise 4-1 pizzas
no more writing the entire description, takes too long and these chapters are quick/easy
'''
favorite_pizzas = ['pepperoni', 'mushroom', 'sausage']
for pizza in favorite_pizzas:
    print("I like " + pizza + " pizza")
# exercise 4-2 animals
# I already know all this stuff from bash/java/javascript/etc
# this isn't my first programming language
# but I guess I can do the basic stuff again anyway just because it's in this book
# and because I might as well laern the python-specific syntax for it
# even if I am familiar with the same basic concepts

# range() lists

for value in range(1,5):
    print(value)
# this goes from 1 (inclusive) UP TO 5
# so the above for loop prints 1,2,3,4 but not 5

numbers = list(range(1,6))  # 1,2,3,4,5

# increment by 2 instead of 1 (1 is default)
even_numbers = list(range(2,11,2)) # 2,4,6,8,10
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# some other useful functions casually mentioned in this chapter:
# min(), max(), sum()
# these can be used with lists

#LIST COMPREHENSION
#comprehension allows you to generate this same list in just one line of code

#below is an example of list comprehension
squares_comprehension = [value**2 for value in range(1,11)]
print(squares_comprehension)
#same as above multi-line for loop but this is a lot more compact
'''
exercise 4-3 counting to twenty
use a for loop to print the numbers from 1 to 20, inclusive
'''
for i in range(1,21):
    print(i)

'''
exercise 4-4 one million
make a lit of the nums from one to a million, then use a for loop
to print them out
'''
# for i in range(1,1000001):
#    print(i)
# I ran it but I'm commenting it out because it makes this program take longer to run,
# which is not desirable considering the way I am running it many times in quick succession
# when I make small changes frequently and then rebuild/run it
'''
summing a million
make a list of the nums from one to a million, and then use the min()
and max() functions to make sure your list actually starts at once and
ends at a million
then finally, use the sum() function to see how quickly python can add
a million numbers
'''
million_comprehension = [value for value in range(1,1000001)]
print("min in the million list: " + str(min(million_comprehension)))
print("max in the million list: " + str(max(million_comprehension)))
print("sum of all digits from 1 to a million: " + str(sum(million_comprehension)))
# tested it and it worked as expected
# also the comprehension didn't take much time at all
# doing the print for all the digits from 1 to a million took a long time,
# maybe because of glyph rendering and how my IDE handles characters and
# lines of output

print("moving on...")
print("="*40)
# ==========================================================
'''
exercise 4-6 odd numbers
use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. use a for loop to print each
number. 
'''
# every other number, so every 2 (the third arg to the function)
# but starting at 1 means 1, 3, 5 etc
# whereas starting with 0 would mean 0, 2, 4, etc
odd_list = [iterator for iterator in range(1,21,2)]
for item in odd_list:
    print(item)
# this is very easy stuff but hopefully I will eventually get to
# more advanced stuff

'''
exercise 4-7 threes
make a list of multiples of 3 from 3 to 30
use a for loop to print the numbers in your list
'''

multiples_of_three = [i for i in range(3,31,3)]
for item in multiples_of_three:
    print(item)

'''
exercise 4-8 cubes
a number raised to the third power is called a cube
for example, the cube of 2 is written as 2**3 in python
make a list of the first 10 cubes (cube of each int from 1 through 10)
and use a for loop to print out the value of each cube
'''
print("cubes below===============")

cubes_comprehension = [i**3 for i in range(1,11)]
for item in cubes_comprehension:
    print(item)

'''
exercise 4-9 cube comprehension
use a list comprehension to generate a list of the first 10 cubes
uhhh I already did that in part 4-8
did they only want me to do a for loop instead?
whatever, I already did it
'''

# LIST SLICE
# part of a list
# a specific group of items in a list in python
# is called a SLICE

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # prints elements 0, 1, and 2 -- not three!
# the above is an example of a list slice

# you can loop through a slice instead of looping through an entire list
# example below:
letters = 'a b c d e f'.split()
for letter in letters[:3]:
    print(letter.title())

# how to copy a list to another list using a slice
letters2 = letters[:]
letters2.append('g')
print("letters2:")
print(letters2)
print("letters:")
print(letters)
# deep copy vs. shallow copy and all that jazz
# if you did a simple assignment without a slide, both lists
# would be just two different ways of pointing to the same list
# rather than two separate list variables

# EXERCISE 4-10 SLICES
'''
using one of the programs you wrote in this chapter, add several lines to the 
end of the program that does the following:
1. print the message, "the first three items in the list are"
and then a slice to print the first three items in the list
2. print the message: three items from the middle of the list are:
and then a slice to print three items from the middle of the list
3. finally print the message "the last three items in the list are:"
followed by the last three items in the list
'''
# honestly I feel like this chapter has gone on for way too long about
# lists, I get it and this is a waste of time

cars_list = ['Ferrari', 'Chevrolet', 'Audi', 'Mercedes', 'Ford',
             'Toyota', 'Mazda', 'Hyundai', 'BMW', 'Fiat']
print("the first three items in the list are: ")
print(cars_list[0:3])
print("three items from the middle of the list are:")
print(cars_list[4:7])
print("the last three items in the list are:")
print(cars_list[-3:len(cars_list)])

# EXERCISE 4-11 my pizzas, your pizzas
'''
use your program from 4-1
make a copy of pizzas, and call it friend_pizzas
then do the following steps:
-add a new pizza to the original second list
-add a different pizza to the list
-prove that the two lists are different by
printing the message: 
"my favorite pizzas are" and then use a for
loop to print the first list
print the message "my friend's favorite pizzas are"
and then use a for loop to print the second list
'''
favorite_pizzas1 = ['pepperoni', 'mushroom', 'sausage']
friend_pizzas = favorite_pizzas1[:]
favorite_pizzas1.append('pineapple')
friend_pizzas.append('deep dish')
print("my favorite pizzas are: ", end="")
for pizza in favorite_pizzas1:
    print(pizza + " ", end="")
print("\nmy friend's favorite pizzas are: ", end="")
for pizza in friend_pizzas:
    print(pizza + " ", end="")

# exercise 4-12 more loops
'''
all versions of food.py in this section have avoided
using for loops when printing to save space
choose a version of foods.py, and write two for loops
to print each list of foods
'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my foods:")
for food in my_foods:
    print(food)
print("friend's foods:")
for food in friend_foods:
    print(food)


# done with lists now

# TUPLES
# python refers to a value that can't change as being immutable
# an immutable list is called a tuple
# tell me something I don't know
# this is kind of a waste of time because it's such basic review
# but oh well
# a list uses square brackets
# but a tuple uses parentheses
'''
writing over a tuple
you can't modify a value in a tuple
however, you can redefine the entire tuple
'''

# tuple is like const in java
# use it for things that don't change and shouldn't be able to be changed

# exercise 4-13 buffet
'''
a buffet-style restaurant offers only five basic foods
think of five simple foods and store them in a tuple

use a for loop to print each food offered by the restaurant
try to modify one of the items, and make sure python won't let you
the restaurant changes its menu, so rewrite the tuple
and then use a for loop to print the items in the new menu
'''
buffet_menu = ('salad', 'chicken', 'soup', 'green beans', 'steak')
for item in buffet_menu:
    print(item)
# now replace it
buffet_menu = ('salad', 'chicken', 'soup', 'carrots', 'salmon')
for item in buffet_menu:
    print(item)
# so you can replace an entire tuple, but not an individual value in it

# lines should be less than 80 characters, generally

# exercise 4-15 code review
'''
choose three of the progams you've written in this chapter and 
modify each one to comply with PEP 8
use four spaces for each identation level
use less than 80 characters on each line
don't use blank lines excessively in your program files

'''
# my programs are basically pep 8 compliant as-is


