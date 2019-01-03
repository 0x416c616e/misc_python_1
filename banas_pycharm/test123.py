import random
import sys
import os
print("hello")
# I already know some of this
# but I'm just reviewing
# and also getting experience with PyCharm instead of vim or something
'''
multi-line quote
asdasdasd
asdasdf
'''
print("new changes")
name = "Alan"
print(name)

#types in python:
#numbers, strings, lists, tuples, and dictionaries

#arithmetic operators: + - * / % ** //

quote = "\"Always remember you're unique"

multi_line_quote = '''just
like everyone else
'''
print("%s %s %s" % ("I like the quote", quote, multi_line_quote))

print("I don't like ", end="")
print("newlines")

#===============================================

#list example
grocery_list = ['Juice', #doesn't have to be on separate lines, but it can be
                'Tomatoes',
                'Potatoes',
                'Bananas']
print('First Item:', grocery_list[0])

grocery_list[0] = "Green Juice"
print('New first item: ', grocery_list[0])

print(grocery_list[1:3])

other_events = ['Wash car', 'vacuum',
                'Cash check']

#nested lists
to_do_list = [other_events, grocery_list]
print(to_do_list)
print(to_do_list[1][1])

grocery_list.append('Onions')
grocery_list.insert(1, 'Cilantro')
grocery_list.remove("Cilantro")
grocery_list.sort()

grocery_list.reverse()

del grocery_list[4]

print("to-do list after being changed:")
print(to_do_list)

print("a second to-do list:")
to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))


#tuples
pi_tuple = (3,1,4,1,5,9)

#converting tuple to list
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

#len(tuple) min(tuple) max(tuple) etc


'''
dictionaries/maps
key-values with a UNIQUE key for each value
you can't join dictionaries together the way you can join lists
'''
#dictionaries use curly braces
super_villains = {'Fiddler': 'Whatever', 'Something': 'blah'}





