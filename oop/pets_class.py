# OOP EXERCISE ANDELA LEVEL UP 35.


class Pets:
    """
    This class holds instances of dogs.
    """

    animal_type = "mammals"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def walk(self):
        return self.name + " is walking!"


class Dog:

    def __init__(self, is_hungry):
        self.is_hungry = True

    def eat(self):
        self.is_hungry = False
        return "My dogs are not hungry."

    def walk(self):
        return Pets.get_name(self) + ", is walking."
