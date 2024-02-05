class Phonebook:
    def __init__(self):
        self.phonebook = {}

    def add_contact(self, name, number):
        self.phonebook[name] = number
        print(f"Contact {name} added with phone number {number}")

    def edit_contact(self, name, new_number):
        if name in self.phonebook:
            self.phonebook[name] = new_number
            print(f"Contact {name} edited with new phone number {new_number}")
        else:
            print(f"Contact {name} not found in the phonebook")

    def display_contacts(self):
        if not self.phonebook:
            print("Phonebook is empty.")
        else:
            print("Phonebook:")
            for name, number in self.phonebook.items():
                print(f"{name}: {number}")


phonebook_app = Phonebook()

while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Display Contacts")
    print("4. Exit")

    function = input("Enter any of the functions below (1-4): ")

    if function == "1":
        name = input("Enter the name: ")
        number = input("Enter the phone number: ")
        phonebook_app.add_contact(name, number)

    elif function == "2":
        name = input("Enter the name of the contact to edit: ")
        new_number = input("Enter the new phone number: ")
        phonebook_app.edit_contact(name, new_number)

    elif function == "3":
        phonebook_app.display_contacts()

    elif function == "4":
        print("Exiting phonebook app.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")


def add_contact(name, number):
    return None