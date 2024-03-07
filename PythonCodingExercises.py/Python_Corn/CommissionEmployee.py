from decimal import Decimal


class CommissionEmployee:
    def __int__(self, first_name, last_name, NIN, sales, rates):
        self._first_name = first_name
        self._last_name = last_name
        self._NIN = NIN
        self._sales = sales
        self._rates = rates

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def NIN(self):
        return self._NIN

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        if value < Decimal(0.0):
            raise ValueError(f'Invalid amount{value}')
        self._sales = value

    @property
    def rates(self):
        return self._rates

    @rates.setter
    def rates(self):
        if Decimal(0.0) < self.rates < Decimal(1.0):
            raise ValueError(f'Invalid rate amount {rates}')
        self._rates = rates

    def earning(self):
        return self.sales * (self.rates / 100)

    def __repr__(self):
        return f"first name:{self.first_name}\nLast name: {self._last_name}\n" \
               f'NIN: {self._NIN}\nEarning:{self.earning()}'


bioke = CommissionEmployee()
print(bioke)
