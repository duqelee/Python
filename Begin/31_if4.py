a = 100 > 0
b = 100 < 0
if a == b:
    print("맞다")
else:
    print("틀리다")

id = "imagine"
password = "1234"

if id == "imagine2":
    if password == "123":
        print("로그인 되었습니다.")
    else:
        print("패스워드가 틀렸습니다.")
else:
    print("아이디가 틀렸습니다.")

if 0:
    print(1111)
a = bool(1)
if a:
    print("부울참")
else:
    print("부울거짓")
b = 0xFF
if b:
    print("16진수참")
else:
    print("16진수거짓")
