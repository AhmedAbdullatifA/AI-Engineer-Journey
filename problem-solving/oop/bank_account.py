# Bank Account
# Create a class called BankAccount that represents a simple bank account.

# The class should contain:
# owner
# balance

# Implement the following methods:
# deposit(amount)
# withdraw(amount)
# display_balance()

# Rules
# deposit() adds money to the balance.
# withdraw() subtracts money from the balance.
# The user cannot withdraw more money than the current balance.
# The user cannot deposit or withdraw a negative amount.
# display_balance() displays the current balance.

# Example
# account = BankAccount("Ahmed", 1000)
# account.deposit(500)
# account.withdraw(300)
# account.display_balance()
# Expected Output
# Deposit successful: 500
# Withdrawal successful: 300
# Current Balance: 1200

# If the user tries:

# account.withdraw(5000)

# Output should indicate that the balance is insufficient.

# Requirements

# Use:

# __init__
# Instance attributes
# Instance methods
# Basic validation

class BankAccount :
    def __init__(self, owner, balance=0):
        self.owner = owner

        if balance < 0:
            print("Initial balance cannot be negative")
            self.balance = 0
        else:
            self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful: {amount} added to the account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 :
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful: {amount} removed from the account.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Current balance: {self.balance}")


invalid_account = BankAccount("Alice", -1000) # Initial balance cannot be negative
b1 = BankAccount("Alice", 1000)
b1.deposit(500)
b1.withdraw(200)
b1.display_balance()
b1.withdraw(2000)  # Attempt to withdraw more than the balance
b1.deposit(-100)  # Attempt to deposit a negative amount