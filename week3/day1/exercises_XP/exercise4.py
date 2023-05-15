class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(animal_sold, "has been sold.")
        else:
            print(animal_sold, "is not in the zoo.")

    def sort_animals(self):
        animal_dict = {}
        for animal in self.animals:
            if animal[0] not in animal_dict:
                animal_dict[animal[0]] = [animal]
            else:
                animal_dict[animal[0]].append(animal)
        sorted_dict = dict(sorted(animal_dict.items()))
        return sorted_dict

    def get_groups(self):
        animal_dict = self.sort_animals()
        group_number = 1
        for key in animal_dict:
            print(group_number, ":", animal_dict[key])
            group_number += 1

# Example usage
ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Lion")
ramat_gan_safari.add_animal("Elephant")
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Ape")
ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Bear")
ramat_gan_safari.get_animals()

ramat_gan_safari.get_groups()
