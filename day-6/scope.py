# scope.py
def calc(r1):
    result = 3.14 * (r1**2) # 제곱 연산자
    return result

r=float(input("원의 반지름 입력:"))
area = calc(r)
print(area)
# print(result) #result는 지역변수여서 오류가 난다

# print(result) : result는 지역 변수(함수 종료되면 소멸)
##########################################
def calc2(r2):
    a = 3.14 *r2**2 # r1 : 반지름
    return a
a=0
rr = float(input("원의 반지름 입력:"))
area2 = calc2(rr)
print(area2)
print(a)
# print(a) 밖에서 a를 선언했었지만 return a의 의미는 a를 반환한다는게 아니라 a라는 지역 변수의 값만 리턴한다는 뜻 이여서 
# a를 반환한다고 전역변수 a는 변하지 않는다