from pets_class import Pets, Dog


# Create object instances of the class Pets.
pet1 = Pets('Tom', 6)
pet2 = Pets('Fletcher', 7)
pet3 = Pets('Larry', 9)


# Create object instances of the class Dog.
dogs = Dog(False)


# Print out our output.
print("I have 3 dogs.")
print(pet1.name + " is " + str(pet1.age) + ".")
print(pet2.name + " is " + str(pet2.age) + ".")
print(pet3.name + " is " + str(pet3.age) + ".")
print("And they are all " + Pets.animal_type + ", of course.")
print(dogs.eat())
print(pet1.walk())
print(pet2.walk())
print(pet3.walk())
