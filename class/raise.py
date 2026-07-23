# raise.py
# throw vs thrwos java 에서 사용됨 
# throw : 오류를 일부로 발생시킴
# throws : 호출 던지기 오류처리게 던지기

# raise : 오류를 일부로 발생 시킴
# age =-5
# if age <= 0:
#         raise ValueError("나이가 0보다 작거나 같을 수는 없다")

try :
    age = int(input("나이를 입력해 주세요"))
    if age <= 0:
        raise ValueError("나이가 0보다 작거나 같을 수는 없다")
except ValueError as e: # 오류 메시지 를 받아옴 
    print("오류발생",e)
else:
    print("나이는 :",age)
finally :
    print("끝")