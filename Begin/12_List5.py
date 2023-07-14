animal = ["human", "birds", "elephant", 5, 3.14]
# print(type(animal[4]))

for i in range(5):
    print(type(animal[i]))
del animal[:3]
print(animal)
