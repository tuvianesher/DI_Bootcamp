class Family:
    def __init__(self, last_name):
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations! {kwargs['name']} has been born.")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        print("Members:")
        for member in self.members:
            print(member['name'])


# Create an instance of the Family class
family = Family("Smith")

# Test the methods
family.born(name="Emily", age=4, gender="Female", is_child=True)
print(f"Is Sarah 18 or older? {family.is_18('Sarah')}")
family.family_presentation()
