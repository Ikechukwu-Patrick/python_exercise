# This line defines a class named Person
class Person:

    # This is the constructor, which takes three parameters: self, name, and age
    # It assigns the name and age arguments to the object's attributes using self
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This is a method that prints the object's name and age using self
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

    # This is another method that increases the object's age by one using self
    def birthday(self):
        self.age += 1
        print(f"Happy birthday, {self.name}! You are now {self.age} years old.")


# This line creates an object of the Person class with the name "Alice" and the age 20
alice = Person("Alice", 20)

# This line calls the introduce method on the alice object
alice.introduce()

# This line calls the birthday method on the alice object
alice.birthday()
