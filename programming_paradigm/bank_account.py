# Bank Account  class
#Initialising my Bank account with amount
class BankAccount:
    def __init__(self, initial_balance):
        self.amount = initial_balance
    def deposit(self, amount):
        self.amount += amount
        return self.amount
    def withdraw(self, amount):
        if amount <= amount:
             self.amount -= amount
             print("Withdraw successful")
             return True
        
        else:
            False
            print(f"Insufficent ammount{amount} ")
    def display_balance(self):
        return print(self.amount)

