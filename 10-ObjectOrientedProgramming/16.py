import random

class Bank():
    def __init__(self):
        self.balance=0
        self.account_num='11111111111111111111111111'

    def deposit(self,ammount):
        self.balance+=ammount

    def withdraw(self,ammount):
        if ammount<=self.balance:
            self.balance-=ammount
        else:
            print('Insufficient funds on the account')
    
    def status(self):
        print(f'Bank account no: {self.account_num[0:2]} {self.account_num[2:6]} {self.account_num[6:10]} {self.account_num[10:14]} {self.account_num[14:18]} {self.account_num[18:22]} {self.account_num[22:26]}\nBalance: PLN {self.balance}')


acc1=Bank()
acc1.deposit(1000)
acc1.status()
acc1.withdraw(1001)
acc1.withdraw(997)
acc1.status()


