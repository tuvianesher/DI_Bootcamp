class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / (self.age * 10)

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} won the fight"
        elif self.run_speed() * self.weight < other_dog.run_speed() * other_dog.weight:
            return f"{other_dog.name} won the fight"
        else:
            return "It's a tie"


# Create instances of the Dog class
dog1 = Dog("Max", 3, 15)
dog2 = Dog("Buddy", 5, 12)
dog3 = Dog("Charlie", 4, 20)

# Test the methods
print(dog1.bark())
print(dog2.run_speed())
print(dog3.fight(dog2))
