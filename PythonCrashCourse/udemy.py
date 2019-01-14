# take a string and return alternating caps
def myfunc(some_string):
    counter = 1
    return_string = ""
    for letter in range(0, (len(some_string))):
        if counter % 2 == 0:
            return_string += some_string[letter].upper()
        else:
            return_string += some_string[letter].lower()
        counter = counter + 1
        print(counter)
    return return_string
print(myfunc("antarctica"))