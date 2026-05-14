# lotto.py
import random


def get_lotto(): # def 함수이름(매개변수):
    numbers=[] # 비어있는 리스트 만들기
    while len(numbers) < 6:
        r=random.randint(1,45)
        if (r not in numbers):
            numbers.append(r)
    return numbers


print(f"로또 번호는 {get_lotto()} 입니다")
# get_lotto 호출 -> 리스트 만들고 , 6개를 체울때 까지 만듦
















