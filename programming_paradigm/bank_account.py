# Bank Account  class
#Initialising my Bank account with amount
class BankAccount:
    def __init__(self, initial_balance):
        # Initialize account with a starting balance
        self.account_balance = initial_balance

    def deposit(self, amount):
        # Add the deposit amount to the balance
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        # Only withdraw if there is enough balance
        if amount <= self.account_balance:
            self.account_balance -= amount
            print("Withdraw successful")
            return True
        else:
            print(f"Insufficient funds to withdraw ${amount}")
            return False

    def display_balance(self):
        # Print the current account balance
        print(f"Current balance: ${self.account_balance}")

#
