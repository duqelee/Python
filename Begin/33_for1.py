animals = ["dog", "cat", "lion"]

for i in range(3):
    print(f"{i+1}번째 요소명은 {animals[i]}이고 글자수는 {len(animals[i])}입니다.")
a = "dog" in animals
print(a)

for b in animals:
    print(b)
