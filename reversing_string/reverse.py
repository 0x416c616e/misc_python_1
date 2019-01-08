
string_to_reverse = input("Type a string you want to reverse: ")
reversed_string = ""
for i in range(0, len(string_to_reverse)):
    reversed_string += string_to_reverse[(-1)-i]

print("reversed string: " + reversed_string)
