class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_bal = 0
    def deposit(self, amount):
        self.account_bal += amount
        return self
    def withdrawal(self, amount):
        self.account_bal -= amount
        return self
    def displayBal(self):
        print(f"User: {self.name}, Balance: {self.account_bal}")
        return self
    def transfer(self, other_user, amount):
        other_user.deposit(amount)
        self.withdrawal(amount)
        return self
    
user1 = User("Taylor", "taylor@email.com")
user2 = User("Roxy", "roxy@email.com")
user3 = User("Joey", "joey@email.com")
user1.deposit(50).deposit(100).deposit(200).withdrawal(50).displayBal()
user2.deposit(25).deposit(75).withdrawal(10).withdrawal(10)
user3.deposit(150).displayBal()
user1.transfer(user3, 5).displayBal()
user3.displayBal()