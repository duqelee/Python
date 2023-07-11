#import random
#quiz = """    ┏━━━━━┓
#    ┃ 　　 　┃
#    ┃　┏━┓　┃
#    ┗━┛　┃　┃
#    　　┏━┛　┃
#    　　┃　┏━┛
#    　　┗━┛
#    　　┏━┓
#    　　┃　┃
#　    　┗━┛
#　    　　〇
#　    　　ｏ
#　    　　　(・д・)"""
#print()
#print(quiz)
#print("1~10까지 숫자가 있습니다.")
#print()
#computer_num = random.randint(1, 10)
#user_num = 0
#count = 0
#while computer_num != user_num :
#    user_num = int(input("컴퓨터가 뽑은 숫자는?"))
#    count +=1
#
#    if computer_num > user_num :
#        print("더 큰 수 입니다.")
#    elif computer_num < user_num :
#        print("더 작은 수 입니다.")
#
#    print()
#
#print(f"{computer_num} 정답입니다. {count}회 만에 맞추셨습니다.")





import random
com_num = random.randint(1, 10)
sel_num = 0
i = 0
for i in range(100) :
    sel_num = int(input("컴퓨터가 선택한 숫자를 맞춰보세요"))
    if com_num == sel_num :
        break
    elif com_num > sel_num :
        print("더 큰 수 있니다.")
    elif com_num < sel_num :
        print("더 작은 수 입니다.")
print("컴퓨터가 선택한 숫자는", com_num, "이고, ", i+1, "번 만에 맞추셨습니다.")
        
