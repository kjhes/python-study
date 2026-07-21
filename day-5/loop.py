import sys
# 1부터 100까지의 수 중에서 5의 배수 만 빼고 더하기
cnt = 1
sum = 0

while cnt < 101 :
    if cnt%5 != 0: #cnt%5 는 나머지를 말함 -> 즉 5의 배수만을 말함 = 5로 나눴을때 나머지가 0이 아님
        sum += cnt # 합에 5의 배수를 추가
        cnt +=1 # 횟수 증가
    else :
        cnt +=1 # 횟수 증가
        continue # continue 는 현재 반복을 끝내고 반복문의 시작 부분으로 이동
print("cnt:",cnt,"sum:",sum)

#####################################################

user_pass = input("패스워드를 입력하시오(영어3자): ")
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z',]
for letter1 in password:
        for letter2 in password:
            for letter3 in password:
                guess = letter1+letter2+letter3
                print(guess)
                if guess == user_pass:
                    print("당신의 패스워드는 "+guess)
                    sys.exit() # 즉시 중지

