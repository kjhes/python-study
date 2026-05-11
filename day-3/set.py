# SET(집합)
# 순서가 없는 모음 , 중복 안됨
# {}, set([])

my_set = {"홍길동","김길동","장길동"}
print(my_set)

football = {"홍길동","김길동","장길동"}
# baseball = {"홍길동","오길동","하길동"}
baseball = set(["홍길동","감길동","오길동"])

# 교집합
print(football & baseball)
print(football.intersection(baseball))

# 합집합
print(football | baseball)
print(football.union(baseball))

# 차집합
print(football - baseball)
print(football.difference(baseball))

# 추가
football.add("김길동") #중복이 안됨
print(football)

#삭제
baseball.remove("오길동")

print(type(baseball))

spool = list(baseball)
print(type(spool))

spool2 = tuple(baseball)
print(type(spool2))