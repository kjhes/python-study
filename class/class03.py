print("상속,super,오버라이딩,다형성")
# 오버로딩 - 생성자나 함수에 들어가는 매게변수가 다른 여러개의 함수나 생성자를 만드는것
# 자바와 파이썬에서의 오버로딩은 다름 자바에서는 여러개가 동시에 작용하지만 파이썬 에서는 마지막 깨 덮어씌워짐

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = name
    def work(self):
        print(self.name,"직원이 일합니다")
    def print_info(self):
        print("이름:",self.name)

# 자식 클래스
class Developer(Employee): #파이썬에서 상속 받을때 에는 자식 클래스 이름을 쓰고 그 옆 괄호에 부모 클래스 이름을 쓴다
    def __init__(self, name, salary,language):
        # 어차피 부모에서 이미 name 과 salary 를 정의했기때문에 굳이 새로 만들어서 초기화 할 필요가 없다
        super().__init__(name, salary)
        self.language = language # 자식에만 있는 멤버 변수(인스턴스 변수)
    def work(self): #오버 라이딩(재정의) ,파이썬 에서 오버 로딩은 없음 
        print(self.name,"개발자가",self.language,"프로그램을 작성합니다.")
    def print_info(self):
        super().print_info()
        super().work()
        print("사용 언어는",self.language,"입니다")

# 자식 클래스 2
# 선생님 -> 과목 subject
# 선생님이 ~ 과목을 강의합니다
# 교과 과목으로 과목도 출력(이름,급여 포함 출력)
class Teacher(Employee):
    def __init__(self, name, salary,subject):
        super().__init__(name, salary)
        self.subject = subject
    def print_info(self):
        super().print_info()
        super().work()
    def work(self):
        print(self.name,"선생님이",self.subject,"과목을 강의합니다")

# 객체 생성
d= Developer("홍길동",4500000,"파이썬")
t= Teacher("홍박사",3000000,"체육")

print("개발자 정보")
d.print_info()


print("\n교사 정보")
t.print_info()

# ---------------
print("\n 직원들의 업무")
e_list = [d,t]
for i in e_list:
    i.work()

#  자바에 다형성은 부모 타입의 자식 객체를 만들 수 있다는것 인데
#  파이썬에서 다형성은 객체가 같은 이름의 함수를 갔고있음 
#  -> 실행할 때 마다 각각의 서로다른 객체의 함수가 실행
#  개발자 객체는 개발자의 work() 를 실행했고
#  교사 객체는 교사의 work() 를 실행했음