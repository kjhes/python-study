ac_count = int(input("아메리카노 판매 개수"))
lt_count = int(input("카페라떼 판매 개수"))
cp_count = int(input("카푸치노 판매 개수"))

ac_price=2000
lt_price=2500
cp_price=3000


print(f"총 매출은 {(ac_price*ac_count )+ (lt_count*lt_price) + (cp_count*cp_price)}입니다")	
m_in = int(input("투입한 돈"))
p_in = int(input("물건값 돈"))
charge = m_in - p_in

print("거스름돈:",charge)
coin500s = charge //500
charge = charge % 500
coin100s = charge //100 
charge = charge % 100

print("500원",coin500s)
print("100원",coin100s)

        
