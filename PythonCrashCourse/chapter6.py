print("chapter 6 python crash course")
# faster than my first 4 chapters, not wasting time now
# chapter 6 covers: DICTIONARIES
# key value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

# adding new key-value pairs
# dictionaries are dynamic, so you can add new key-value pairs at any time

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# modifying values in a dictionary
alien_0['x_position'] = 50
print(alien_0)

# removing key-value pairs
del alien_0['points']
print(alien_0)

# looping through all key-value pairs
user_0 = {
       'username': 'efermi',
       'first': 'enrico',
       'last': 'fermi',
       }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# you can use whatever nams you want, but it's easier to understand with key and value
for apple, orange in user_0.items():
    print("\nKey: " + apple)
    print("Value: " + orange)


favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
# looping through keys only
for name in favorite_languages.keys():
    print(name.title())

# you can also use the sorted() function to sort them

# looping through all values in a dictionary with values()
for language in favorite_languages.values():
    print(language)

# getting rid of duplicates with set()
# the set() function will only get the unique items
# notice how python was in the example dictionary twice
# but if you use set() it will only show up once
print("="*40)
for language in set(favorite_languages.values()):
    print(language.title())

# NESTING
# sometimes you'll want to store a set of dictionaries in a list or a list of items as
# a value in a dictionary
# this is nesting

# try not to nest lists and dictionaries too deeply though

# nested dictionaries kind of remind me of JSON

