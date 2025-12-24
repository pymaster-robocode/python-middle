import requests


def send_notification(user: str, message: str):
    # у реальному житті тут email / telegram / api
    print(f"Notify {user}: {message}")

class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        send_notification(self.owner, f"Deposit: {amount}")

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        send_notification(self.owner, f"Withdraw: {amount}")

    def transfer(self, other_account, amount: float):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Invalid account")
        self.withdraw(amount)
        other_account.deposit(amount)

    def get_data(self, data_type):
        response = requests.get(f"https://bank.data/{self.owner}/{data_type}")
        if response.ok:
            return response.text
        else:
            return "Bad Response!"