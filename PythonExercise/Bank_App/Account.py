class Account:
    def __init__(self, name: str, account_number: int, balance: int, phone_number: int):
        self.phone_number = phone_number
        self.balance = balance
        self.name = name
        self.account_number = account_number

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Invalid input, input positive amount")
        self.balance += amount

    def withdrawal(self, amount, pin):
        self.validatePin(pin)
        if self.balance < amount:
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
        return self.number

    def setNumber(self, number):
        self.phone_number = number
