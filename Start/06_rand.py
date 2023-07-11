#import random
#print(random.random())

#import random
#print(f"선택한 수는 {random.randint(12,546)}")

#import random
#a = random.uniform(1.132, 324.3)
#print(f"1.132와 324.3 사이에 선택한 수는 {a}입니다.")

#import random
#a = random.randrange(5, 20)
#print(f"5, 20 사이에 선택한 수는 {a}입니다.")

#import random
#a = ["apple", "banana", "orange", "cat"]
#random.shuffle(a)
#print(f"{a} 입니다.")

#import random
#a = ["apple", "banana", "orange", "cat"]
#print(f"{random.choice(a)} 입니다.")

#import random
#a = random.choices([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
#print(f"선택한 수는 {a} 입니다.")

#import random
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#b = random.sample(a, 5)
#print(f"선택한 수는 {b} 입니다.")

#import random
#value = int(input("1부터 10까지 숫자 중 하나를 선택하세요."))
#selcom = random.randint(1, 10)
#if selcom == value :
#    print("정답")
#else :
#    print(f"오답, 컴퓨터가 선택한 수는 {selcom} 입니다.")

import random
print(random.randrange(12))
