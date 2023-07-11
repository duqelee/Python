#su = int(input("홀짝을 구분할 숫자를 입력하시요.\n"))
#if su % 2 == 0 :
#    print(f"{su}은(는) 짝수이다.")
#    print(f"{su} 하하하")
#else :
#    print(f"{su}은(는) 홀수이다.")

su = int(input("합격여부 알고자 하는 점수를 알려주세요.\n"))
if su > 100 :
    print(f"{su}은(는) 있을 수 없는 점수")
elif su >= 90 :
    print(f"{su}은(는) 고득점 합격")
    print(f"{su}점 하하하")
elif su > 60 :
    print(f"{su}은(는) 그럭저럭 합격")
elif su == 60 :
    print(f"{su}은(는) 턱걸이 합격")
elif su < 60 :
    print(f"{su}은(는) 불합격")
else :
    print(f"{su}은(는) 마이너스 점수는 불가능")
