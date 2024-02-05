import unittest

import Phonebook


class TestPhonebook(unittest.TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.captured_output = None

    def test_something(self, _fixture_=None):
        self.phonebook = Phonebook

    def test_add_contact(self):
        name = "John Does"
        number = "123-456-7890"
        self.phonebook.add_contact(name, number)
        self.assertEqual(self.phonebook.Phonebook[name], number)
        self.assertEqual(self.captured_output.getValue().strip(), f"Contact {name} added with phone number {number}")
