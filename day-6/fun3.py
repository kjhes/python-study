# fun3.py
def dis_price(price,dis_percent):
    res= price - (price * (dis_percent/100))
    return res

final_price_a = dis_price(10000,10) #dis_price
print(f"a 상품의 가격은: {final_price_a}원 입니다")

final_price_b = dis_price(50000,20)
print(final_price_b)