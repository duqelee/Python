books = {"톰소여의모험": 3000, "안데르센": 5000, "이순신전기": 4000}

print(type(books))
print(books["안데르센"])
print(books["톰소여의모험"])
print(books.keys())
print(books.values())
books["공산당선언"] = 10000
print(books)
books["e"] = "가"
books["f"] = "나"
print(books)
