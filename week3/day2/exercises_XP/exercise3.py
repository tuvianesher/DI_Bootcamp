import random
from exercise_2 import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dog_names):
        dog_names = list(dog_names)
        dog_names.append(self.name)
        print(f"{', '.join(dog_names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            trick = random.choice(tricks)
            print(f"{self.name} {trick}")


# Create instances of the PetDog class
pet_dog1 = PetDog("Max", 3, 15)
pet_dog2 = PetDog("Buddy", 5, 12)
pet_dog3 = PetDog("Charlie", 4, 20)

# Test the methods
pet_dog1.train()
pet_dog2.play(pet_dog1.name, pet_dog3.name)
pet_dog3.do_a_trick()
