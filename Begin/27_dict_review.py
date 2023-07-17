books = {"os": 300, "database": 500, "prog": 200}
books["network"] = 600
print(books)
dict_keys_list = list(books.keys())
dict_items_list = list(books.items())

for i in range(4):
    print(books[dict_keys_list[i]])

for i in range(4):
    print(dict_items_list[i])

print("prog" in books)
del books["os"]
print(books)
