#alan's python 3 exercises
#chapter 3 of Python Crash Course
#LISTS
#chapter 3 goes over lists
#a list if a collection of items in a particular order
#this kind of reminds me of arrays from java
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
#this is all really basic stuff but I'm just gonna go through the entire book anyway
#accessing elements in a list
print(bicycles[0])

#the last index in a list is -1
print(bicycles[-1])
#second to last is -2, and so on and so forth
print(bicycles[-2])

message = "My first bike was a " + bicycles[0].title() + "."

print(message)

#=============================
#Exercise 3-1
'''
Store the names of a few of your friends in a list called names.
Print each element in the list, one at a time.
'''
friends = ['John', 'John', 'Greg', 'Tom']

print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])

#==================================
'''
Exercise 3-2: Greetings
Start with the list you used in exercise 3-1, but instead of just printing 
each person's name, print a message to them. The text of each message should
be the same, but each message should be personalized with the person's name
'''

#I could use loops and a function for this, but this exercise doesn't
#want you to do all that just yet

part1 = "Hello, "
part2 = "! How are you doing today?"
print(part1 + friends[0] + part2)
print(part1 + friends[1] + part2)
print(part1 + friends[2] + part2)
print(part1 + friends[3] + part2)

#===================================
'''
Exercise 3-3: your own list
Think of your fav mode of transportation, and make a list that stores several examples.
Use your list to print a series of statements about these items,
such as "I'd like to own a Honda motorcycle."
'''
coolCars = ['Ferrari 488 GTB', 'Tesla Model S 100D', 'Acura NSX', 'Mazda Miata']
coolString = "It would be cool to drive a "

#reverse order for no particular reason
print(coolString + coolCars[-1] + ".")
print(coolString + coolCars[-2] + ".")
print(coolString + coolCars[-3] + ".")
print(coolString + coolCars[-4] + ".")
#ideally I'd want to remember DRY (Don't Repeat Yourself) but this book
#hasn't gone over functions yet so I'll do that later


#changing, adding, and removing elements

#changing an existing value
coolCars[0] = 'Ford Mustang'
print(coolCars[0])
coolCars.append('Hennessey Venom F5')
print("Cool cars list now has an additional car: \n", coolCars)


