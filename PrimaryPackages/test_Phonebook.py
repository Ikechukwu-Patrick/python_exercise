import unittest

from PrimaryPackages.Phonebook import PhoneBook


class TestPhoneBook(unittest.TestCase):
    def setUp(self):
        self.phone_book = PhoneBook()
        self.phone_book.add_contact("Micheal", "1234567890")
        self.phone_book.add_contact("Marvelous", "9876543210")
        self.phone_book.add_contact("James", "33344455565")

    def test_add_contact(self):
        self.phone_book.add_contact("Alice", "1111111111")
        self.assertIn("Alice", self.phone_book.list_contacts())

    def test_delete_contact(self):
        self.phone_book.delete_contact("John")
        self.assertNotIn("John", self.phone_book.list_contacts())

    def test_get_contact(self):
        self.assertEqual(self.phone_book.get_contact("Micheal"), "1234567890")
        self.assertEqual(self.phone_book.get_contact("Alice"), "Contact not found")


