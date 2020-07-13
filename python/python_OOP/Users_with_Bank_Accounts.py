class BankAccount:
    def __init__(self, int_rate=0.00, balance=0):
        self.rate = int_rate
        self.bal = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.bal += amount
        return self
    def withdraw(self, amount):
        self.bal -= amount
        if self.bal < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.bal -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.bal}")
        return self
    def yield_interest(self):
        if self.bal > 0:
            self.bal += self.bal*self.rate
        else:
            print("Account balance is negative")
        return self

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)  # now the User class can use attributes from the BankAccount class
    def deposit(self):
        self.account.deposit()
        return self
    def withdraw(self):
        self.account.withdraw()
        return self
    def displayBal(self):
        print(self.account.balance)
        return self
    def transfer(self, other_user):
        other_user.account.deposit()
        self.account.withdraw()
        return self