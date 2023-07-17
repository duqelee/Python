animals = ["dog", "cat", "lion"]

for h in animals:
    print(h)

for i in range(3):
    print(f"{i+1}번째 요소명은 {animals[i]}이고, 자릿수는 {len(animals[i])}입니다.")

for i, v in enumerate(animals):
    print(i, v)
