class Passbook :
    def __init__(self,owner,balance):
        self.owner =owner
        self.balance =balance
    def despoit(self,input):
        self.balance +=input
        print(f"입금결과 : 투입한 금액: {input},현재 잔액:{self.balance}")
    def withdraw(self,ouput):
        if self.balance >= ouput:
            print("출력 금액 :",ouput)
            self.balance -=ouput
            return ouput
        else:
            print("잔액 부족")


class MinusPassbook(Passbook):
    def withdraw(self, ouput):
        if self.balance >= ouput:
            self.balance -=ouput
            print(f"출력결과 : 출력 금액: {ouput},현재 잔액:{self.balance}")
        elif self.balance - ouput >= -1000000:
            self.balance -=ouput
            print(f"출력결과 : 출력 금액: {ouput},현재 잔액:{self.balance}")
        else : 
            print("마이너스 한도 초과")

ac1 =Passbook("홍길동",100000)
ac1.withdraw(120000)
ac1.withdraw(70000)

ac2 = MinusPassbook("김철수",100000)
ac2.withdraw(120000)
ac2.withdraw(900000)
