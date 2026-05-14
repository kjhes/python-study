# 자바에서 클래스와 비교
# 자바 클래스
# 메서드(기능) , 생성자 , 멤버변수(속성)

# 파이썬 클래스

class Board:
    def set_data(self,title,writer): 
        self.title = title # 파이썬에서는 this 대신 self 를 쓴다
        self.writer = writer # 오른쪽에 writer 은 받아온 인수값이고 왼쪽은 멤버변수이다
        # 내 자신 (객체)의미: java: this , python: self
        self.cnt=0 # 맴버변수를 만들고 초기값을 지정했다 단 자바에서 처럼 맴버 변수를 선언할 필요가 없다
    def cntup(self): # python 클래스에서 함수를 만들때 첫 인자에 self 를 넣어야 한다
        # 인스턴스를 불러오는 참조값 이기 때문에 항상 맨 앞에 붙여야 한다
        # Board 라는 클래스의 bo1이라는 인스턴스를 만들고 bo1.set_data() 라고 실행했을때 사실을 Board.set_data(bo1) 이렇게 들어가기 때문에
        self.cnt+=1

b1 = Board() # 왼쪽은 참조 변수, 인스턴스 , 객체 변수 
b2 = Board()
b1.set_data("축구의 시대","정묭규") # 멤버 변수를 초기화 하는 함수
b2.set_data("영원한 리베로","홍명보")

b1.cntup()
b1.cntup()
b2.cntup()

print(f"b1_title: {b1.title}, b1_writer: {b1.writer}, b1_cnt:{b1.cnt}")
print(f"b2_title: {b2.title}, b2_writer: {b2.writer}, b2_cnt:{b2.cnt}")

b3=Board()
b3.cntup() # cnt를 set_data 에서 만들어야 하는데 set_data를 실행하지 않아서 오류가 난다 cnt 초기화를 한번도 안했기 때문에