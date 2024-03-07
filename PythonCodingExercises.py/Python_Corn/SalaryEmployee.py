import CommissionEmployee


class SalaryEmployee(CommissionEmployee):
    def __int__(self, first_name, last_name, nin, sales, rate, base_pay):
        super().__init__(first_name, last_name, nin, sales, rate)
        self.base_pay = base_pay

