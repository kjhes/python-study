print("다중 상속과 mro")
class Login:
    def run (self):
        print("run() 실행")

    def login(self):
        print("login() 실행")

class Printer:
    def run (self):
        print("Printer 클래스 run()실행")

    def print_info(self):
        print("print_info() 실행")

# 다중 상속
class Study(Login,Printer):
    def study(self):
        print("수업중입니다")

s = Login()
# 상속 우선순위 (왼쪽 ) 부모의 함수 호출
s.run()

# 상속 우선순위가 낮은 부모의 함수 호출
print("함수 탐색 순서:")
print(Study.mro())

