class BankAccount:
    def __init__(self, int_rate=0.00, balance=0):
        self.rate = int_rate
        self.bal = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.bal += amount
        return self
    def withdraw(self, amount):
        if self.bal - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.withdraw(5)
        self.bal -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.bal}")
        return self
    def yield_interest(self):
        if self.bal > 0:
            self.bal += self.bal*self.rate
        return self

acct1 = BankAccount(0.05, 100)
acct2 = BankAccount(0.10, 1000)
acct1.deposit(10).deposit(10).deposit(10).withdraw(30).yield_interest().display_account_info()
acct2.deposit(10).deposit(10).withdraw(5).withdraw(5).withdraw(5).withdraw(5).yield_interest().display_account_info()
