class Account():

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Deposit Accepted")
        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            unavailable = "Funds Unavailable!"
            return unavailable

        self.balance -= amount
        print("Withdrawel Accepted")
        return self.balance

    def __str__(self):
        return  f"Account owner:  {self.owner} \nAccount balance: {self.balance}"

acct1 = Account('Jose',100)
print(acct1.owner)
print(acct1.balance)
print(acct1)

acct1.deposit(50)
print(acct1.balance)

acct1.withdraw(50)
print(acct1.balance)

print(acct1.withdraw(500))