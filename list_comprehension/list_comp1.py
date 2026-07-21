# 컴프리헨션
# 반복문과 조건문을 한 줄로
# 간단하게 작성하여 리스트나 딕셔너리 , 세트를 만드는 방법
# 1. for 리스트
# [저장할_값(표현식) for 변수 in 반복할_데이터]
numbers = [] # 빈 리스트
for i in range(1,6): # 1~5
    numbers.append(i)
print(numbers)

# 2. 리스트 컴프리헨션
numbers = [i for i in range(1,6)]
print(numbers)

# 3. 계산하여 리스트에 저장
mul = []
for i in range(1,6):
    mul.append(i*i)
print(mul)

mul = [i*i for i in range(1,6)]
print(mul)

# 4. 조건이 있는 리스트 
even_num = []
for i in range(1,11):
    if(i % 2 == 0):
        even_num.append(i)
print(even_num)
# 5. 조건이 있는 리스트 컴프리헨션
even_num = [i for i in range(1,11) if i%2 == 0]
print(even_num)
# 6. 문자열을 이용한 리스트 컴프리헨션
names = ["홍명보","홍길동","홍박사"]
str_length=[len(a) for a in names]
print(str_length)



# 길이가 5개이상인 단어만 저장 , 리스트 컴프리헨션
words = ["kiwi", "apple", "banana","pear","lime" ]
result = [a for a in words if len(a) >=5]
print(result)


# if와 else가 모두 있는 리스트 컴프리헨션
# 기본 형식
# [참일_때_값 if 조건식 else 거짓일_때_값 for 변수 in 반복할_데이터]


res = ["짝수" if i%2==0 else "홀수" for i in range(1,11)]
print(res)

# 딕셔너리 컴프리헨션
# 딕셔너리 키" 값의 형태로 저장합니다.
# 기본 형식 
# {키: 값 for 변수 in 반복할_데이터}
squars={i :i*i for i in range(1,11) }
print(squars)

# 조건 점수가 80점 이상인 사람들만 저장
scores= {
    "김철수" : 85,"이영희" : 70,"홍길동" : 90
}

res = {k:v  for v,k in scores.items()}


res = [i*3 for i in range(1,11)]
print(res)


res = [i for i in range(1,21) if i %3 ==0]
print(res)

res = [i  if i %3 ==0 else 0 for i in range(1,21)]
print(res)

res = {}