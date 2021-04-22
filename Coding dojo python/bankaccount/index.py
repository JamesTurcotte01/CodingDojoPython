class BankAccount:
    def __init__(self, name, int_rate, balance): 
        self.name=name
        self.int_rate=int_rate
        self.balance=balance


    def deposit(self, balance):
        self.balance += balance 
        return self

    def withdraw(self, balance):
        self.balance -= balance
        return self

    def display_account_info(self):
        print("user: ", self.name, "balance: ", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self

james=BankAccount ("james", 0.01, 1000)
olivia=BankAccount ("olivia",0.01, 10000)

james.deposit(200).deposit(200).deposit(200).withdraw(100).yield_interest().display_account_info()
olivia.deposit(100).deposit(50).withdraw(10).withdraw(12).withdraw(8).withdraw(5000).yield_interest().display_account_info()