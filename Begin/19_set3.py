animals = {"cat", "dog"}
print(type(animals))
animals.update({"tiger", 3.14, 5645564})
print(animals)
animals.remove(3.14)
print(animals)
animals.clear()
print(animals)
animals.update({1, 2, 3, 4, 5, 6})
print(animals)

string = "AaBBb"
print(type(string))
print(string.capitalize())
string = set(string)
print(type(string))
print(string)
string.clear()
print(string)
del string
