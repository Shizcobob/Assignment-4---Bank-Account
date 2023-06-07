class bankaccount:

    def __int__(self, in_rate, balance):
        self.interest_rate = 0.01
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance-amount>0:
            self.balance-=amount
        else: 
            print("Insufficient funds: Charging a $5 Fee")
            self.balance-=5

    def display_info(self):
        print("Balance : {self.balance}")
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.interest_rate
    
    


