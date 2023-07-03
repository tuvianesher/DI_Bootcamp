class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal_type, quantity=1):
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
        else:
            self.animals[animal_type] = quantity

    def get_info(self):
        output = f"{self.name}'s farm\n\n"
        for animal, quantity in self.animals.items():
            output += f"{animal} : {quantity}\n"
        output += "\nE-I-E-I-0!"
        return output

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animal_types_str = ', '.join(animal_types)
        return f"{self.name}'s farm has {animal_types_str}."


# Test the code
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
