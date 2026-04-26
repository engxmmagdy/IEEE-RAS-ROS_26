
class bankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount





money = bankAccount()
money.deposit(50)
money.withdraw(20)
print(money.balance)