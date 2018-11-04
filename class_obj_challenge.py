#Bank account

class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.bal=balance
    def deposit(self,dep):
        self.bal=self.bal+dep
        return "Deposit accepted: Balance is {}".format(self.bal)
    def withdraw(self,wid):
        if self.bal<wid:
            return "Funds not available"
        else:
            self.bal=self.bal-wid
            return "Withdrawl accepted: Balance is {}".format(self.bal)
    def __str__(self):
        return "Account owner is {} : Balance is {}".format(self.owner,self.bal)

acct1=Account('Murali',5000)
print(acct1)
print(acct1.deposit(600))
print(acct1.withdraw(4000))
print(acct1.deposit(5000))
print(acct1.withdraw(7000))
