import random
import time

num1 = 0
num2 = 0
score = 0
c_ans = 0
ans = 0
now1 = time.time()
for i in range(1, 11) :
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print(f"{i}번 문제입니다.")
    c_ans = num1 * num2
    ans = int(input(f"{num1} * {num2} = "))
    if c_ans == ans :
        score += 1
        print(f"정담입니다. 현재접수는 {score} 입니다.")
    else :
        score -= 1
        print(f"오담입니다. 현재접수는 {score} 입니다.")
    print()
now2 = time.time()
print(f"{round(now2 - now1, 1)}초 동안 총 {i}문제를 푸셨습니다.")
print(f"당신의 점수는 총 {score}점 입니다.")
print("수학퀴즈가 종료되었습니다.")

