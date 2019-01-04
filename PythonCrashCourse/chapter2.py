#I'm Alan and this is my chapter 2 exercises file. It's a bunch of notes
#and learning and exercises from the No Starch Press book called
#Python Crash Course. (comment #1 for exercise 2-10)

#2-1 simple message as described in book
message = "this is a message just for you!"
print(message)
#2-2 change value and then print
#this is too easy, why am I wasting my time on this?
message = "this is a new message"
print(message)
string1 = 'single quotes'
string2 = "double quotes"
print("in python, you can use " + string1 + " or " + string2, end="")
print(" and the last print() had no \nnewline afterwards")

#title capitalization
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "bob"
last_name = "ross"
full_name = first_name + " " + last_name
#concatenation, I already know these concepts
print(full_name)
print("newline \nand\t\t\ttab")

#stripping whitespace from a string example
favorite_language = ' python' #notice space at the beginning
'''
use lstrip for front
rstrip for rear'''
print(favorite_language.lstrip())



#========================================

print("next section...\n")
print("="*30) #repetition

#2-3 personal message
#store a person's name in a variable, and print a message to that person
name2 = "Alan"
print("Hello, " + name2 + "!")


#2-4 name cases
#store a person's name in a variable, and then print that person's name in
#lowercase,. uppercase, and titlecase

name_case_test = "JoHn DoE"
print(name_case_test.upper())
print(name_case_test.lower())
print(name_case_test.title())

'''2-5 famous quote
find a quote from a famous person you admire, print the quote and the name
of its author. your output should look something like the following,
including the quotation marks:
Albert Eintein once said, "A person who
never made a mistake never tried anything
new.
'''
print("Eric Schmidt once said, \"Do not\n"
      "be afraid to fail, but also, do \n"
      "not be afraid to succeed.\"")



#2-6 famous quote 2
#repeat exercise 205 but this time store the famous person's name
#in a variable called famous_person. Then compose your message and
#store it in a new variable called message. print your message.
famous_person = "Eric Schmidt"
message = famous_person + " once said, \"Do not\n" \
                          "be afraid to fail, but also, do \n" \
                          "not be afraid to succeed.\""
print("new message:")
print(message)


print("=" * 30 + "\nmoving on to 2-7:")
#2-7 stripping names
#store a person's name, and include some whitespace characters at the
#beginning and end of the name. make sure you use each character combo,
#\t and \n, at least once. print the name displayed, so the whitespace
#around the name is displayed. then print the name using each of the three
#stripping functions, lstrip(), rstrip(), and strip()
space_name = "\t bob something \n"
print(space_name)
print(space_name.rstrip())
print(space_name.lstrip())
print(space_name.strip())




#=======================================
'''
8    8  8    8  8     8  8888   88888  88888   88888
88   8  8    8  88   88  8   8  8      8    8  8
8 8  8  8    8  8 8 8 8  8888   88888  88888    888
8  8 8  8    8  8  8  8  8   8  8      8   8       8
8   88  888888  8     8  8888   88888  8    8  888888 
'''

print("="*30 + "\n 2-8:")

#not gonna be bothered to write down all the basic arithmetic stuff
#and operator things I already learned from pervious programmign classes
#regular math, modulus, floor division, ints and floats, etc.
#convert an int to a str with str() or else you'll get errors
#when concatenating numeric types with strings
#and so on and so forth
#PEMDAS, parentheses, etc.

'''
Exercise 2-8: NUMBER EIGHT
write addition, subtraction, multiplication, and division operations
that each result in the number 8
be sure to enclose your operations in print statements to see the results
you should create four lines that look like this:
print(5 + 3)
'''
print(28%10) #modulus
print((16//5)+5) #floor division
print(2**3) #exponentiation
print(20-(10+2)) #order of operations

'''
Exercise 2-9: favorite number
store your favorite number in a variable.
then, using that variable, create a message that reveals your 
favorite number. print that message.
'''
favorite_number = 2147483647 #double mersenne prime number
                             #also the greatest signed 32-bit int value
                             #comes up in games and underflow attacks
print("My favorite number is " + str(favorite_number) + ".")


#comments
'''
I've been using comments
throughout this whole thing
so there's not much else to say here
'''
#code should ideally be self-documenting, but some comments here and there
#don't hurt
#but don't overdo it

'''
Exercise 2-10: adding comments
choose two of the programs you've written, and add at least one comment 
to each. if you don't have anything specific to write because your programs
are too simple at this point, just add your name and the current date at the
top of each program file. then write one sentence describing what the program
does.
'''
#ok, I commented the top of this program, and also EZcrypt, which is a Java
#program I also put on GitHub

#The Zen of Python
import this
#programming language easter egg?


