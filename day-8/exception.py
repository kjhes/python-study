
try :
    num = int(input("숫자를 입력하세요"))
    res = 10 / num
except ValueError: # except 는 특정 에러가 났을때 실행하는 코드를 말함
    print("숫자를 입력하세요")
except ZeroDivisionError: # 0으로 나눌 수 없음
    print("0으론 나눌 수 없습니다")
except Exception as e: # 우리가 생각하지 못한 에러 전체를 한번에 묶어 버림
    print("error:",e)
else:
    print("결과:",res)
finally: # 오류가 생기든 안 생기든 무조건 실행됨
    print("종료")