class BankAccount:

    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    def display_balance(self):
        print("Current balance:", self.__balance)


# Create a bank account
account = BankAccount(1000)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(300)

# Display balance
account.display_balance()