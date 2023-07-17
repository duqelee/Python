books = {"os": 5000, "prog": 3000, "database": 7000, "structure": 4000}

dict_itemslist = list(books.items())
print(type(dict_itemslist[0]))
print(type(dict_itemslist))
for i in range(4):
    print(dict_itemslist[i])
