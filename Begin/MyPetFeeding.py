cat = {
    "name" : "나비",
    "age" : 5,
    "hungry" : True,
    "weught" : 5,
    "photo" : "*(^_^)*~~~~~~~~"
}

def feed(pet) :
    pet["hungry"] = False
    pet["weight"] = pet["weight"] + 1

print(cat)
feed(cat)
print(cat)
