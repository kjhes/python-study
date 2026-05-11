import turtle
# 그림 그리는 모듈
t= turtle.Turtle() #turtle 객체 생성, t 변수에 할당
t.shape("turtle") # 모양 설정 
radius = 50 # 반지름 설정
t.circle(radius) #원 그리기
t.forward(30) #fd , forward 앞으로 이동한다
t.circle(radius) #원 그리기
t.forward(30) #fd , forward 앞으로 이동한다
t.circle(radius) #원 그리기

for _ in range(4): #필요없는 변수를 만들때에는 _를 사용한다
    t.forward(2*radius)
    t.right(90)
# 한변의 길이가 반지름의 2배인 정사각형 생성
for _ in range(3): #필요없는 변수를 만들때에는 _를 사용한다
    t.forward(2*radius)
    t.right(120)
# 한변의 길이가 반지름의 2배인 정삼각형 생성