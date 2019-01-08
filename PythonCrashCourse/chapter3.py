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

#APPENDING
coolCars.append('Hennessey Venom F5')
print("Cool cars list now has an additional car: \n", coolCars)

coolCars2 = [] #starting blank
coolCars2.append('Chevy Camaro')
coolCars2.append('Mitsubishi Lancer Evo')
coolCars2.append('Honda S2000')
print(coolCars2)

#==============
#INSERTION
coolCars2.insert(0, 'Dodge Viper')
print(coolCars2)

#===========
#REMOVING
del coolCars2[1] #goodbye, camaro
print(coolCars2)

#removing with pop() instead of delete
#pop is for the stack data structure and will return whatever you popped
print("popping coolCars2:")
print(coolCars2.pop())

print("here's what's left:")
print(coolCars2)
#by default, it popped what was at the end of the list
someCar = coolCars2.pop()
#you can assign what was popped to a new variable
print("someCar is " + someCar)
#you can also pop at a specific location, which is unlike a traditional stack
#pop(1) or pop(5) or pop(n) really
anotherCar = coolCars.pop(0) #first item in the list
print("anotherCar is " + anotherCar)
'''
I am getting back into camelCase because that's what I was used to in Java
but I should really go back to using snake_case for python even though
I don't like it as much.
'''
print("="*30)
#=================
#REMOVING BY VALUE
print(coolCars)
coolCars.remove('Acura NSX')
print(coolCars)
#note: remove() only gets rid of the first occurence of what you're removing
#if there are two of the same value in the list, the second one will stay

#=========================================
'''
Exercise 3-4: guest list 
if you could invite anyone, living or deceased, to dinner, who would you invite?
make a list that includes at least three people you'd like to invite to dinner
then use your list to print a message to each person, inviting them to dinner
'''
dinner_list = ['Linus Torvalds', 'Richard Stallman', 'Tim Berners-Lee',
               'Brian Kernighan', 'Bill Gates', 'Ada Lovelace', 'Grace Hopper']

dinner_message1 = "Hello! Let's get food some time, "
print(dinner_message1 + dinner_list[0] + "!")
print(dinner_message1 + dinner_list[1] + "!")
print(dinner_message1 + dinner_list[2] + "!")
print(dinner_message1 + dinner_list[3] + "!")
print(dinner_message1 + dinner_list[4] + "!")
print(dinner_message1 + dinner_list[5] + "!")
print(dinner_message1 + dinner_list[6] + "!")



#======================================
'''
Exercise 3-5 guest list
you just head that one of your guests can't make the dinner, so you need
to send out a new set of invitations
you'll have to think of someone else to invite
'''
print("="*40)
print(dinner_message1 + dinner_list[0] + "!")
print(dinner_message1 + dinner_list[1] + "!")
print(dinner_message1 + dinner_list[2] + "!")
print(dinner_message1 + dinner_list[3] + "!")
print(dinner_message1 + dinner_list[4] + "!")
print(dinner_message1 + dinner_list[5] + "!")
print(dinner_message1 + dinner_list[6] + "!")

print(dinner_list[0] + " can't make it after all!")
dinner_list[0] = 'Steve Wozniak'
print(dinner_list[0] + "will be coming instead!")
print("New list:")
print(dinner_message1 + dinner_list[0] + "!")
print(dinner_message1 + dinner_list[1] + "!")
print(dinner_message1 + dinner_list[2] + "!")
print(dinner_message1 + dinner_list[3] + "!")
print(dinner_message1 + dinner_list[4] + "!")
print(dinner_message1 + dinner_list[5] + "!")
print(dinner_message1 + dinner_list[6] + "!")


