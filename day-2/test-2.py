ac_count = int(input("아메리카노 판매 개수"))
lt_count = int(input("카페라떼 판매 개수"))
cp_count = int(input("카푸치노 판매 개수"))

ac_price=2000
lt_price=2500
cp_price=3000


print(f"총 매출은 {(ac_price*ac_count )+ (lt_count*lt_price) + (cp_count*cp_price)}입니다")	