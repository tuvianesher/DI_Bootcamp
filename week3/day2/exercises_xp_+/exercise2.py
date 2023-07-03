class Family:
    def __init__(self, last_name):
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)
        print("Congratulations! A new family member was born.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print("Family Presentation:")
        for member in self.members:
            print(member['name'])

class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(last_name)
        self.members[0].update({'power': 'fly', 'incredible_name': 'MikeFly'})
        self.members[1].update({'power': 'read minds', 'incredible_name': 'SuperWoman'})

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name} can use the power: {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 years old.")

    def incredible_presentation(self):
        super().family_presentation()
        print("Incredibles Presentation:")
        for member in self.members:
            print(f"Incredible Name: {member['incredible_name']}, Power: {member['power']}")


# Create an instance of the TheIncredibles class
incredibles = TheIncredibles("Parr")

# Call the incredible_presentation method
incredibles.incredible_presentation()

# Add Baby Jack using the inherited born method
incredibles.born(name="Baby Jack", age=0, gender="Male", is_child=True, power="Unknown Power")

# Call the incredible_presentation method again
incredibles.incredible_presentation()
