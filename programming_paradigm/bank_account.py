# Understand the fundamentals of OOP in Python by implementing 
# a BankAccount class that encapsulates banking operations. 
# Use command line arguments to interact with instances of 
# this class.


class BankAccount():
    def __init__(self,account_balance):
        self.account_balance = account_balance
        account_balance = 0
        return account_balance
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):
        if self.account_balance > amount:
            return True
        else:
            return False
        self.account_balance -= amount
        return self.account_balance
    
    def display_balance(self):
        return f"Current Balance: ${amount}"
        

        
