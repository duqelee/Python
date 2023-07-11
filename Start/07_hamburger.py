store = """___                ___      _____     ______   ___ 
|   w   |     |  |   w    /       |   |          |   w
|     |  |     |  |    |   |        |   |          |    |
|___/   |     |  |   /    |     __     |__       |   /
|   w   |     |  |__/    |        w   |          |__/ 
|     |  w    /   |   w   |        |   |          |   w 
|___/   w__/    |    w  w____/    |_____  |    w"""
menu = """1 불고기버거 : 5,500원
2 치즈버거 : 4,500원
3 에그버거 : 4,000원

6 콜라 : 2,500원
7 사이다 : 2,000원

각 버거 세트메뉴 있습니다.
세트메뉴 주문시 500원 할인 됩니다."""
bar = "#" * 40

print(store)
print(bar)
print(menu)
print(bar)

b_order = input("햄버거를 주문하세요.")
d_order = input("음료를 주문하세요.")
s_order = input("세트메뉴로 주문하시겠습니까?")

b_price = 0
d_price = 0
s_price = 0

if b_order == "불고기버거" :
    b_price = 5500
elif b_order == "치즈버거" :
    b_price = 4500
elif b_order == "에그버거" :
    b_price = 4000

if d_order == "콜라" :
    d_price = 2500
elif d_order == "사이다" :
    d_price = 2000
    
if s_order == "예" :
    s_price = 500
else :
    s_price = 0

a_price = b_price + d_price - s_price
print(f"주문 내용은 {b_order}와 {d_order}에 세트메뉴 {s_order}이고 총가격은 {a_price} 입니다.")
