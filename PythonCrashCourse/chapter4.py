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

