class Character:
    def __init__(self, name):
        self.name = name
        self.life = 20
        self.attack = 10
        print(f"A new character named {self.name} has been created.")

    def basic_attack(self, other_character):
        print(f"{self.name} is attacking {other_character.name}.")
        other_character.life -= self.attack


class Druid(Character):
    def __init__(self, name):
        super().__init__(name)
        print("I am a Druid.")

    def meditate(self):
        print(f"{self.name} is meditating.")
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        print(f"{self.name} is getting help from an animal.")
        self.attack += 5

    def fight(self, other_character):
        print(f"{self.name} is fighting against {other_character.name}.")
        other_character.life -= 0.75 * self.life + 0.75 * self.attack


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        print("I am a Warrior.")

    def brawl(self, other_character):
        print(f"{self.name} is brawling with {other_character.name}.")
        other_character.life -= 2 * self.attack
        self.life += 0.5 * self.attack

    def train(self):
        print(f"{self.name} is training.")
        self.attack += 2
        self.life += 2

    def roar(self, other_character):
        print(f"{self.name} is roaring at {other_character.name}.")
        other_character.attack -= 3


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        print("I am a Mage.")

    def curse(self, other_character):
        print(f"{self.name} is cursing {other_character.name}.")
        other_character.attack -= 2

    def summon(self):
        print(f"{self.name} is summoning magical powers.")
        self.attack += 3

    def cast_spell(self, other_character):
        print(f"{self.name} is casting a spell on {other_character.name}.")
        attack_points = min(self.attack, other_character.life)
        other_character.life -= attack_points


# Testing the classes
druid = Druid("Gandalf")
warrior = Warrior("Aragorn")
mage = Mage("Merlin")

# Using methods
druid.meditate()
warrior.train()
mage.summon()

druid.basic_attack(warrior)
warrior.brawl(druid)
mage.curse(druid)

print(druid.life)  # Output: 28
print(warrior.life)  # Output: 29
print(mage.attack)  # Output: 13
