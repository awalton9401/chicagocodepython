

class User:
    def __init__(self, name, email_address, account_balance):
        self.name = name
        self.email = email_address
        self.account_balance = account_balance
        
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self

    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

    # def __str__(self):
    #     return f"{self.fname} {self.lname}"

user1=User("Andre Walton", "awalton9401@hotmail.com", 500)
user2=User("Amber Walton", "awalton9401@hotmail.com", 700)
user3=User("Anita Redding", "awalton9401@hotmail.com", 800)


user1.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawl(200)
user2.make_deposit(100).make_deposit(100).make_withdrawl(50).transfer_money(user3,100)
user3.make_deposit(100).make_deposit(50).make_deposit(50).make_deposit(50)


user1.display_user_balance()
user2.display_user_balance()
user3.display_user_balance()







