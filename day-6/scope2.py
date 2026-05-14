# 스코프(scope)
#  파이썬은 변수를 찾을때 가까운 영역부터 찾음 ( 무조건 바깥쪽으로 나아가면서 찾음 , 안쪽으로 역방향 X)
#  LEGB 규칙 파이썬이 변수를 찾는 순서 (Local -> Enclosing -> Global -> Built-in)

a = '홍길동' # 전역
b = 99 # 전역

def function1():
    a = '이순신' # 지역
    c = [1 ,2 ,3] # 지역
    
    def function2():
        d = (1, 2, 3) # 지역 , 인클로징
        print('Local a =',a) # 바깥 함수 이순신
        print('Local b =',b) # 전역 99
        print('Local c =',c) # 바깥 함수 [1,2,3]
        print('Local d =',d) # 지역 (1,2,3)
        
    
    function2()
    print('Enclosing a =',a) # 지역 이순신
    print('Enclosing b =',b) # 전역 99
    print('Enclosing c =',c) # 지역 [1,2,3]
    # print('Enclosing d =',d) # error
function1()
print('Global a =',a) # 전역 홍길동
print('Global b =',b) # 전역 99
# print('Global c =',c) # error
# print('Global d =',d) # error