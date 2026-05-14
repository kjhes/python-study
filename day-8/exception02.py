fruits=["사과","배","오렌지"]


try:
    index = int(input("번호 입력:"))
    if index <0 or index >=len(fruits):
        raise IndexError # 오류(예외)를 강제로 발생시킴        
except IndexError:
    print("인덱스를 잘못 입력했습니다")
except ValueError:
    print("입력 오류")
except Exception as e:
    print("error:",e)
else :
    print(fruits[index])
    print("정상작동")