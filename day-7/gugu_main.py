from gugu_modul import v_gugudan as v
from gugu_modul import h_gugudan as h
stop=0  
while stop==0:
    num=int(input("숫자를 입력하세요(1:세로, 2:가로)")) 
    if num == 1:
        v()
    elif num ==2:
        h()
    elif num ==0:
        stop =1
    else :
        print("숫자를 입력하세욘")



