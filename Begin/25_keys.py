books = {"design": 100, "prog": 200, "os": 500, "php": 400}
print(books.keys())
print(type(books))
books_dict_keylist = list(books.keys())
print(type(books_dict_keylist))
print(books_dict_keylist)
print(books["design"])
for i in range(4):
    print(books_dict_keylist[i])
books_dict_valuelist = list(books.values())
print(type(books_dict_valuelist))
print(books_dict_valuelist)
