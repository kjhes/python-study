print("sort()와 람다 함수")
# 리스트 안에 튜플
# 순서 있음 : 리스트[] , 튜플() ,딕셔너리{key : value} - 키와 값이 한 쌍
# 순서 없음 : 집합{} - 순서가 없다 , 중복 안됨
students =[
    # 시험점수
    ("홍길동",60),
    ("권율",92),
    ("이순신",88),
    ("유관순",74)

    ]

for a in list(sorted(students ,key=lambda x:x[1])):
    print(a)
# print(list(sorted(students ,key=lambda x:x[1]))) #sorted 는 특이하게 이전까지와 다르게 리스트와 함수의 위치가 반대로 되어져 있다
# 왜냐 key 라는 키워드 인수에 들어가기 때문이다
# lambda x:x 라는 것 자체가 오름차순 정렬이라는 뜻을 가진다 이유는 잘 모르겠음

# 내림차순 정렬
for a in list(sorted(students ,key=lambda x:x[1],reverse = True)):
    print(a)

print("딕셔너리 -> 리스트의 정렬")
print("="* 60)

stu = [
    {"name":"홍길동","score":70},
    {"name":"아이유","score":88},
    {"name":"홍길동","score":70},
    {"name":"홍길동","score":70}
    ]

# "name" , "score" :키(key)
# "유재석" , 52 : 값(value)
dict = sorted(stu,key = lambda s : s["score"],reverse=True)

# reduce()는 앞에서부터 두 값을 계산하고,
# 그 결과를 다음 값과 다시 계산함