import unittest

from OOP.Bank_App import Bank
from OOP.InvalidAmountError import InvalidAmountError


class MyTestCase(unittest.TestCase):
    def test_that_i_can_register_customers_in_the_bank(self):
        bank = Bank("Omi Ewa's Bank")
        bank.register_customer("first_name", "last_name", "6969")
        self.assertEqual(len(bank.list_of_accounts), 1)

    def test_that_i_can_deposit_money_in_the_bank(self):
        bank = Bank("Omi Ewa's Bank")
        bank.register_customer("first_name", "last_name", "6969")
        bank.deposit(1, 5000)
        self.assertEqual(5000, bank.check_balance(1, "6969"))

    def test_that_bank_can_deposit_multiple__times_balance_increases(self):
        bank = Bank("Omi Ewa's Bank")
        bank.register_customer("first_name", "last_name", "6969")
        bank.deposit(1, 700)
        bank.deposit(1, 700)
        self.assertEqual(1400, bank.check_balance(1, "6969"))

    def test_that_balance_can_not_change_when_i_deposit_negative_values(self):
        bank = Bank("Omi Ewa's Bank")
        bank.register_customer("first_name", "last_name", "6969")
        self.assertRaises(InvalidAmountError, lambda: bank.deposit(1, -3000))
        self.assertEqual(0, bank.check_balance(1, "6969"))

    def test_that_we_can_withdraw_money_from_the_bank(self):
        bank = Bank("Omi Ewa's Bank")
        bank.register_customer("first_name", "last_name", "6969")
        bank.deposit(1, 1200)
        bank.withdraw(1, 700, "6969")
        self.assertEqual(500, bank.check_balance(1, "6969"))