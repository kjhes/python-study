# recusrion 재귀 호출 (함수 내부에서 자기 자신을 호출하는 것)
#  5! (팩토리얼) : 1*2*3*4*5
def fact(n): #fact(매개변수 하나)
    # res = n
    # while n > 1:
    #     n-=1
    #     res = res * n 
    # return res
    if n == 1:
        return 1 
    else : 
        return n * fact(n-1)
    

a=int(input("정수를 입력하세요")) #5를 입력
res=fact(a) #함수 호출, 인수 a(정수 숫자)를 넣어 반환된 결과값을 res 변수안에 저장
print(res)



# 순환 함수를 활용하여 1부터 입력받은 숫자까지의 합을 구하는 프로그렘
# def ssum(n,cnt = 1):
#     if n == cnt:
#         return cnt
#     else :
#         return cnt + ssum(n,cnt+1)


def ssum(n):
    if n == 1:
        return n
    else :
        return n + ssum(n-1)

b= int(input("숫자를 입력하세요"))
print(ssum(b))