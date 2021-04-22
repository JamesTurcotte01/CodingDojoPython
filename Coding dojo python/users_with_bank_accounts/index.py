class User:
    def __init__(self, name, email, balance):
        self.name=name
        self.email=email
        self.account_balance=balance


    def make_deposit(self, amount):
        self.account_balance += amount
        return(self)

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return(self)
    
    def display_user_balance(self):
        print("user: " +self.name, "balance: " +str(self.account_balance))
        return(self)

olivia = User("olivia turcotte","ot@gmail.com",(0))
monty = User("monty python", "mp@gmail.com",(0))
finley = User("finley grace", "fg@gmail.com",(0))



class CheckingAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance


    def deposit(self, balance):
        self.balance += balance 
        return self

    def withdraw(self, balance):
        self.balance -= balance
        return self

    def display_account_info(self):
        print("user: ", "balance: ", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self

monty=CheckingAccount (0.01, 1000)
olivia=CheckingAccount (0.01, 10000)
finley=CheckingAccount (0.01, 100000)

finley.display_account_info()