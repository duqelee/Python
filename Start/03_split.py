#이스케이프 시퀀스
# \m 엔터키
# \t 탭키
# \\ 원화기호
a, b = input("곱샘할 두 수를 입력하세요. 예) 3 4 \n").split()
print(f"{a}와 {b}의 덧샘 결과는 {int(a) + int(b)} 입니다.")
print(f"{a}와 {b}의 뺠샘 결과는 {int(a) - int(b)} 입니다.")
print(f"{a}와 {b}의 곱샘 결과는 {int(a) * int(b)} 입니다.")
print(f"{a}와 {b}의 나눗샘 결과는 {int(a) / int(b)} 입니다.")
