# class2.py
# 생성자 연습

class Board:
    def __init__(self,title,writer): # 파이썬에서의 생성자 역활을 할 수 있음
        # “인스턴스(객체)가 생성될 때” 자동 실행되는 함수를 __init__
        self.title = title
        self.writer = writer
        self.cnt = 0
    def cntup(self):
        self.cnt+=1



b1=Board("축구의 시대","정묭규")
b2=Board("영원한 리베로","홍명보")

b1.cntup()
b2.cntup()












