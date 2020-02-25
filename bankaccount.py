class BankAccount:
    def __init__(self, balance):
        self.int_rate = 0.01
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= -5
            print("Insuffient funds")

        return self

    def display_account_info(self):
        print(self.balance)

        return self

    def yield_interest(self):
        self.balance += self.int_rate * self.int_rate

        return self


account1=BankAccount(100)
account2=BankAccount(100)


account1.deposit(10)
account1.deposit(10)
account1.deposit(10)

account1.display_account_info().yield_interest().display_account_info()

account1.withdraw(200)

account1.display_account_info().yield_interest()



account2.deposit(100)
account2.deposit(20)

account2.withdraw(100)

account2.display_account_info().yield_interest().display_account_info()