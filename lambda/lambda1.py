# 1. 람다 함수는?
#
# 람다 함수는 이름 없이 사용하는 일회용 함수입니다
# 일반 함수는 def를 사용하지만,
# 람다 함수는 lambda라는 단어를 사용합니다.
# 람다 함수는 짧고 간단한 계산에 적합합니다.

# 일반 함수 형식
# def 함수이름(매개변수):
#     return 계산식
#
# 람다 함수 형식
# lambda 매개변수: 계산식
# lambda 받는 값 : 돌려 보내는 값

def double(x):
    return x * 2

b= lambda x : x*2
print(b(2))

print(double(2))
# b = double(a) #메모리가 쓸데없이 낭비됨

print("2제곱 람다 함수 비교")
print("=" * 60 )#문자 반복의 의미
b = lambda x : x**2 # == x*x
print(b(5))
print(b(10))

add = lambda a,c : a+c
print("10+20 = ",add(10,20))

mul = lambda a,c : a*c
print("4*5 = ",mul(4,5))

# 조건식이 들어간 람다 함수
lambda x : "짝수" if x%2==0 else "홀수"
# lambda 식에서는 if 만 사용할 수 없기때문에 lambda x : if x%2==0 x 형태는 사용할 수 없음
# 그 이유는 lambda에는 표현식만 올 수 있기 때문이다 else 가 없으면 항상 값을 반환하지 못함
print("="*50)
# 매게변수가 없는 람다함수 - 입력없이 항상 같은 값을 출력함
h = lambda : "안녕하세요"
print(h())
# 10과 60중에 더 큰 값을 출력하는 람다함수
compare = lambda a,b : a if a>b else b
print(compare(10,60))

number = [1,2,3,4,5]
multiple = lambda x : x*2
# rsult = list(map(multiple() , number)) 안되는 이유 map 에서는 알아서 매개변수를 빼서 해주는데 여기서는 multiple() 처럼 인수로 아무것도 주지 않았기 떄문에 error 가 난다 즉 어차피 map 이 알아서 인수를 넣어줄 텐데 내가 그걸 넣어버려서 오류가 난것 
result = list(map(multiple, number)) 
print("원본",number)
print("결과",result)

print("map() 으로 점수를 5점 올리기")
score = [78,89,91,56]

reseult = list(map(lambda x : x+5,score))

print("원본",score)
print("결과",reseult)

# 형식
# filter(조건 함수 , 리스트)
#
# 람다 함수의 계산 결과가 True 이면 남기고,
# False 이면 제외합니다
num = [10,33,45,26,40]
print(list(filter(lambda x : x%3==0,num)))
# 람다함수 내 표현식의 결과가 True 이라면 결과를 추출하고 아님 버린다

# filter()을 이용하여 합격점수인 것만 출력하기 70점 이상
jumsu = [45,60,90,77,55]
print(list(filter(lambda x : x>=70,jumsu)))




