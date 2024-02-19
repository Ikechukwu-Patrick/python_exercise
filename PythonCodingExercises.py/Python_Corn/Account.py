from decimal import Decimal


class Account:

    def __int__(self, name, balance: Decimal):
        self.nane = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < Decimal(0.00):
            raise ValueError("Invalid amount for balance")
        self.__balance = balance

    def __repr__(self):
        return f"Name {self.nane}  Balance: {self.__balance}"


a1 = Account.balance

print(a1)
