class BankAccount:
    def __init__(self, int_rate=.02, balance = 0):
        self.int_rate = int_rate
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

class User: 
    def __init__(self, name, email):
        self.name = name 
        self.email = email
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)

        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

        return self

    def yield_interest(self):
        self.account.yield_interest()

        return self


    def display_account_info(self):
        self.account.display_account_info()

        return self


user1=User("andre", "awalton9401@ghotmail")
acct1 = BankAccount(int_rate = .5, balance = 500)
user1.account = acct1

user1.display_account_info()

user1.display_account_info().yield_interest().display_account_info()