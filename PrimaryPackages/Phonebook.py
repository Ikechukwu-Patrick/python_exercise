class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def get_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return "Contact not found"

    def list_contacts(self):
        return self.contacts


phone_book = PhoneBook()
phone_book.add_contact("Micheal", "1234567890")
phone_book.add_contact("Marvelous", "9876543210")
print(phone_book.list_contacts())
print(phone_book.get_contact("Micheal"))
phone_book.delete_contact("Micheal")
print(phone_book.list_contacts())
