class BankAccount:
    def __init__(self, int_rate = 0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        # print(self.balance)
        return self
    def withdraw(self,amount):
        self.balance -= amount
        # print(self.balance)
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance*self.int_rate + self.balance
            # print(self.balance)
            return self

        else:
            print("Insufficient Funds")

account1 = BankAccount(0.02,100)
account2 = BankAccount(0.03,200)

account1.deposit(100).deposit(50).deposit(50).withdraw(75).yield_interest().display_account_info()

account2.deposit(50).deposit(50).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()