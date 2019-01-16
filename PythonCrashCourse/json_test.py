book = {}
book['alan'] = {
    'name': 'alan',
    'address': '123 red street',
    'phone': 789789789
}
book['alice'] = {
    'name': 'alice',
    'address': '456 blue street',
    'phone': 123123123
}
import json
some_string = json.dumps(book)
print(some_string)
with open("c://data/book.txt","w") as f:
    f.write(some_string)
    print("got here")






