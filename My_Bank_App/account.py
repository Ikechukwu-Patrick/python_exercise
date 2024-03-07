class Account:
    def __init__(self, name: str, account_number: int, balance: int, pin: str):
        self.balance = None
        self.pin = pin
        self.name = name
        self.account_number = account_number

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Invalid input, input positive amount")
        self.balance += amount

    def withdraw(self, amount, pin):
        self.validatePin(pin)
        balance_after_deposit = self.balance - 300
        if balance_after_deposit < amount:
            raise ValueError("Sorry you cannot withdraw as your balance is not enough")
        if amount < 0:
            raise ValueError("Invalid input, input positive number")
        self.balance -= amount

    def balanceChecker(self, amount):
        if self.balance > amount:
            self.balance += amount

    def validatePin(self, pin):
        if self.pin != pin:
            raise ValueError("Your pin is incorrect, enter the correct pin for this account")

    def setBalance(self, balance):
        self.balance = balance

    def getNumber(self):
        return self.account_number

    def setNumber(self, number):
        if number != self.account_number:
            raise ValueError("No account found")
        self.account_number = number
