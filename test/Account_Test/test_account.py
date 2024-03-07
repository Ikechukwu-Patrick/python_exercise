import unittest

from My_Bank_App.account import Account


class account_Test(unittest.TestCase):
    def test_that_account_can_deposit(self):
        account = Account("Omi Ewa", 189, 0, "pin")
        account.deposit(2000)
        self.assertEqual(2000, account.getBalance())
