from collections import namedtuple
from dataclasses import dataclass
from decimal import Decimal

Player = namedtuple('Player', ["name"])

p1 = Player("franklin")
print(p1)


@dataclass(order=True)
class Account:
    name: str
    balance: Decimal

    def withdraw(self, amount: Decimal):
        return self.balance - amount


a1 = Account("Omi Ewa", Decimal('10.00'))
print(a1)

