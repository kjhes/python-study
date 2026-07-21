# 클래스 변수와 인ㅁ스턴스 변수(참조변수)
print("클래스변수와 인스턴스변수")

class Student:
    s_name= "중앙직업전문학교" # 클래스 변수 = java 의 static - 객체가 필요 없음 클래스 이름으로 호출
    def __init__(self,name,score):#자바의 생성자와 유사하다
        self.name = name
        self.score = score
    def print_info(self):
        print("학교:",Student.s_name)
        print("이름:",self.name)
        print("점수:",self.score)
    

s1 = Student("홍길동",90)
s2 = Student("유관순",75)
Student.s_name = "글로벌직업전문학교"
s2.score = 99
s1.print_info()
s2.print_info()

print("\n"+"=" * 50)
print("파이썬의 함수 오버로딩")

class Calculator:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=100):
        return a+b+c
    
c1 = Calculator()
print(c1.add(10,20))
# 파이썬에서 같은 이름의 함수 여러번 작성-오버로딩
# 파이썬에서는 마지막 함수가 덮어씌움