# math_fun.py
# 내장 함수  vs  외장 함수

# ==================================
# 내장 함수
# len() # 길이 측정
# str() # 문자열로 변환
# list() # 리스트로 변환
# tuple() # 튜플로 변환
# split() # 문자열 나누기
# strip() # 공백제거
# del() # 삭제

res = divmod(11,3) # div : 몫 mod : 나머지 
print(res) # (몫,나머지) 튜플 구조로 출력 

print(type(abs(-5))) # 절대값 int
print(type(abs(-4.4))) # float

print(pow(4,2)) # 제곱 4**2랑 같음

print(max(10,20,30)) # 최대값
print(min(10,20,30)) # 최소값

print(round(12.45999)) # 반올림
# ===================================================
# 외장 함수 : 내장되있는 함수가 아니라 바깥에서 불러와서 사용해야함
import math
from math import * # math 안에 있는 함수,변수를 모두 불로오겠다는 뜻 더 이상 모듈이름.함수() 이런식으로 할 필요가 없음
# math 안에 있는 모든 함수를 네임스페이스에 가져옴


print(math.floor(24.9)) # 단순히 math() 로 하면 불러와 지지 않음 앞에 모듈에서 가져오는거기 때문에 모듈이름.함수() 형태로 작성해야함
print(math.sqrt(16)) # 제곱근을 출력
print(math.factorial(16)) # 팩토리얼 출력
print(math.pi) # 원주율 출력






