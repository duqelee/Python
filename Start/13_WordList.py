#x = ["사과", "배", "바나나"]
#print(x)

#planet = ["수성", "금성", "지구", "화성"]
#print(planet)
#planet[2] = "목성"
#print(planet)
#planet.append("지구")
#print(planet)
#planet.remove("목성")
#print(planet)

# Make Dictionary
print("나의 영어사전")
print("="*60)
vocca = ["Apple : 사과", "Anytime : 언제나", "Answer : 대답", "Animation : 만화"]
user = 0
while user != "4" :
    #for i in range(4) :
    #    print(f"{vocca[i]}")
    #for i in vocca :
    #    print(f"{i}")
    #
    print("""
    ======== 사전 수정 모드 ========
    1. 등록된 단어 보기
    2. 단어 추가하기
    3. 단어 삭제하기
    4. 사전 수정모드 종료하기
    ================================""")

    user = input("원하는 기능을 입력하세요(숫자만...). ")
    if user == "1" :
        print()
        print("등록된 단어")
        for i in vocca :
            print(f"{i}")
    elif user == "2" :
        print()
        new_vocca = input("입력할 새로운 단어는? ")
        vocca.append(new_vocca)
        for i in vocca :
            print(f"{i}")
    elif user == "3" :
        print()
        del_vocca = input("삭제할 단어는? ")
        vocca.remove(del_vocca)