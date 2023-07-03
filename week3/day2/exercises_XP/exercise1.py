class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Siamese(Cat):
    def sing(self, sounds):
        return f"{sounds}"


# Create instances of the cat breeds
bengal_cat = Bengal("Bengal Cat", 3)
chartreux_cat = Chartreux("Chartreux Cat", 5)
siamese_cat = Siamese("Siamese Cat", 2)

# Create a list of all cat instances
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Create an instance of the Pets class with all_cats as the argument
sara_pets = Pets(all_cats)

# Take all the cats for a walk using the walk method
sara_pets.walk()
