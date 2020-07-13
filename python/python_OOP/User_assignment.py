# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.
# For this assignment, we'll add some functionality to the User class:
# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance


class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_bal = 0
    def deposit(self, amount):
        self.account_bal += amount
    def withdrawal(self, amount):
        self.account_bal -= amount
    def displayBal(self):
        print(f"User: {self.name}, Balance: {self.account_bal}")
    def transfer(self, other_user, amount):
        other_user.deposit(amount)
        self.withdrawal(amount)
    
user1 = User("Taylor", "taylor@email.com")
user2 = User("Roxy", "roxy@email.com")
user3 = User("Joey", "joey@email.com")
user1.deposit(50)
user1.deposit(100)
user1.deposit(200)
user1.withdrawal(50)
user1.displayBal()
user2.deposit(25)
user2.deposit(75)
user2.withdrawal(10)
user2.withdrawal(10)
user3.deposit(150)
user3.displayBal()
user1.transfer(user3, 5)
user1.displayBal()
user3.displayBal()