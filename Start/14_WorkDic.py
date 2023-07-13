#x = ["사과", "오징어", "문어", "수박"]
#y = {"과일" : "사과", "생선" : "오징어", "유인원" : "침팬치", "액체" : "물"}
#print(x)
#print(y)
#
#planets = {"수성" : "Mercury", "금성" : "Vinus", "지구" : "Earth", "화성" : "Mars"}
#print(planets)
#x = planets["지구"] #키를 사용
#y = planets.get("수성") #함수 사용
##print("지구는 영어로 ", x)
#print("수성은 영어로 ", y)
#
#planets["목성"] = "Jupiter"
#print(planets)
#
#del planets["금성"]
#print(planets)

dic_han = {"자" : "아들자(子)","여" : "여자녀(女)","천" : "하늘천(天)", "지" : "땅지(地)","천" : "내천(川)"}
user_input = input("찾고자 하는 한자의 뜻을 입력하세요. \n >>>")

if user_input in dic_han :
    print(f"입력하신 {user_input}의 의미는 {dic_han[user_input]}입니다.")
else :
    print("검색한 한자는 등록되어 있지 않습니다.")