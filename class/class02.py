print("*args 로 여러개의 값 받기")

class Calc:
    def add(self,*nums):
        tot = 0
        for i in nums: # 튜플에서 하나씩 꺼내서 끝까지 반복
            tot += i
        return tot
c = Calc()
print(c.add(1,2,3,4,5,6,7,8,9,10))

# ===================================================
# isinstance 값이 해당 자료형인지 확인하는 함수


class Type_class:
    def t_data(self,data):
        if isinstance(data,int):
            print("정수:", data)
        elif isinstance(data,str):
            print("문자열 : ",data)
        elif isinstance(data,list):
            print("리스트 :",data)
        else :
            print("없는 자료형 입니다")

t = Type_class()
t.t_data("문자열")
t.t_data(10)
t.t_data(10.0)
t.t_data([1,2,3])